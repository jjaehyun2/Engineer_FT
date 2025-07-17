package {
	import as3isolib.display.scene.IsoGrid;
	import as3isolib.geom.IsoMath;
	import as3isolib.geom.Pt;
	

	import com.greensock.TweenLite;
	import com.utilities.EmbedSecure;
	
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.filters.GlowFilter;
	import flash.geom.Point;
	import flash.trace.Trace;
	import flash.utils.Timer;
	
	import masputih.isometric.Tile;
	import masputih.isometric.World;
	import masputih.isometric.*;
	
	
	/**
	 * ...
	 * @author Ian Stokes
	 */
	public class Character extends MovableTile{
		public var art:MovieClip
		public var poz:Object
		public var spritePoz:Point
	
		
		public var _active:Boolean = false
		public var _state:String="notActive"
		public var _type:String = "farmer"
		public var newContainer:MovieClip
		public var _destinationTimer:Timer
		public var _destinationTimer2:Timer
		public var _startPosition:Point
		public var _myPlot:FarmPlot
		public var _myServiceTable:ServiceTable

		public var _myOrder:MovieClip
		public var _orderStage:uint=0
		public var _orderObjHolder:Sprite
		public var _orderObjHolder2:Sprite
		public var _currentInnovation:Number=1
		public var itemOnTable:MovieClip
		public var atTable:Boolean = false
		public var atTrash:Boolean=false
		public var typeCollected:Number = 0
		public var plotCompleted:Boolean = false;
		public var orderPresentOnTable:Boolean = false
		//public var avatarIsPacking:uint = 0;
		public var _spriteOriginY:Number = 0;
		public var _spriteOriginX:Number = 0;
		public var _bubbleSn:Number = 0
		public var _currentMessage:String
		public var _embed:EmbedSecure
		public var _leaveState:String = "happy"
		public var activelyMoving:Boolean = false;
		public var currentPlot:FarmPlot;
		public var itemToGet:MovieClip
		public var _grid_reference:IsoGrid;
		public var _world_reference:World;
		
		
		public function Character(iso:IsoGrid, typ:String = "farmer_male", artz:EmbedSecure = null, world:World = null) {
			//_embed=artz
			_world_reference = world;
			_grid_reference = iso;
			setSkin(typ);
			super(iso);
			
			sprites=[art];
			art.x -= (art.width / 2);
			art.y -= (art.height / 2) + 20;
			art.mouseEnabled = false;
			if (art.orderObjHolder) {
				art.orderObjHolder.alpha = 0;
				
				while (itemGot.numChildren > 0) { itemGot.removeChildAt(0) }
			}
			_spriteOriginY = art.y;
			_spriteOriginX = art.x;	
			//_spriteOriginY = 0;
			//_spriteOriginX = 0;	
			spans = [0, 0];
			newContainer = container as MovieClip;
			newContainer.newParent = this;
	
		}
		public function setSkin(typ:String):void {
			_type=typ
			
			switch(_type) {
				case "farmer_male":
					var skin:Class = farmerClip;
					break
				case "farmer_female":
					skin= avatarClip_female;
					break
				case "player_male":
					//trace("setting skin to male")
					skin= avatarClip_male;
					break
				case "player_female":
					skin= avatarClip_female;
					break	
				case null:
					skin= farmerClip;
					break
			}
			
			//trace("incoming type"+_type)
			art=new skin();
			//art = skin;
			
			
		}
		
		public override function onTweenStart(...args):void {
			dirInc = 1;
			//sprites[0].gotoAndStop("forward");
			//trace(this.directionAr.length);
			if (this.directionAr.length > 1)
				sprites[0].gotoAndStop(this.directionAr[dirInc]);
			else 
				sprites[0].gotoAndStop("stand");
			dirInc++;
			
		}
		public function makeHot(event:Event):void {
			Main.soundSet["select"].play();
			this.container.dispatchEvent(new Event(AllSettings.EVENT_CURRENTFARMER, true));
		}
		public function removeHot():void {
			
			//removeStroke();
		}
		public function addStroke(event:Event):void {
			Main.soundSet["select3"].play()
			//trace("add stroke")
			var filt:Array = new Array();
			var g:GlowFilter = new GlowFilter(0xFFFF00, 1, 3, 3, 100);
			filt.push(g);
			mainContainer.filters = filt;
		}
		public function removeStroke(event:Event=null):void 
		{
			//trace("removeStroke...");
			if (!_active) {
				
				var filt:Array = new Array();
				mainContainer.filters = new Array()	}	
		}
		
		public function get type():String {
			return _type;
		}
		public function set state(str:String):void {
			_state = str;
		}
		public function get state():String {
			return _state;
		}
		public function set enabled(bol:Boolean):void {
			this.newContainer.mouseEnabled = bol;
			this.newContainer.buttonMode = bol
			
		}
		public function set gameStartPosition(pt:Point):void {
			_startPosition = pt;
		}
		public function set plot(plt:FarmPlot):void {
			
			_myPlot = plt;
			//if(!_myPlot){_myPlot.orderTaken=false}
			
		}
		public function get plot():FarmPlot {
			return _myPlot;
		}
		public function set myServiceTable(tbl:ServiceTable):void {
			_myServiceTable = tbl;
		}
		public function get itemGot():MovieClip {
			return art.orderObjHolder;
		}
		public function get orderStage():uint {
			return _orderStage;
		}
		public function set orderStage(num:uint):void {
			_orderStage = num;
		}
		public function set currentInnovation(num:Number):void {
			_currentInnovation = num;
		}
		public function get currentInnovation():Number {
			return _currentInnovation
		}
		
		public function get currentMessage():String {
			return _currentMessage;
		}

		public function set leaveState(str:String):void {
			_leaveState = str;
		}
	}
	
}