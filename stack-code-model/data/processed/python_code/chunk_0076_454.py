package metaswarm.node.components.tag   {
	import flash.display.*;
	import flash.text.*;
	
	//should this extend shape instead????
	public class TagButtonState extends Sprite {
		//private var typeOfButton:uint;
		private var bgColor:uint;
		private var lineColor:uint;
		private var size:uint;
	
		public function TagButtonState(lineColor:uint, bgColor:uint, size:uint) {
			//this.typeOfButton = typeOfButton;
			this.bgColor = bgColor;
			this.lineColor = lineColor;
			this.size = size;
			//draw();
		}
	
		//need ref to tag, can't do this yet
		/*private function draw():void {
			//tag.tagButton = new TagButton();
			//tag.addChild(tag.tagButton);
			
			var fmt:TextFormat = new TextFormat( );
			
			fmt.font = "Arial";
			fmt.size = size;
			//tag.t.embedFonts = true;
			//tag.t.antiAliasType = AntiAliasType.ADVANCED;
			tag.t.text = "";
			tag.t.setTextFormat(fmt);
			tag.t.selectable = false;
			tag.t.mouseEnabled = false;
			tag.id = 0;
			
			tag.t.x += 5;
			tag.t.y -= 25;
			//t.width = 
			//t.height =
			tag.t.background = true
			tag.t.backgroundColor = bgColor; //light gray
			//tag.t.border = true;
			tag.t.borderColor = lineColor; //dark gray
			tag.t.autoSize = TextFieldAutoSize.LEFT;
			//addChild(this);
			
			tag.t.text = tag.dat[tag.id];
			
			tag.addChild(tag.t);
		}*/
		
	}
}