package hall.view
{
	import common.baseui.UIBase;
	import common.event.EventCenter;
	
	import laya.display.Sprite;
	import laya.events.Event;
	import laya.ui.Button;
	import laya.utils.Handler;
	
	import manager.UIManager;
	
	import net.Message;
	import net.ProtoMessage;
	
	import ui.hall.CreatRoomViewUI;
	
	public class CreatRView extends UIBase
	{
		
		protected var _skin:CreatRoomViewUI;
		protected var typeSeleBtns:Vector.<Button> = new Vector.<Button>();
		public function CreatRView(container:Sprite=null)
		{
			super(container);
			//skinRes = "res/atlas/hall/creatRoom.json";
		}
		
		override public function show():void
		{
			if(_isShow)
			{
				return;
			}
			super.show();
			_skin.pinshiGameType.visible = false;
			_skin.srddzGameType.visible = false;
			switch(UserData.roomtype)
			{
				case 3010:
					_skin.shichangSele.y=398;
					_skin.gameType.visible=true;
					_skin.xiangshangGameType.visible = true;
					_skin.sddzGameType.visible = false;
					_skin.shichangSele.visible = true;
					_skin.jushuSele.visible = false;
					break;
				case 3000:
					_skin.shichangSele.y=398;
					_skin.gameType.visible=false;
					_skin.shichangSele.visible = true;
					_skin.jushuSele.visible = false;
					break;
				case 4000://三人斗地主
					_skin.shichangSele.y=398;
					_skin.gameType.visible=true;
					_skin.xiangshangGameType.visible = false;
					_skin.sddzGameType.visible = true;
					_skin.shichangSele.visible = false;
					_skin.jushuSele.visible = true;
					break;
				case 4001://四人斗地主
					_skin.shichangSele.y=398;
					_skin.gameType.visible=true;
					_skin.xiangshangGameType.visible = false;
					_skin.sddzGameType.visible = false;
					_skin.srddzGameType.visible = true;
					_skin.shichangSele.visible = false;
					_skin.jushuSele.visible = true;
					_skin.jushuSele.labels = "6局,12局,20局";
					break;
				case 4002://拼十
					_skin.shichangSele.y=398;
					_skin.gameType.visible=true;
					_skin.xiangshangGameType.visible = false;
					_skin.sddzGameType.visible = false;
					_skin.pinshiGameType.visible = true;
					_skin.shichangSele.visible = false;
					_skin.jushuSele.visible = true;
					_skin.jushuSele.labels = "10局,20局,34局";
					break;
			}
			
//			if(UserData.roomtype == 4002)
//			{
//				_skin.costType.visible = false;
//			}else{
//				_skin.costType.visible = true;
//			}
			
			
			
			onSele(taishu,payTime,payType);
			
			_skin.gameTit.text=AppConfig.costRule[UserData.roomtype+""]["mark"];
			_skin && UIManager.instance.uiCommonLayer.addChild(_skin);
		}
		
		override public function hide():void
		{
			super.hide();
			if(_skin && _skin.parent)
			{
				_skin.parent.removeChild(_skin);
			}
		}
		
		override protected function onLoaded():void
		{
			super.onLoaded();
			trace("creatRoom.json onLoaded!!");
			
			_skin = new CreatRoomViewUI();
			_skin.mouseThrough = true;
			if(_isShow)
			{
				UIManager.instance.uiCommonLayer.addChild(_skin);
			}
			
			init();
		}
		
		protected var _taishu:int=0;//50,100,无封顶
		protected var _payType:int=0;//4人支付，1人支付
		protected var _payTime:int=3;//4，8，16； 15，20，30，60
		protected var _xiangshanGameType:int=128;//106清10混6  128清12混8
		protected var _sddzGameType:int = 101;//101叫分 102抢地主
		protected var _srddzGameType:int = 101;//101上海玩法 102安徽玩法
		protected var _pinshiGameType:int = 101;
		protected var _costType:int = 1;//房间类型 0约局场 2金币场 
		protected var _payJushu:int = 0;
		
		public function get taishu():int{return QuickUtils.getLocalVar("taishu",_taishu);}
		public function set taishu(value:int):void{QuickUtils.setLocalVar("taishu",value);}
		
		public function get payType():int{return QuickUtils.getLocalVar("payType",_payType);}
		public function set payType(value:int):void{QuickUtils.setLocalVar("payType",value);}
		
		public function get payTime():int{return QuickUtils.getLocalVar("payTime",_payTime);}
		public function set payTime(value:int):void{QuickUtils.setLocalVar("payTime",value);}
		
		public function get payJushu():int{return QuickUtils.getLocalVar("payJushu",_payJushu);}
		public function set payJushu(value:int):void{QuickUtils.setLocalVar("payJushu",value);}
		
		public function get xiangshanGameType():int{return QuickUtils.getLocalVar("xiangshanGameType",_xiangshanGameType);}
		public function set xiangshanGameType(value:int):void{QuickUtils.setLocalVar("xiangshanGameType",value);}
		
		public function get sddzGameType():int{return QuickUtils.getLocalVar("sddzGameType",_sddzGameType);}
		public function set sddzGameType(value:int):void{QuickUtils.setLocalVar("sddzGameType",value);}
		
		public function get srddzGameType():int{return QuickUtils.getLocalVar("srddzGameType",_srddzGameType);}
		public function set srddzGameType(value:int):void{QuickUtils.setLocalVar("srddzGameType",value);}
		
		public function get pinshiGameType():int{return QuickUtils.getLocalVar("pinshiGameType",_pinshiGameType);}
		public function set pinshiGameType(value:int):void{QuickUtils.setLocalVar("pinshiGameType",value);}
		
		public function get costType():int{return QuickUtils.getLocalVar("costType",_costType);}
		public function set costType(value:int):void{QuickUtils.setLocalVar("costType",value);}
		
		public var taishuRule:int = AppConfig.taiRef[0];
		public var payTimeRule:int = AppConfig.payTimeRef[0];
		public var payTypeRule:int = AppConfig.payTypeRef[0];
		
		
		
		protected function init():void
		{
			_skin.confirmBtn.on(Event.CLICK,this,onCreatRoom,[0]);//这个是创建
			_skin.matchBtn.on(Event.CLICK,this,onCreatRoom,[1]);//这个是匹配
//			_skin.cancelBtn.on(Event.CLICK,this,onCancelCreatRoom);
		 	_skin.maskBtn.on(Event.CLICK,this,onCancelCreatRoom);
			
			//_skin.taishuSele.
//			_skin.taishuSele.selectHandler = Handler.create(this,onTaishuChange,null,false);
			_skin.jushuSele.selectHandler = Handler.create(this,onjushuChange,null,false);
			_skin.payTypeSele.selectHandler = Handler.create(this,onpayTypeChange,null,false);
			
			_skin.shichangSele.selectHandler = Handler.create(this,onshichangChange,null,false);
			_skin.xiangshangGameType.selectHandler = Handler.create(this,onXiangsGameTypeChange,null,false);
			_skin.sddzGameType.selectHandler = Handler.create(this,onSddzGameTypeChange,null,false);
			_skin.srddzGameType.selectHandler = Handler.create(this,onSrddzGameTypeChange,null,false);
			_skin.pinshiGameType.selectHandler = Handler.create(this,onPinshiGameTypeChange,null,false);
			_skin.costType.selectHandler = Handler.create(this,onCostTypeChange,null,false);
			
			
			onSele(taishu,payTime,payType);
		}
		
		protected function onSele(taishu:int,payTime:int,payType:int):void
		{
//			_skin.taishuSele.selectedIndex = taishu;
//			if(payTime < 3)
//			{
//				_skin.jushuSele.selectedIndex = payTime;
//			}
//			else
//			{
//				_skin.shichangSele.selectedIndex = payTime-3;
//			}
			_skin.payTypeSele.selectedIndex = payType;
			
			taishuRule = AppConfig.taiRef[taishu];
			
			if(UserData.roomtype == UserData.RoomType_SanDizhu)
			{
				payTimeRule = AppConfig.payTimeRef[payJushu];
			}
			else if(UserData.roomtype == UserData.RoomType_SirenDizhu)
			{
				payTimeRule = AppConfig.payTimeRef[payJushu];
			}
			else if(UserData.roomtype == UserData.RoomType_DandanPinshi)
			{
				payTimeRule = AppConfig.payTimeRef[payJushu+7];
			}
			else
			{
				payTimeRule = AppConfig.payTimeRef[payTime];
			}
			payTypeRule = AppConfig.payTypeRef[payType];
			
			_skin.shichangSele.selectedIndex=this.payTime-3;
			_skin.jushuSele.selectedIndex = this.payJushu;
			
			_skin.xiangshangGameType.selectedIndex = this.xiangshanGameType==106?1:0;
			_skin.sddzGameType.selectedIndex = this.sddzGameType == 101 ? 0 : 1;
			_skin.srddzGameType.selectedIndex = this.srddzGameType == 101 ? 0 : 1;
			_skin.pinshiGameType.selectedIndex = this.pinshiGameType == 101 ? 0 : 1;
			_skin.costType.selectedIndex = this.costType == 0 ? 0: 1;
			
			
			
			//计算rule
			preCalculateCost();
		}
		
		protected function preCalculateCost():void
		{
			var playerNum:int = 4;
			if(UserData.roomtype == UserData.RoomType_SanDizhu)
			{
				playerNum = 3;
			}
			else 	if(UserData.roomtype == UserData.RoomType_SirenDizhu)
			{
				playerNum = 4;
			}
			if(payType == 1)
			{
				_skin.preCostTf.text = "每人支付 "+AppConfig.costRule[UserData.roomtype+""][payTimeRule+""]/playerNum+"";
			}
			else
			{
				_skin.preCostTf.text = "房主支付 "+AppConfig.costRule[UserData.roomtype+""][payTimeRule+""]/playerNum+"";
			}
		}
		
		protected function onTaishuChange(idx:int):void
		{
			taishu = idx;
			taishuRule = AppConfig.taiRef[taishu];
			trace("taishu::" + taishu);
		}
		
		protected function onjushuChange(idx:int):void
		{
			if(idx == -1)
			{
				return;
			}
			//_skin.shichangSele.selectedIndex = -1;
			payJushu = idx;
			trace("payTime::" + payJushu);
			
			if(UserData.roomtype == UserData.RoomType_DandanPinshi)
			{
				payTimeRule = AppConfig.payTimeRef[payJushu+7];
			}
			else
			{
				payTimeRule = AppConfig.payTimeRef[payJushu];
			}
			
			preCalculateCost();
		}
		
		protected function onshichangChange(idx:int):void
		{
			payTime = idx+3;
			
			trace("payTime::" + payTime);
			payTimeRule = AppConfig.payTimeRef[payTime];
			preCalculateCost();
		}
		
		protected function onpayTypeChange(idx:int):void
		{
			payType = idx;
			payTypeRule = AppConfig.payTypeRef[payType];
			trace("payType::" + payType);
			preCalculateCost();
		}
		protected function onXiangsGameTypeChange(idx:int):void
		{
			xiangshanGameType=AppConfig.xiangshangGameTypeRef[idx];
			trace("xiangshanGameType:"+idx,AppConfig.xiangshangGameTypeRef[idx])
		}
		
		protected function onSddzGameTypeChange(idx:int):void
		{
			sddzGameType=AppConfig.sddzGameTypeRef[idx];
			trace("sddzGameType:"+idx,AppConfig.sddzGameTypeRef[idx])
		}
		
		protected function onSrddzGameTypeChange(idx:int):void
		{
			srddzGameType=AppConfig.srddzGameTypeRef[idx];
			trace("sddzGameType:"+idx,AppConfig.srddzGameTypeRef[idx])
		}
		
		protected function onPinshiGameTypeChange(idx:int):void
		{
			pinshiGameType=AppConfig.pinshiGameTypeRef[idx];
			trace("pinshiGameType:"+idx,AppConfig.pinshiGameTypeRef[idx])
		}
		
		protected function onCostTypeChange(idx:int):void{
			costType = idx;
			trace("costType::",costType);
		}
		
		protected function onCreatRoom(type:int,e:Event):void
		{
			//检查玩家的钻石是否够,不够提示充值
			var playerNum:int = 4;
			if(UserData.roomtype == UserData.RoomType_SanDizhu)
			{
				playerNum = 3;
			}
			else 	if(UserData.roomtype == UserData.RoomType_SirenDizhu)
			{
				playerNum = 4;
			}
			if(payType == 1)//4人
			{
				if(UserData.Diamond < AppConfig.costRule[UserData.roomtype+""][payTimeRule+""]/playerNum)
				{
					QuickUtils.popMessage("房卡不够,请充值!");
					return;
				}
			}
			else
			{
				if(UserData.Diamond < AppConfig.costRule[UserData.roomtype+""][payTimeRule+""]/playerNum)
				{
					QuickUtils.popMessage("房卡不够,请充值!");
					return;
				}
			}
			
			UserData.Rule = [taishuRule,payTimeRule,payTypeRule];
			switch(UserData.roomtype)
			{
				
				case UserData.RoomType_Xizhou:
					UserData.Rule.push(0,costType);
					break;
				case UserData.RoomType_Xiangshan:
					UserData.Rule.push(xiangshanGameType,costType);
					break;
				case UserData.RoomType_SanDizhu:
					UserData.Rule.push(sddzGameType,costType);
					break; 
				case UserData.RoomType_SirenDizhu:
					UserData.Rule.push(srddzGameType,costType);
					break; 
				case UserData.RoomType_DandanPinshi:
					UserData.Rule.push(pinshiGameType,costType);
					break; 
			}
			trace("rule::",UserData.Rule);
			
//			UserData.Rule = [payTimeRule];
			
			//todo
			//			message Create_Room {
			//				required string SID    	= 1;	//
			//				required int32 Type    	= 2; 	//
//			optional int32  PayType = 3;    // 支付类型(按时间, 按局数)
			//				optional int32 City    	= 3; 	//
			//				optional string PWD    	= 4;    //	密码
			//				repeated int32 Rule  	= 5; 	// 规则列表
			//			}
			var creatObj:Object = new Object();
			creatObj.SID = UserData.SID;
			creatObj.Type = UserData.roomtype;//游戏类型b
			//creatObj.PayType = payType;//游戏类型
			creatObj.City = UserData.City;
			creatObj.PWD = UserData.passWard;
			creatObj.Rule =UserData.Rule;// [taishuRule,payTimeRule,payTypeRule];//规则类型
//			creatObj.Rule = [payTimeRule];//规则类型
			var data:*;
			if(type == 0){//创建房间
				data = ProtoMessage.getProtoMessage(Message.Create_Room,creatObj);
			}else if(type==1){//匹配房间
				data = ProtoMessage.getProtoMessage(Message.Match_Room,creatObj);
			}
			
			
			EventCenter.instance.event(EventCenter.SOCKET_SEND,data);
			
			//Pomelo.instance.connect(5000,true);
			
			hide();
			
			//EventCenter.instance.once(EventCenter.LOGIN_SUCCESS,this,onLoginSuccess,[data]);
		}
		
		protected function onLoginSuccess(data:*):void
		{
			EventCenter.instance.event(EventCenter.SOCKET_SEND,data);
		}
		
		protected function onCancelCreatRoom(e:Event):void
		{
			hide();
		}
		
	}
}