package
{
	import com.baseoneonline.flash.astar.AStar;
	import com.utilities.BitMapper;
	import com.utilities.Clock;
	import com.utilities.EmbedSecure;
	import com.utilities.Scoring_Floater;
	import com.utilities.Scoring_counter;
	
	import flash.display.Bitmap;
	import flash.display.MovieClip;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.events.TextEvent;
	import flash.geom.Point;
	import flash.text.TextField;
	
	//import net.hires.debug.Stats;
	/**
	 * ...
	 * @author Ian Stokes www.unit2design.com 2010
	 */
	public class Hud extends Sprite
	{
		private var _bugWindow:Sprite = new Sprite()	
		private var _bugText:TextField = new TextField()
		
		public var _scoreSprite:Sprite = new Sprite();
		private var _scoreObj:Scoring_counter
		
		public var floatCash:Number; 
		private var _dispatchType:String;
		private var _aStar:AStarTest
		//counters
		public var _clock:Clock;
		private var _clockSprite:Sprite = new Sprite()
		public var startTime:String;
		//
		public var _level:Scoring_counter
		private var _levelSprite:Sprite = new Sprite()
		//
		public var _coms:Scoring_counter
		private var _comsSprite:Sprite = new Sprite()
		//
		public var _cash:Scoring_counter
		private var _cashSprite:Sprite = new Sprite()
		//
		public var _exp:Scoring_counter
		private var _expSprite:Sprite = new Sprite()
		//
		private var _art:EmbedSecure;
		private var _numberArt:Class
		//
		private var _muteButton:Sprite = new Sprite();
		private var game:Boolean = false;
		//private var _textUnit:Class
		
		private var _floatingScoreArt:Array = new Array
		private var _scoreToWin:Number=0
		public static const EVENT_TIMEOUT:String = "event_timeout_hud"
		public static const EVENT_WIN:String = "event win"
		public static const EVENT_MUTE:String = "event_mute"
		
		private var won:Boolean = false;
		
		// Right now the hud is getting created at every level start. 
		// Probably best use of resources.
		public function Hud(art:EmbedSecure = null) 
		{
			_art=art
			this.name = "HUD";
			if (Main.debug) {
				_bugWindow.graphics.beginFill(0x000000);
				_bugWindow.graphics.drawRect(100, 0, 200, 100);
				_bugText.width = 200;
				_bugText.x = 105;
				_bugWindow.graphics.endFill();
				_bugText.textColor = 0xffffff;
				_bugText.text = "debug";
				_bugWindow.addChild(_bugText);
				_bugWindow.x=400
				//addChild(_bugWindow);
			//	_bugWindow.addChild(new Stats()) ;
				//_aStar = new AStarTest()
				//addChild(_aStar)
				//_aStar.x=450
				counterSetup()
			};
			
		}
		private function counterSetup():void {
			
			var bitMapper:BitMapper = new BitMapper();
			var numberArtAr:Array = bitMapper.buildDataObject("scoring", 1, 14, new numbas());
			//
			_clock = new Clock ("00:00", numberArtAr, _clockSprite, { x:0, y:0 } );
			_clock.addEventListener(Clock.LEVELEND_EVENT,timeOut);
			//_clockSprite.scaleX = .7
			//_clockSprite.scaleY = .7
			_clockSprite.y = 0;
			_clockSprite.x = 55;
			addChild( _clockSprite);
			var clock:MovieClip = new textUnit();
			clock.x = _clockSprite.x - 70;
			clock.copy.text = "TIME";
			addChild(clock);
			////
			_level = new Scoring_counter ("000", numberArtAr, _levelSprite);
			_levelSprite.x = 274;
			
			addChild(_levelSprite);
			var lev:MovieClip=new textUnit()
			lev.x=_levelSprite.x-70
			addChild(lev)
			
			
			
			
			// cash HUD	
			_cash = new Scoring_counter ("00000", numberArtAr, _cashSprite);
			_cashSprite.x = 510;
			addChild(_cashSprite);
			
			var cashText:MovieClip=new textUnit();
			cashText.x=_cashSprite.x-70
			addChild(cashText)
			cashText.copy.text="CASH"
			
			//XP HUD	
			_exp = new Scoring_counter ("000", numberArtAr, _expSprite);
			_expSprite.x = 660
			//addChild(_expSprite);
			
			var exp:MovieClip = new textUnit();
			exp.x = _expSprite.x - 70
			exp.copy.text="XP"
			//addChild(exp)
			
			//Coin HUD
			_coms = new Scoring_counter ("000", numberArtAr, _comsSprite);
			_comsSprite.x=395;
			//addChild(_comsSprite);
			
			var com:MovieClip = new textUnit();
			com.x = _comsSprite.x - 70;
			com.copy.text="COINS";
			//addChild(com);
			
			
			
			//temp
			level=1
		}
		
		private function overMuteButton(event:Event):void
		{
			//trace("overMuteButton...");
		}
		//****getters & setters*********
		
		public function set level(num:uint):void {
			_level.updatePoints(num)
		}
		
		public function set coins(num:uint):void {
			if (game)
				_coms.addPoints(num)
		}
		public function set cash(num:uint):void {
			if (game)
			{
				_cash.addPoints(num)
				checkScore()
			}
			
		}

		public function get muteButton():Sprite {
			return _muteButton	
		}
		////end
		public function reset():void {
			game = false;
			_level.rst();
			_coms.rst();
			_cash.rst();
			_exp.rst();
		}
		
		public function setClock(time:String):void {
			trace("Setting clock: " + time);
			_clock.startClock(time);
		}
		public function stopClock():void{
			_clock.stopClock();
		}
		
		public function resetAll():void {
			trace("Resetting Hud");
			_level.rst();
			_coms.rst();
			_cash.rst();
			_exp.rst();
			game = true;
			_clock.startClock(Main.currentSetting.start_time);
		}
		
		private function setupFloaterScore():void {
			trace("setupFloaterScore")
			
			//var bitMapper2:BitMapper = new BitMapper();
			// _messaging = bitMapper2.buildDataObject("messaging", 1, 2, new _messages());
			var bitMapper:BitMapper = new BitMapper();
			_floatingScoreArt = bitMapper.buildDataObject("floating score", floatCash, 11,new numbas());
		}
		
		public function floatScore(targ:Sprite,num:Number,loc:Point):void {
			trace('Hud.floatScore: '+num);
			cash = num;
			floatCash = num;
		}

		private function timeOut(event:Event):void {
			_dispatchType = event.target.name;
			dispatchEvent(new Event(EVENT_TIMEOUT, true));
		}
		public function get dispatchType():String {
			return _dispatchType;
		}
		public function set scoreToWin(sc:Number):void {
			_scoreToWin = sc;
		}
		public function get scoreToWin():Number {
			return _scoreToWin;
		}
		public function checkScore():void {
			if (_cash.currentScore >= _scoreToWin && !won) {
				won = true;
				dispatchEvent(new Event(EVENT_WIN, true));
			}
		}
	}
}