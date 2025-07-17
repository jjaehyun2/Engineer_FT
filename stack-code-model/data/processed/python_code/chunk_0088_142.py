package com.tourism_in_lviv.air.view.mediator.component
{	
	import com.tourism_in_lviv.air.constants.ViewConst;
	import com.tourism_in_lviv.air.model.ModelLocator;
	import com.tourism_in_lviv.air.model.modelino.DataInfoModelLocator;
	import com.tourism_in_lviv.air.utils.CollectionUtils;
	import com.tourism_in_lviv.air.view.ui.popup.ComponentOptionsCallout;
	
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TouchEvent;
	
	import mx.collections.ArrayCollection;
	
	import org.robotlegs.mvcs.Mediator;
	
	import spark.events.IndexChangeEvent;
	import spark.events.PopUpEvent;
	import spark.transitions.SlideViewTransition;
	
	import views.FactsView;

	/**
	 * 
	 * @author Ihor Khomiak
	 */
	public class FactsMediator extends Mediator
	{
		[Inject]
		/**
		 * 
		 * @default 
		 */
		public var view:FactsView;
		
		[Inject]
		/**
		 * 
		 * @default 
		 */
		public var dataInfoModel:DataInfoModelLocator;
		
		[Inject]
		/**
		 * 
		 * @default 
		 */
		public var modelLocator:ModelLocator;
		
		private var touchBegin_X:int;
		
		/**
		 * 
		 * @default 
		 */
		public var optionsCallout:ComponentOptionsCallout = new ComponentOptionsCallout();
		
		/**
		 * 
		 */
		public function FactsMediator()
		{
			super();
		}

		override public function onRegister():void
		{
			dataInfoModel.allFactsSignal.add( getAllFactsCollection_ResultHandler );
			
			view.factsList.addEventListener( IndexChangeEvent.CHANGE, factsList_IndexChangeHandler );
			view.btnCategory.addEventListener( MouseEvent.CLICK, btnCategory_clickHandler );
			view.btnOptions.addEventListener( MouseEvent.CLICK, btnOptions_clickHandler );
			view.addEventListener( TouchEvent.TOUCH_BEGIN, touch_BeginHandler );
			view.addEventListener( TouchEvent.TOUCH_END, touch_EndHandler );
			
			if( view.selectedCategory )    // if user changed selectedCategory on selected view than ti will set this new value to modelLocator.selectedCategory
				modelLocator.selectedFactCategory = view.selectedCategory;
			
			if( modelLocator.selectedFactCategory )
				view.factsList.dataProvider = modelLocator.selectedFactCategory.items;
		}
		
		override public function onRemove():void
		{
			view.factsList.removeEventListener( IndexChangeEvent.CHANGE, factsList_IndexChangeHandler );
			view.btnCategory.removeEventListener( MouseEvent.CLICK, btnCategory_clickHandler );
			view.btnOptions.removeEventListener( MouseEvent.CLICK, btnOptions_clickHandler );
			view.removeEventListener( TouchEvent.TOUCH_BEGIN, touch_BeginHandler );
			view.removeEventListener( TouchEvent.TOUCH_END, touch_EndHandler );
		}
		
		/**
		 * 
		 * @param event
		 */
		protected function factsList_IndexChangeHandler( event:IndexChangeEvent ):void
		{
			view.navigator.pushView( views.DescriptionView, {selectedItem: view.selectedFact, selectedIndex:view.selectedFactIndex} ); //moving to Description view
		}

		/**
		 * 
		 * @param event
		 */
		protected function btnOptions_clickHandler( event:Event ):void
		{
			optionsCallout.addEventListener(PopUpEvent.CLOSE, optionsCalloutCloseHandler);   // Add an event handler for the close event to check for any returned data
			optionsCallout.open(view.btnOptions, true);    // Open as a modal callout
		}
		
		/**
		 * 
		 * @param event
		 */
		protected function optionsCalloutCloseHandler(event:PopUpEvent):void      // Handle the close event from the Callout
		{
			if (!event.commit)   // If commit is false, no data is returned
				return;
			
			if( event.data == ViewConst.LIST_SORTING_NAME )
				CollectionUtils.sortByProperty( view.factsList.dataProvider as ArrayCollection, 'name' );
			else if ( event.data == ViewConst.LIST_SORTING_RANDOM )
				view.factsList.dataProvider = new ArrayCollection(( view.factsList.dataProvider as ArrayCollection ).toArray().sort( CollectionUtils.mixArray ));
			else if ( event.data == ViewConst.LIST_SORTING_ASCENDING )
				CollectionUtils.sortByProperty( view.factsList.dataProvider as ArrayCollection, 'name', false );
			else if ( event.data == ViewConst.LIST_SORTING_DESCENDING )
				CollectionUtils.sortByProperty( view.factsList.dataProvider as ArrayCollection, 'name', true );
				
			optionsCallout.removeEventListener(PopUpEvent.CLOSE, optionsCalloutCloseHandler);
		} 
		
		/**
		 * 
		 * @param event
		 */
		protected function btnCategory_clickHandler( event:Event ):void
		{
			moveToCategoryView();
		}
		
		/**
		 * 
		 * @param event
		 */
		protected function touch_BeginHandler( event:TouchEvent ):void
		{
			touchBegin_X = event.localX; //save begin X point
		}
		
		/**
		 * 
		 * @param event
		 */
		protected function touch_EndHandler( event:TouchEvent ):void
		{
			if( touchBegin_X >= 0 && touchBegin_X <= 7 )  //if user touch screen and move on it from left to right (from any number from "0 to 7" to 100 px)
			{
				if( event.localX >= 100 )
					moveToCategoryView();
			}
		}
		
		private function moveToCategoryView():void
		{
			var transition:SlideViewTransition = new SlideViewTransition();
			transition.direction = 'right';
			view.navigator.pushView( views.CategoryView, new ArrayCollection( [dataInfoModel.factCategorys, modelLocator.selectedFactCategory] ), null, transition); //moving to CategoryView and sending there category collection and selectedCategory from models
		}

		private function getAllFactsCollection_ResultHandler( collection:ArrayCollection ):void
		{
			view.factsList.dataProvider = collection;
		}
	}
}