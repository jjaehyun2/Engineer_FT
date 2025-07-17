package modules.srddzGame.srddzInerGame.model
{
	import modules.srddzGame.srddzInerGame.model.data.PaixingLogic;
	
	import rb.framework.mvc.AbstractLayer;
	
	/**四人斗地主数据*/
	public class SrddzModel extends AbstractLayer
	{
		public static const Stage_jiaofen:int = 1;
		/**保留加倍功能可扩充*/
		public static const Stage_jiabei:int = 2;
		public static const Stage_dapai:int = 3;
		
		
		/**房主*/
		public var roomOwnerUid:String = "";
		
		/***/
		public var isMouseDwon:Boolean = false;
		
		/**当前地主的位置*/
		public var dizhuPos:int = -1;
		
		/**当前的叫分*/
		public var difen:int = 0;
		
		/**当前的倍数*/
		public var beishu:int = 1;
		
		/**是否荒番*/
		public var isHuang:Boolean = false;
		/**是否头撂*/
		public var isTouliao:Boolean = false;
		/**是否明王*/
		public var isMingW:Boolean = false;
		/**是否是直接赢*/
		public var isStrictWin:Boolean = false;
		/**报道状态 0没有报道 1报道 2双报道*/
		public var baodaoState:int = 0;
		/**是否选择过报到*/
		public var isSeleBaodao:Boolean = false;
		/**是否选择过报到后直接赢*/
		public var isSeleStrictWin:Boolean = false;
		
		/**报到的牌*/
		public var baodaoCards:Array = [];
		
		/**报到数量*/
		public var baodaoNum:int = 0;
		
		/**当前的阶段*/
		public var stage:int = 0;
		
		public var curHandlePos:int = 0;
		
		public var srddzMsgs:SrddzMsgs = new SrddzMsgs();
		
		public var isStrictShowCalc:Boolean = false;
		
		public var beKickedPlayer:Object = {};
		
		public var isAutoHandle:Boolean = false;
		
		/**是否正在出牌中*/
		public var isDragingcard:Boolean = false;
		
		/**游戏是否已经开始*/
		public var isGameStart:Boolean = false;
		
		public function get gameHasStarted():Boolean
		{
			if(isGameStart || srddzMsgs.ACK_RoomInfo.RoundCount > 0)
			{
				return true;
			}
			return false;
		}
		
		public static var DissolveResult_REF:Array = ["等待操作","同意" ,"拒绝"];
		
		/**重播时，前几步一步到位*/
		public var preStepNum:int = 4;
		
		public var replayData:Array = [];
		public var replayCurStep:int = 0;
		
		/**0暂停 1播放中*/
		public var replayState:int = 0;
		
		/**是否要中断播放*/
		public var needCutdownReplay:Boolean = false;
		
		/**是否已经在玩家操作的时候预出牌了*/
		public var isClientPrePop:Boolean = false;
		
		/**玩家预出的牌*/
		public var isClientPrePopCards:int = 0;
		
		
		public function SrddzModel()
		{
			super();
		}
		
		override public function onAdd():void
		{
			
		}
		
		override public function onRemove():void
		{
			
		}
		
		/**玩家的信息*/
		public var playerInfoVec:Vector.<Object> = new Vector.<Object>();
		/**明牌*/
		public var mingpaiVec:Vector.<Boolean> = new Vector.<Boolean>();
		/**加倍*/
		public var jiabeiVec:Vector.<Boolean> = new Vector.<Boolean>();
		/**玩家的叫分 默认0分 -1是不叫*/
		public var jiaofenVec:Vector.<int> = new Vector.<int>();
		/**玩家已经出的炸弹*/
		public var outZhadanNumVec:Vector.<int> = new Vector.<int>();
		
		/**玩家手里的牌*/
		public var handleCards:Vector.<Array> = new Vector.<Array>();
		/**记录每个玩家每一步的出牌*/
		public var outputCards:Vector.<Array> = new Vector.<Array>();
		/**底牌*/
		public var dipaiCards:Array = [];
		/**当前出牌的玩家*/
		public var curOutputPos:int = -1;
		/**当前操作的玩家*/
		public var curOptPos:int = -1;
		/**是否是流局*/
		public var isLiu:Boolean = false;
		
		/**是否是当前局结束*/
		public var isEnd:Boolean = false;
		
		public var isSelfSitDown:Boolean = false;
		public var selfChairPos:int = 0;
		
		protected var _chairNum:int = 4;
		
		/**设置一共有几个人玩*/
		public function get chairNum():int
		{
			return _chairNum;
		}
		
		public function set chairNum(value:int):void
		{
			_chairNum = value;
			playerInfoVec.length = 0;
			
			outputCards.length = chairNum;
			handleCards.length = chairNum;
			mingpaiVec.length = chairNum;
			jiabeiVec.length = chairNum;
			jiaofenVec.length = chairNum;
			outZhadanNumVec.length = chairNum;
			dipaiCards.length = 0;
			
			var i:int;
			var len:int = _chairNum;
			
			for(i=0;i<len;i++)
			{
				outputCards[i] = new Array();
				handleCards[i] = new Array();
				mingpaiVec[i] = false;
				jiabeiVec[i] = false;
				jiaofenVec[i] = 0;
				outZhadanNumVec[i] = 0;
				
			}
			isGameStart = false;
			
			isEnd = false;
			isLiu = false;
		}
		
		public function resetCard():void
		{
			dizhuPos = -1;
			difen = 0;
			beishu = 1;
			//isHuang = false;
			isTouliao = false;
			isMingW = false;
			baodaoState = 0;
			baodaoNum = 0;
			
			isSeleBaodao = false;
			isSeleStrictWin = false;
			baodaoCards = [];
			
			curOutputPos = -1;
			curOptPos = -1;
			
			curOutputCards.length = 0;
			dipaiCards.length = 0;
			var i:int;
			var len:int = _chairNum;
			for(i=0;i<len;i++)
			{
				outputCards[i].length = 0;
				handleCards[i].length = 0;
				mingpaiVec[i] = false;
				jiabeiVec[i] = false;
				jiaofenVec[i] = 0;
				outZhadanNumVec[i] = 0;
			}
			
			isEnd = false;
			isLiu = false;
		}
		
		public function reset():void
		{
			beKickedPlayer = {};
			resetCard();
		}
		
		/**更新玩家手里的牌*/
		public function updateHandleCards(pos:int,cards:Array):void
		{
			handleCards[pos] = cards.concat();
			handleCards[pos].sort(PaixingLogic.compCardsFun);
		}
		
		/**叫地主完成给对应的玩家手里加上三张牌 四人斗地主不是地主的玩家不给底牌具体值*/
		public function addDipaiToHandleCards(pos:int,cards:Array):void
		{
			dipaiCards = cards.concat();
			handleCards[pos] = handleCards[pos].concat(cards);
			handleCards[pos].sort(PaixingLogic.compCardsFun);
		}
		
		/**明牌通知更新地主玩家手里的牌*/
		public function updateMingpai(pos:int,cards:Array):void
		{
			mingpaiVec[pos] = true;
			handleCards[pos] = cards.concat();
			handleCards[pos].sort(PaixingLogic.compCardsFun);
		}
		
		/**当前出的牌*/
		public var curOutputCards:Array = [];
		
		/**出牌*/
		public function outputPockers(pos:int,cards:Array):void
		{
			curOutputPos = pos;
			curOutputCards = cards.concat();
			curOutputCards.sort(PaixingLogic.compCardsFun);
			
			outputCards[pos].push(cards);
			
			var i:int,len:int=cards.length;
			
			for(i=0;i<len;i++)
			{
				var idx:int = handleCards[pos].indexOf(cards[i]);
				if(idx != -1)
				{
					handleCards[pos].splice(idx,1);
				}
				else //不知道别人的牌就随便干掉一个
				{
					handleCards[pos].splice(0,1);
				}
				
				if(pos == dizhuPos && baodaoState != 0)
				{
					idx = baodaoCards.indexOf(cards[i]);//从报到的牌里面删除出掉的牌
					if(idx != -1)
					{
						baodaoCards.splice(idx,1);
					}
				}
				
				
			}
			
	
			
		}
		
		
		//*****************************************************
		/**根据玩家的椅子号返回玩家的位置</br>
		 * 
		 * 3个人的时候是
		 *  0bottom 1right 2left 
		 * </br>
		 * 4个人的时候是
		 *  0bottom 1right 2top 3left
		 * 
		 * */
		public function getChairDirByPos(pos:int):int
		{
			if(pos == -1)
			{
				return -1;
			}
			var returnDir:int = 0;
			returnDir = pos-selfChairPos;
			if(returnDir < 0)
			{
				returnDir = returnDir + chairNum;
			}
			
			return returnDir;
		}
		
		/**根据玩家的位置 返回玩家对应的椅子号*/
		public function getChairPosByDir(dir:int):int
		{
			var returnPos:int;
			returnPos = selfChairPos + dir;
			
			if(returnPos > chairNum-1)
			{
				returnPos = returnPos - chairNum;
			}
			return returnPos;
		}
		
		public function updateOnePlayerInfo(info:Object):void
		{
//			if(info.pos%2 == 0)
//			{
//				info.sex = 1;
//			}
//			else
//			{
//				info.sex = 2;
//			}
			
			var i:int;
			var len:int = playerInfoVec.length+0;
			var has:Boolean = false;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == info.uid)
				{
					if(playerInfoVec[i].pos != info.pos)
					{
						trace("传过来的数据有错误!!!!!!");
					}
					
					updateObjFromObj(playerInfoVec[i],info);
					
					has = true;
					break;
				}
			}
			
			if(has == false)//之前里面没有
			{
				playerInfoVec.push(info);
			}
			
			if(info.uid == UserData.selfuid)
			{
				selfChairPos = info.pos;
				if(selfChairPos == -1)
				{
					isSelfSitDown = false;
					selfChairPos = 0;
				}
				else
				{
					isSelfSitDown = true;
				}
			}
		}
		public function playerByPos(pos:int):Object
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].pos == pos)
				{
					return playerInfoVec[i];
				}
			}
			return null;
		}
		
		public function playerByUid(uid:int):Object
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					return playerInfoVec[i];
				}
			}
			return null;
		}
		
		public function getPlayerPosByUid(uid:int):int
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					return playerInfoVec[i].pos;
				}
			}
			return 0;
		}
		
		public function getPlayerUidByPos(pos:int):int
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].pos == pos)
				{
					return playerInfoVec[i].uid;
				}
			}
			return 0;
		}
		
		
		
		public function getPlayerNicknameByUid(uid:int):String
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					return playerInfoVec[i].nickname;
				}
			}
			return "";
		}
		
		protected function updateObjFromObj(obj:Object,fromObj:Object):void
		{
			obj.prePos = obj.pos;
			for (var p:String in fromObj)
			{
				if(fromObj[p] != undefined)
				{
					obj[p] = fromObj[p];
				}
			}
		}
		
		public function sitDown(uid:String, pos:int,score:int):void
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					
					playerInfoVec[i].pos = pos;
					playerInfoVec[i].score = score;
					playerInfoVec[i].canKick = false;
					
					if(uid == UserData.selfuid)
					{
						if(pos != -1)
						{
							isSelfSitDown = true;
							selfChairPos = pos;
						}
						else
						{
							isSelfSitDown = false;
							selfChairPos = 0;
						}
					}
				}
			}
		}
		
		public function standup(uid:String, pos:int):void
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					
					playerInfoVec[i].pos = pos;
					playerInfoVec[i].canKick = false;
					
					if(uid == UserData.selfuid)
					{
						if(pos != -1)
						{
							isSelfSitDown = true;
							selfChairPos = pos;
						}
						else
						{
							isSelfSitDown = false;
							selfChairPos = 0;
						}
					}
				}
			}
		}
		
		public function updateReadyState(pos:int,readyState:Boolean,piaoValue:int):void
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].pos == pos)
				{
					playerInfoVec[i].readystate = true;
					playerInfoVec[i].piao = piaoValue;
					break;
				}
			}
		}
		
		//从玩家列表中删除某个玩家
		public function leavePlayer(uid:int):void
		{
			var i:int;
			var len:int = playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
				{
					playerInfoVec.splice(i,1);
					break;
				}
			}
		}
		
		public function updatePlayerInfoVec(arr:Array):void
		{
			var i:int;
			var len:int = arr.length;
			var info:Object;
			for(i=0;i<len;i++)
			{
				info = arr[i];
				if(UserData.isReplay)
				{
					info.index = info.index != undefined ? info.index : 0;
					info.diamond = info.diamond != undefined ? info.diamond : 0;	
					info.Icon = info.Icon != undefined ? info.Icon : "";
					info.score = info.score != undefined ? info.score : 0;	
					info.coin = info.coin != undefined ? info.coin : 0;
					info.readystate = info.readystate != undefined ? info.readystate : 0;
					info.uid = info.uid != undefined ? info.uid : 0;
					info.IP = info.IP != undefined ? info.IP : "";
					info.Name = info.name;
					info.Index = info.index;
					info.Coin = info.coin;
					info.readystate = 1;
					info.UID = info.uid;
					info.Diamond = info.diamond;
					if(info.icon)
					{
						info.Icon = info.icon;
					}
					
				}
				info.nickname = info.Name;
				info.uid = info.UID;
				info.ip = info.IP;
				info.pos = info.Index;
				info.golds = info.Coin;
				
				if(info.uid != "" || info.uid != 0)
				{
					if(info.state == 3)
					{
						beKickedPlayer[info.pos] = info.uid;
						info.state = 1;
						info.pos = -1;
					}
					else if(info.state == 4)
					{
						beKickedPlayer[info.pos] = info.uid;
						info.state = 2;
						info.pos = -1;
					}
					updateOnePlayerInfo(arr[i]);
				}
			}
		}
		
		/**胡牌后，将所有readystate改为0*/
		public function setPlayerReadyFalse():void
		{
			var i:int,len:int=playerInfoVec.length;
			
			for(i=0;i<len;i++)
			{
				playerInfoVec[i].readystate = 0;
			}
		}
		
		/**判断是否可以报到*/
		public function getBaodaoNum():int
		{
			return PaixingLogic.getBaodaoNum(handleCards[selfChairPos]);
		}
		
		public function getBaodaoCards():Array
		{
			return PaixingLogic.getBaodaoCards(handleCards[selfChairPos]);
		}
		

		

	}
}