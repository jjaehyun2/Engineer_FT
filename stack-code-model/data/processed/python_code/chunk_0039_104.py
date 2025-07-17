package {
	
	
	import common.CommonModule;
	import common.event.EventCenter;
	
	import hall.HallModule;
	import hall.view.RecordView;
	
	import laya.ani.swf.MovieClip;
	import laya.display.Sprite;
	import laya.display.Stage;
	import laya.events.Event;
	import laya.net.HttpRequest;
	import laya.net.Loader;
	import laya.net.LocalStorage;
	import laya.net.WorkerLoader;
	import laya.utils.Browser;
	import laya.utils.Handler;
	import laya.webgl.WebGL;
	
	import manager.LoadingManager;
	import manager.MessageManager;
	import manager.UIManager;
	
	import net.Message;
	import net.Pomelo;
	import net.ProtoMessage;

	public class Main 
	{ 
		public static var ui:Sprite=new Sprite();
		public static var pop:Sprite=new Sprite();
		
		protected var myWorker:*;
		protected var preClock:int = 0;
		
		protected var isLoadLoaded:Boolean = false;
		private var room:String;
		private var roomid:int;
		private var isHasRoom:Boolean=false;
		
		public static var root:Main;
		
		public function Main()
		{
			root = this;
			new WX();//
			Laya.init(640, 1038,WebGL);	
			
//			var mc:MovieClip = new MovieClip();
//			mc.load("res/swfs/.swf",true);
//			mc.play();
//			
//			mc.x = 200;
//			mc.y = 200;
//			mc.width = 100;
//			mc.height = 100;
//			Laya.stage.addChild(mc);
//			return;
			
			if(Browser.window.roomstr){
				this.roomid=parseInt(Browser.window.roomstr[0]);
				UserData.uniqueCode=Browser.window.roomstr[1];
				this.isHasRoom=true;
				//https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx59a78e47791c020c&redirect_uri=http://www.zhonglewangluo.com/index22a.php?room=581178--bbatu9gqtvh0en39ft8g&response_type=code&scope=snsapi_userinfo&state=unit&connect_redirect=1#wechat_redirect
				
			}
					
			if(AppConfig.isXianshang)//
			{
				WorkerLoader.workerPath = "libs/worker.js";
				//开启worker线程
				WorkerLoader.enable = true;
				
				myWorker = new Browser.window.Worker("libs/littleTimer.js");
				myWorker.onmessage = function (evt):void {
					var offset:int = evt.data - preClock;
					EventCenter.instance.event(EventCenter.ON_LITTLETIMEER,offset);
					preClock = evt.data;
					
					if(ModuleDef.CurGameModule && ModuleDef.CurGameModule.inGame)
					{
						HallModule.instance.goEmpty();
					}
				};
				myWorker.postMessage("start"); // start the worker.
//				Laya.stage.screenAdaptationEnabled=false;
				
				Laya.stage.on(Event.RESIZE,this,function():void{
					if(QuickUtils.sysem()=="windows"||QuickUtils.sysem()=="ipad"||QuickUtils.sysem()=="mac")
					{
						//return
					}
					if(QuickUtils.getScreen()==false){
						Browser.window.document.getElementById("layaContainer").style.display="none";
						Browser.window.document.getElementById("displayScreen").style.display="block";
					}else{
						Browser.window.document.getElementById("layaContainer").style.display="block";
						Browser.window.document.getElementById("displayScreen").style.display="none";
					}
				})
			}
			checkVersion();
			
			//			Stat.show(Browser.clientWidth - 120 >> 1, Browser.clientHeight - 100 >> 1);
			//60帧率运行
			Laya.stage.frameRate=laya.display.Stage.FRAME_SLOW;
			
			Laya.timer.loop(1000,this,tryLoadLoadRes);
//			alert(QuickUtils.sysem())
			if(QuickUtils.sysem()=="windows"){
				//设置适配模式
				Laya.stage.scaleMode = "showall";//exactfit //showall
				//设置横竖屏
				resizeStage()
				//Laya.stage.screenMode = Stage.SCREEN_HORIZONTAL;
				
				//Laya.stage.screenMode = Stage.SCREEN_HORIZONTAL
				
				//Laya.stage.on(Event.RESIZE,this,resizeStage);
				//Laya.timer.frameLoop(10,this,resizeStage);
				
//				
				
				
				//Laya.stage.screenMode = Stage.SCREEN_VERTICAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
				//设置水平对齐
				Laya.stage.alignH = "center";
				//设置垂直对齐
				Laya.stage.alignV = "top";
			}else if(QuickUtils.sysem()=="ipad"||QuickUtils.sysem()=="mac"){
				//设置适配模式
				Laya.stage.scaleMode = "showall";//exactfit //showall
				//设置横竖屏
				Laya.stage.screenMode = Stage.SCREEN_VERTICAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
				//设置水平对齐
				Laya.stage.alignH = "center";
				//设置垂直对齐
				Laya.stage.alignV = "middle";
			}else{
				//设置适配模式
				Laya.stage.scaleMode = "exactfit";//exactfit //showall
				//设置横竖屏
				Laya.stage.screenMode = Stage.SCREEN_VERTICAL;//SCREEN_VERTICAL //SCREEN_HORIZONTAL
				//设置水平对齐
				Laya.stage.alignH = "center";
				//设置垂直对齐
				Laya.stage.alignV = "top";
			}
			
			Laya.stage.on(Event.CLICK,this,clickStage);
		}
		
		protected function clickStage(e:Event):void
		{
			trace("点击了舞台");
			trace(e.target);
			trace(e.currentTarget);
		}
		
		protected function resizeStage():void
		{

			if(HallModule.instance && HallModule.instance.isInHall == false)
			{
				return;
			}
			
			if(Browser.width < Browser.height)//不正常了
			{
				Laya.stage.screenMode = Stage.SCREEN_VERTICAL;
			}
			else
			{
				Laya.stage.screenMode = Stage.SCREEN_HORIZONTAL
			}
			
		}
		
		protected function tryLoadLoadRes():void
		{
			trace("tryLoadLoadRes........");
			Laya.loader.load([{url: "res/atlas/load.atlas", type: Loader.ATLAS}],Handler.create(this, onLoaded));
		}
		
		private var bg:laya.display.Sprite;
		
		public function checkVersion():void
		{
//			var version:String = AppConfig.version;
//			if(version > QuickUtils.getLocalVar("version",1))
//			{
//				QuickUtils.setLocalVar("version",version);
//				AppConfig.reloadLaya();
//			}
		}

		
		protected function onLoaded():void
		{
			if(isLoadLoaded == true)
			{
				return;
			}
			
			trace("onLoaded........");
			Laya.timer.clear(this,tryLoadLoadRes);
			isLoadLoaded = true;
			
			UIManager.instance.initLoadingView();
			LoadingManager.instance.loadCommon(this,onCommonLoaded);
			

		}
		
		protected function onCommonLoaded():void
		{
			trace("commonLoaded........");
			Browser.window.protobuf.load("res/qcloud.proto?v="+AppConfig.version, onProtoLoaded);	
			EventCenter.instance.on(EventCenter.LOGIN_SUCCESS,this,onGotUserinfoSuccess);  //wenjie
		}
		
		protected function getUserInfo():void
		{
			var http:HttpRequest = new HttpRequest();
			http.on(Event.COMPLETE, this,onGotUserinfo);
			http.send("http://" + AppConfig.httpHallIp +":"+ AppConfig.httpHallPort+"/getUserData?openid="+Browser.window.wxInfo.openid,null, "get", "text");
		}
		
		protected function onGotUserinfo(data:Object):void
		{
			var user:Object = JSON.parse(data as String);
			
			UserData.SID = user.sid;
			UserData.nickname = user.nick_name;
			UserData.uid = user.id;
			UserData.roomid = user.room_id;
			UserData.Coin = user.coin;
			UserData.Diamond = user.diamond;
			UserData.ServerTime = user.benefit_time;
			UserData.Icon = user.icon;
			//UserData.score = user.score;
			
			onGotUserinfoSuccess();
			
		}
		
		private function onProtoLoaded(err, root):void
		{ 
			AppConfig.proto = root.QCLOUD;
			
			//Main.root.getUserInfo()
			Pomelo.instance.connect(5000,true); // wenjie
		}
		
		private function onGotUserinfoSuccess(data:Object=null):void
		{
			trace("login success!!!!!!");
			
			if(ModuleDef.CurGameModule && ModuleDef.CurGameModule.inGame)//在游戏中
			{
				return;
			}
			
			initModules();//初始化modules
			
			/**
			 * 添加邀请好友直接进入房间
			 */
			var info:Object=Browser.window.wxInfo;
			//trace(info,info.type=="")
			
			if(AppConfig.isNewHall == false)
			{
				trace(this.isHasRoom)
				if(this.isHasRoom==true){
					
					
					RecordView.gameName=parseInt(Browser.window.roomstr[2])==1?"象山麻将":"西周麻将";
					var intoRoomObj:Object = {SID:UserData.SID,UID:UserData.uid,RID:this.roomid,PWD:UserData.passWard,code:UserData.uniqueCode};
					EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.Into_Room,intoRoomObj));
					EventCenter.instance.once(MessageManager.HALL,this,onGotHallMessage);
				}
				else
				{
					HallModule.instance.gotoHall();
//					new WX();
				}
			}
			else
			{
				if(info.type==""){
					var roo_id:int=parseInt(info.id);
					UserData.uniqueCode=info.uniqueCode;
					UserData.roomid=this.roomid;
					var intoRoom_Obj:Object = {SID:UserData.SID,UID:UserData.uid,RID:roo_id,PWD:UserData.passWard,code:UserData.uniqueCode};
					EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.Into_Room,intoRoom_Obj));
					EventCenter.instance.once(MessageManager.HALL,this,onGotHallMessage);
				}else{
					var creatObj:Object = new Object();
					creatObj.SID = UserData.SID;
					creatObj.Type = info.type;//游戏类型
					//creatObj.PayType = payType;//游戏类型
					creatObj.City = UserData.City;
					creatObj.PWD = UserData.passWard;
					creatObj.Rule = [25,info.id||"19",23];//规则类型
					
					var dataBuff:* = ProtoMessage.getProtoMessage(Message.Create_Room,creatObj);
					EventCenter.instance.event(EventCenter.SOCKET_SEND,dataBuff);
					
					EventCenter.instance.once(MessageManager.HALL,this,onGotHallMessage);
					
				}
			}
			
			
			if(AppConfig.autoJoin)
			{
				var into_Room_Obj:Object = {SID:UserData.SID,UID:UserData.uid,RID:LocalStorage.getItem("lastRoomId"),PWD:UserData.passWard};
				EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.Into_Room,into_Room_Obj));
			}
			
			
		}
		protected function onGotHallMessage(msg:Message):void
		{
			EventCenter.instance.off(MessageManager.HALL,this,onGotHallMessage);
			
			if(msg.messageId == Message.ACKBC_Into_Room)//进入房间
			{
				trace("ACKBC_Into_Room!!!!!!!!!!!!!!!!!!!!!!!!0000"); 
				var intoObj:Object = AppConfig.proto.ACKBC_Into_Room.decode(msg.params[0]);
				
				UserData.roomtype = intoObj.Type;
				UserData.Rule = intoObj.Rule;
				
				LoadingManager.instance.startLoadGameRes(this,function():void
				{
					LoadingManager.instance.loadGameJS(this,onMajiangJsLoaded);
				})
			}
			else if(msg.messageId == Message.ACK_Create_Room)//c房间
			{
				var obj:Object = AppConfig.proto.ACK_Create_Room.decode(msg.params[0]);
				UserData.roomid = obj.RID;
				UserData.passWard = obj.PWD;
				//				UserData.Rule = obj.Rule;
				UserData.roomtype = obj.Type;
				
				LocalStorage.setItem("lastRoomId",obj.RID);
				
				LoadingManager.instance.startLoadGameRes(this,function():void
				{
					LoadingManager.instance.loadGameJS(this,onMajiangJsLoaded);
				})
				var intoRoomObj:Object = {SID:UserData.SID,UID:UserData.uid,RID:UserData.roomid,PWD:UserData.passWard};
				EventCenter.instance.event(EventCenter.SOCKET_SEND,ProtoMessage.getProtoMessage(Message.Into_Room,intoRoomObj));
			}
			msg.complete();
		}
		
		protected function onMajiangJsLoaded():void
		{
			LoadingManager.instance.onGoInGameBackLoad();
			ModuleDef.CurGameModule.instance.startGame();
		}
		
		private function initModules():void
		{
			CommonModule.instance.startup();
			if(AppConfig.isNewHall==false)
			{
				HallModule.instance.startup();
			}
			
//			GameModule.instance.startup();
		}
		
		
	
	}
}