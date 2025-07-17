package 
{
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.net.URLLoaderDataFormat;
	import flash.text.TextField;
	
	/**
	 * ...
	 * @author Ben Mason
	 */
	public class GlossaryScreenGraphic extends MovieClip
	{
		private var callBackClip:MovieClip;
		private var buttonFactory:ButtonFactory;
		private var closeButton:ApplicationButton;
		private var textFileLoader:URLLoader;
		
		private var glossaryItemDisplay:GlossaryItemDisplay;
		private var partItems:Array = new Array();
		private var partItemContainer:Sprite;
		
		public function GlossaryScreenGraphic(callBackClip:MovieClip) {
			this.callBackClip = callBackClip;
			buttonFactory = new ButtonFactory();
			closeButton = buttonFactory.create(ButtonFactory.SUBSCREEN_CLOSE, closeButtonClicked);
			closeButton.x = 395;
			closeButton.y = -206;
			glossaryItemDisplay = new GlossaryItemDisplay();
		}
		
		private function createItems(e:Event):void {
			var textFile:String = textFileLoader.data;
			partItemContainer = new Sprite();
			var partNames:Array = textFile.split("\n");
			trace(partNames[0]);
			
			var tempX:int = -220;
			var tempY:int = -134;//-174;
			
			for (var i:int = 1; i <= partNames.length; i++) {
				var item = new GlossaryItem(partNames[i - 1], i);
				item.x = tempX + ((i > 8) ? 240 : (i > 12) ? 480 : 0);
				item.y = tempY;
				partItems.push(item);
				partItemContainer.addChild(item);
				trace(item.height);
				tempY += item.height;
				if (i == 8 || i == 12) tempY = -134;
			}
			this.addChild(partItemContainer);
			partItemContainer.addChild(item);
			partItemContainer.addEventListener(MouseEvent.MOUSE_OVER, changeItemDisplay);
			partItemContainer.addEventListener(MouseEvent.MOUSE_OUT, removeItemDisplay);
		}
		
		private function changeItemDisplay(e:MouseEvent):void {
			if (e.target is TextField) {
				if (e.target.parent is GlossaryItem) {
					glossaryItemDisplay.changeDisplay(e.target.parent.getPartIndex());
					glossaryItemDisplay.setPos(e.target.parent.x + e.target.parent.width, e.target.parent.y + e.target.parent.height / 2);
					trace(glossaryItemDisplay.y);
					if (!this.contains(glossaryItemDisplay)) this.addChild(glossaryItemDisplay);
				}
			}
			else if (e.target is GlossaryItem) {
				glossaryItemDisplay.changeDisplay(e.target.getPartIndex());
				if (!this.contains(glossaryItemDisplay)) this.addChild(glossaryItemDisplay);
				glossaryItemDisplay.setPos(e.target.x + e.target.width, e.target.y + e.target.height / 2);
			}
		}
		
		private function removeItemDisplay(e:MouseEvent):void {
			if (this.contains(glossaryItemDisplay)) this.removeChild(glossaryItemDisplay);
		}
		
		public function animate():void {
			addEventListener(Event.ENTER_FRAME, animateToEnd);
		}
		
		private function animateToEnd(e:Event):void {
			if (this.currentFrame == 1) {
				this.play();
			} else {
				if (this.currentFrame == this.totalFrames) {
					this.stop();
					this.addChild(closeButton);
			
					if (textFileLoader == null) {
						textFileLoader = new URLLoader(new URLRequest("files/glossary_part_names.txt"));
						textFileLoader.addEventListener(Event.COMPLETE, createItems);
					}
					else {
						this.addChild(partItemContainer);
					}
					removeEventListener(Event.ENTER_FRAME, animateToEnd);
				}
			}
		}
		
		public function closeButtonClicked():void {
			this.gotoAndStop(1);
			this.removeChild(closeButton);
			this.removeChild(partItemContainer);
			callBackClip.closeGlossaryScreen();
		}
	}
}