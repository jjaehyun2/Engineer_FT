package metaswarm.node.components.tag   {
	import flash.display.*;
	import flash.text.*;
	import metaswarm.node.components.Particle;
	
	public class Tag extends Particle{
		
		//add formatting constants here
		public var tagMaker:TagMaker;
		public var tagButton:TagButton;
		//zoom velocity
		//private var val:String;
		public var t:TextField;
		//var fmt:TextFormat;
		public var uniqArr:Array = new Array();
		public var isUniq:Boolean = new Boolean();
		
		//need an idea for select and filter functions
		//e.g. select matching text with id eq to this.
		//this is id of array element no textBox
		public var id:uint;
		
		//cnt not nec, can just use array length
		//var cnt:uint;
		public var dat:Array;
		//var dat:Array = ["cherry", "orange", "soda", "pop"];
		
		public function Tag():void
		{
			t = new TextField();
			tagMaker = new TagMaker(this);
			//fmt = new TextFormat( );
			init();
		}
		public function init():void {
			visible = false;
			//focusRect = false;
			//tabEnabled = false;
			//tag.mouseEnabled = false;
		}
		
		public function load(dat:Array):void{
			this.dat = dat;
		}
		public function make():void{
			tagMaker.make();
		}
		
		public function incr():void{
			if(id < dat.length-1){
				id++;
			}else{
				id=0;
			}
			t.text = dat[id];
			isUniq = uniqArr[id];
			//t.text = String(this.tgx) + ", " + String(this.tgy);
		}
		
		public function decr():void{
			if(id > 0){
				id--;
			}else{
				id=dat.length-1;
			}
			t.text = dat[id];
			isUniq = uniqArr[id];
			//t.text = String(this.tgx) + ", " + String(this.tgy);
		}
		
		/*public function getDatAt(id):void{
			return dat[id];
		}*/
		
	}//end class
}//end pkg