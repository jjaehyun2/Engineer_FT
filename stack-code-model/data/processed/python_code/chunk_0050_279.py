package com.fw.view.ui.mainui.battle
{
	import com.fw.mgr.WndMgr;
	import com.fw.view.comps.base.GamePanel;
	import com.fw.view.ui.battlegateinfo.BattleGateInfoWnd;
	import com.fw.view.ui.mainui.battle.scene.BattleGateBtn;
	import com.fw.view.ui.mainui.battle.scene.BattleMapScene;
	import com.fw.view.ui.mainui.battle.scene.CloudLayer;
	import com.losttemple.utils.AssetsUtil;
	
	import starling.display.Sprite;
	import starling.events.Event;
	
	public class BattlePanel extends GamePanel implements IBattleCloud
	{
		private var _mapScene:BattleMapScene;
		private var _stageBtnLayer:Sprite;
		private var _cloudLayer:CloudLayer;
		
		public function BattlePanel(w:int, h:int)
		{
			super(w, h);
		}
		
		override protected function initialize():void
		{
			_mapScene = new BattleMapScene(this);
			addChild(_mapScene);
			_mapScene.drawBg(AssetsUtil.getImgsUrlByName("bigpic/map2.jpg"), initOtherLayer);
			_mapScene.scale = 0.6;
			
		}
		
		private function initOtherLayer():void
		{
			_stageBtnLayer = new Sprite();
			addChild(_stageBtnLayer);
			var gateBtn:BattleGateBtn = new BattleGateBtn();
			_stageBtnLayer.addChild(gateBtn);
			gateBtn.x = 750;
			gateBtn.y = 1150;
			gateBtn.addEventListener(Event.TRIGGERED, onClickGate);
			
			_cloudLayer = new CloudLayer(_mapScene.maxwidth, _mapScene.maxheight);
			addChild(_cloudLayer);
			updateCloudLayer();
		}
		
		private function onClickGate(e:Event):void 
		{
//			trace("gate");
			WndMgr.intstance.showWindow(BattleGateInfoWnd);
		}
		
		public function updateCloudLayer():void
		{
			if(_cloudLayer == null)
				return;
			_cloudLayer.scaleX = _cloudLayer.scaleY = _mapScene.scale;
			_cloudLayer.x = _mapScene.x;
			_cloudLayer.y = _mapScene.y;
			
			if(_stageBtnLayer == null)
				return;
			_stageBtnLayer.scaleX = _stageBtnLayer.scaleY = _mapScene.scale;
			_stageBtnLayer.x = _mapScene.x;
			_stageBtnLayer.y = _mapScene.y;
		}
		
	}
}