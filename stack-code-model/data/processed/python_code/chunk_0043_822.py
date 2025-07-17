package modules.nnGame.inerGame.context
{
	import common.event.EventCenter;
	import common.tools.SoundPlay;
	
	import laya.media.SoundManager;
	
	import manager.MessageManager;
	
	import modules.nnGame.inerGame.controller.RNnController;
	import modules.nnGame.inerGame.controller.NnController;
	import modules.nnGame.inerGame.model.RNnModel;
	import modules.nnGame.inerGame.model.NnModel;
	import modules.nnGame.inerGame.view.NnView;
	
	import rb.framework.mvc.GameContext;
	import rb.framework.mvc.Module;
	
	public class NnContext extends GameContext
	{
		protected var _view:NnView;

		public function get view():NnView
		{
			return _view;
		}
		
		protected var _controller:NnController;
		protected var _rcontroller:RNnController;
		
		public function get controller():NnController
		{
			if(UserData.isReplay)//这个是重播
			{
				return _rcontroller;
			}
			else
			{  
				return _controller
			}
		}
		
		protected var _model:NnModel;
		protected var _rmodel:RNnModel;
		
		public function get model():NnModel
		{
			if(UserData.isReplay)//这个是重播
			{
				return _rmodel;
			}
			else
			{
				return _model;
			}
		}
		
		
		public function NnContext(key:String="", module:Module=null, parentNode:GameContext=null)
		{
			super(key, module, parentNode);
		}
		
		override public function open():void
		{
			super.open();
			initUI();
			trace("addView(srddz)////////////////");
			
			this.addView(_view);
			if(UserData.isReplay)
			{
				this.addController(_rcontroller);
				this.addModel(_rmodel);
			}
			else
			{
				this.addController(_controller);
				this.addModel(_model);
			}
			
			trace("nngamecontext UserData.roomtype::" + UserData.roomtype);
			setChairNum(10);
			
			SoundPlay.swithMusic("game");
			
			trace("NnContext open:::...");
			trace("注册了游戏内的消息！！！");
			MessageManager.instance.continueQueue(MessageManager.GAME);
			
			EventCenter.instance.event(EventCenter.GameContextReady,null);
			
		}
		
		override public function close():void
		{
			super.close();
			SoundManager.stopMusic();
		}
		
		protected function initUI():void
		{
			if(!_view)
			{
				_view = new NnView();
			}
			
			if(UserData.isReplay)
			{
				if(!_rcontroller)
				{
					_rcontroller = new RNnController();
				}
				
				if(_rmodel)
				{
					_rmodel = new RNnModel();
				}
			}
			else
			{
				if(!_controller)
				{
					_controller = new NnController();
				}
				
				if(!_model)
				{
					_model = new NnModel();
				}
			}
		}
		
		public function setChairNum(num:int):void
		{
			if(UserData.isReplay)
			{
				_rmodel.chairNum = num;
			}
			else  
			{
				_model.chairNum = num;
			}
			
			_view.setChairNmu(num);
		}
	}
}