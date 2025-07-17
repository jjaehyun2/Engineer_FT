package metaswarm.node.components.icon {
	import flash.display.DisplayObject;
    import flash.display.Graphics;
    import flash.display.Shape;
	import flash.display.Sprite;
	
	public class IconMaker extends Sprite{
		
		public var icon:Icon;
		
		public function IconMaker(icon:Icon):void{
			this.icon = icon;
			init();
		}
		public function init():void {
			//
		}
		public function make():void {
			//trace("make the icon button");
			icon.iconButton = new IconButton();
			icon.addChild(icon.iconButton);
		}
	}
}