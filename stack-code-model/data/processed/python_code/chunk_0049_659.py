package metaswarm.ui.uistates   {
	import metaswarm.ui.Ui;
	import metaswarm.ui.UiState;
	
	class ContactState implements UiState{
		
		var main:Ui;
		
		function ContactState(main:Ui)
		{
			//trace("construct ExploreState");
			this.main = main;
			init();
		}	
		public function init():void{
		}
		
		//delegated methods*********************************************
		public function onEnterFrame():void{
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
		}
		public function onKey1():void{
			//main.mainState = main.explore;
		}
		public function onKey2():void{
			//main.mainState = main.preview;
		}
		public function onKey3():void{
			//main.mainState = main.about;
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