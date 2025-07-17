package com.profusiongames.windows 
{
	import com.profusiongames.beings.Player;
	import starling.display.Image;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.text.TextField;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class UpgradeArea extends Sprite 
	{
		[Embed(source = "../../../../lib/Graphics/menus/upgrades menu/upgraded.png")]private var _mark:Class;
		private var _ticks:int;
		private var _list:Vector.<Image> = new Vector.<Image>();
		
		private var _sep:int = 20;
		private var _priceField:TextField;
		private var _upgradeButton:UpgradeButton;
		private var _prices:Array;
		private var _callback:Function;
		public function UpgradeArea(dx:int, dy:int, prices:Array, onSuccessUpgradeCallback:Function ) 
		{
			x = dx;
			y = dy;
			_prices = prices;
			_callback = onSuccessUpgradeCallback;
			//touchable = false;
			
			_priceField = new TextField(40, 24, "$$$", "Cartoonist", 22, 0xEEEEEE, true);
			_priceField.border = true;
			
			_priceField.x = 109;
			addChild(_priceField);
			
			_upgradeButton = new UpgradeButton();
			_upgradeButton.x = 150;
			_upgradeButton.addEventListener(Event.TRIGGERED, upgrade);
			addChild(_upgradeButton);
			
			ticks = 0;
		}
		
		private function upgrade(e:Event):void 
		{
			//check price.
			//subtract price
			//update tick
			if (_prices[ticks] != "max" && Player.money > _prices[ticks])
			{
				Player.money -= _prices[ticks];
				ticks++;
				_callback();
			}
		}
		
		public function get ticks():int 
		{
			return _ticks;
		}
		
		public function set ticks(value:int):void 
		{
			if (value > 5) return;
			if (value < 0) return;
			if (value > _ticks)
			{
				//add more ticks
				for (var i:int = _ticks; i < value; i++)
				{
					var t:Image = new Image(Texture.fromBitmap(new _mark()));
					t.x = _sep * _list.length;
					_list.push(t);
					addChild(t);
					if (_list.length >= 3)
						t.x += 1;
				}
			}
			else
			{
				//remove some ticks
				for (var i2:int = value; i2 < _ticks; i2++)
				{
					var t2:Image = _list[i2];
					removeChild(t2);
					t2.dispose();
				}
				_list.length = value;
			}
			_ticks = value;
			
			_priceField.text = "" + _prices[ticks];
		}
		
		public function set price(value:int):void
		{
			_priceField.text = "" + value;
		}
		
	}

}