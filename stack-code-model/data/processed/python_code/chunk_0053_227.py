package modules.game.majiangGame.model
{

	public class MajiangMsgs
	{
		/**
		 * 进入房间</br>
		 * 
		 * {</br>
			Name    string  // Nick Name</br>
			UID     string  // User ID  用户ID</br>
			RID     int     // 房间号</br>
			IP      string  //</br>
			Index   int     // 房间位置// 0=东</br>
			Icon    string  // 头像</br>
			Coin    int     // 金币</br>
			Type    int     // 类型</br>
			Diamond int     // 钻石</br>
			Level   int     // 等级</br>
			Robot   bool    // 是否是机器人</br>
			GPS_LNG float64 //  经度 Longitude   简写Lng</br>
			GPS_LAT float64 //  纬度 Latitude    简写Lat</br>
			MSG     string</br>
		}</br>
		 * */
		public var ACKBC_Into_Room:Object;
		
		/**
		 *  message ACK_RoomInfo {
	required int32 ID   			= 1;
	optional int32 Type 			= 2;
	optional int32 City 			= 3;
	optional int32 Level     		= 4;
	optional int32 MinCoin  		= 5; 		//最小底分
	optional int32 MaxCoin  		= 6; 		//最大底分
	repeated int32 Rule   			= 7; 		//规则ID
	
	//---------------------------------------
	
	optional int32 Seat  		= 8;        // 座位数量
	optional int32 UserCount     = 9; 		// 用户数量
	optional int32 CurIndex      = 10;       // 当前出牌的用户
	optional int32 CurToolIndex  = 11;       // 当前操作用户
	optional int32 ZhuangIndex   = 12;       // 庄家的UID
	optional string MSG 			= 13;		// 
}
		 * */
		public var ACK_RoomInfo:Object;
		
		public var ACK_Room_User:Object;
		
		
		
		/**
		 * 游戏开始
		 * RID        int</br>
			MSG        string</br>
			Dict       int    //</br>
			StartIndex int    // 开始的位置</br>
			ZhuangUID  string // 从庄家开始</br>
		 * 
		 * */
		public var ACKBC_Start:Object;
		
		/**发牌
		 * 
		 * UID   string</br>
		 * Cards []*interface{}</br>
		 * */
		public var ACK_UserCard:Object;
		
		public var ACK_User_SeatCard:Object;
		
		
		/**
		 * 摸牌
		 * 
		 * UID     string //user id  摸牌的人</br>
			CID     int    //Card ID</br>
			Forward int    //从前面拿牌=0     从后面拿牌=1</br>
			Type    int    //牌型</br>
			Num     int    //号</br>
			MSG     string </br>
		 * 
		 * */
		public var ACK_GetCard:Object;
		
		/**广播摸牌
		 * 
		 * UID     string //user id  摸牌的人</br>
		 * Forward int    //从前面拿牌=0     从后面拿牌=1</br>
		 * */
		public var ACKBC_GetCard:Object;
		
		/**
		 * 广播通知可以操作出牌
		 */
		public var ACKBC_CurPlayer:Object;
		
		/**
		 * 出牌通知
		 * 
		 * UID  string // user id  出牌的人</br>
		   CID  int    // Card ID</br>
		   Type int    // 牌型</br>
		   Num  int    // 号</br>
		   MSG  string //</br>
		 * 
		 * */
		public var ACKBC_PutCard:Object;
		
		/**
		 * 通知玩家操作
		 * UID     string</br>
		   Type    []int // 吃 碰 杠 胡  有可能在一起</br>[1,1,0,0]  
		    MSG     string</br>
			TimeOut int</br>
		 * */
		public var ACK_WaitTool:Object;
		
		public var ACKBC_Chow:Object;
		public var ACKBC_Peng:Object;
		public var ACKBC_Kong:Object;
		public var ACKBC_Sitdown:Object;
		public var ACKBC_Standup:Object;
		public var ACKBC_Ready:Object;
		public var ACKBC_Exit_Room:Object;
		public var NotifyStartGame:Object;
		public var ACKBC_Win:Object;
		public var ACKBC_Draw:Object;
		public var ACKBC_Total:Object;
		public var ACKBC_Card_Init:Object;
		public var MSG_NOTIFY_SUMMARY:Object;
		public var AckDisband:Object;
		public var NotifyDisband:Object;
		public var NotifyUserState:Object;
		//public var ACK_BattleDetail:Object;
		
		
		//***********************下面都是之前的
		
		
		
		/**
		 {</br>
		 enum ENTER_REL</br>
		 {</br>
		 ENTER_OK = 0;</br>
		 ENTER_WRONG_INGAME = 1; //游戏中</br>
		 ENTER_WRONG_RELOAD = 2;	//需要重新load</br>
		 ENTER_WRONG_CHANNEL= 3; //请求的频道不对</br>
		 ENTER_WRONG_GOLDS  = 4;	//玩家金币不符合要求</br>
		 ENTER_WRONG_ACCOUNT= 5;	//帐号异常，禁止登陆</br>
		 ENTER_WRONG_OTHERLOGIN = 6;//帐号在别处上线</br>
		 ENTER_WRONG_ROOMFULL = 7;//房间已满</br>
		 ENTER_WRONG_OTHERGAME = 8;//在另外的游戏中</br>
		 ENTER_WRONG_NULLPOP = 9;//连续15把不下注，或者携带筹码小于最底倍连续5把不下注；踢回大厅</br>
		 ENTER_WRONG_GOLDS_LITTLE = 10;//玩家金币不符合要求，太少</br>
		 ENTER_WRONG_GOLDS_MUCH = 11;//玩家金币不符合要求，太多</br>
		 ENTER_WRONG_TABLE_VIP = 12;//桌子VIP</br>
		 ENTER_WRONG_CHGT      =13;//换桌</br>
		 }</br>
		 required ENTER_REL rel = 1;   //状态			//状态</br>
		 optional int64 golds	= 2;</br>
		 optional int32 step	= 3;</br>
		 optional int32 cid	= 4 [default = 0];</br>
		 optional int32 gid	= 5 [default = 0];</br>
		 optional int32 rtype	= 6 [default = 0];</br>
		 optional int32 ridx	= 7 [default = 0];</br>
		 optional int64 bank	= 8 [default = 0];</br>
		 }</br>
		 */
		public var control_user_enterroom_Info:Object;
		
		/**
		 {</br>
		 required int32 rel = 1;   //状态</br>
		 optional int32 uid	= 2;</br>
		 optional int64 golds	= 3;</br>
		 }</br>
		 */
		public var control_add_golds_Info:Object;
		
		/**
		 {</br>
		 required int32 n	= 1;	//流水号</br>
		 optional int32 rel = 2;   //状态   //状态</br>
		 }</br>
		 */
		public var control_gate_Info:Object; 
		
		/**
		 {</br>
		 required int32 uid	= 1;</br>
		 }</br>
		 */
		public var control_bonus_golds_Info:Object;
		
		/**
		 {</br>
		 enum PSEND_REL</br>
		 {</br>
		 PROPS_SEND_OK = 0;					//赠送成功</br>
		 PROPS_CLASS_ERROR = 1;			//道具类型错误</br>
		 PROPS_GOLDS_ERROR = 2;			//金币错误</br>
		 PROPS_PLAYER_ERROR = 3;			//玩家错误</br>
		 PROPS_PRICE_TYPE_ERROR = 4;	//金币购买的其他情况-------暂时不支持	</br>
		 PROPS_ALL_PLAYER_ERROE = 5;	//群发玩家错误</br>
		 PROPS_UN_VIP = 6;						//只有vip1以上才能发</br>
		 }</br>
		 required PSEND_REL rel = 1;   //状态</br>
		 optional int32 fuid	= 2;</br>
		 optional int32 pid	= 3;		//道具ID</br>
		 optional int64 cost	= 4;		//道具消费</br>
		 optional int64 bonus	= 5;	//筹码奖励</br>
		 optional int32 pclass	= 6;	//道具类型,0,普通道具;1,表情包;2,工资卡;3,喇叭</br>
		 optional int32 timelen	= 7;	//有效时间（单位可以使天，年，秒，等）</br>
		 repeated int32 uids     = 8 [packed=true];</br>
		 }</br>
		 */
		public var control_use_prop_Info:Object;
		
		/**
		{</br>
		required int32 type	= 1;	//0,join;2,leave;3,up level;6,slots bonus</br>
		optional int32 tid	= 2 [default = 0];</br>
		optional int32 uid	= 3 [default = 0];</br>
		optional string nn	= 4 [default = ""];			//昵称</br>
		optional int32 vip	= 5 [default = 0];</br>
		optional sint32 pos	= 6 [default = 0];</br>
		optional int32 level	= 7 [default = 0];		//经验</br>
		optional int64 golds	= 8 [default = 0];</br>
		optional int64 bonus	= 9 [default = 0];			</br>
		optional int32 vipday	= 10 [default = 0];</br>
		optional int64 pond	= 11 [default = 0];</br>
		optional int64 seat	= 12 [default = -1];		//椅子号</br>
		}
		*/
		public var control_game_msg_Info:Object;
		
		/**
		{</br>
		required int32 pos = 1;</br>
		optional sint32 seat = 2 [default = -1];		//椅子号</br>
		optional string nn = 3 [default = ''];			//昵称</br>
		optional int32 smiletype = 4 [default = 0];</br>
		optional int32 smileid = 5 [default = 0];</br>
		optional int32 state  = 6 [default = 0];</br>
		optional int32 uid  = 7 [default = 0];</br>
		}
		*/
		public var control_player_smile_Info:Object;
		
		
		/**
		 {</br>
		 required int32 rel = 1;		//状态   //状态</br>
		 optional int32 uid = 2;</br>
		 optional string nn = 3;		//昵称</br>
		 optional string msg = 4;</br>
		 }</br>
		 
		 */
		public var control_game_chat_Info:Object;
		
		/**
		 {</br>
		 message user_attr</br>
		 {</br>
		 required int32 uid = 1;
		 optional int32 pos = 2 [default = 0];</br>
		 optional int32 level = 3 [default = 0];			//经验</br>
		 optional int32 vip = 4 [default = 0];</br>
		 optional int64 golds = 5 [default = 0];
		 optional string nn = 6;							//昵称	</br>				
		 optional string sex = 7;						//性别</br>
		 optional int32 seat = 8 [default = -1];			//椅子号</br>
		 optional int32 sign = 9 [default = 0];			//第一位表示是否手机玩家</br>
		 optional int32 lockdealer = 10 [default = 0];	//当前庄家申请下庄(延迟游戏结束后下庄)</br>
		 optional int32 firstbet = 11;					//第一个操作，为1</br>
		 optional int64 chips = 12 [default = 0];		//当前筹码</br>
		 optional int64 lstchips = 13 [default = 0];		//上轮下注筹码总量</br>
		 optional int32 action = 14 [default = 0];		//德州玩家的动作</br>
		 optional int32 laction = 15 [default = 0];		//德州玩家的动作</br>
		 optional string cs = 16 [default = ''];			//德州玩家扑克</br>
		 optional int32 pstate = 17 [default = 0];		//德州状态 1表示正在参与游戏</br>
		 optional int32 serieswins = 18 [default = 0];		//百家乐连赢次数</br>
		 
		 }</br>
		 repeated user_attr users = 1;</br>
		 }</br>
		 */
		public var control_user_list_Info:Object;
		
		/**
		 {</br>
		 required int64 bonus = 1;</br>
		 optional int64 pond  = 2;</br>
		 }</br>
		 */
		public var control_lottery_award_Info:Object;
		
		/**
		 {</br>
		 required int32 cmd = 1;</br>
		 optional int32 uid = 2;</br>
		 optional int32 sid = 3;</br>
		 }
		 */
		public var control_msg_Info:Object;
		
		/**
		 {</br>
		 required int32 type = 1;</br>
		 optional int32 rel = 2;		//状态 </br>
		 optional string un = 3;</br>
		 optional string nn = 4;		//昵称</br>
		 optional string fun = 5;</br>
		 optional string fnn = 6;	//昵称</br>
		 }</br>
		 */
		public var control_gameitem_friend_Info:Object;
		
		/**
		 {</br>
		 required int32 rel = 1;   //状态 </br>
		 optional int32 pid = 2;</br>
		 optional int32 deadline = 3;</br>
		 optional int32 price = 4;</br>
		 optional int64 stones = 5;</br>
		 }
		 */
		public var control_buy_smile_Info:Object;
		
		/**
		 {</br>
		 required int32 uid = 1;</br>
		 optional int32 unbanker = 2;				//当前庄家申请下庄(延迟游戏结束后下庄)</br>
		 repeated int64 gatebet = 3 [packed=true];	</br>
		 optional int32 rel = 4;						//状态 </br>
		 optional int64 golds = 5;	</br>
		 }
		 */
		public var control_game_offline_Info:Object;
		
		/**
		 {</br>
		 optional int32 banker = 1 [default = 0];		//当庄的位置</br>
		 message nuserend</br>
		 {</br>
		 optional int32 uids = 1 [default = 0];			//用户ID</br>
		 optional int32 golds = 2 [default = 0];		//用户金币</br>
		 optional int32 pos = 3 [default = 0];       //玩家位置</br>

		 }</br>
		 repeated userend nuserend = 2;						//用户信息</br>
		 optional int32 nDice1 = 3 [default = 0];							//第一个骰子</br>
		 optional int32 nDice2 = 4 [default = 0];							//第二个骰子</br>
		 * optional int32 curround = 5 [default =0];//当前第几局 }		
		 }
		 */
		public var control_game_mjstart_Info:Object;
		
		/**
		 * message control_game_mjopration   //ACK|GLID_MAHJONG_OPRATION  12806 发送玩家的操作</br>
{</br>
	optional int32 uid = 1 [default = 0]; 	//用户ID</br>
	optional int32 mjid = 2 [default = 0];	//摸到的牌，或者是别人打的牌</br>
	optional int32 opration = 3 [default = 0];	//可以操作的类型 碰（4），胡（32），听（16），自摸（64），杠（8）假设这个操作有碰和杠 那么这个值是:12(0000 1100)按位与就好了</br> 
	optional int32 waittime = 4 [default = 0];	//等待时间</br>
	message opercard</br>
	{</br>
		optional int32 card = 1 [default = 0];		//碰，胡，听 的牌</br>
		optional int32 type = 2 [default = 0];//0 胡 1听 2碰 3杠</br>
		message hucard</br>
		{</br>
			optional int32 card = 1 [default = 0]; //停牌后胡的牌</br>
		}</br>
		repeated hucard nhucard=3;//听牌后胡的牌</br>
		message koucard</br>
		{</br>
			optional int32 card = 1 [default = 0]; //听牌后可以扣的牌</br>
		}</br>
		</br>
		message gangcard</br>
		{</br>
			optional int32 card = 1 [default = 0]; //可以杠的牌</br>
			optional int32 type = 2 [default = 0]; //杠的类型，0碰杠 1暗杠 ，2明杠</br>
		}</br>
		repeated koucard nkoucard =4;//可以扣的牌</br>
		optional int32 gangtype = 5 [default = -1]; //杠的类型，0碰杠 1暗杠 2明杠</br>
		repeated gangcard ngangcard =6;//可以杠的牌</br>
	}</br>
	repeated opercard nopercard=5;</br>
}
		 */
		public var control_game_mjopration_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1[default = 0];//用户ID</br>
		 message usercard</br>
		 {</br>
		 optional int32 card = 1[default = 0];</br>
		 }</br>
		 repeated usercard nusercard = 2;//用户手上的牌</br>
		 }
		 */
		public var control_game_mjcard_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1 [default = 0];//用户ID</br>
		 optional int32 card = 2 [default = 0];//碰的牌</br>
		 optional int32 pos = 3 [default = 0];//碰牌人的位置</br>
		 optional int32 waitime = 4 [default = 0];//碰完牌等待出牌时间</br>
		 optional int32 rel = 5 [default =1];//碰牌操作返回 0失败 1成功</br>
		 }
		 */
		public var control_game_operation_peng_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1 [default = 0];//用户ID</br>
		 optional int32 card = 2 [default = 0];//杠的牌</br>
		 optional int32 pos = 3 [default = 0];//杠牌人的位置</br>
		 optional int32 type = 4 [default = 0];//杠牌的类型    0碰杠 1暗杠 3+1</br>
		 message MoneryOp</br>
		 {</br>
		 optional int32 nuid = 1 [default = 0];//用户ID</br>
		 optional int64 monery =2 [default = 0];//加减钱数值</br>
		 }</br>
		 repeated MoneryOp nMoneryOp =5;//杠产生的金币操作</br>
		 optional int32 rel = 6 [default = 1]; //杠牌操作返回 0失败 1成功</br>
		 }
		 */
		public var control_game_operation_gang_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1 [default = 0];//用户ID</br>
		 optional int32 card = 2 [default = 0];//牌ID</br>
		 optional int32 pos = 3 [default = 0];//出牌人的位置</br>
		 optional int32 rel = 4 [default = 1];//出牌操作返回 0失败 1成功</br>
		 }
		 */
		public var control_game_operation_pop_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1 [default = 0]; //用户ID</br>
		 message holdcard</br>
		 {</br>
		 optional int32 card = 1 [default = 0];//持有的牌，明牌的话会把牌数据发给客户端</br>
		 optional int32 type = 2 [default = 0];//0表示持有的 1表示扣的</br>
		 }</br>
		 repeated holdcard nholdcard = 2;//持有的牌</br>
		 optional int32 rel = 3 [default = 1];//停牌操作返回 0失败 1成功</br>
		 }
		 */
		public var control_game_operation_ting_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid = 1 [default = 0];//抢杠人ID</br>
		 optional int32 guid = 2 [default = 0];//杠牌人ID</br>
		 optional int32 card =3 [default = 0];//杠的牌</br>
		 }
		 */
		public var control_game_operation_qianggang_Info:Object;
		
		/**
		 {</br>
		 message userinfo</br>
		 {</br>
		 optional int32 uid = 1 [default = 0];//用户id</br>
		 optional string name = 2 [default = ""];//用户名字</br>
		 optional int32 ratio =3 [default = 0];//用户翻数</br>
		 optional int32 gangfen =4 [default = 0];//杠的分数</br>
		 optional int64 zongfen =5 [default = 0];//总分</br>
		 optional int32 type = 6 [default = 0];//类型 0为与自己无关 1输家 2赢家</br>
		 message card//牌</br>
		 {</br>
		 optional int32 card = 1 [default = 0];//牌</br>
		 }</br>
		 repeated card ngangcard = 7;//杠的牌</br>
		 repeated card npengcard = 8;//碰的牌</br>
		 repeated card nholdcard = 9;//手上持有牌</br>
		 message hucardtype</br>
		 {</br>
		 optional int32 type = 1 [default = 0];//牌型</br>
		 optional int32 ratio =2 [default = 0];//多少翻</br>
		 }</br>
		 repeated hucardtype nhucardtype= 10;//胡牌的类型</br>
		 }</br>
		 optional int32 roomid =1 [default = 0];//房间号</br>
		 optional int32 innings =2 [default = 0];//当前局数</br>
		 repeated userinfo userinfos=3;//玩家信息</br>
		 optional int32 curtype =4 [default = 0];//当局是自摸还是点炮 0自摸 1点炮 2流局</br>
		 optional int32 zimoorpaopos =5 [default = 0];//自摸或者点炮玩家位置</br>
		 optional int32 rel =6 [default = 1];//胡牌操作返回 0失败 1成功</br>
		 }
		 */
		public var control_game_operation_hu_Info:Object;
		
		/**
		 {</br>
		 optional int32 rtype = 1 [default = 0];  //rtype</br>
		 optional int32 ridx  = 2 [default = 0];	//ridx</br>
		 optional int32 tid   = 3 [default = 0];	//桌子ID</br>
		 optional int32 roomstate =4 [default = 0];	//当前该桌子的状态</br>
		 optional int32 BankerPos = 5 [default = 0];	//当前桌子上庄的位置</br>
		 optional int32 CurrdOutCardpos = 6 [default = 0];//当前出牌玩家的位置</br>
		 optional int32 curcount = 7 [default =0];//当前局数</br>
		 optional int32 sumcount = 8 [default =0];//总局数</br>
		 optional int32 ncode = 9 [default =0];//房号</br>
		 optional int32 roomtype = 10 [default =0];//当前麻将类型 1襄阳玩法 2襄阳全频道 3宜城跑恰摸八</br>
		 optional int32 remaincard =11 [default =0];//剩余的牌输</br>
		 optional int32 magiccard = 12 [default =-1];//百搭牌</br>
		 </br>
		 }*/
		public var control_game_operation_tableinfo_Info:Object;
		
		/**
		 message control_game_operation_userinfo //ACK|GLID_MAHJONG_OPERATION_USERINFO	12817 发送玩家信息</br>
{</br>
	message user_attr</br>
	{</br>
		optional int32 uid = 1 [default = 0]; //用户ID</br>
		optional int32 pos = 2 [default = 0];	//用户位置</br>
		optional int32 vip = 3 [default = 0];	//用户VIP等级</br>
		optional string sex = 4 [default = ""];//用户性别</br>
		optional int32 sign = 5 [default = 0];//用户从哪个平台登录 PC or phone</br>
		optional string nickname =6 [default = ""];//用户名字</br>
		message card_attr</br>
		{</br>
			optional int32 type =1 [default = 0];//牌的类型 牌的类型 0碰 1明杠 2 暗杠 3持有 4已出 5扣牌 6可以胡的牌 7吃的牌</br>
			optional int32 card =2 [default = 0];//牌值</br>
			optional int32 isPeng =3 [default = 0];//（如果是已经出的牌，0表示没有，1表示被碰或者杠了</br>
			optional int32 chicards =4;//（如果是吃的话，这个就是吃的牌组</br>
		}</br>
		repeated card_attr card =7;//牌信息,其他玩家显示碰或杠的 自己才传持有</br>
		optional int32 level =8 [default = 0];//用户的等级</br>
		optional int32 golds =9 [default = 0];//用户金币</br>
		optional int32  readystate=10 [default = 0];//是否准备</br>
		optional int32 isTing =11 [default = 0];//是否已经听牌 0没有 1 有</br>
		optional string ip =12 [default = ""];//玩家的IP地址</br>
		optional int32 piao = 13 [default =0];//漂</br>
	}</br>
	repeated user_attr user =1;//用户信息</br>
	optional int32 handlepos =2 [default = 0];//当前操作玩家的位置  //后面是操作通知的信息</br>
	 * 
	 * optional int32 reconnect =3 [default = 0];//是否断线重连</br>
}</br>
		 */
		public var control_game_operation_userinfo_Info:Object;
		
		/**
		 {</br>
		 optional int32 uid =1 [default = 0];//用户ID</br>
		 optional int32 pos =2 [default = 0];//用户位置</br>
		 optional int32 piao = 3 [default =0];//漂</br>
		 optional int32 rel = 4 [default =1];//状态，1成功 0失败 3是已经准备过了</br>
		 }
		 */
		public var control_game_operation_ready_Info:Object;
		
		/**
		 {</br>
		 message userinfo</br>
		 {</br>
		 optional int32 uid =1 [default = 0];//用户ID</br>
		 optional string name = 2 [default =""];//用户名称</br>
		 optional int32 zimocount =3 [default = 0];//自摸次数</br>
		 optional int32 jiepaocount =4 [default = 0];//接炮次数</br>
		 optional int32 dianpaocount =5 [default =0];//点炮次数</br>
		 optional int32 angangcount =6 [default =0];//暗杠次数</br>
		 optional int32 minggang = 7 [default =0];//明杠次数</br>
		 optional int32 zongchengji =8 [default = 0];//总成绩</br>
		 }</br>
		 optional int32 roomtid =1 [default =0];//房间号</br>
		 optional int32 curcount =2 [default =0];//当前局数</br>
		 optional int32 sumcount =3 [default =0];//总局数</br>
		 repeated userinfo userinfos =4;//用户信息</br>
		 }
		 */
		public var control_game_settlement_Info:Object;
		
		/**
		 {</br>
		 required int32 type	= 1;	//0进入  1离开</br>
		 optional int32 tid	= 2 [default = 0];</br>
		 optional int32 uid	= 3 [default = 0];</br>
		 optional string nn	= 4 [default = ""];			//昵称</br>
		 optional int32 vip	= 5 [default = 0];</br>
		 optional sint32 pos	= 6 [default = 0];</br>
		 optional int32 level	= 7 [default = 0];		//经验</br>
		 optional int64 golds	= 8 [default = 0];</br>
		 optional int64 bonus	= 9 [default = 0];</br>			
		 optional int32 vipday	= 10 [default = 0];</br>
		 optional int64 pond	= 11 [default = 0];</br>
		 optional int64 seat	= 12 [default = -1];		//椅子号</br>
		 }*/
		public var control_game_mj_msg_Info:Object;
		
		/**
		 * {</br>
		 * optional int32 uid = 1 [default = 0];//用户ID</br>
			optional int32 card = 2 [default = 0];//牌ID</br>
			optional int32 pos = 3 [default = 0];//出牌人的位置</br>
			optional int32 rel = 4 [default = 1];//出牌操作返回 0失败 1成功</br>
			optional int32 waittime =5 [default =0];//超时时间</br>

		 * }</br>
		 * 
		 * */
		public var control_game_operation_mopai_info:Object;
		
		
		/**
message control_game_operation_jieshan //ACK|GLID_MAHJONG_OPERATION_JIESAN  12822 解散</br>
{</br>
	optional int32 uid =1 [default =0];//发起解散ID</br>
	optional int32 ntype =2 [default =0];//类型, 0是解散信息。 1是牌局开始前桌主解散 2是第一局没有打完解散，房卡退还 3解散成功 4解散失败</br>
	optional int32 TimeOut=3 [default=0];//超时时间</br>
	message user</br>
	{</br>
		optional int32 uid =1 [default =0];//其他用户的ID</br>
		optional int32 state=2 [default =0];//0表示等待操作，1表示同意 2表示拒绝</br>
	}</br>
	repeated user userinfo =4;//其他用户的状态</br>
}</br>
		 * */
		public var control_game_operation_jieshan_info:Object;
		
		/**
		 * message control_game_operation_koupai ////ACK|GLID_MAHJONG_OPERATION_KOUPAI  12824 扣牌</br>
{</br>
	optional int32 rel = 1 [default =1];//1表示成功 0失败</br>
	message card</br>
	{</br>
		optional int32 card = 1 [default =0];</br>
	}</br>
	repeated card koucards = 2;//还可以扣的牌</br>
	repeated card ting = 3;//现在听的牌</br>
}
		 * 
		 * */
		public var control_game_operation_koupai_info:Object;
		
		/**
		 * 
		 * message control_game_operation_hucard</br>
{</br>
	optional int32 rel = 1 [default =1];//1表示成功 0失败</br>
	message ting</br>
	{</br>
		optional int32 card = 1 [default =0];</br>
		message hu</br>
		{</br>
			optional int32 card = 1 [default =0];</br>
		}</br>
		repeated hu nhu = 2;//可以胡的牌</br>
	}</br>
	repeated ting nting = 2;//可以听的牌</br>
}
		 * 
		 * */
		public var control_game_operation_hucard_info:Object;
		
		
		/**
		 * 踢人</br>
		 * message control_game_operation_kill ////ACK|GLID_MAHJONG_OPERATION_KILLP  12823 踢人</br>
{</br>
	optional int32 rel = 1 [default =1];//踢人状态，1表示成功，0表示失败</br>
	optional int32 uid = 2 [default =1];//被踢人的id;</br>
	optional int32 pos = 3 [default =1];//被踢人的位置</br>
}</br>
		 * */
		public var control_game_operation_kill_info:Object;
		
		/**
		 * 
		 * message control_game_operation_exitroom //ACK|GLID_MAHJONG_OPERATION_USEREXIT 12826 用户自己退出</br>
{</br>
	optional int32 rel = 1 [default =1];//1表示成功 0失败</br>
	optional string errorinfo = 2 [default = ""];//错误原因</br>
	 * optional int32 userid= 3 [default =0];//用户ID</br>
}</br>
		 * */
		public var control_game_operation_exitroom_info:Object;
		

		/**message control_game_operation_chi //ACK|GLID_MAHJONG_MJCARD_CHI 12828 吃牌</br>
		{</br>
			optional int32 rel = 1 			[default =1];	//状态，1成功</br>
			optional int32 uid = 2 			[default =0];	//用户ID</br>
			optional int32 pos = 3 			[default =0];	//用户位置 </br>
			optional int32 chicard = 4 		[default =0];	//吃的牌
			repeated int32 chicards =5;						//用户吃后的牌组</br>
		}*/
		public var control_game_operation_chi_info:Object;
		
		
		/**
		 * message control_game_operation_buhua //ACK|GLID_MAHJONG_OPERATION_BUHUA 12829 补花</br>
{</br>
	optional int32 rel = 1 			[default =1];	//状态，1成功</br>
	optional int32 uid = 2 			[default =0];	//用户ID</br>
	optional int32 pos = 3 			[default =0];	//用户位置</br>
	optional int32 count = 4 		[default =0];	//补花数量</br>
	repeated int32 buhuacards =5;						//补花的牌</br>
	repeated int32 huanhuicards =6;					//补花换回来的牌</br>
}
		 * */
		public var ACK_TransferHuaResponse:Object;
		
		/**
		 * message control_game_mjmagic      //ACK|GLID_MAHJONG_OPERATION_BAIDA  //12830 百搭</br>
{</br>
	optional int32 fancard = 1[default = 0];//翻牌</br>
	optional int32 magiccard = 2[default = 0];//百搭</br>
}</br>
		 * */
		public var control_game_mjmagic_info:Object;
		
		
		public function MajiangMsgs()
		{
		}
	}
}