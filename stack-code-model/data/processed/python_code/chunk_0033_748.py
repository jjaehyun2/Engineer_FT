package view {
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import model.YuanJian;
	
	/**
	 * ...
	 * @author hongjie
	 */
	public final class YuanJianTip extends Sprite {
		
		private static var _instance:YuanJianTip;
		
		private var _mytf:TextFormat
		
		private var _nameTF:TextField;
		
		private var _codeTf:TextField;
		
		//private var _widthTf:TextField;
		//
		//private var _heightTf:TextField;
		
		public function YuanJianTip() {
			super();
			this.mouseChildren = false;
			this.mouseEnabled = false;
			
			_mytf = new TextFormat();
			_mytf.size = 16;
			_mytf.color = 0xffffff;
			_mytf.font = "黑体";
			
			var label:TextField = new TextField();
			label.text = 'name:';
			label.setTextFormat(_mytf);
			label.x = 10;
			label.y = 10;
			addChild(label);
			
			_nameTF = new TextField();
			_nameTF.text = 'dsfdsfdf';
			_nameTF.setTextFormat(_mytf);
			_nameTF.x = 50;
			_nameTF.y = label.y;
			addChild(_nameTF);
			
			label = new TextField();
			label.text = 'code:';
			label.setTextFormat(_mytf);
			label.x = 10;
			label.y = 30;
			addChild(label);
			
			_codeTf = new TextField();
			_codeTf.text = 'dsfdsfdfsdfdsfsfds';
			_codeTf.setTextFormat(_mytf);
			_codeTf.x = 50;
			_codeTf.y = label.y;
			addChild(_codeTf);
			
			//label = new TextField();
			//label.text = 'width:';
			//label.setTextFormat(_mytf);
			//label.x = 10;
			//label.y = 50;
			//addChild(label);
			//
			//_widthTf = new TextField();
			//_widthTf.text = 'dsfdsfdf';
			//_widthTf.setTextFormat(_mytf);
			//_widthTf.x = 50;
			//_widthTf.y = label.y;
			//addChild(_widthTf);
			//
			//label = new TextField();
			//label.text = 'height:';
			//label.setTextFormat(_mytf);
			//label.x = 10;
			//label.y = 70;
			//addChild(label);
			//
			//_heightTf = new TextField();
			//_heightTf.text = 'dsfdsfdf';
			//_heightTf.setTextFormat(_mytf);
			//_heightTf.x = 50;
			//_heightTf.y = label.y;
			//addChild(_heightTf);
		}
		
		public function setYuanJian(yuanJian:YuanJian):void {
			var h:int = 0;
			_nameTF.text = yuanJian.name;
			_nameTF.setTextFormat(_mytf);
			h = _nameTF.textWidth;
			_nameTF.width = _nameTF.textWidth + 10;
			
			_codeTf.text = yuanJian.code;
			_codeTf.setTextFormat(_mytf);
			h = h > _codeTf.textWidth ? h : _codeTf.textWidth;
			_codeTf.width = _codeTf.textWidth + 10;
			
			//_widthTf.text = yuanJian.reallyWidth.toString();
			//_widthTf.setTextFormat(_mytf);
			//h = h > _widthTf.textWidth ? h : _widthTf.textWidth;
			//
			//_heightTf.text = yuanJian.reallyHeight.toString();
			//_heightTf.setTextFormat(_mytf);
			//h = h > _heightTf.textWidth ? h : _heightTf.textWidth;
			
			const g:Graphics = this.graphics;
			g.clear();
			g.beginFill(0x000000, .6);
			g.drawRect(0, 0, h + 60, 60);
			g.endFill();
		}
		
		public static function get instance():YuanJianTip {
			if (!_instance) {
				_instance = new YuanJianTip();
			}
			return _instance;
		}
	
	}

}