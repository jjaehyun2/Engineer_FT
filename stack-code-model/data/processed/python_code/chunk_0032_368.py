package framework.core.view
{
	import flash.events.Event;

	import framework.model.AppModelLocator;
	import framework.module.CommonModule;
	
	import mx.containers.Box;
	import mx.events.FlexEvent;
	
	// ===================================================================== //
	//                           EXCLUDED API                                //
	// ===================================================================== //	
	[Exclude(name="percentWidth", kind="prope                                                                                                                                                                                                                                                                     rty")]
	[Exclude(name="percentHeight", kind="property")]
	[Exclude(name="direction", kind="property")]
	
	[Exclude(name="show", kind="event")]
	
	// ===================================================================== //
	//                              EVENTS                                   //
	// ===================================================================== //
	/**
	 *  Dispatched when sub view is created.
	 *
	 *  @eventType mx.events.FlexEvent.ENTER
	 */
	[Event(name="open", type="mx.events.FlexEvent")]
	
	public class SubWindow extends Box
	{
		// ================================================================= //
		//                             VARIABLES                             //
		// ================================================================= //
		/**
		 *  This property contain the model with all data.
		 *  
		 *  @see framework.model.AppModelLocator
		 */
		private var _model:AppModelLocator = AppModelLocator.getInstance();

		
		[Bindable]
		/**
		 *  This property is common module. This module is storage for all
		 *  common variables in the system.
		 *  
		 *  @default model.commonModule
		 *  
		 *  @see framework.module.CommonModule
		 */
		protected var storage:CommonModule = model.commonModule;
		
		// ================================================================= //
		//                        ITERFACES METHODS                          //
		// ================================================================= //
		public function open():void
		{
			
		}
		
		public function update():void
		{
			// TODO : override this method for use, when sub view is active
		}
		
		// ================================================================= //
		//                          COMMON METHODS                           //
		// ================================================================= //
		/**
		 *  BaseWindow. Constructor.
		 */
		public function SubWindow()
		{
			super();
			
			percentWidth = 100;
			percentHeight = 100;
			
			setStyle("paddingBottom", 5);
			setStyle("paddingTop", 5);
			setStyle("paddingLeft", 5);
			setStyle("paddingRight", 5);
			// update bindable by model
			model = AppModelLocator.getInstance();
		}

		
		[Bindable(event="modelChange")]
		/**
		 *  The model with all data.
		 */
		public function get model():AppModelLocator
		{
			return _model;
		}
		/**
		 *  @private
		 */
		public function set model(value: AppModelLocator):void
		{
			_model = value;
			// update binding
			dispatchEvent(new Event("modelChange"));
		}
	}
}