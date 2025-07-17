package modules.xizhouGame
{
	import common.CommonModule;
	
	import hall.HallModule;
	import hall.view.RecordView;
	
	import laya.display.Stage;
	import laya.utils.Browser;
	
	import modules.game.GameModule;
	import modules.game.majiangGame.view.animation.HuAnimation;
	
	import rb.framework.errors.SingletonError;
	
	/*[COMPILER OPTIONS:ForcedCompile]*/ 
	public class XizhouGameModule extends GameModule
	{
		public static var inGame:Boolean=false;
		
		static	private  var _instance:XizhouGameModule;
		
		// --- Static Functions ------------------------------------------------------------------------------------------------------------------------------------ //
		
		public static function get instance():XizhouGameModule{
			
			if (_instance == null){
				_instance = new XizhouGameModule();
			};
			return (_instance);
		}
		
		public function XizhouGameModule()
		{
			if (_instance != null){
				throw (new SingletonError(this));
			};
			_instance = this;
		}
		
		override public function startGame():void
		{
			Browser.window.document.title = AppConfig.nameTitle+"西周麻将";
			if(inGame == true)
			{
				return;
			}
			HallModule.instance.goEmpty();
			inGame=true;
			CommonModule.instance.gotoCommonContext();
			this.switchState(this.gameContext);
			inGameResize();
			if(AppConfig.isNewHall == false){
				RecordView.gameName="西周麻将";
				WX.onMenuShareTimeline(UserData.nickname+"-"+AppConfig.nameTitle+"西周麻将 【房间号："+UserData.roomid+"】",UserData.roomid+"-"+UserData.uniqueCode+"-2");
				WX.onMenuShareAppMessage(UserData.nickname+"-"+AppConfig.nameTitle+"西周麻将 【房间号："+UserData.roomid+"】","房主创建了西周麻将 【房间号:"+UserData.roomid+"】"+AppConfig.getRule(UserData.Rule[1]).desc+"局",UserData.roomid+"-"+UserData.uniqueCode+"-2");
			}else{
				WX.onMenuShareTimeline(UserData.nickname+"-"+AppConfig.nameTitle+"西周麻将 【房间号："+UserData.roomid+"】",UserData.roomid+"--"+UserData.uniqueCode);
				WX.onMenuShareAppMessage(UserData.nickname+"-"+AppConfig.nameTitle+"西周麻将【房间号："+UserData.roomid+"】","房主创建了西周麻将 【房间号:"+UserData.roomid+"】"+AppConfig.getRule(UserData.Rule[1]).desc+"局",UserData.roomid+"--"+UserData.uniqueCode);
			}
			trace("startMajiangGame...........");
			
			
		}
		
		override public function stopGame(gotoHall:Boolean=true,needClear:Boolean=false):void
		{
			if(needClear)
			{
				_majiangGameContext.controller.clear();
			}
			inGame=false;
			isSettlement = false;
			this.switchState(this._mainContext);
			if(gotoHall){
				if(AppConfig.isNewHall){
					QuickUtils.gotoHall();
				}else{
					inHallResize();
					HallModule.instance.gotoHall();
				}
			}
			HuAnimation.instance.noticeHide();
			
		}
		
//		override protected function resize():void
//		{
//			if(inGame)
//			{
//				Laya.stage.screenMode = Stage.SCREEN_HORIZONTAL;
//				Laya.stage.size(1038,640);//1038,640
//			}
//			else
//			{
//				if(QuickUtils.sysem()=="windows"){
//					Laya.stage.screenMode = Stage.SCREEN_HORIZONTAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
//				}else if(QuickUtils.sysem()=="ipad"||QuickUtils.sysem()=="mac"){
//					Laya.stage.screenMode = Stage.SCREEN_VERTICAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
//				}else{
//					Laya.stage.screenMode = Stage.SCREEN_VERTICAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
//				}
//				Laya.stage.size(640,1038);
//			}
//		}
	}
}