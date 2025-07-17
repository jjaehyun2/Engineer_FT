package views.forms {
	import events.FormEvent;
	
	import starling.display.BlendMode;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.textures.Texture;

	public class CheckBox extends Sprite {
		private var _selected:Boolean = false;
		private var txtreOn:Texture = Assets.getAtlas().getTexture("checkbox-on");
		private var txtreOff:Texture = Assets.getAtlas().getTexture("checkbox-off");
		private var img:Image = new Image(txtreOff);
		private var isEnabled:Boolean = true;
		private var _id:String;
		public function CheckBox(_selected:Boolean=false) {	
			super();
			selected = _selected;
			img.x = 13;
			img.y = 13;
			img.addEventListener(TouchEvent.TOUCH,onClick);
			img.blendMode = BlendMode.NONE;
			render();
			addChild(img);
		}

		private function onClick(event:TouchEvent):void {
			var touch:Touch = event.getTouch(img);
			if(touch && touch.phase == TouchPhase.ENDED && isEnabled){
				_selected = !_selected ;
				render();
				this.dispatchEvent(new FormEvent(FormEvent.CHANGE,{value:_selected}));
			}
		}
		private function render():void {
			if(selected)
				img.texture = txtreOn;
			else
				img.texture = txtreOff;
		}
		
		public function enable(_b:Boolean):void {
			isEnabled = _b;
			img.alpha = (_b) ? 1 : 0.25;
		}

		public function get selected():Boolean {
			return _selected;
		}

		public function set selected(value:Boolean):void {
			_selected = value;
		}

		public function get id():String {
			return _id;
		}

		public function set id(value:String):void {
			_id = value;
		}
		

	}
}