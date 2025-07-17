package metaswarm.control {
    import flash.display.*;
	import flash.events.*;
	import flash.ui.Keyboard;
	import flash.net.*;
	import flash.utils.*;
	import flash.text.*;

	//import fl.controls.Label;

    public class Router extends Sprite
    {
		private var _controller:Controller; 
		//var dropped:Subset;
		//var picked:Subset;
		//var idle:Subset;
		
		//these should be scoped to methods
		private var _ctrlPressed:Boolean;
		private var _shftPressed:Boolean;
		private var _altPressed:Boolean;
		private var _mousedOver:Boolean;
		
		private var _focusedNode:Node;
		private var _focusedButton:Object;
		
        public function Router(controller:Controller):void
		{
			this._controller = controller; 
			
			_ctrlPressed = false;
			_shftPressed = false;
			_altPressed = false;
			_mousedOver = false;
			
			_focusedNode = new Node();
			_focusedButton = new Object();

			init();
		}
		private function init():void{ 
			//can't access this.stage until main is added to stage
			//addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
		}
		
		//delegated methods **********************************************************
		public function onEnterFrame(event:Event):void{
			_controller.onEnterFrame();
			//cmdTag.x = mouseX;
			//cmdTag.y = mouseY;
		}
		
		public function onkeyDown(event:KeyboardEvent):void
		{
			if (event.keyCode == Keyboard.RIGHT){
				_controller.onRightKey();
			}else if (event.keyCode == Keyboard.LEFT){
				_controller.onLeftKey();
			}else if (event.keyCode == Keyboard.UP){
				_controller.onUpKey();
			}else if (event.keyCode == Keyboard.DOWN){
				_controller.onDownKey();
			}else if (event.keyCode == Keyboard.SPACE){
				_controller.onSpaceKey();
			}else if (event.keyCode == 49){
				trace("pressed 1");
				_controller.onKey1();
			}else if (event.keyCode == 50){
				trace("pressed 2");
				_controller.onKey2();
			}else if (event.keyCode == 51){
				trace("pressed 3");
				_controller.onKey3();
			}else if (event.keyCode == 52){
				trace("pressed 4");
				_controller.onKey4();
			}else if (event.keyCode == 53){
				trace("pressed 5");
				_controller.onKey5();
			}else if (event.ctrlKey == true || event.shiftKey == true){ 
			
				_ctrlPressed = event.ctrlKey;
				_shftPressed = event.shiftKey;
				
				if(_mousedOver){
					//just clear for now
					_controller.onShftOut();
						
					if(!_shftPressed && _ctrlPressed){
						_controller.onCtrlOver(_focusedNode, _focusedButton);
					}else if(_shftPressed && !_ctrlPressed){
						_controller.onShftOver(_focusedNode, _focusedButton);
					}else if(_shftPressed && _ctrlPressed){
						_controller.onCtrlShftOver(_focusedNode, _focusedButton);
					}else{
						//trace("neither ctrl nor shift was pressed and yet here we are");
					}
				}
			}else{
				//trace("you pressed an invalid key: " + event.keyCode);
			}
		}
		
		public function onkeyUp(event:KeyboardEvent):void
		{
			//reset ctrl and shft key states
			_ctrlPressed = event.ctrlKey;
			_shftPressed = event.shiftKey;
			
			//retest for focus conditions
			if(_mousedOver){

				//just clear for now
				_controller.onShftOut();
				
				if(!_shftPressed && _ctrlPressed){
					_controller.onCtrlOver(_focusedNode, _focusedButton);
				}else if(_shftPressed && !_ctrlPressed){
					_controller.onShftOver(_focusedNode, _focusedButton);
				}else if(_shftPressed && _ctrlPressed){
					_controller.onCtrlShftOver(_focusedNode, _focusedButton);
				}else{
					//trace("neither ctrl nor shift was pressed and yet here we are");
					_controller.onMouseOver(_focusedNode, _focusedButton);
				}
			}
		}
		
		//maybe get rid of this since it competes with mouseUp
		public function onMouseClick(event:MouseEvent):void{
			//trace(getQualifiedClassName(event.target));
			var grandparentClass:String = getQualifiedClassName(event.target.parent.parent);
			
			if(grandparentClass == "Node"){
				if(_ctrlPressed && _shftPressed){
					_controller.onCtrlShftClick(event.target.parent.parent, event.target);
				}else if(_ctrlPressed == true){
					_controller.onCtrlClick(event.target.parent.parent, event.target);
				}else if(_shftPressed == true){
					_controller.onShftClick(event.target.parent.parent, event.target);
				}else{
					_controller.onMouseClick(event.target.parent.parent, event.target);
				}
			}else{
				//trace("uh oh, grandparent is not a Node but a: " + grandparentClass);
			}
		}
		
		public function onMouseDown(event:MouseEvent):void
		{
			//var parentClass:String = getQualifiedClassName(event.target.parent);
			var grandparentClass:String = getQualifiedClassName(event.target.parent.parent);
			
			if(!_ctrlPressed && !_shftPressed && !_altPressed && grandparentClass == "Node"){
				_controller.onMouseDown(event.target.parent.parent, event.target);
			}else{
				//break if ctrl, shft, or alt is pressed
				//trace("don't drag");
			}
		}
		
		public function onMouseUp(event:MouseEvent):void
		{
			//var parentClass:String = getQualifiedClassName(event.target.parent);
			var grandparentClass:String = getQualifiedClassName(event.target.parent.parent);
			
			if(!_ctrlPressed && !_shftPressed && !_altPressed && grandparentClass == "Node"){
				_controller.onMouseUp(event.target.parent.parent);
			}else{
				//break if ctrl, shft, or alt is pressed
				//trace("don't drag");
			}
		}
		
		public function onMouseOver(event:MouseEvent):void
		{
			var grandparentClass:String = getQualifiedClassName(event.target.parent.parent);
			
			if(grandparentClass == "Node"){
				_mousedOver = true;
				_focusedNode = event.target.parent.parent;
				_focusedButton = event.target;
				if(!_ctrlPressed && !_shftPressed){
					_controller.onMouseOver(event.target.parent.parent, event.target);
				}else if(_ctrlPressed && !_shftPressed){
					_controller.onCtrlOver(event.target.parent.parent, event.target);
				}else if(!_ctrlPressed && _shftPressed){
					_controller.onShftOver(event.target.parent.parent, event.target);
				}else if(_ctrlPressed && _shftPressed){
					_controller.onCtrlShftOver(event.target.parent.parent, event.target);
				}
			}else{
				//trace("uh oh, grandparent is not a Node but a: " + grandparentClass);
			}
		}
		
		public function onMouseOut(event:MouseEvent):void
		{
			var grandparentClass:String = getQualifiedClassName(event.target.parent.parent);
			
			if(grandparentClass == "Node"){
				_mousedOver = false;
				//just clear for now
				_controller.onShftOut();
				_controller.onMouseOut(event.target.parent.parent);
			}else{
				//trace("uh oh, grandparent is not a Node but a: " + grandparentClass);
			}
		}

    }//end class
}//end pkg