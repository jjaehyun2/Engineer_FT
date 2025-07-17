package modules.sddzGame
{
	import common.CommonModule;
	
	import hall.HallModule;
	import hall.view.RecordView;
	
	import laya.utils.Browser;
	
	import modules.sddzGame.context.GameMainContext;
	import modules.sddzGame.sddzInerGame.context.SDdzGameContext;
	
	import rb.framework.errors.SingletonError;
	import rb.framework.mvc.GameContext;
	import rb.framework.mvc.Module;
	
	/*[COMPILER OPTIONS:ForcedCompile]*/ 
	public class SDdzGameModule extends Module
	{
		
		public var needResize:Boolean = false;
		/**是否在游戏中*/
		public static var inGame:Boolean=false;
		/**是否暂停游戏消息队列*/
		public static var isPauseGameQueue:Boolean = false;
		/**是否是在收到了总的结算数据了*/
		public static var isSettlement:Boolean = false;
		
		static	private  var _instance:SDdzGameModule;
		
		public static function get instance():SDdzGameModule{
			
			if (_instance == null)
			{
				_instance = new SDdzGameModule();
			}
			return _instance;
		}
		
//		public static function get curGameModule():SDdzGameModule
//		{
//			return ModuleDef.CurGameModule.instance;
//			
//		}
		
		public function SDdzGameModule()
		{
			super();
			if (_instance != null)
			{
					throw (new SingletonError(this));
			}
			_instance = this;
		}
		
		protected var _main:GameMainContext;
		public function get main():GameMainContext
		{
			return _main;
		
		}
		
		protected var _sddzGameContext:SDdzGameContext;
		
		public function get gameContext():SDdzGameContext
		{
			return _sddzGameContext;
		}
		
		protected var _mainContext:GameContext;
		
		public override function startup():void{
			if(_mainContext == null)
			{
				_mainContext = new GameContext("sddzGameMainmain",this);
				_main = new GameMainContext("sddzGameMain",this,_mainContext);
				_sddzGameContext = new SDdzGameContext("sddzGame",this,_main);
			}
			this.switchState(this._mainContext);
			
		}
		
		public function stopGame(gotoHall:Boolean=true,needClear:Boolean=false):void
		{
			if(needClear)
			{
				_sddzGameContext.controller.clear();
			}
			inGame=false;
			isSettlement = false;
			this.switchState(this._mainContext);
			
			if(gotoHall){
				//inHallResize();
				HallModule.instance.gotoHall();
			}
		}
		
		public function startGame():void
		{
			Browser.window.document.title = AppConfig.nameTitle+"三人斗地主";
			if(inGame == true)
			{
				return;
			}
			
			HallModule.instance.goEmpty();
			inGame=true;
			
			//inGameResize(); 
			
			CommonModule.instance.gotoCommonContext();
			RecordView.gameName="三人斗地主";
			this.switchState(this.gameContext);
			
			WX.onMenuShareTimeline(UserData.nickname+"-"+AppConfig.nameTitle+"三人斗地主("+AppConfig.costRule[UserData.roomtype+""][UserData.Rule[3]]+")【房间号："+UserData.roomid+"】",UserData.roomid+"--"+UserData.uniqueCode);
			WX.onMenuShareAppMessage(UserData.nickname+"-"+AppConfig.nameTitle+"三人斗地主("+AppConfig.costRule[UserData.roomtype+""][UserData.Rule[3]]+")【房间号："+UserData.roomid+"】","房主创建了三人斗地主 【房间号:"+UserData.roomid+"】"+AppConfig.getRule(UserData.Rule[1]).desc+"",UserData.roomid+"--"+UserData.uniqueCode);			
			trace("startSddzGame...........");
		}
	}
}