package components {
	
	import application.utils.StaticGUI;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import starling.text.TextFormat;
	
	
	public class LabelWithTitleBlock extends LayoutGroup {
		private var title:Label;
		private var label:Label;
		private var titleStyle:TextFormat;
		
		private var labelStyle:TextFormat;
		private var titleStr:String;
		private var promptStr:String;
		
		public function LabelWithTitleBlock(title:String, prompt:String) {
			titleStr = title;
			promptStr = prompt;
			super();
			//this.title = "Screen C";
		}
		
		override protected function initialize():void {
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.horizontalAlign = HorizontalAlign.CENTER;
			layout.verticalAlign = VerticalAlign.TOP;
			layout.gap = Settings._getIntByDPI(15);
			this.layout = layout;
			
			labelStyle = new TextFormat;
			labelStyle.font = '_bpgArialRegular';
			labelStyle.size = Settings._getIntByDPI(25);
			labelStyle.horizontalAlign = HorizontalAlign.CENTER;
			labelStyle.color = 0x7f8486;
			
			titleStyle = new TextFormat;
			titleStyle.font = '_bpgArialRegular';
			titleStyle.size = Settings._getIntByDPI(24);
			titleStyle.color = 0x575a5b;
			
			title = StaticGUI._addLabel(this, titleStr, titleStyle);
			label = StaticGUI._addLabel(this, promptStr, labelStyle);
		
		}
		
		override public function dispose():void {
			
			StaticGUI._safeRemoveChildren(title, true);
			StaticGUI._safeRemoveChildren(label, true);
			
			super.dispose();
			
			title = null;
			label = null;
			titleStyle = null;
			
			labelStyle = null;
			titleStr = null;
			promptStr = null;
			
		}
	}
}