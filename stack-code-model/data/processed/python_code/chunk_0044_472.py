package modules.game.majiangGame.context
{
	import common.event.EventCenter;
	import common.tools.SoundPlay;
	
	import modules.game.majiangGame.controller.MajiangGameController;
	import modules.game.majiangGame.controller.ReplayMajiangGameController;
	import modules.game.majiangGame.model.MajiangModel;
	import modules.game.majiangGame.model.ReplayMajiangModel;
	import modules.game.majiangGame.view.MajiangGameView;
	
	import laya.media.SoundManager;
	
	import manager.MessageManager;
	
	import rb.framework.mvc.GameContext;
	import rb.framework.mvc.Module;
	
	public class MajiangGameContext extends GameContext
	{
		protected var _majiangGameView:MajiangGameView;

		public function get view():MajiangGameView
		{
			return _majiangGameView;
		}

		protected var _majiangGameController:MajiangGameController;
		protected var _rMajiangGameController:MajiangGameController;

		public function get controller():MajiangGameController
		{
			if(UserData.isReplay)//这个是重播
			{
				return _rMajiangGameController;
			}
			else
			{
				return _majiangGameController;
			}
		}

		protected var _majiangModel:MajiangModel;
		protected var _rMajiangModel:MajiangModel;

		public function get model():MajiangModel
		{
			if(UserData.isReplay)//这个是重播
			{
				return _rMajiangModel;
			}
			else
			{
				return _majiangModel;
			}
		}

		
		public function MajiangGameContext(key:String="", module:Module=null, parentNode:GameContext=null)
		{
			super(key, module, parentNode);
		}
		
		override public function open():void
		{
			super.open();
			
			initUI();
			trace("addView(_majiangGameView)////////////////");
			
			this.addView(_majiangGameView);
			if(UserData.isReplay)
			{
				this.addController(_rMajiangGameController);
				this.addModel(_rMajiangModel);
			}
			else
			{
				this.addController(_majiangGameController);
				this.addModel(_majiangModel);
			}
			
			
			trace("majiang gamecontext UserData.roomtype::" + UserData.roomtype);
			
			setChairNum(4);

			SoundPlay.swithMusic("game");
			
			trace("MajiangGameContext open:::...");
			trace("注册了游戏内的消息！！！");
			
			//_majiangGameView.onAdd();
			MessageManager.instance.continueQueue(MessageManager.GAME);
			
			//发送麻将准备好了
			EventCenter.instance.event(EventCenter.GameContextReady,null);
			
			//QuickTween.main_ui_reset();
		}
		
		protected function initUI():void
		{
			if(_majiangModel==null)
			{
				_majiangModel = new MajiangModel();
			}
			
			if(_rMajiangModel == null)
			{
				_rMajiangModel = new ReplayMajiangModel();
			}
			
			if(_rMajiangGameController == null)
			{
				_rMajiangGameController = new ReplayMajiangGameController();
			}
			
			if(_majiangGameView == null)
			{
				_majiangGameView = new MajiangGameView();
			}
			if(_majiangGameController == null)
			{
				_majiangGameController = new MajiangGameController();
			}
		}
		
		override public function close():void
		{
			super.close();
			SoundManager.stopMusic();
			//_majiangGameView.onRemove();
			
			//_majiangGameView.onRemove();
		}
		
		public function setChairNum(num:int):void
		{
			if(UserData.isReplay)
			{
				_rMajiangModel.chairNum = num;
			}
			else
			{
				_majiangModel.chairNum = num;
			}
			
			_majiangGameView.setChairNmu(num);
			
			
		}
		
	
	}
}