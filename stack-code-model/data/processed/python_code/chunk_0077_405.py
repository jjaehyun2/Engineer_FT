package org.openPyro.managers
{
	import org.openPyro.core.IDataRenderer;
	import org.openPyro.core.MeasurableControl;
	import org.openPyro.events.PyroEvent;
	import org.openPyro.managers.toolTipClasses.DefaultToolTipRenderer;
	
	import flash.display.DisplayObject;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	import flash.utils.getDefinitionByName;
	import flash.utils.getQualifiedClassName;
	
	public class TooltipManager
	{
		
		private var rendererInstance:DisplayObject;
		private var _defaultRendererClass:Class = DefaultToolTipRenderer

		public function TooltipManager() {}
		
		private var stage:Stage;
		private var hideTimer:Timer 
		private var currentTarget:DisplayObject;
		
		public function showToolTip(event:MouseEvent, data:Object, rendererClass:Class=null):void
		{
			if(!rendererClass){
				rendererClass = DefaultToolTipRenderer;
			}
			currentTarget= event.target as DisplayObject;
			stage = event.target.stage;
			if(!stage) return;
			if(!rendererInstance || getDefinitionByName(getQualifiedClassName(rendererInstance)) != rendererClass){
				rendererInstance =new rendererClass();
				stage.addChild(rendererInstance);
				if(rendererInstance is MeasurableControl){
					MeasurableControl(rendererInstance).validateSize();
					MeasurableControl(rendererInstance).validateDisplayList();
					MeasurableControl(rendererInstance).addEventListener(PyroEvent.UPDATE_COMPLETE, onRendererUpdate);
				}
			}			
			else{
				rendererInstance.visible = true;
			}
			IDataRenderer(rendererInstance).data = data;
			positionTooltipFunction();
			if(_moveWithMouse){
				stage.addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);
			}	
			
			currentTarget.addEventListener(MouseEvent.MOUSE_OUT, hideToolTip)	
			
			if(!hideTimer){
				hideTimer = new Timer(5000,1);
				hideTimer.addEventListener(TimerEvent.TIMER, onHideTimer);
			}
			
			hideTimer.reset();
			hideTimer.start();
				
		}
		
		private function onHideTimer(event:TimerEvent):void{
			hideToolTip();
		}
		
		
		private function onRendererUpdate(event:PyroEvent):void{
			positionTooltipFunction();	
		}
		
		private function onMouseMove(event:Event):void{
			if(rendererInstance)
				positionTooltipFunction();
				
		}
		
		/**
		 * positionTooltip is a Function that is in the public namespace.
		 * This way, if you wanted to provide a custom positioning algorithm,
		 * you can just by doing:
		 * 	TooltipManager.getInstance.positionToolTipFunction = function(){ ... }
		 */ 
		public var positionTooltipFunction:Function = function():void{
			if(!stage) return;
			if(stage.mouseX < (stage.stageWidth - rendererInstance.width-20)){
				rendererInstance.x  = stage.mouseX+10;
			}
			else{
				rendererInstance.x  = stage.mouseX-rendererInstance.width-5;
			}
			if(stage.mouseY < stage.stageHeight-60){
				rendererInstance.y = stage.mouseY+10;
			}
			else{
				rendererInstance.y = stage.mouseY-rendererInstance.height-5;
			}
		}
		
		public function hideToolTip(event:Event=null):void
		{
			rendererInstance.visible = false;
			if(stage)
				stage.removeEventListener(MouseEvent.MOUSE_MOVE, onMouseMove);	
		}
		
		private var _moveWithMouse:Boolean = false;
		public function set moveWithMouse(b:Boolean):void{
			_moveWithMouse = b
		}
		public function get moveWithMouse():Boolean{
			return _moveWithMouse;
		}
				
		private static var instance:TooltipManager;
		public static function getInstance():TooltipManager
		{
			if(!instance)
			{
				instance = new TooltipManager();
			}
			return instance;
		}	
	}
}