package  
{
	import flash.display.Sprite;
	import flash.events.KeyboardEvent;
	import flash.events.MouseEvent;
	import flash.filters.BlurFilter;
	/**
	 * ...
	 * @author UnknownGuardian
	 */
	public class BetterUpgradeBar extends UpgradeBar
	{
		public var c:Child;
		
		public function BetterUpgradeBar() 
		{
			MMaxAmmo.addEventListener(MouseEvent.CLICK, maxAmmoClick);
			MAmmoReload.addEventListener(MouseEvent.CLICK, ammoReloadClick);
			MAmmoTransfer.addEventListener(MouseEvent.CLICK, ammoTransferClick);
			CMaxAmmo.addEventListener(MouseEvent.CLICK, childMaxAmmoClick);
			CForce.addEventListener(MouseEvent.CLICK, forceClick);
			CLife.addEventListener(MouseEvent.CLICK, lifeClick);
			CShotSpeed.addEventListener(MouseEvent.CLICK, CShotSpeedClick);
			childCreate.addEventListener(MouseEvent.CLICK, childCreateClick);
		}
		
		private function childCreateClick(e:MouseEvent):void 
		{
			c = new Child();
			c.isHeld = true;
			c.x = e.stageX;
			c.y = e.stageY;
			DataManager.children.push(c);
			Layers.Display.addChild(c);
			c.addEventListener(MouseEvent.CLICK, placeChild);
			stage.addEventListener(KeyboardEvent.KEY_UP, doNotPlaceChild);
		}
		
		private function doNotPlaceChild(e:KeyboardEvent):void 
		{
			c.kill();
			stage.removeEventListener(KeyboardEvent.KEY_UP, doNotPlaceChild);
			c.removeEventListener(MouseEvent.CLICK, placeChild);
			c = null;
		}
		
		private function placeChild(e:MouseEvent):void 
		{
			if (c.x > 480)
			{
				c.x = 480;
			}
			Layers.Display.removeChild(c);
			Layers.Ships.addChild(c);
			c.isHeld = false;
			c.removeEventListener(MouseEvent.CLICK, placeChild);
			stage.removeEventListener(KeyboardEvent.KEY_UP, doNotPlaceChild);
			c = null;
		}
		
		private function CShotSpeedClick(e:MouseEvent):void 
		{
			DataManager.childShotSpeed--;
			shootSpeedText.text = DataManager.childShotSpeed.toString();
		}
		
		private function lifeClick(e:MouseEvent):void 
		{
			DataManager.childLife++;
			lifespanText.text = DataManager.childLife.toString();
		}
		
		private function forceClick(e:MouseEvent):void 
		{
			DataManager.childForce++;
			pushForceText.text = DataManager.childForce.toString();
		}
		
		private function childMaxAmmoClick(e:MouseEvent):void 
		{
			DataManager.childMaxAmmo++;
			childMaxAmmoText.text = DataManager.childMaxAmmo.toString();
		}
		
		
		private function ammoTransferClick(e:MouseEvent):void 
		{
			DataManager.childTransferRate--;
			ammoTransferText.text = DataManager.childTransferRate.toString();
			if (DataManager.childTransferRate == 0)
			{
				MAmmoTransfer.enabled = false;
				MAmmoTransfer.removeEventListener(MouseEvent.CLICK, ammoTransferClick);
				MAmmoTransfer.filters = [new BlurFilter(2, 2, 1)];
			}
		}
		
		private function ammoReloadClick(e:MouseEvent):void 
		{
			DataManager.mother.bulletReloadRate++;
			ammoReloadText.text = DataManager.mother.bulletReloadRate.toString();
		}
		
		private function maxAmmoClick(e:MouseEvent):void 
		{
			DataManager.mother.bulletReserveMax += 500;
			maxAmmoText.text = DataManager.mother.bulletReserveMax.toString();
		}
		
	}

}