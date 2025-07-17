package
{
	/**
	 * ...
	 * @author ian
	 */
	import as3isolib.display.scene.IsoGrid;
	import com.utilities.EmbedSecure;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.filters.GlowFilter;
	import flash.utils.Timer;
	import masputih.isometric.Box;
	public class TrashUnit extends Box
	{
		private var _art:EmbedSecure;
		private var _artSprite:MovieClip;
		private var _innovationAr:Array = new Array();
		private var _curNum:Number = 0
		public var plot:MovieClip = new MovieClip()
		public var cellLocation:Object = new Object()
		private var _currentItemToGet:MovieClip
		private var _currentSearchNum:Number=0
		public static const EVENT_CALL_PLAYER:String = "call player";
		public var myName:String="table"
		public function TrashUnit(iso:IsoGrid,boxHeight:Number,art:EmbedSecure,cellX:Number,cellY:Number) 
		{
			cellLocation = { x:cellX, y:cellY };
			_art=art
			super(iso, boxHeight)
			this.myName="table"
			fillColor = Math.random() * 0xFFFFFF;
			spans = [2, 2]
			walkable = false
			// erik
			//var tableArt:Class = _art.grabClass("trash");
			_artSprite = new trash()
		   _artSprite.mouseEnabled=true
			sprites = [_artSprite]
			_artSprite.buttonMode = true;
		   _artSprite.useHandCursor=true
			_artSprite.addEventListener(MouseEvent.MOUSE_OVER, addStroke)
			_artSprite.addEventListener(MouseEvent.MOUSE_OUT, removeStroke)
			_artSprite.addEventListener(MouseEvent.MOUSE_DOWN, clicked);
			//setupInnovations()
			plot.myParent=this
		}
		private function driveAvatar():void {
			
			plot.cellLocation=cellLocation
			
			plot.dispatchEvent(new Event(EVENT_CALL_PLAYER, true))
			
			}
		private function addStroke(event:Event):void {
			//trace("add trash stroke")
			var filt:Array = new Array();
			var g:GlowFilter = new GlowFilter(0xff0000, 1, 3, 3, 100);
			filt.push(g);
			event.target.filters = filt;
		}
		private function removeStroke(event:Event):void {
			var filt:Array = new Array();
			event.target.filters = new Array()		}
		
		private function clicked(event:Event):void {
			removeStroke(event)
			
			_currentItemToGet=event.currentTarget as MovieClip
			 driveAvatar();
		}
	}

}