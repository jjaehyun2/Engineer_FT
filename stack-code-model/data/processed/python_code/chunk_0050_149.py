package com.wm.deal.ui 
{
	import com.wm.deal.cmd.CmdStartDeal;
	import com.wm.deal.cmd.core.CmdFactory;
	import com.wm.net.py.ClientConnect;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import flash.text.TextField;
	
	/**
	 * ...
	 * @author weism
	 */
	public class ActionView extends Sprite 
	{
		private var _needHand:TextField;
		private var _needFlop:TextField;
		private var _needTurn:TextField;
		private var _needRiver:TextField;
		
		public function ActionView() 
		{
			super();
			_needHand = new TextField();
			addChild(_needHand);
			_needHand.border = true;
			_needHand.text = "发手牌"
			_needHand.addEventListener(MouseEvent.CLICK, onClickHand);
			
			_needFlop = new TextField();
			addChild(_needFlop);
			_needFlop.border = true;
			_needFlop.text = "发翻牌"
			_needFlop.x = 120;
			_needFlop.addEventListener(MouseEvent.CLICK, onClickFlop);
			
			_needTurn = new TextField();
			addChild(_needTurn);
			_needTurn.border = true;
			_needTurn.text = "发转牌"
			_needTurn.x = 240;
			_needTurn.addEventListener(MouseEvent.CLICK, onClickTurn);
			
			_needRiver = new TextField();
			addChild(_needRiver);
			_needRiver.border = true;
			_needRiver.text = "发河牌"
			_needRiver.x = 360;
			_needRiver.addEventListener(MouseEvent.CLICK, onClickRiver);
		}
		
		private function onClickRiver(e:MouseEvent):void 
		{
			for each (var conn in ClientConnect.CONNECTS) 
			{
				CmdFactory.addCmd(2004, conn, CmdStartDeal).sendCmd([3]);// 为3，要求client发送手牌数据过来
			}
		}
		
		private function onClickTurn(e:MouseEvent):void 
		{
			for each (var conn in ClientConnect.CONNECTS) 
			{
				CmdFactory.addCmd(2004, conn, CmdStartDeal).sendCmd([2]);// 为2，要求client发送手牌数据过来
			}
		}
		
		private function onClickFlop(e:MouseEvent):void 
		{
			for each (var conn in ClientConnect.CONNECTS) 
			{
				CmdFactory.addCmd(2004, conn, CmdStartDeal).sendCmd([1]);// 为1，要求client发送手牌数据过来
			}
		}
		
		private function onClickHand(e:MouseEvent):void 
		{
			for each (var conn in ClientConnect.CONNECTS) 
			{
				CmdFactory.addCmd(2004, conn, CmdStartDeal).sendCmd([0]);// 为0，要求client发送手牌数据过来
			}
		}
		
	}

}