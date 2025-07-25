package com.ui.item
{
	import com.game.consts.ConstFlowTipSize;
	import com.game.module.CDataManager;
	import com.ui.util.CBaseUtil;
	import com.ui.util.CFilterUtil;
	
	import flash.display.MovieClip;
	
	import flash.events.TouchEvent;
	import flash.geom.Point;
	
	import framework.fibre.core.Notification;
	import framework.resource.faxb.items.Item;
	import framework.rpc.NetworkManager;
	import framework.util.ResHandler;
	import framework.view.notification.GameNotification;
	
	/**
	 * @author caihua
	 * @comment 气泡里面的道具
	 * 创建时间：2014-8-19  11:30:42 
	 */
	public class CItemToolInBubble extends CItemAbstract
	{
		private var _id:int;
		private var _hasTip:Boolean;
		private var _toolConfig:Item;
		//显示数量
		private var _showNum:Boolean = false;
		//显示浮窗
		private var _isShowTips:Boolean = false;
		//道具数量为0 ，是否置灰
		private var _zeroGray:Boolean = false;
		
		private var _buyNum:int = 1;
		//2 - 银豆  1- 金豆
		private var _buyType:int = 0;
		
		public static const BUY_TYPE_SILVER:int = 2;
		public static const BUY_TYPE_GOLD:int = 1;
		private var _num:int;
		

		public function CItemToolInBubble(id:int , showNum:Boolean , showTip:Boolean , zeroGray:Boolean = true)
		{
			_id = id;
			_isShowTips = showTip;
			_showNum = showNum;
			_zeroGray = zeroGray;
			_toolConfig = CBaseUtil.getToolConfigById(_id);
			super("common.item.inbubble");
		}
		
		override protected function drawContent():void
		{
			var cls:Class = ResHandler.getClass("common.tool.img");
			
			var item:MovieClip = new cls();
			var frameIndex:int = CBaseUtil.getIconFrameByIconId(_toolConfig.icon);
			item.gotoAndStop(frameIndex);
			mc.imgpos.addChild(item);
			
			if(_isShowTips)
			{
				this.addEventListener(TouchEvent.TOUCH_OVER , __toggleFlowTip , false , 0 , true);
				this.addEventListener(TouchEvent.TOUCH_OUT , __toggleFlowTip , false , 0 , true);
			}
			
			//数量
			mc.tfbg.visible = _showNum;
			mc.energytf.visible = _showNum;
			
			mc.mouseChildren = false;
			
			//如果是体力，直接使用
			if(CBaseUtil.isEnergyTool(_id))
			{
				this.addEventListener(TouchEvent.TOUCH_TAP , __onClickedUseEnergy , false , 0 , true);
			}
			
			CBaseUtil.regEvent(GameNotification.EVENT_TOOL_DATA_UPDATE , __onUpdate);
			
			__update();
		}
		
		override protected function dispose():void
		{
			super.dispose();
			CBaseUtil.removeEvent(GameNotification.EVENT_TOOL_DATA_UPDATE , __onUpdate);
		}
		
		private function __onUpdate(d:Notification):void
		{
			__update();
			this.unlock();
		}
		
		private function __update():void
		{
			_num = CDataManager.getInstance().dataOfUserTool.getToolNumById(_id);
			
			//一次性使用道具秒黑
			if(_num <= 0)
			{
				if(_zeroGray)
				{
					mc.filters = [CFilterUtil.grayFilter];
				}
				
				mc.tfbg.visible = false;
				mc.energytf.visible = false;
			}
			else
			{
				mc.filters = null;
				mc.tfbg.visible = _showNum;
				mc.energytf.visible = _showNum;
			}
			
			mc.energytf.text = "" + _num;
		}
		
		protected function __onClickedUseEnergy(event:TouchEvent):void
		{
			//检测是否可使用
			if(_num <= 0)
			{
				return;
			}
			
			if(!this.entryLock())
			{
				return;
			}
			
			NetworkManager.instance.sendServerUseTool(_id , 1);
		}
		
		protected function __toggleFlowTip(event:TouchEvent):void
		{
			if(!_hasTip)
			{
				_hasTip = true;
				CBaseUtil.showTip(_toolConfig.desc , mc.localToGlobal(new Point(mc.flowtippos.x -10 , mc.flowtippos.y + 20)) , ConstFlowTipSize.FLOW_TIP_MAX);
			}
			else
			{
				_hasTip = false;
				CBaseUtil.closeTip()
			}
		}
		
		public function set lock(value:Boolean):void
		{
			mc.lock.visible = value;
		}
		
		public function get itemid():int
		{
			return _id;
		}
		
		public function get buyType():int
		{
			return _buyType;
		}
	}
}