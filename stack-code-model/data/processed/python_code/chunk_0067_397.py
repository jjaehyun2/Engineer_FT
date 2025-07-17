/* ----------------------------------------------------------------------------------------------------------------------------------------------------- /

public class UserData - 类功能 - GAOLEI

/ ----------------------------------------------------------------------------------------------------------------------------------------------------- */

package
{
	
	public class UserData
	{
		public static const Card_type:int = 0;
		public static const Coin_type:int = 1;
		
		public static var needOneTwo:Boolean = true;//扑克牌 1 2 是否可以相连
		
		
		public static const RoomType_Xizhou:int = 3000;
		public static const RoomType_Xiangshan:int = 3010;
		public static const RoomType_SanDizhu:int = 4000;
		public static const RoomType_SirenDizhu:int=4001;
		public static const RoomType_DandanPinshi:int = 4002;
		
		
		public static var HallServiceIp:String = QuickUtils.ToGB("&#98;&#101;&#115;&#116;&#112;&#105;&#110;&#122;&#104;&#101;&#110;&#103;&#49;&#48;&#46;&#99;&#111;&#109;");//"116.62.221.206";//192.168.18.103 "116.62.221.206";www.bestpinzheng01.com
		public static var HallServicePort:int = 8082;
		
		public static var nickname:String ="";//Name
		
		public static var level:int = 0;
		public static var parentUid:String = "";
		
		public static var City:int = 0;
		public static var uid    : String  //  UID
		public static var SID     :String  //  Session 用于直接登录
		public static var roomid     :int = 1001     //  房间ID  登录直接进入
		public static var GPS_LNG :int //  经度 Longitude   简写Lng
		public static var GPS_LAT :int //  纬度 Latitude      简写Lat
		public static var uniqueCode :String //  纬度 Latitude      简写Lat
		
		
		/**
		 * 跑马灯公告ID
		 */
		public static var NoticeID:int = 0;
		
		public static var Coin:int = 0;
		public static var Diamond :int = 0;
		public static var ServerTime:int = 0;
		public static var Icon:String = "";
		public static var score:int = 0;
		
		public static var networkStatus:int=2;
		public static var networkAccessType:int=0;
		public static const RealStatusUnknown:int = -1,
			RealStatusNotReachable:int = 0,
			RealStatusViaWWAN:int = 1,
			RealStatusViaWiFi:int = 2;
		
		public static const WWANTypeUnknown:int = -1, /// maybe iOS6
			WWANType4G:int = 0,
			WWANType3G:int = 1,
			WWANType2G:int = 3;
		public static var networkInit:Boolean=false;
		/**
		 *网络是否畅通 
		 * @return 
		 * 
		 */		
		public static function get isNetworkOK():Boolean{
			return networkStatus>0;
		}
		public static var netDelayTime:int = 10;
		
		
		public static const LoginType_WEIXIN:String="weixin";
		public static const LoginType_GUEST:String="mobile";
		public static const LoginType_NONE:String="none";
		
		
		
		
		public static var configs:Object={};
		public static var avatar:String =null;
		
		public static var serverTime:int = 0;
		public static var icon:String = "";
		public static var passWard:String="";
		
		public static var playType:int;
		public static var ip:String="";
		
		
		/**
		 *能不能连续点击坐下
		 */
		public static var isCanSitdown:Boolean=true;
		//用户名
		public static var username:String =null;
		//param地址
		public static var param:String = null;
		//通讯session
		public static var sessionKey:String = null;
		/**
		 *房卡数量 
		 */		
		public static var room_card:int = 0;
		//局数
		public static var room_round:int = 0;
		
		//金币
		public static var golds:int = 0;
		// 星币
		public static var stones:int = 0;
		public static var newplayer:int = 0;
		public static var locale:String = null;
		//性别
		public static var sex:String = null;
		//pkey
		public static var pkey:String = null;
		//系统公告
		public static var sysboard:String = null;
		//是否离线
		public static var offline:Boolean = false;
		//登录大厅
		public static var shortpkey:String = null;
		//是否已经登录
		public static var bLogined:Boolean = false;
		
		//相框
		public static var photoframe:String=null;
		
		//登场特效
		public static var effect:String=null;
		
		//挂件
		public static var pendant:String=null;
		
		//电量
		public static var power:int = -1;
		/**
		 *审核屏蔽 
		 */		
		public static var audit:int=0;
		
		public static var state:int = 0;//0正常，1=>'禁止私聊',2=>'禁止聊天',3=>'禁止旁观',4=>'禁止进入游戏',5=>'冻结'
		
		/**guize*/
		public static var Rule:Array = [];
		
		public static const roomtype_reference:Object = {4002:"蛋蛋拼十",4001:"四人斗地主",4000:"三人斗地主",3000:"西周麻将",3010:"象山麻将" ,2000:"四川血流" ,2010:"四川血战",
			4:"十堰玩法",5:"随州买马玩法",7:"上海敲麻",8:"上海百搭",9:"无锡麻将",10:"苏州麻将",11:"江苏三人麻将",12:"泰州麻将"};
		
		/**参数：{rounds:8/16局,type:1襄阳经典 2襄阳全频道 3宜城跑恰摸}*/
		public static var roomtype:int=3000;
		
		/**
		 *番数
		 */		
		public static var fanshu:int=8;
		
		//本地存储的设置，可以追加，类型默认值要预设好
		public static var settings:UserSetting=new UserSetting();
		
		public static var me:Object={uid:0,pid:"",username:"",tel:"",birthday:"",reg_ip:"",reg_date:0,gender:"f",subutype:"",utype:"pc",nickname:"",group_id:5,locale:"",avatar:"",upuid:0,ad:"pc",login_ip:"",login_times:0,login_date:0,pay:0,pay_num:0,pay_value:0,pay_date:0,agent_pay:0,agent_pay_num:0,agent_pay_date:0,agent_pay_value:0,to_agent:0,remark:"",sign:"",regcity:"",regarea:"",new_user:1,today_pay_golds:0,yesterday_pay_golds:0,yesterday_pay_date:0,golds:0,bank:0,changes:0,vip_level:0,vip_bonus_days:0,lucky_exp:0,lucky_coin:0,lucky:0,bonus_golds:0,bonus_lucky:0,startdumb:0,dumblimit:0,state:0,online:1,online_times:7614,game_times:0,game_rounds:0,game_wins:0,game_draw:0,game_max_wins:0,game_changes:0,game_service:0,ismotor:0,pay_golds:0,agent_pay_golds:0,refund_golds:0,cast_coin_times:0};
		
		
		public static var pid:String="";
		
		/**是否是重播*/
		public static var isReplay:Boolean = false;
		
		/**返回大厅之前是不是重播*/
		public static var isPreReplay:Boolean =  false;
		
		/**礼券数量*/
		public static var myLottery:int = 0;
		/**牌局结束时获得的奖券*/
		public static var changeLottery:int = 0;
		
		/**打开重播界面是不是需要重新获取数据刷新*/
		public static var isReplayRefresh:Boolean = true;
		
		/**重播用这个*/
		public static var replayUid:String = "";
		
		public static function get selfuid():String
		{
			if(isReplay)
			{
				return UserData.replayUid;
			}
			else
			{
				return UserData.uid;
			}
		}
		
		/**剩余时间*/
		public static var leftTime:int =  0;
		
		/**剩余时间*/
		public static var leftDissolveTime:int =  0;
		
		
		// --- Static Functions ------------------------------------------------------------------------------------------------------------------------------------ //
//		public static function clear():void{
//			configs={};
//			avatar =null;
//			state=0;
//			uid="0";
//			room_card=0;
//			//昵称
//			nickname = null;
//			//用户名
//			username =null;
//			//param地址
//			param = null;
//			//通讯session
//			sessionKey = null;
//			//金币
//			golds = 0;
//			// 星币
//			stones = 0;
//			newplayer = 0;
//			locale = null;
//			//性别
//			sex = null;
//			//pkey
//			pkey = null;
//			//系统公告
//			sysboard = null;
//			//是否离线
//			offline = false;
//			//登录大厅
//			shortpkey = null;
//			//是否已经登录
//			bLogined = false;
//			
//			//相框
//			photoframe=null;
//			
//			//登场特效
//			effect=null;
//			
//			//挂件
//			pendant=null;
//			
//			audit=0;
//			
//			state = 0;//0正常，1=>'禁止私聊',2=>'禁止聊天',3=>'禁止旁观',4=>'禁止进入游戏',5=>'冻结'
//			
//			//本地存储的设置，可以追加，类型默认值要预设好
//			settings=new UserSetting();
//			
//			me={uid:0,pid:"",username:"",tel:"",birthday:"",reg_ip:"",reg_date:0,gender:"f",subutype:"",utype:"pc",nickname:"",group_id:5,locale:"",avatar:"",upuid:0,ad:"pc",login_ip:"",login_times:0,login_date:0,pay:0,pay_num:0,pay_value:0,pay_date:0,agent_pay:0,agent_pay_num:0,agent_pay_date:0,agent_pay_value:0,to_agent:0,remark:"",sign:"",regcity:"",regarea:"",new_user:1,today_pay_golds:0,yesterday_pay_golds:0,yesterday_pay_date:0,golds:0,bank:0,changes:0,vip_level:0,vip_bonus_days:0,lucky_exp:0,lucky_coin:0,lucky:0,bonus_golds:0,bonus_lucky:0,startdumb:0,dumblimit:0,state:0,online:1,online_times:7614,game_times:0,game_rounds:0,game_wins:0,game_draw:0,game_max_wins:0,game_changes:0,game_service:0,ismotor:0,pay_golds:0,agent_pay_golds:0,refund_golds:0,cast_coin_times:0};
//			
//		}
	}
	
}

class UserSetting{
	public var autoBuy:Boolean=true,autoLogin:Boolean=true,loginType:String=UserData.LoginType_NONE,showCardtype:Boolean=false,useNewRaise:Boolean=false,autoSit:Boolean=true,goldNotice:int=1
}