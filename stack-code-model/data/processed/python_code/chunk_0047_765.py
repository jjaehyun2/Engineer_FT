package metaswarm.node.components   {
	import flash.display.DisplayObject;
	import flash.display.Graphics;
	import flash.display.Shape;
	import flash.display.Sprite;
	
	public class Particle extends Sprite{
		
		//public bc used in subclass plot functions
		//public static const DEF_CLR:Color 	= #000000;
		//public static const FOC_CLR:Color 	= #FF0000;
		private static const EASE:Number 	= .25;
		private static const SNAP:Number 	= 1;
		
		//Target Coordinates
		internal var tgx:Number;
		internal var tgy:Number;
		
		//Previous Coordinates
		public var px:Number;
		public var py:Number;
		
		//distance to target
		private var dx:Number;
		private var dy:Number;
		
		//velocity
		private var vx:Number;
		private var vy:Number;
		
		//atTarget:Boolean; unnec. used expression instead		
		//hidden:Boolean; use inherited prop visible instead
		//infocus:Boolean; not needed because mouse events
		//are object oriented. that is they test for focus
		//internally
		
		//x
		//y
		//visible : Boolean 
			
		//still unclear about constructors, see pg 180 of FofEd anim.	
		public function Particle(tgx:Number=0,
								 tgy:Number=0,
								 dx:Number=0,
								 dy:Number=0,
								 vx:Number=0,
								 vy:Number=0):void
		{
			this.x = 0;
			this.y = 0;
			this.tgx = tgx;
			this.tgy = tgy;
			this.dx = dx;
			this.dy = dy;
			this.vx = vx;
			this.vy = vy;
			this.px = 0;
			this.py = 0;
			//init();
		}	
		
		/*public function init():void {
			//nothing for now
		}*/
		
		public function isVisible():Boolean { 
			return this.visible; 
		}
		
		//use move(x,y) instead
		/*public function position(xNew:Number, yNew:Number):void
		{
			this.x = xNew;
			this.y = yNew;
		}*/
		
		public function goToTarget():void {
			//trace("x,y before: " + dx + " " + dy);
			//trace("tgs before: " + tgx + " " + tgy);
			dx = tgx - x;
			dy = tgy - y;
			if(Math.sqrt(dx*dx + dy*dy) < SNAP){
				x = tgx;
				y = tgy;
				//removeEventListener(Event.Enter_FRAME, onEnterFrame);
			}else{
				vx = dx * EASE;
				vy = dy * EASE;
				x += vx;
				y += vy;
			}
			//trace("after: " + dx + " " + dy);
			//trace("tgs after: " + tgx + " " + tgy);
		}
		
		public function snapToTarget():void{ //<-------------wtf
			x = tgx;
			y = tgy;
		}
				
		public function setTarget(a:Number, b:Number):void {//<-------------wtf
			tgx = a;
			tgy = b;
		}
		
		public function setPrev(a:Number, b:Number):void {//<-------------wtf
			px = a;
			py = b;
		}
		
		//getFocus():Interactive Object
		//hitTestPoint(x:Number, y:Number, shapeFlag:Boolean = false):Boolean 
		//startDrag()
		//stopDrag()
	}
}