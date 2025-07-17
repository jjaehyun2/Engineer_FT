package com.controls.collapsePanel
{	
	import com.controls.collapsePanel.interfaces.IErrorViewer;
	
	import flash.events.MouseEvent;
	
	import mx.core.IUIComponent;
	import mx.core.IVisualElement;
	import mx.events.FlexEvent;
	
	import spark.components.Button;
	import spark.components.HGroup;
	import spark.components.Image;
	import spark.components.SkinnableContainer;
	import spark.components.supportClasses.GroupBase;
	
	[SkinState("collapsed")]
	public class CollapsePanel extends SkinnableContainer implements IErrorViewer
	{
		[Bindable]
		public var title:String;
		[Bindable]
		public var showError:Boolean;
		
		[Bindable]
		public var errorVisibleWhenExpaneded:Boolean;
		
		public var _fillToAll:Boolean;	
		
		[Bindable]
		public function get fillToAll():Boolean
		{
			return _fillToAll;
		}
		public function set fillToAll(value:Boolean):void
		{
			_fillToAll = value;
			if(value)
			{
				percentHeight = 100;
				invalidateSize();
				invalidateSkinState();
			}
		}
		
		[SkinPart(required="false")]
		public var headerBar:HGroup;
		[SkinPart(required="false")]
		public var collapseButton:Button;
		
		protected var _collapsed:Boolean;
		
		[Bindable]
		public function get collapsed():Boolean
		{
			return _collapsed;
		}
		public function set collapsed(value:Boolean):void
		{
			_collapsed = value;
			if(fillToAll)
			{
				if(!value)
				{
					percentHeight = 100;
				}
				else
				{
					height = headerBar.height;
				}
			}
			
			invalidateSkinState();
		}
		
		private var _errorStringGlobal:String;
		
		public function CollapsePanel()
		{
			super();
			addEventListener(FlexEvent.CREATION_COMPLETE, onCreationComplete);
		}
		
		override public function removeElement(element:IVisualElement):IVisualElement
		{
			trace("removed element: " );
			return super.removeElement(element);
		}
		
		override public function removeElementAt(index:int):IVisualElement
		{
			trace("removed element at: " );
			return super.removeElementAt(index);
		}
		
		private function onCreationComplete(event:FlexEvent):void
		{
			removeEventListener(FlexEvent.CREATION_COMPLETE, onCreationComplete);
		}
		
		override protected function getCurrentSkinState():String
		{
			return collapsed ? "collapsed" : super.getCurrentSkinState();
		}
		
		protected function collapseButtonClickHandler(event:MouseEvent):void
		{
			collapsed = !collapsed;
		}
		
		override protected function partAdded(partName:String, instance:Object) : void
		{
			super.partAdded(partName, instance);
			if (instance == collapseButton)
			{
				Button(instance).addEventListener(MouseEvent.CLICK, collapseButtonClickHandler);
			}
		}
		override protected function partRemoved(partName:String, instance:Object) : void
		{
			if (instance == collapseButton)
			{
				Button(instance).removeEventListener(MouseEvent.CLICK, collapseButtonClickHandler);
			}
			super.partRemoved(partName, instance);
		}
		
		[Bindable]
		public function get errorStringGlobal():String
		{
			return _errorStringGlobal;
		}
		
		public function set errorStringGlobal(value:String):void
		{
			_errorStringGlobal = value;
		}

	}
}