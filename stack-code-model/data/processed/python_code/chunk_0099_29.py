package screens 
{
	import elements.Accumulated;
	import elements.Controls;
	import elements.Hud;
	import elements.Roulette;
	import managers.CacheManager;
	import managers.RouletteManager;
	import managers.SoundManager;
	import methods.Coins;
	import methods.System;
	import starling.display.Image;
	import starling.display.Sprite;
	/**
	 * ...
	 * @author LeleoSan
	 */
	public class Game extends Sprite
	{
		/** objects */
		private var accumulated:Accumulated;
		private var roulettes:RouletteManager;
		private var controls:Controls;
		private var hud:Hud;
		private var cacheData:CacheManager;
		/** consts */
		private const CASH_DEFAULT:int = 1000;//1000
		private const BET_MAX:int = 500;
		private const TO_ACCUMU:int = 10;
		/** variables */
		private var cash:int;
		private var bet:int;
		private var win:int;
		private var playing:Boolean;
		
		public function Game() 
		{
			cacheData = new CacheManager();
			
			cash = CASH_DEFAULT;
			bet = 0;
			win = 0;
			playing = false;
			
			addChild(new Image(Root.assets.getTexture("bg2")));
			addChild(new Image(Root.assets.getTexture("interface")));
			accumulated = new Accumulated();
			addChild(accumulated);
			addChild(new Image(Root.assets.getTextureAtlas("spriteAll").getTexture("logoGame.png")));
			
			roulettes = new RouletteManager();
			addChild(roulettes);
			
			controls = new Controls(getClick);
			addChild(controls);
			
			hud = new Hud();
			addChild(hud);
			
			hud.setText(Hud.CREDITS, String(cash));
			hud.setText(Hud.BET, String(bet));
			hud.setText(Hud.WIN, String(win));
			
			controls.events("add");
		}
		private function getClick(_name:String):void
		{
			switch (_name) {
				case "Menu":
					
					break;
				case "Spin":
					if (!playing && bet > 0) {
						playing = true;
						SoundManager.play(SoundManager.FX_LEVER, 0, SoundManager.C_EFFECTS);
						if (!Accumulated.active) {
							Accumulated.count++;
							if (Accumulated.count >= TO_ACCUMU) {
								accumulated.setStatus(true);
							}
						}
						roulettes.turning(System.getValues(), result);
						cacheData.saveCash(cash);
					}
					break;
				default:
					var valueBet:int = 0;
					if (_name == "Max") {
						if (cash == 0) {
							SoundManager.play(SoundManager.FX_NOMONEY, 0, SoundManager.C_EFFECTS);
						} else {
							SoundManager.play(SoundManager.FX_BET, 0, SoundManager.C_EFFECTS);
						}
						valueBet = BET_MAX;
					} else if (_name == "Clear") {
						cash = cash + bet;
						bet = 0;
					} else if (_name.indexOf("Bet") != -1) {
						if (cash == 0) {
							SoundManager.play(SoundManager.FX_NOMONEY, 0, SoundManager.C_EFFECTS);
						} else {
							SoundManager.play(SoundManager.FX_BET, 0, SoundManager.C_EFFECTS);
						}
						valueBet = int(_name.replace("Bet", ""));
					}
					if ((cash - valueBet) >= 0 && (bet + valueBet) <= BET_MAX) {
						bet += valueBet;
						cash -= valueBet;
					}
					hud.setText(Hud.BET, String(bet));
					hud.setText(Hud.CREDITS, String(cash));
			}
		}
		private function result(_values:Array):void
		{
			trace("#: " + _values);
			//_values = ["bar", "bar", "bar"];////////////////////////////////// TEMP
			
			var mulberryAmount:int = 0;
			for (var i:int = 0; i < _values.length; i++) {
				if (_values[i] == "mulberry") { mulberryAmount++; }
			}
			if (mulberryAmount > 0) {
				jackpot("mulberry", mulberryAmount);
			} else if (_values[0] == _values[1] && _values[1] == _values[2]) {
				jackpot(_values[0], 3);
			} else {
				jackpot("");
			}
		}
		private function jackpot(_name:String, _type:int = 1):void
		{
			win = 0;
			if (_type == 3) {
				win = bet * Roulette.getPrize(_name);
				SoundManager.play(SoundManager.FX_PAY, 0, SoundManager.C_EFFECTS);
				if (_name == "bar" || _name == "seven" || _name == "clover") {
					SoundManager.play(SoundManager.FX_JACKSPOT1, 0, SoundManager.C_EFFECTS);
					Coins.to(this, 50, 0.7, freeToPlay);
				} else {
					SoundManager.play(SoundManager.FX_JACKSPOT0, 0, SoundManager.C_EFFECTS);
					Coins.to(this, 30, 0.5, freeToPlay);
				}
				if (Accumulated.active) {
					accumulated.setStatus(false);
					win = win * accumulated.PAY;
					SoundManager.play(SoundManager.FX_ACCUMULATED, 0, SoundManager.C_EFFECTS);
				}
			} else if (_name == "mulberry") {
				if (_type == 2) {
					win = Roulette.MULBERRY_PRIZE2;
					Coins.to(this, 20, 0.3, freeToPlay);
				} else {
					win = Roulette.MULBERRY_PRIZE;
					Coins.to(this, 10, 0.3, freeToPlay);
				}
				SoundManager.play(SoundManager.FX_PAY, 0, SoundManager.C_EFFECTS);
			}			
			bet = 0;
			cash = cash + win;
			cacheData.saveCash(cash);
			hud.setText(Hud.CREDITS, String(cash));
			hud.setText(Hud.BET, String(bet));
			hud.setText(Hud.WIN, String(win));
			
			if (_type != 3 && _name != "mulberry") {
				freeToPlay();
			}
		}
		private function freeToPlay():void
		{
			playing = false;
			if (cash == 0) {
				trace("ACTIVE CLOCK");
			}
		}
		public function destroy():void
		{
			if (accumulated) { accumulated.destroy(); accumulated = null; }
			if (roulettes) { roulettes.destroy(); roulettes = null; }
			if (controls) { controls.destroy(); controls = null; }
			if (hud) { hud.destroy(); hud = null; }
			removeChildren(0, -1, true);
			removeFromParent(true);
		}
	}

}