package components {
	
	import application.AssetsLoader;
	import application.utils.StaticGUI;
	import feathers.controls.Label;
	import feathers.controls.LayoutGroup;
	import feathers.controls.TextInput;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.skins.ImageSkin;
	import flash.geom.Rectangle;
	import starling.text.TextFormat;
	
	
	public class InputWithTitleBlock extends LayoutGroup {
		private var title:Label;
		private var titleStyle:TextFormat;
		private var titleDisabledStyle:TextFormat;
		
		private var inputStyle:TextFormat;
		private var inputPromptStyle:TextFormat;
		private var titleStr:String;
		private var inputPromptStr:String;
		private var userInputSkin:ImageSkin;
		private var userInput:TextInput;
	
		
		public function InputWithTitleBlock(title:String, inputPrompt:String) {
			titleStr = title;
			inputPromptStr = inputPrompt;
			super();
			//this.title = "Screen C";
		}
		
		override protected function initialize():void {
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.horizontalAlign = HorizontalAlign.CENTER;
			layout.verticalAlign = VerticalAlign.TOP;
			layout.gap = Settings._getIntByDPI(20);
			this.layout = layout;
			
			inputStyle = new TextFormat;
			inputStyle.font = '_bpgArialRegular';
			inputStyle.size = Settings._getIntByDPI(24);
			inputStyle.horizontalAlign = HorizontalAlign.CENTER;
			inputStyle.color = 0xd3d4d4;
			
			inputPromptStyle = new TextFormat;
			inputPromptStyle.font = '_bpgArialRegular';
			inputPromptStyle.size = Settings._getIntByDPI(24);
			inputPromptStyle.horizontalAlign = HorizontalAlign.CENTER;
			inputPromptStyle.color = 0xd3d4d4;			
			
			titleStyle = new TextFormat;
			titleStyle.font = '_bpgArialRegular';
			titleStyle.size = Settings._getIntByDPI(24);
			titleStyle.color = 0x575a5b;
			
			titleDisabledStyle = new TextFormat;
			titleDisabledStyle.font = '_bpgArialRegular';
			titleDisabledStyle.size = Settings._getIntByDPI(24);
			titleDisabledStyle.color = 0xabadad;
			
			title = StaticGUI._addLabel(this, titleStr, titleStyle);
			title.disabledFontStyles = titleDisabledStyle;
			
			userInputSkin = new ImageSkin(AssetsLoader._asset.getTexture("posta_declare_field_default.png"));
			userInputSkin.disabledTexture = AssetsLoader._asset.getTexture("posta_declare_field_disabled.png")
			userInputSkin.scale9Grid = StaticGUI._getScale9GridRect(userInputSkin.width, userInputSkin.height);
			
			userInput = StaticGUI._addTextInput(this, inputPromptStr, inputStyle, inputPromptStyle);
			userInput.backgroundSkin = userInputSkin;
			
		
		}
		
		override public function dispose():void {
			
			StaticGUI._safeRemoveChildren(userInput, true);
			StaticGUI._safeRemoveChildren(title, true);
			userInputSkin.dispose();
			
			title = null;
			titleStyle = null;
			titleDisabledStyle = null;
			
			inputStyle = null;
			inputPromptStyle = null;
			titleStr = null;
			inputPromptStr = null;
			userInputSkin = null;
			userInput = null;
			
			super.dispose();
		}
	}
}