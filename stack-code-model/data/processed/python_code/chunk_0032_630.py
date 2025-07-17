package metaswarm.ui.uistates   {
	import metaswarm.*;
	import metaswarm.ui.Ui;
	import metaswarm.ui.UiState;
	import metaswarm.swarm.Swarm;
	import com.greensock.TweenLite;
	
	public class PreviewState implements UiState{
		
		private var main:Ui;
		
		public function PreviewState(main:Ui)
		{
			//trace("construct ExploreState");
			this.main = main;
			init();
		}	
		public function init():void{
		}
		
		//delegated methods*********************************************
		public function onOpenState():void{
			main.cmdLog.append("in preview state");
		}
		public function onEnterFrame():void{
			main.swarm.rePosition();
			main.swarm.reSize();
			main.hoverLabel.update();
		}
		public function onRightKey():void{
		}
		public function onLeftKey():void{
		}
		public function onUpKey():void{
		}
		public function onDownKey():void{
		}
		public function onSpaceKey():void{
			//main.mainState = main.xxx;
			TweenLite.to(main.swarm, 1, {scaleX:3, scaleY:3});
		}
		public function onKey1():void{
			trace("previewState->onKey1");
			main.swarm.explore();
			main.uiState = main.explore;
			main.cmdLog.append("explore mode");
		}
		public function onKey2():void{
			//main.mainState = main.preview;
		}
		public function onKey3():void{
			//main.mainState = main.about;
			TweenLite.to(main.swarm, .25, {scaleX:3, scaleY:3});
		}
		public function onKey4():void{
			//main.mainState = main.contact;
		}
		public function onMouseClick(node:Node, button:Object):void{
		}
		public function onCtrlClick(node:Node, button:Object):void{
		}
		public function onShftClick(node:Node, button:Object):void{
		}
		public function onAltClick(node:Node, button:Object):void{
		}
		public function onCtrlShftClick(node:Node, button:Object):void{
		}
		public function onCtrlShftOver(node:Node, button:Object):void{
		}
		public function onCtrlShftOut():void{
		}
		public function onMouseDown(node:Node, button:Object):void{
			//target.drag();
		}
		public function onMouseUp(target:Node):void{
			//target.drop();
		}
		public function onMouseOver(target:Node, button:Object):void{
			//target.startPrev();
		}
		public function onCtrlOver(target:Node, button:Object):void{
			//target.startPrev();
		}
		public function onShftOver(target:Node, button:Object):void{
			//target.startPrev();
		}
		public function onCtrlOut():void{
			//target.startPrev();
		}
		public function onShftOut():void{
			//target.startPrev();
		}
		public function onMouseOut(target:Node):void{
			//target.stopPrev();
		}

		
	}//end class
}//end pkg