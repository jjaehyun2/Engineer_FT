package 
{
	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import flash.events.Event;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	/**
	 * ...
	 * @author ...
	 */
	public class SelectTutorialPage extends MovieClip
	{
		protected const TUTS_PER_PAGE:uint = 3;
		protected var callback:Function;
		protected var buttonRects:Array;
		protected var firstButtonRect:Rectangle;
		protected var secondButtonRect:Rectangle;
		protected var thirdButtonRect:Rectangle;
		protected var currentSelection:int = -1;
		protected var currentVideoPathIndex:int = 1;
		public var moviePlaying:Boolean = false;
		protected var tutorialIndicator:TutorialIndicator;
		protected var videoPath:String;
		protected var originalPos:Point = new Point(0, 0);
		protected var hasButtons:Boolean;
		
		public function SelectTutorialPage() {}
		
		public function initialize(hasButtons:Boolean = true):void {
			this.hasButtons = hasButtons;
			
			tutorialIndicator = new TutorialIndicator();
			tutorialIndicator.y = 515;
			
			this.firstButtonRect = new Rectangle(10, 75, 240, 40);//10, 490, 240, 40);
			this.secondButtonRect = new Rectangle(251, 75, 240, 40);
			this.thirdButtonRect = new Rectangle(492, 75, 240, 40);
			
			this.buttonRects = new Array(this.firstButtonRect, this.secondButtonRect, this.thirdButtonRect);
			
			this.callback = defaultCallback;//callback;
			
			if (this.hasButtons) this.addEventListener(MouseEvent.MOUSE_MOVE, mouseMoved);
			if (this.hasButtons) this.addEventListener(MouseEvent.CLICK, mouseClicked);
			//this.addEventListener(Event.ENTER_FRAME, enterf);
			this.gotoAndStop(1);
		}
		
		protected function defaultCallback():void {
			//does nothing except avoid null error, make sure to set callback manually
			trace("SET");
		}
		
		public function setCallback(callback:Function):void {
			this.callback = callback;
		}
		
		public function enterf(e:Event):void {
			//trace(mouseX + " " + mouseY);
		}
		
		public function mouseMoved(e:MouseEvent):void {
			//trace(e.localX + " " + e.localY);
			var yOffset = moviePlaying ? 450 : 0;
			trace(yOffset);
			
			for (var i:int = 0; i < buttonRects.length; i++) {
				if (buttonRects[i].containsPoint(new Point(e.localX, e.localY - yOffset))) {
					this.gotoAndStop(moviePlaying ? i + 6 : i + 2);
					currentSelection = i;
					return;
				}
			}
			currentSelection = -1;
			this.gotoAndStop(moviePlaying ? 5 : 1);
		}
		
		public function mouseClicked(e:MouseEvent):void {
			if (currentSelection != -1) {
				callback();
				moviePlaying = true;
				if (this.contains(header)) header.gotoAndStop(currentSelection + 1);
				//if (!this.contains(tutorialIndicator)) this.addChild(tutorialIndicator);
				addTutorialIndicator(currentSelection);//tutorialIndicator.x = buttonRects[currentSelection].x + (buttonRects[currentSelection].width / 2);
			}
		}
		
		public function updateHeader():void {
			if (this.contains(header)) header.gotoAndStop(currentVideoPathIndex);
		}
		
		public function getVideoPath():String {
			trace(currentSelection);
			currentVideoPathIndex = currentSelection < 0 ? 1 : currentSelection + 1;
			return videoPath + "_" + (currentVideoPathIndex) + ".mp4";//currentSelection + 1) + ".mp4";
		}
		
		public function setVideoPath(path:String):void {
			this.videoPath = path;
		}
		
		public function getPreviousVideoPath():String {
			currentVideoPathIndex = (currentVideoPathIndex - 1) < 1 ? TUTS_PER_PAGE : currentVideoPathIndex - 1;
			
			updateHeader();
			addTutorialIndicator(currentVideoPathIndex - 1);
			return videoPath + "_" + currentVideoPathIndex + ".mp4";
			/*if (loop) return videoPath + "_" + ((currentVideoPathIndex - 1) < 1 ? TUTS_PER_PAGE : currentVideoPathIndex - 1) + ".mp4";
			else return videoPath + "_" + ((currentVideoPathIndex - 1) < 1 ? 1 : currentVideoPathIndex - 1) + ".mp4";*/
		}
		
		public function getNextVideoPath():String {
			currentVideoPathIndex = currentVideoPathIndex + 1 > TUTS_PER_PAGE ? 1 : currentVideoPathIndex + 1;
			
			updateHeader();
			addTutorialIndicator(currentVideoPathIndex - 1);
			return videoPath + "_" + currentVideoPathIndex + ".mp4";
			
			//return videoPath + "_" + (currentVideoPathIndex + 1) + ".mp4";
		}
		
		public function setOriginalPos(x:Number, y:Number):void {
			originalPos.x = x;
			originalPos.y = y;
			this.x = x;
			this.y = y;
		}
		
		public function addTutorialIndicator(frame:int = 0):void {
			if (hasButtons) {
				if (!this.contains(tutorialIndicator)) this.addChild(tutorialIndicator);
				tutorialIndicator.x = buttonRects[((frame >= 0) && (frame <= 2)) ? frame : 0].x + (buttonRects[((frame >= 0) && (frame <= 2)) ? frame : 0].width / 2);
			}
		}
		
		public function setToOriginalPos():void {
			this.x = originalPos.x;
			this.y = originalPos.y;
		}
		
		public function removeTutorialIndicator():void {
			if (hasButtons) if (this.contains(tutorialIndicator)) this.removeChild(tutorialIndicator);
		}
		
		public function getCurrentVideoPathIndex():int {
			return currentVideoPathIndex;
		}
	}
}