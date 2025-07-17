package metaswarm.ui   
{
    import flash.display.*;
	import flash.events.*;
	import flash.ui.Keyboard;
	import flash.net.*;
	import flash.utils.*;
	import flash.text.*;
	import metaswarm.ui.hoverlabel.HoverLabel;
	import metaswarm.ui.log.Log;
	import metaswarm.ui.sidebar.Sidebar;
	import metaswarm.swarm.Swarm;
	import metaswarm.ui.uistates.AboutState;
	import metaswarm.ui.uistates.ContactState;
	import metaswarm.ui.uistates.ExploreState;
	import metaswarm.ui.uistates.PreviewState;

	//import fl.controls.Label;
	
	//UI
    public class Ui extends Sprite
    {	
		public var w:int;
		public var h:int;
		
		public var swarm:Swarm;
		public var sidebar:Sidebar;
		public var hoverLabel:HoverLabel;
		public var cmdLog:Log;
		//public var lastCmd:Label;
		
		//internal states
		public var explore:UiState;
		public var preview:UiState;
		//public var about:UiState;
		//public var contact:UiState;
		
		//internal state holder
		public var uiState:UiState;
		
        public function Ui():void
		{
			swarm = new Swarm();
			sidebar = new Sidebar();
			hoverLabel = new HoverLabel();
			//lastCmd = new Label();
			cmdLog = new Log();
			
			explore = new ExploreState(this);
			preview = new PreviewState(this);
			//about = new AboutState(this);
			//contact = new ContactState(this);
			
			uiState = explore;
		
			init();
		}
		public function init():void{ 
			//can't access this.stage until main is added to stage
			//so listen for event then use stage
			addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
		}
		
		public function onAddedToStage(event:Event):void
		{
			swarm.x = stage.stageWidth/6;
			swarm.y = stage.stageHeight/6;
			swarm.w = stage.stageWidth*(2/3);
			swarm.h = stage.stageHeight*(2/3);
		}
		
		//delegate
		public function onOpenState():void{
			//
			uiState.onOpenState();
		}
		public function onEnterFrame():void{
			//
			uiState.onEnterFrame();
		}
		public function onRightKey():void{
			//
			uiState.onRightKey();
		}
		public function onLeftKey():void{
			//
			uiState.onLeftKey();
		}
		public function onUpKey():void{
			//
			uiState.onUpKey();
		}
		public function onDownKey():void{
			//
			uiState.onDownKey();
		}
		public function onSpaceKey():void{
			//
			uiState.onSpaceKey();
		}
		public function onKey1():void{
			//
			uiState.onKey1();
		}
		public function onKey2():void{
			//
			uiState.onKey2();
		}
		public function onKey3():void{
			//
			uiState.onKey3();
		}
		public function onKey4():void{
			//
			uiState.onKey4();
		}
		public function onMouseClick(node:Node, button:Object):void{
			//
			uiState.onMouseClick(node, button);
		}
		public function onCtrlClick(node:Node, button:Object):void{
			//
			uiState.onCtrlClick(node, button);
		}
		public function onShftClick(node:Node, button:Object):void{
			//
			uiState.onShftClick(node, button);
		}
		public function onAltClick(node:Node, button:Object):void{
			//
			uiState.onAltClick(node, button);
		}
		public function onCtrlShftClick(node:Node, button:Object):void{
			//
			uiState.onCtrlShftClick(node, button);
		}
		/*function onDataBoxClick(node:Node, button:Object):void{
			uiState.onDataBoxClick(node, button);
		}*/
		public function onMouseDown(node:Node, button:Object):void{
			//
			uiState.onMouseDown(node, button);
		}
		public function onMouseUp(target:Node):void{
			//
			uiState.onMouseUp(target);
		}
		public function onMouseOver(target:Node, button:Object):void{
			//
			uiState.onMouseOver(target, button);
		}
		public function onCtrlOver(target:Node, button:Object):void{
			//
			uiState.onCtrlOver(target, button);
		}
		public function onShftOver(target:Node, button:Object):void{
			//
			uiState.onShftOver(target, button);
		}
		public function onCtrlShftOver(node:Node, button:Object):void{
			//
			uiState.onCtrlShftOver(node, button);
		}
		public function onCtrlOut():void{
			//
			uiState.onCtrlOut();
		}
		public function onShftOut():void{
			//
			uiState.onShftOut();
		}
		public function onCtrlShftOut():void{
			//
			uiState.onCtrlShftOut();
		}
		public function onMouseOut(target:Node):void{
			//
			uiState.onMouseOut(target);
		}
	
    }//end class
}//end pkg