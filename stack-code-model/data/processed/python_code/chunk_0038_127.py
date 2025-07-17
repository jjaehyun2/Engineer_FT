package application.utils {
	import feathers.controls.AutoComplete;
	import feathers.controls.Button;
	import feathers.controls.Label;
	import feathers.controls.TextInput;
	import feathers.controls.ButtonState;
	import feathers.controls.text.BitmapFontTextRenderer;
	import feathers.controls.text.TextFieldTextEditor;
	import feathers.controls.text.TextFieldTextRenderer;
	import feathers.core.ITextEditor;
	import feathers.core.ITextRenderer;
	import feathers.skins.ImageSkin;
	import feathers.text.BitmapFontTextFormat;
	import flash.geom.*;
	import flash.text.AntiAliasType;
	import flash.text.TextFormatAlign;
	import starling.core.Starling;
	import starling.display.DisplayObject;
	import starling.display.DisplayObjectContainer;
	import starling.display.Image;
	import starling.text.TextFormat;
	import starling.textures.Texture;
	
	public class StaticGUI extends Object {
		
		
		public static const TOP_CENTER:String = "TC";
		public static const TOP_LEFT:String = "TL";
		public static const CENTER_CENTER:String = "CC";
		public static const BOTTOM_CENTER:String = "BC";
		public static const RIGHT_CENTER:String = "RC";
		public static const RIGHT_TOP:String = "RT";
		
		
		public function StaticGUI() {
			return;
		} // end function
		
		public static function commaNum(param1:int):String {
			var _loc_2:* = "";
			var _loc_3:* = String(param1);
			var _loc_4:* = 0;
			while (_loc_3.length > 0) {
				
				_loc_2 = (_loc_3.length > 3 ? (",") : ("")) + _loc_3.slice(_loc_3.length - 3, _loc_3.length) + _loc_2;
				_loc_3 = _loc_3.slice(0, _loc_3.length - 3);
			}
			return _loc_2;
		} // end function
		
		//[Inline]
		public static function safeRemoveChild(param1:DisplayObject, dispose:Boolean = false):Boolean {
			if (param1 == null) {
				//Tracer._log("couldnt remove: " + param1);
				return false;
			} else if (dispose == true) {
				param1.dispose();
			}
			if (param1.parent == null) {
				//Tracer._log("couldnt remove: " + param1);
				return false;
			}
			var _loc_2:* = param1.parent;
			_loc_2.removeChild(param1);
			return true;
		} // end function
		
		public static function _safeRemoveChildren(param1:Object, dispose:Boolean = false):* {
			if (param1 == null) {
				//Tracer._log("couldnt remove: " + param1);
				return false;
			} else if (dispose == true) {
				
				if (param1.hasOwnProperty('texture')) param1.texture.dispose();
				
				if (param1.hasOwnProperty('numChildren')) {
					while (param1.numChildren > 0) {
						param1.getChildAt(0).dispose();
						param1.removeChildAt(0)	
					}
				
				}
				
				param1.dispose();
			}
			
			return null;
		}
		
		public static function _getScale9GridRect(sourceWidth:int = 100, sourceHeight:int = 100):Rectangle {
			
			var scale:uint = Starling.current.contentScaleFactor;
			var rect:Rectangle = new Rectangle(4*scale, 4*scale, sourceWidth - (4*scale * 2), sourceHeight - (4*scale * 2));
			
			return rect;
		}
		   
		   
		public static function _setButtonBitmapLabel(target:Button,  lab:String, yoff:Number, fontName:String, ls:Number, fontSize:int = -1):Button{
			
			var $btn:Button = Button(target);
			$btn.label = lab;
			$btn.labelOffsetY = yoff;
			
			var format:BitmapFontTextFormat = new BitmapFontTextFormat(fontName);
			format.letterSpacing = ls;
			
			format.align = TextFormatAlign.CENTER;
			if (fontSize != -1)
			{
				format.size = fontSize;
			}
			
			$btn.defaultLabelProperties.textFormat = format;
			
			$btn.validate();
			
			return $btn; 
			
		}
		
		
			public static function _addBtnSkinBFont(cont:*, label:String='', fStyle:BitmapFontTextFormat = null, bSkin:ImageSkin = null):Button {
				
				var btn:Button = new Button;
				//btn.fontStyles = fStyle;
				btn.label = label;
				btn.labelFactory = function():ITextRenderer{
					var renderer:BitmapFontTextRenderer = new BitmapFontTextRenderer();
					renderer.textFormat = fStyle;
					return renderer;
				};
				btn.defaultSkin = bSkin;
				
				cont.addChild(btn);
				btn.validate();
				return btn;
			}
		
		   
			public static function _addBtnSkin(cont:*, label:String='', fStyle:TextFormat = null, bSkin:ImageSkin = null):Button {
				
				var btn:Button = new Button;
				btn.fontStyles = fStyle;
				btn.label = label;
				btn.labelFactory = function():ITextRenderer {
					var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
					
					renderer.embedFonts = true;
					//renderer.textFormat = btnStyle
					return renderer;
				}
				btn.defaultSkin = bSkin;
				
				cont.addChild(btn);
				btn.validate();
				return btn;
			}
		   
		   public static function _changeFormatOfBitmapText(_bitmapTextfield:BitmapFontTextRenderer,
															_x:Number, 
															_y:Number,
															fontName:Object, 
															_align:String = TextFormatAlign.LEFT,
														   _isHTML:Boolean = false,
														   _letterSpacing:int = -3,
														   _size:int = -1,
														   _color:uint = 0xffffff):void {
												   
				var htmlTxt:BitmapFontTextRenderer = _bitmapTextfield;

				var format:BitmapFontTextFormat = new BitmapFontTextFormat(fontName);
				format.letterSpacing = _letterSpacing;
				if (_size != -1)
				{
					format.size = _size;
				}
				
				format.color = _color;
				format.align = _align;
				htmlTxt.textFormat = format;
				htmlTxt.x = _x;
			    htmlTxt.y = _y;
				htmlTxt.wordWrap = true;
				htmlTxt.touchable = false;
			    htmlTxt.validate();
		   }
		
		
		public static function _setButtonWithBitmapFont(cont:DisplayObjectContainer, 
													 propObj:Object, 
											  defaultTexture:Texture, 
												hoverTexture:Texture, 
												 downTexture:Texture, 
											 disabledTexture:Texture, 
												    fontName:String, 
												          ls:Number, 
												 fontSize:int = -1):Button{
																								   
			var $btn:Button = new Button();
			
			//$btn.useHandCursor = true;
			
			if (defaultTexture) $btn.defaultSkin = new Image(defaultTexture);
			if (hoverTexture) $btn.hoverSkin = new Image(hoverTexture);
			if (downTexture) $btn.downSkin = new Image(downTexture);
			if (disabledTexture) $btn.disabledSkin = new Image(disabledTexture);
			
			for (var prop:String in propObj){
				$btn[prop] = propObj[prop];
				
			}
			
			$btn.labelFactory = function():ITextRenderer{
				var textRenderer:BitmapFontTextRenderer = new BitmapFontTextRenderer();
				//textRenderer.width = $btn.width + 50;
				textRenderer.wordWrap = true;
				var format:BitmapFontTextFormat = new BitmapFontTextFormat(fontName);
				format.letterSpacing = ls;
				
				format.align = TextFormatAlign.CENTER;
				if (fontSize != -1)
				{
					format.size = fontSize;
				}
				textRenderer.textFormat = format
				
				 return textRenderer;
			}
			
			cont.addChild($btn);
			$btn.validate();
			$btn.pivotX = int($btn.width / 2);
			$btn.pivotY = int($btn.height / 2);
			
			return $btn; 
			
		}
		
		
		public static function _creatBitmapFontTextRenderer(cont:DisplayObjectContainer,
					  curText:String, 
					 _x:Number, 
					 _y:Number, 
					 _width:Number, 
					_height:Number,  
					 fontName:Object, 
					_align:String = TextFormatAlign.LEFT,
					  _isHTML:Boolean = false,
					  _letterSpacing:int = -3,
					  _size:int = -1,
					  _leading:int = 0,
					  _color:uint = 0xffffff):BitmapFontTextRenderer {
					   
			var htmlTxt:BitmapFontTextRenderer = new BitmapFontTextRenderer();

			var format:BitmapFontTextFormat = new BitmapFontTextFormat(fontName);
			
			format.letterSpacing = _letterSpacing;
			if (_size != -1)
			{
			 format.size = _size;
			}
			
			format.color = _color;
			format.align = _align;
			format.leading = _leading;
			
			htmlTxt.textFormat = format;
			htmlTxt.text = curText;
			htmlTxt.wordWrap = true;
			htmlTxt.touchable = false;
			   cont.addChild(htmlTxt);
			if(_width!=-1)htmlTxt.width = _width;
			htmlTxt.height = _height;
			  
			   htmlTxt.x = _x;
			   htmlTxt.y = _y;
			   
			   htmlTxt.validate();
			   return htmlTxt;   
					   
		}
		
		public static function _addTextInput(cont:DisplayObjectContainer, prompt_txt:String = '', inputStyle:TextFormat = null, promptStyle:TextFormat = null):TextInput {
			
			var input:TextInput = new TextInput;
			input.prompt = prompt_txt;
			input.fontStyles = inputStyle;
			input.promptFontStyles = promptStyle;
			
			input.promptFactory = function():ITextRenderer {
				var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				renderer.embedFonts = true;
				return renderer;
			};
			
			
			input.textEditorFactory = function():ITextEditor {
				var renderer:TextFieldTextEditor = new TextFieldTextEditor();
				renderer.embedFonts = true;
				return renderer;
			};
			
			
			cont.addChild(input);
			input.validate();
			return(input);
		}
		
		public static function _addAutoComplete(cont:DisplayObjectContainer, prompt_txt:String = '', inputStyle:TextFormat = null, promptStyle:TextFormat = null):AutoComplete {
			
			var input:AutoComplete = new AutoComplete;
			input.prompt = prompt_txt;
			input.fontStyles = inputStyle;
			input.promptFontStyles = promptStyle;
			
			input.promptFactory = function():ITextRenderer {
				var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				renderer.embedFonts = true;
				return renderer;
			};
			
			
			input.textEditorFactory = function():ITextEditor {
				var renderer:TextFieldTextEditor = new TextFieldTextEditor();
				renderer.embedFonts = true;
				return renderer;
			};
			
			
			cont.addChild(input);
			input.validate();
			return(input);
		}
		
		public static function _addBFTR(cont:DisplayObjectContainer, lab_txt:String = '', labStyle:BitmapFontTextFormat = null):BitmapFontTextRenderer {
			
			var lab:BitmapFontTextRenderer = new BitmapFontTextRenderer;
			
			lab.text = lab_txt;
			lab.textFormat = labStyle;
					
			cont.addChild(lab);
			lab.validate();
			return lab;
		}
		
		public static function _addLabelBFont(cont:DisplayObjectContainer, lab_txt:String = '', labStyle:BitmapFontTextFormat = null):Label {
			
			var lab:Label = new Label;
			lab.text = lab_txt;
			//lab.fontStyles = labStyle;
			
			lab.textRendererFactory = function():ITextRenderer {
				var renderer:BitmapFontTextRenderer = new BitmapFontTextRenderer();
				renderer.textFormat = labStyle;
				return renderer;
			};
			
			cont.addChild(lab);
			lab.validate();
			return lab;
		}
		
		public static function _addLabel(cont:DisplayObjectContainer, lab_txt:String = '', labStyle:TextFormat = null):Label {
			
			var lab:Label = new Label;
			lab.text = lab_txt;
			lab.fontStyles = labStyle;
			
			lab.textRendererFactory = function():ITextRenderer {
				var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				renderer.antiAliasType = AntiAliasType.ADVANCED;
				
				renderer.embedFonts = true;
				return renderer;
			};
			
			
			cont.addChild(lab);
			lab.validate();
			return(lab);
		}
		
		//[Inline]
		public static function _addButton(cont: DisplayObjectContainer,
										  xPos: int = 0,
										  yPos: int = 0,
										  text: String = null,
									    fstyle: TextFormat = null,
								          skin: ImageSkin = null):Button {
			
			var btn:Button = new Button();
			if (text) btn.label = text;
			if (fstyle) btn.fontStyles = fstyle;
			if (skin) btn.defaultSkin = skin;
			
			btn.labelFactory = function():ITextRenderer {
				var renderer:TextFieldTextRenderer = new TextFieldTextRenderer();
				renderer.embedFonts = true;
				//renderer.textFormat = btnStyle
				return renderer;
			}
			
			
			//btn.x = xPos;
			//btn.y = yPos;
			
			cont.addChild(btn);
			btn.validate();
			
			return btn;
		}
		
		
		[Inline]
		public static function _checkObj(obj:*):Boolean {
			if (obj != undefined) return true else return false;
		}
		public static function _updateButtonSkin(bt: Button,
										     btName: String = '',
									    defaultSkin: Texture = null,
								          hoverSkin: Texture = null,
									       downSkin: Texture = null):void {
			if (btName && btName != '') bt.name = btName;
			if (defaultSkin) bt.setSkinForState(ButtonState.UP, new Image(defaultSkin));  ButtonState.UP
			if (hoverSkin) bt.setSkinForState(ButtonState.HOVER, new Image(hoverSkin));
			if (downSkin) bt.setSkinForState(ButtonState.DOWN, new Image(downSkin));
		}
		
		
		//[Inline]
		public static function intWithZeros(num:int, length:int):String {
			var str:String = String(num);
			var strLen:int = str.length;
			var newStr:String = "";
			
			for (var i:int = 0; i < length - strLen; i++) {
				newStr += "0";
			}
			
			newStr = newStr + str;
			return newStr;
		}
		
		
		public static function setAlignPivot(disp:*, align:String = CENTER_CENTER):void
		{
			switch (align) 
			{
				case CENTER_CENTER:
					disp.pivotX = int(disp.width / 2);
					disp.pivotY = int(disp.height / 2);
				break;
				
				case TOP_CENTER:
					/*disp.pivotX = int(0);
					disp.pivotY = int(disp.height/2);*/
					disp.pivotX = int(disp.width / 2);
					disp.pivotY = int(0);
				break;
				
				case RIGHT_CENTER:
					disp.pivotX = int(disp.width);
					disp.pivotY = int(disp.height / 2);
				break;
				
				case RIGHT_TOP:
					disp.pivotX = int(disp.width);
					disp.pivotY = int(0);
				break;
				
			}
		}
		
		public static function random(min:int = 0, max:int = int.MAX_VALUE):int
		{
			if (min == max) return min;
			if (min < max) return min + (Math.random() * (max - min + 1));
			else return max + (Math.random() * (min - max + 1));
		}
		
		public static function randomTwoRange(firstRange:int, secondRange:int, diapason:int):int
		{
			var num:Number = Math.floor(Math.random() * 2);
			
			if (num == 0)
			{
				return random(firstRange - diapason, firstRange + diapason);
			}
			else
			{
				return random(secondRange - diapason, secondRange + diapason);
			}
		}
		
		
		[Inline]
		public static function isEvenInt(num:int):Boolean
		{
		  return (num % 2 == 0);
		}
		
		[Inline]
		public static function shuffleArray(arr:Array):Array
		{
			var shuffledArr:Array = new Array(arr.length);
			 
			var randomPos:Number = 0;
			for (var i:int = 0; i < shuffledArr.length; i++)
			{
				randomPos = int(Math.random() * arr.length);
				shuffledArr[i] = arr.splice(randomPos, 1)[0];   //since splice() returns an Array, we have to specify that we want the first (only) element
			}
			
			return shuffledArr;
		}
		
		
	
	}
}