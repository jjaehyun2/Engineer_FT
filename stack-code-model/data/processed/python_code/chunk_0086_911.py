package metaswarm.node.components.tag   {
	import flash.display.*;
	import flash.text.*;
	
	public class TagMaker extends Sprite{
		
		private var tag:Tag;
		
		public function TagMaker(tag:Tag):void{
			this.tag = tag;
			init();
		}
		public function init():void {
			//
		}
		
		/*public function make():void {
			//trace("make the tag button");
			tag.tagButton = new TagButton();
			tag.addChild(tag.tagButton);
		}*/
		
		public function make():void {
			//tag.tagButton = new TagButton();
			//tag.addChild(tag.tagButton);
			
			var fmt:TextFormat = new TextFormat( );
			
			fmt.font = "Arial";
			fmt.size = 5;
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
			tag.t.backgroundColor = 0xCCCCCC; //light gray
			tag.t.border = true;
			tag.t.borderColor = 0x333333; //dark gray
			tag.t.autoSize = TextFieldAutoSize.LEFT;
			//addChild(this);
			
			tag.t.text = tag.dat[tag.id];
			
			tag.addChild(tag.t);
		}
	}
}