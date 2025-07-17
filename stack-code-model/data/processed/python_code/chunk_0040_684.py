package metaswarm.node.components.databox   {
	import flash.display.*;
	import flash.text.*;
	import flash.events.*;
	import flash.utils.*;
	import metaswarm.node.components.Particle;
	
	public class DataBox extends Particle{
		
		//need an idea for select and filter functions
		//e.g. select matching text with id eq to this.
		//this is id of array element no textBox
		//var id:uint;
	
		public var dat:Array;
		
		public var t:TextField = new TextField();
		
		public var closeButton:CustomSimpleButton;
		public var popoutButton:CustomSimpleButton;
		public var popinButton:CustomSimpleButton;
		//var loadExtButton:CustomSimpleButton;
		
		public var dataBoxMaker:DataBoxMaker;
		
		public function DataBox():void{
			dataBoxMaker = new DataBoxMaker(this);
			init();
		}
		public function init():void {
			visible = false;
			focusRect = true;
			tabEnabled = true;
			
			//addEventListener(MouseEvent.CLICK, onMouseClick);
		}
		public function load(dat:Array):void{
			this.dat = dat;
		}
		public function make():void {
			dataBoxMaker.make();
		}
		
		private function onMouseClick(event:MouseEvent):void{
			//trace(getQualifiedClassName(event.target));
			
			/*if(getQualifiedClassName(event.target) == "::CustomSimpleButton"){
				switch (event.target.type) {
					case CLOSE:
						trace("close");
						break;
					case POPOUT:
						trace("popout");
						parent.thumb.load(dat[0] + dat[1]);
						parent.thumb.make();
						parent.thumb.x = this.width;
						parent.thumb.y = this.y;
						parent.addChild(parent.thumb);
						break;
					case POPIN:
						trace("popin");
						break;
					default:
						trace("Not a valid type of button");
				}
			}*/
		}
		
	}//end class
}//end pkg