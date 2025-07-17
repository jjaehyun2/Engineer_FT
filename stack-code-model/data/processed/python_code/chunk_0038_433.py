package modules.game.majiangGame.model
{
	import common.view.PopBox;
	
	import laya.maths.Point;
	
	import modules.game.majiangGame.view.card.BaseCard;
	
	import rb.framework.mvc.AbstractLayer;
	
	/**这个类是用来存放整个麻将桌面的游戏数据的 所有数据都是 下 右 上 左*/
	public class MajiangModel extends AbstractLayer
	{
		public var isStrictShowCalc:Boolean = false;
		
		public var beKickedPlayer:Object = {};
		
		public var isAutoHandle:Boolean = false;
		public var pengGangStepObj:Object = new Object();
		
		public var koupaiwancheng:Boolean = false;
		
		/**是否正在出牌中*/
		public var isDragingcard:Boolean = false;
		
		/**是否直接跳过胡的动画*/
		public var isNeedSkipHuAni:Boolean = false;
		
		public var warnCThenBaoipStr:String = "\n点击确认会承包对方，是否确认？";
		
		public function get gameHasStarted():Boolean
		{
			if(isGameStart || majiangMsgs.ACK_RoomInfo.RoundCount > 0)
			{
				return true;
			}
			return false;
		}
		
		/**游戏是否已经开始*/
		public var isGameStart:Boolean = false;
		
		
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
		
		public var isClientPrePopCard:int = 0;
		

		
		
		public var majiangMsgs:MajiangMsgs = new MajiangMsgs();
		public var fengquan:int = 0;
		
		public function MajiangModel()
		{
			super();
		}
		
		protected function initData():void
		{
			
		}
		
		override public function onAdd():void
		{
			
		}
		
		override public function onRemove():void
		{
			
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
		
		public var tingCardsOfKouBtn:Array = [];
		public var tingCardsOfCancelBtn:Array = [];
		
		public var kouCards:Array = [];
		
		/**0正花  1野花*/
		public function getHuaArr(type:int,pos:int):Array
		{
			var retArr:Array = [];
			var xiangduiIdx:int = 0;
			var zhenghua:Array = [];
			
			xiangduiIdx = getshaiziIdxByPos(pos);
//			zhenghua = [35+xiangduiIdx,39+xiangduiIdx];
			zhenghua.push(35+xiangduiIdx);
			if(xiangduiIdx==2 )
			{
				xiangduiIdx = 3;
			}
			else if(xiangduiIdx==3)
			{
				xiangduiIdx = 2;
			}
			zhenghua.push(39+xiangduiIdx);
			
			var i:int,len:int=huaVec[pos].length;
			for(i=0;i<len;i++)
			{
				if(zhenghua.indexOf(huaVec[pos][i]) != -1)//正花
				{
					if(type == 0)
					{
						retArr.push(huaVec[pos][i]);
					}
				}
				else
				{
					if(type == 1)
					{
						retArr.push(huaVec[pos][i])
					}
				}
			}
			return retArr;
		}
		
		
		
		
		public function resetCard():void
		{
			var i:int;
			var len:int = _chairNum;
			
			for(i=0;i<len;i++)
			{
				
				outputCardsVec[i].length = 0;
				huaVec[i].length = 0;
				chiVec[i].length = 0;
				chiFromVec[i].length = 0;
				pengVec[i].length = 0;
				pengFromVec[i].length = 0;
				mingGangVec[i].length = 0;
				mingGangFromVec[i].length = 0;
				anGangVec[i].length = 0;
				anGangFromVec[i].length = 0;
				kouVec[i].length = 0;
				theFourteenCardVec[i] = -1;
			}
		}
		
		
		/**游戏重新开始，重新设置数据*/
		public function reset():void
		{
			beKickedPlayer = {};
			var i:int;
			var len:int = _chairNum;
			
			for(i=0;i<len;i++)
			{
				
				outputCardsVec[i].length = 0;
				huaVec[i].length = 0;
				chiVec[i].length = 0;
				chiFromVec[i].length = 0;
				pengVec[i].length = 0;
				pengFromVec[i].length = 0;
				mingGangVec[i].length = 0;
				mingGangFromVec[i].length = 0;
				anGangVec[i].length = 0;
				anGangFromVec[i].length = 0;
				kouVec[i].length = 0;
				
				theFourteenCardVec[i] = -1;
				isTingVec[i] = false;
				
				TingHuCardVec[i].length = 0;
				TingDownCardVec[i].length = 0;
				
				overHuaVec[i] = 0;
			}
			
			//selfChairPos = 0;
			curOutPutPos = -1;
			isHu = false;
			isLiu = false;
			leftDesktopCardsNum = 0;
			
			tempKouCards = [];
			
			isNextCancelBtnKou = false;
			theTingCardBeforKou = 0;
			
			tingCardsOfKouBtn = [];
			tingCardsOfCancelBtn = [];
			kouCards = [];
			
			curHandlePos = 0;
			
			koupaiwancheng = false;
			
			majiangMsgs.control_game_operation_hucard_info = null;
			
			huArr.length = 0;
			
			//chengBaoArr = [0,0,0,0];
		}
		
		public var chengBaoArr:Array = [];
		
		//下面是麻将在客户端的一些数据
		/**玩家的信息*/
		public var playerInfoVec:Vector.<Object> = new Vector.<Object>();
		
		public var isSelfSitDown:Boolean = false;
		
		public function updateOnePlayerInfo(info:Object):void
		{
			if(info.pos%2 == 0)
			{
				info.sex = 1;
			}
			else
			{
				info.sex = 2;
			}
			
			var i:int;
			var len:int = playerInfoVec.length;
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
				//info.sex = "f";
				playerInfoVec.push(info);
//				playerInfoVec[info.pos] = info;
//				playerInfoVec[info.pos].sex = "f";
				
//				if(info.hasOwnProperty("nickname"))
//				{
//					info["nickname"] = QuickUtils.decodeNickName(info["nickname"]);
//				}
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
		
		/**根据玩家的座位号取玩家点数对应的序列*/
		public function getshaiziIdxByPos(pos:int):int
		{
			for(var i:int=0;i<chairNum;i++)
			{
				if(pos == (zhuangpos+i)%chairNum)
				{
					return i;
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
		
//		/**根据玩家的uid更新玩家手里的钱*/
//		public function updateGoldsByUid(uid:int,money:int):void
//		{
//			var i:int;
//			var len:int = playerInfoVec.length;
//			
//			for(i=0;i<len;i++)
//			{
//				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
//				{
//					playerInfoVec[i].golds += money;
//				}
//			}
//		}
		
//		/**根据玩家的uid同步玩家手里的钱*/
//		public function syntheticGoldsByUid(uid:int,money:int):void
//		{
//			var i:int;
//			var len:int = playerInfoVec.length;
//			
//			for(i=0;i<len;i++)
//			{
//				if(playerInfoVec[i] && playerInfoVec[i].uid == uid)
//				{
//					playerInfoVec[i].golds = money;
//				}
//			}
//		}
		
		/**baida[0]:翻的牌 baida[1]:百搭牌*/
		public var baida:Array = [];
		
		
		/**玩家手里的花的牌,根据椅子号来的*/
		public var huaVec:Vector.<Array> = new Vector.<Array>();
		
		/**记录玩家第一次补花   是否完成*/
		public var overHuaVec:Vector.<int> = new Vector.<int>();
		
		/**玩家手里的花的牌数量*/
		public var huaNum:Vector.<int> = new Vector.<int>();
		
		/**吃的牌，根据椅子号来的*/
		public var chiVec:Vector.<Array> = new Vector.<Array>();
		public var chiFromVec:Vector.<Array> = new Vector.<Array>();
		
		/**碰的牌 根据椅子号来的 */
		public var pengVec:Vector.<Array> = new Vector.<Array>();
		public var pengFromVec:Vector.<Array> = new Vector.<Array>();
		
		/**明杠的牌 根据椅子号来的*/
		public var mingGangVec:Vector.<Array> = new Vector.<Array>();
		public var mingGangFromVec:Vector.<Array> = new Vector.<Array>();
		
		/**暗杠的牌 根据椅子号来的*/
		public var anGangVec:Vector.<Array> = new Vector.<Array>();
		public var anGangFromVec:Vector.<Array> = new Vector.<Array>();
		
		/**听牌时扣的牌 根据椅子号来的*/
		public var kouVec:Vector.<Array> = new Vector.<Array>();
		
		/**玩家打出去的牌 根据椅子号来的*/
		public var outputCardsVec:Vector.<Array> = new Vector.<Array>();
		
		/**所有牌 根据椅子号来的（包括第十四张牌）*/
		public var allCardsVec:Vector.<Array> = new Vector.<Array>();
		
		/**第十四张牌*/
		public var theFourteenCardVec:Vector.<int> = new Vector.<int>();
		
		/**是否当前是听状态*/
		public var isTingVec:Vector.<Boolean> = new Vector.<Boolean>();
		
		/**听之后胡的牌*/
		public var TingHuCardVec:Vector.<Array> = new Vector.<Array>();
		
		/**是否胡了*/
		public var isHu:Boolean = false;
		
		/**是否是流局*/
		public var isLiu:Boolean = false;
		
		/**桌子上剩余的牌的数量*/
		public var leftDesktopCardsNum:int = 0;
		
		
		protected var _chairNum:int = 3;
		
		/**玩家听牌后倒下的牌*/
		public var TingDownCardVec:Vector.<Array> = new Vector.<Array>();
		
		public var huArr:Array = [];
		

		/**设置一共有几个人玩*/
		public function get chairNum():int
		{
			return _chairNum;
		}

		/**
		 * @private
		 */
		public function set chairNum(value:int):void
		{
			_chairNum = value;
			
			playerInfoVec.length = 0;
			//playerInfoVec.length = _chairNum;
			
			huaVec.length = _chairNum;
			chiVec.length = _chairNum;
			chiFromVec.length = _chairNum;
			pengVec.length = _chairNum;
			pengFromVec.length = _chairNum;
			mingGangVec.length = _chairNum;
			mingGangFromVec.length = _chairNum;
			anGangVec.length = _chairNum;
			anGangFromVec.length = _chairNum;
			kouVec.length = _chairNum;
			outputCardsVec.length = _chairNum;
			allCardsVec.length = _chairNum;
			theFourteenCardVec.length = _chairNum;
			isTingVec.length = _chairNum;
			TingHuCardVec.length = _chairNum;
			huaNum.length = _chairNum;
			
			TingDownCardVec.length = _chairNum;

			//第十四张牌 默认-1表示没有
			var i:int;
			var len:int = _chairNum;
			
			for(i=0;i<len;i++)
			{
				huaVec[i] = new Array();
				chiVec[i] = new Array();
				chiFromVec[i] = new Array();
				pengVec[i] = new Array();
				pengFromVec[i] = new Array();
				mingGangVec[i] = new Array();
				mingGangFromVec[i] = new Array();
				outputCardsVec[i] = new Array();
				anGangVec[i] = new Array();
				anGangFromVec[i] = new Array();
				kouVec[i] = new Array();
				allCardsVec[i] = new Array();
				
				theFourteenCardVec[i] = -1;
				isTingVec[i] = false;
				TingHuCardVec[i] = new Array();
				TingDownCardVec[i] = new Array();
			}
			isHu = false;
			isLiu = false;
			
			leftDesktopCardsNum = 0;
			
			isGameStart = false;
			
			huArr.length = 0;
			
			//chengBaoArr = [0,0,0,0];
		}
		
		public function checkTianhu():Boolean
		{
			var i:int,len:int;
			
			len = chairNum;
			for(i=0;i<len;i++)
			{
				if(chiVec[i].length > 0)
				{
					return false;
				}
				
				if(pengVec[i].length > 0)
				{
					return false;
				}
				
				if(anGangVec[i].length > 0)
				{
					return false;
				}
				
				if(mingGangVec[i].length > 0)
				{
					return false;
				}
				
				if(outputCardsVec[i].length > 0)
				{
					return false;
				}
			}
			
			return true;
		}

		public var selfChairPos:int = 0;
		
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
		
		/**给自己所有牌排个序*/
		public function sortAllCards(pos:int):void	
		{
			
			allCardsVec[pos].sort(compareFunction);
			
			pushToHeadBaida(pos);
		}
		
		public function compareFunction(A:int,B:int):int
		{
			if(A<B)
			{
				return -1;
			}
			else if(A==B)
			{
				return 0;
			}
			else
			{
				return 1;
			}
		}
		
		/**从手里的牌里面去掉吃掉的牌*/
		public function cutChiCard(pos:int,arr:Array):void
		{
			if(isSelfSitDown && (pos == selfChairPos || UserData.isReplay))
			{
				var tempArr:Array = arr;
				
				var i:int;
				var len:int = tempArr.length;
				
				var idx:int =0;
				var num:int = 0;
				
				for(i=0;i<len;i++)
				{
					idx = allCardsVec[pos].indexOf(tempArr[i]);
					
					if(idx != -1)
					{
						allCardsVec[pos].splice(idx,1);
						num += 1;
					}
				}
				
				if(num != 2)
				{
					QuickUtils.popMessageBox("给玩家吃牌的数据有问题！！！吃掉的牌 " + arr[0] + " " + arr[1],PopBox.BTN_QUEREN,null,null,"错误");
				}
			}
			else
			{
				allCardsVec[pos].splice(0,2);//删掉两张牌
				
				
			}
		}
		
		/**从手里的牌里面去掉一张碰掉的牌*/
		public function cutPengCard(pos:int,cardIdx:int):void
		{
			
			if(isSelfSitDown && pos == selfChairPos)
			{
				var tempArr:Array = [cardIdx,cardIdx];
				
				var i:int;
				var len:int = tempArr.length;
				
				var idx:int =0;
				var num:int = 0;
				
				for(i=0;i<len;i++)
				{
					idx = allCardsVec[pos].indexOf(tempArr[i]);
					
					if(idx != -1)
					{
						allCardsVec[pos].splice(idx,1);
						num += 1;
					}
				}
				
				if(num != 2)
				{
					QuickUtils.popMessageBox("给玩家碰牌的数据有问题！！！碰掉的牌 " + cardIdx,PopBox.BTN_QUEREN,null,null,"错误");
				}
			}
			else
			{
				allCardsVec[pos].splice(0,2);//删掉两张牌
			}
		}
		
		/**杠了之后刷新手里的牌
		 * 
		 * @param type 0补杠 1暗杠 2明杠
		 * */
		public function cutGangCard(pos:int,cardIdx:int,type:int):void
		{
			trace("cutGangCard :: pos:: " + pos + " cardIdx::" + BaseCard.CARD_REFERENCE[cardIdx] + " type:: " + type)
			var i:int;
			var tempArr:Array;
			var idx:int = 0;
			var len:int;
			
			if(isTingVec[pos] == true)
			{
				if(kouVec[pos].length > 0 && type != 0)
				{
					kouVec[pos].length -= 1;
				}
			}
			
			if(isSelfSitDown && pos == selfChairPos)
			{
				switch(type)
				{
					case 0://一定有第十四张牌
						if(theFourteenCardVec[pos] !=-1)
						{
							if(theFourteenCardVec[pos] == cardIdx)
							{
								theFourteenCardVec[pos] = -1;
							}
							else
							{
								idx = allCardsVec[pos].indexOf(cardIdx);
								if(idx != -1)
								{
									allCardsVec[pos].splice(idx,1);
								}
								
								allCardsVec[pos].push(theFourteenCardVec[pos]);
								theFourteenCardVec[pos] = -1;
								sortAllCards(pos);
							}
						}
						else
						{
							
							idx = allCardsVec[pos].indexOf(cardIdx);
							if(idx != -1)
							{
								allCardsVec[pos].splice(idx,1);
							}
							sortAllCards(pos);
						}
						
						break;
					case 1://暗杠 一定有第十四张牌
						
						if(theFourteenCardVec[pos] == -1)
						{
							tempArr = [cardIdx,cardIdx,cardIdx,cardIdx];
						}
						else if(theFourteenCardVec[pos] == cardIdx)
						{
							theFourteenCardVec[pos] = -1;
							
							tempArr = [cardIdx,cardIdx,cardIdx];
							
						}
						else
						{
							tempArr = [cardIdx,cardIdx,cardIdx,cardIdx];
							
							allCardsVec[pos].push(theFourteenCardVec[pos]);
							
							theFourteenCardVec[pos] = -1;
							
							sortAllCards(pos);
						}
						
						len = tempArr.length;
						
						for(i=0;i<len;i++)
						{
							idx = allCardsVec[pos].indexOf(tempArr[i]);
							
							if(idx != -1)
							{
								allCardsVec[pos].splice(idx,1);
							}
						}
						break;
					case 2://明杠 不是自己摸的 不用补
						tempArr = [cardIdx,cardIdx,cardIdx];
						
						len = tempArr.length;
						
						for(i=0;i<len;i++)
						{
							idx = allCardsVec[pos].indexOf(tempArr[i]);
							
							if(idx != -1)
							{
								allCardsVec[pos].splice(idx,1);
								
								trace("从自己牌里面去掉了一张 ：：" + tempArr[i]);
							}
						}
						
						break;
					default : break;
				}
			}
			else//不是自己
			{
				switch(type)
				{
					case 0://碰杠去掉一张
						
						if(theFourteenCardVec[pos] != -1)
						{
							theFourteenCardVec[pos] = -1;
						}
						else
						{
							allCardsVec[pos].splice(0,1);
						}
						
						
						
						break;
					case 1://暗杠 去掉四张
						
						if(theFourteenCardVec[pos] != -1)
						{
							theFourteenCardVec[pos] = -1;
							
							if(isTingVec[pos] == true)
							{
								allCardsVec[pos].splice(TingDownCardVec[pos].length,3);
							}
							else
							{
								allCardsVec[pos].splice(0,3);
							}
						}
						else
						{
							if(isTingVec[pos] == true)
							{
								allCardsVec[pos].splice(TingDownCardVec[pos].length,4);
							}
							else
							{
								allCardsVec[pos].splice(0,4);
							}
						}
						
						
						break;
					case 2://明杠 去掉三张
						if(isTingVec[pos] == true)
						{
							allCardsVec[pos].splice(TingDownCardVec[pos].length,3);
						}
						else
						{
							allCardsVec[pos].splice(0,3);
						}
						break;
					default : break;
				}
			}
		}
		
		/**更新所有牌(游戏开始后的第一次发牌）*/
		public function updateAllCardsVecByGameStart(allCards:Array):void
		{
			trace("selfCards ::" + allCards);
			
			var i:int;
			var len:int = allCardsVec.length;
			
			for(i=0;i<len;i++)
			{
				if(i == selfChairPos)
				{
					allCardsVec[i] = new Array();
					var j:int;
					var leng:int = allCards.length;
					for(j=0;j<leng;j++)
					{
						(allCardsVec[i] as Array).push(allCards[j].card);
					}
				}
				else
				{
					allCardsVec[i] = new Array(0,0,0,0,0,0,0,0,0,0,0,0,0);
				}
			}
			
			trace("selfChairPos::" + selfChairPos);
			
			sortAllCards(selfChairPos);
			
		}
		
		/**玩家出牌更新玩家数据*/
		public function outputCard(pos:int,cardIdx:int):void
		{
			curOutPutPos = pos;
			outputCardsVec[pos].push(cardIdx);

			if(isSelfSitDown && pos == selfChairPos)
			{
				if(theFourteenCardVec[pos] != -1)//有第十四张牌
				{
					if(theFourteenCardVec[pos] == cardIdx)
					{
						theFourteenCardVec[pos] = -1;
						return;
					}
				}
				
				var idx:int = allCardsVec[pos].indexOf(cardIdx);
				
				if(idx!=-1)
				{
					allCardsVec[pos].splice(idx,1);
				}
				
				if(theFourteenCardVec[pos] != -1)
				{
					allCardsVec[pos].push(theFourteenCardVec[pos]);
					sortAllCards(pos);
					
					theFourteenCardVec[pos] = -1;
				}
			}
			else//别人的话就出第十四张牌好了，如果没有的话，所以随便出一张
			{
				if(theFourteenCardVec[pos] != -1)
				{
					theFourteenCardVec[pos] = -1;
					return;
				}
				
				allCardsVec[pos].splice(0,1);
				
			}
			
			//outputCardsVec[pos].push(cardIdx);
		}
		
		public function updatePengVec(pos:int,cardIdx:int,targetPos:int):void
		{
			if(pengVec[pos])
			{
				pengVec[pos].push(cardIdx);
				pengFromVec[pos].push(targetPos);
				
//				chengBaoArr[targetPos] += 1;
				
			}
			
		}
		
		public var lastHuanHuaCard:int = -1;
		
		
		/**更新补花*/
		public function updateBuhua(pos:int,huaCards:Array,huanhuiCards:Array):void
		{
			if(huaVec[pos])
			{
				
				huaVec[pos] = huaVec[pos].concat(huaCards);
				
				if(UserData.isReplay || pos == selfChairPos)
				{
					var i:int;
					var len:int = huaCards.length;
					var result:int;
					
					for(i=0;i<len;i++)
					{
						result = allCardsVec[pos].indexOf(huaCards[i]);
						if(result != -1)//找到了
						{
							allCardsVec[pos].splice(result,1);
						}
					}
					
					len = huanhuiCards.length;
					for(i=0;i<len;i++)
					{
						allCardsVec[pos].push(huanhuiCards[i]);
					}
					
					lastHuanHuaCard = huanhuiCards[huanhuiCards.length-1]
					sortAllCards(pos);
				}
				
			}
			
			
		}
		
		
		public function updateChiVec(pos:int,chicard:int,chicards:Array,targetPos:int):void
		{
			if(chiVec[pos])
			{
				var chiData:MajiangChiData = new MajiangChiData();
				chiData.chicard = chicard;
				chiData.chicards = chicards;
				chiVec[pos].push(chiData);
				chiFromVec[pos].push((chairNum+pos-1)%chairNum);
				
//				chengBaoArr[targetPos] += 1;
			}
		}
		
		public function getChiCards(pos:int,chicard:int):Array
		{
			if(chiVec[pos])
			{
				for(var i:int=0;i<chiVec[pos].length;i++)
				{
					if((chiVec[pos][i] as MajiangChiData).chicard == chicard)
					{
						return (chiVec[pos][i] as MajiangChiData).chicards;
					}
				}		
			}
			return [];
		}
		
		/**更新杠 可能关联到碰 碰杠的
		 * 
		 * @param type 0碰杠 1暗杠 2明杠
		 * */
		public function updateGangVec(pos:int,cardIdx:int,type:int,targetPos:int,obj:Object=null):Boolean
		{
			trace("updateGangVec:: pos::" + pos + " cardIdx::" + cardIdx + " type::" + type);
			
			switch(type)
			{
				case 0:
					if(mingGangVec[pos].indexOf(cardIdx) != -1)
						return true;
					mingGangVec[pos].push(cardIdx);
					var idx:int = pengVec[pos].indexOf(cardIdx);
					if(idx != -1)
					{
						if(targetPos == selfChairPos)
						{
							targetPos = pengFromVec[pos][idx];
						}
						pengVec[pos].splice(idx,1);
						pengFromVec[pos].splice(idx,1);
					}
					if(obj)
					{
						obj.TIndex = targetPos;
						obj.TSeat = targetPos;
					}
					
					mingGangFromVec[pos].push(targetPos);
					break;
				case 1:
					if(anGangVec[pos].indexOf(cardIdx) != -1)
						return true;
					anGangVec[pos].push(cardIdx);
					anGangFromVec[pos].push(cardIdx);
					break;
				case 2:
					if(mingGangVec[pos].indexOf(cardIdx) != -1)
						return true;
					mingGangVec[pos].push(cardIdx);
					mingGangFromVec[pos].push(targetPos);
					
					break;
				default:break;
			}
//			chengBaoArr[targetPos] += 1;
			return false;
		}
		
		protected function compareType(A:Object,B:Object):int
		{
			if(A.type<B.type)
			{
				return 1;
			}
			else if(A.type==B.type)
			{
				if(A.card < B.card)
				{
					return -1;
				}
				else if(A.card == B.card)
				{
					return 0;
				}
				else
				{
					return 1
				}
			}
			else
			{
				return -1;
			}
		}
		
		/**更新玩家手里的牌 先出出去，后听牌，肯定没有第十四张牌，听牌专用*/
		public function updateAllCards(pos:int,cards:Array):void
		{
			TingDownCardVec[pos].length = 0;
			var i:int;
			
			var len:int = cards.length;//对这个排序，让其type == 1的放在最前面
			
			if(len%3 == 2)//表示有第十四张
			{
				theFourteenCardVec[pos] = cards[len-1].card;
				len = cards.length-1;
				cards.length = len;
			}
			
			cards.sort(compareType);
			
			trace("更新玩家手里的牌len::" + len);
			if(len > 13)//断线重连的时候用的，显示第十四张牌
			{
				theFourteenCardVec[pos] = cards[len-1].card;
				cards.length = 13;
				len = cards.length;
			}
			
			allCardsVec[pos].length = len;
			var kouNum:int = 0;
			
			for(i=0;i<len;i++)
			{
				allCardsVec[pos][i] = cards[i].card;
				
				trace("allCardsVec[pos][i] i::"+i+" card::" + cards[i].card);
				
				//把扣的牌加入扣的数组里面，供刷新牌的时候调用
				if(pos == selfChairPos)//是自己的话
				{
					if(cards[i].type == 1)
					{
						if(kouVec[pos].indexOf(cards[i].card) == -1)//没有，就加进去	
						{
							kouVec[pos].push(cards[i].card);
						}
					}
				}
				else//是别人的话
				{
					if(cards[i].type == 1)
					{
						if(cards[i].type == 1)
						{
							if(UserData.isReplay)
							{
								if(kouVec[pos].indexOf(cards[i].card) == -1)//没有，就加进去	
								{
									kouVec[pos].push(cards[i].card);
								}
							}
							else
							{
								kouNum += 1;
							}
						}
					}
					
				}
				
				if(cards[i].type == 2)//倒下的牌
				{
					TingDownCardVec[pos].push(cards[i].card);
				}
			}
			
			if(pos != selfChairPos)
			{
				if(UserData.isReplay == false)
				{
					kouVec[pos].length = kouNum/3;
				}
			}
			
			pushToHeadBaida(pos);
			
		}
		
		/**将自己手里的牌中的百搭牌放到最前面*/
		public function pushToHeadBaida(pos):void
		{
			var obj:Object = this.majiangMsgs.control_game_operation_tableinfo_Info;
			if(obj && obj.roomtype == 8)//这个是百搭
			{
				var cardIdx:int = baida[1];
				
				var i:int,len:int = allCardsVec[pos].length;
				var tempArr:Array = [];
				
				for(i=0;i<len;i++)
				{
					if(allCardsVec[pos][i]== cardIdx)
					{
						tempArr.push(allCardsVec[pos][i]);
						allCardsVec[pos].splice(i,1);
						i--;
					}
				}
				
				allCardsVec[pos] = tempArr.concat(allCardsVec[pos]);
				
			}
		}
		
		
		
		/**游戏结束时更新玩家手里的牌*/
		public function updateAllCardsAfterHu(pos:int,cards:Array):void
		{
			var i:int;
			var len:int;
			
			//自己的也要同步
			
			
			
			len = cards.length;
			if(len%3 == 2)//这个是自摸的牌，有第十四
			{
				theFourteenCardVec[pos] = cards[cards.length-1].card;
				len = cards.length-1;
			}
			else
			{
				len = cards.length;
			}
			
			cards.length = len;
			
			cards.sort(compareType);
			
			allCardsVec[pos].length = len;
			
			for(i=0;i<len;i++)
			{
				allCardsVec[pos][i] = cards[i].card;
			}
			
			pushToHeadBaida(pos);
			
			//sortAllCards(pos);
		}
		
		/**大赢家*/
		public var yingjiaArr:Array = [];
		/**最佳炮手*/
		public var paoshouArr:Array = [];
		
		/**根据pos把user位置排好了*/
		public var usersOfRoundData:Array = [];
		
		public function processRoundData():void
		{
			yingjiaArr.length = 0;
			paoshouArr.length = 0;
			
			var users:Array = majiangMsgs.control_game_settlement_Info.userinfos as Array;
			
			var i:int;
			var len:int = users.length;
			
			for(i=0;i<len;i++)
			{
				//大赢家的逻辑
				usersOfRoundData[getPlayerPosByUid(users[i].uid)] = users[i];
				
				if(yingjiaArr[0] == null)
				{
					if(users[i].zongchengji > 0)
					{
						yingjiaArr[0] = users[i];
					}
				}
				else
				{
					if(users[i].zongchengji > yingjiaArr[0].zongchengji)
					{
						yingjiaArr[0] = users[i];
						yingjiaArr[1] = null;
						yingjiaArr[2] = null;
					}
					else
					{
						if(users[i].zongchengji == yingjiaArr[0].zongchengji)
						{
							yingjiaArr.push(users[i]);
						}
					}
				}
				
				if(paoshouArr[0] == null)
				{
					if(users[i].dianpaocount > 0)
					{
						paoshouArr[0] = users[i];
					}
					
				}
				else
				{
					if(users[i].dianpaocount > paoshouArr[0].dianpaocount)
					{
						paoshouArr[0] = users[i];
						paoshouArr[1] = null;
						paoshouArr[2] = null;
					}
					else
					{
						if(users[i].dianpaocount == paoshouArr[0].dianpaocount)
						{
							paoshouArr.push(users[i]);
						}
					}
				}
				
				//最佳炮手的逻辑
			}
		}
		
		/**是否下一次玩家点击取消按钮，进行听的操作*/
		public var isNextCancelBtnKou:Boolean = false;
		
		/**下一次玩家点击取消按钮是否取消亮牌*/
		public var isCancelTingp:Boolean = false;
		
		/**玩家扣牌之前显示听的那张牌*/
		public var theTingCardBeforKou:int = 0;
		
		/**获取指定听哪张牌可以扣掉哪些牌*/
		public function getKouCards(cardIdx:int):Array
		{
			
			var arr:Array = majiangMsgs.control_game_mjopration_Info.nopercard as Array;
			
			var temArr:Array;
			var returnArr:Array = [];
			
			var i:int;
			var len:int = arr.length;
			
			for(i=0;i<len;i++)
			{
				if(arr[i].card == cardIdx)
				{
					temArr = arr[i].nkoucard;
				}
			}
			
			if(temArr != null && temArr.length > 0)
			{
				for(i=0;i<temArr.length;i++)
				{
					returnArr.push(temArr[i].card);
				}
			}
			
			
			return returnArr;
		}
		
		/**供选择的可以杠的牌*/
		public var tempGangCards:Array = [];
		
		/**是不是下次出牌发出杠的命令*/
		public var isNextGang:Boolean = false;
		
		
		/**零时记录选择扣的牌，供点击扣按钮后真实扣掉；或者是点击取消按钮，取消这之前的表现操作*/
		public var tempKouCards:Array = [];
		
		/**断线重连临时记下的玩家打出的牌*/
		public var reenterOutpuCardsVec:Vector.<Array>;
		
		/**断线重连时临时记下的玩家可以胡的牌*/
		public var reenterHuCardsVec:Vector.<Array>;
		
//		/**断线重连进来刷新玩家手里牌的数据*/
//		public function updateCardsByReenter():void
//		{
//			var users:Array = majiangMsgs.control_game_operation_userinfo_Info.user as Array;
//			
//			
//			var i:int,j:int,len:int = users.length;
//			var cardLen:int;
//			
//			var cardArr:Array;
//			var pos:int;
//			var kouAndHandleCard:Array = [];
//			
//			reenterOutpuCardsVec = new Vector.<Array>(chairNum);
//			reenterHuCardsVec = new Vector.<Array>(chairNum);
//			
//			for(i=0;i<len;i++)
//			{
//				cardArr = users[i].card as Array;
//				pos = users[i].pos;
//				cardLen = cardArr.length;
//				
//				reenterOutpuCardsVec[pos] = new Array();
//				kouAndHandleCard[pos] = new Array();
//				
//				reenterHuCardsVec[pos] = new Array();
//				
//				TingDownCardVec[pos] = new Array();
//				
//				for(j=0;j<cardLen;j++)//牌的类型 0碰 1明杠 2 暗杠 3持有 4已出 5扣牌 6可以胡的牌 7
//				{
//					switch(cardArr[j].type)
//					{
//						case 0:
//							pengVec[pos].push(cardArr[j].card);
//							break;
//						case 1:
//							mingGangVec[pos].push(cardArr[j].card);
//							break;
//						case 2:
//							anGangVec[pos].push(cardArr[j].card);
//							break;
//						case 3:
//							kouAndHandleCard[pos].push({"type":0,"card":cardArr[j].card});
//							
//							trace("cardArr[j].card::" + cardArr[j].card+ " type::" + 0 + " pos::" + pos);
//							break;
//						case 4:
//							outputCardsVec[pos].push(cardArr[j].card);
//							reenterOutpuCardsVec[pos].push(cardArr[j]);							
//							break;
//						case 5:
//							kouAndHandleCard[pos].push({"type":1,"card":cardArr[j].card});
//							trace("cardArr[j].card::" + cardArr[j].card + " type::" + 1 + " pos::" + pos);
//							break;
//						case 6:
//							if(cardArr[j].card != undefined)
//							{
//								reenterHuCardsVec[pos].push(cardArr[j].card);
//							}
//							
//							break;
//						case 7:
//							var chiData:MajiangChiData = new MajiangChiData();
//							chiData.chicard = cardArr[j].card;
//							chiData.chicards = cardArr[j].chicards;
//							chiVec[pos].push(chiData);
//							break;
//						case 8:
//							huaVec[pos].push(cardArr[j].card);
//							break;
//						
//						case 9://如果听了 就是听倒的牌
//							kouAndHandleCard[pos].push({"type":2,"card":cardArr[j].card});
//							trace("cardArr[j].card::" + cardArr[j].card + " type::" + 2 + " pos::" + pos);
//							break;
//							
//					}
//				}
//				
//				updateAllCards(pos,kouAndHandleCard[pos]);
//
//				isTingVec[pos] = users[i].isTing == 0 ? false:true;
//			}
//			curHandlePos = majiangMsgs.control_game_operation_userinfo_Info.handlepos;
//			
//		}
		
		public var curHandlePos:int = 0;
		
		
//		/**胡牌之后同步吃的牌*/
//		public function syntheticChiCards(pos:int,cards:Array):void
//		{
//			//todo
//			chiVec[pos] = [];
//			
//			var i:int;
//			var len:int = cards.length;
//			
//			for(i=0;i<len;i++)
//			{
//				var chiData:MajiangChiData = new MajiangChiData();
//				chiData.chicard = cards[i].card;
//				chiData.chicards = cards[i].chicards;
//				chiVec[pos].push(chiData);
//			}
//		}
//	
//		/**胡牌之后同步碰的牌*/
//		public function syntheticPengCards(pos:int,cards:Array):void
//		{
//			pengVec[pos] = [];
//			
//			var i:int;
//			var len:int = cards.length;
//			for(i=0;i<len;i++)
//			{
//				pengVec[pos].push(cards[i].card);
//			}
//		}
//		
//		/**胡牌之后同步暗杠的牌*/
//		public function syntheticAnGangCards(pos:int,cards:Array):void
//		{
//			anGangVec[pos] = [];
//			
//			var i:int;
//			var len:int = cards.length;
//			for(i=0;i<len;i++)
//			{
//				anGangVec[pos].push(cards[i].card);
//			}
//		}
//		
//		/**胡牌之后同步明杠的牌*/
//		public function syntheticMingGangCards(pos:int,cards:Array):void
//		{
//			mingGangVec[pos] = [];
//			
//			var i:int;
//			var len:int = cards.length;
//			for(i=0;i<len;i++)
//			{
//				mingGangVec[pos].push(cards[i].card);
//			}
//		}
		
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
		
		
		//玩家自己打出去牌的位置
		public var selfOutputCardPos:Point = new Point();
		
		
		public function gethuCards(cardIdx:int):Array
		{
			var returnArr:Array = [];
			var i:int,j:int,len:int;
			if(majiangMsgs.control_game_operation_hucard_info != null)
			{
				var info:Object = majiangMsgs.control_game_operation_hucard_info;
				len = info.nting.length;
				
				for(i=0;i<len;i++)
				{
					if(info.nting[i].card == cardIdx)
					{
						for(j=0;j<info.nting[i].nhu.length;j++)
						{
							returnArr.push(info.nting[i].nhu[j].card);
						}
						break;
					}
				}
			}
			
			if(returnArr.length == 0)//从之前的胡去取
			{
				var arr:Array = majiangMsgs.control_game_mjopration_Info.nopercard as Array;
				len = arr.length;
				for(i=0;i<len;i++)
				{
					if(arr[i].type == 1)//听
					{
						if(arr[i].card == cardIdx)
						{
							for(j=0;j<arr[i].nhucard.length;j++)
							{
								returnArr.push(arr[i].nhucard[j].card);
							}
							break;
						}
					}
				}
			}
			
			return returnArr;
		}
		
		public var curOutPutPos:int = -1;
		
		//从打出去的牌中去掉碰杠掉的牌
		public function cutOutput(pos:int,cardIdx:int):void
		{
			var idx:int = outputCardsVec[pos].indexOf(cardIdx);
			
			if(idx != -1)
			{
				outputCardsVec[pos].splice(idx,1);
			}
		}
		
//		public static const WUXIHUAARRCONST:Array = [1537,1553,1569,1585,1281,1297,1313,1329];
//		
//		public static const SUZHOUGHUACONST:Array = [1793, 1809, 1825, 1841,1537,1553,
//			1569,1585,1281,1297,1313,1329,1025,1041,1057];
//		
//		public static const TAIZHOUGHUACONST:Array = [1537,1553,
//			1569,1585,1281,1297,1313,1329,1025,1041,1057,769,785,801,817];//769:"z东.png",785:"z南.png",801:"z西.png",817:"z北.png",
		
		public function judgeHua(cardIdx:int):Boolean
		{
//			1537:"h春.png",1553:"h夏.png",1569:"h秋.png",1584:"h冬.png",
//			1281:"h梅.png",1297:"h兰.png",1313:"h菊.png",1329:"h竹.png",
			
			var huaArr:Array = [35,36,37,38,39,40,41,42];
			
//			switch(UserData.roomtype)
//			{
//				case 9:
//				case 11:	
//					huaArr = WUXIHUAARRCONST;
//					break;
//				case 10:
//					huaArr = SUZHOUGHUACONST;
//					break;
//				case 12:
//					huaArr = TAIZHOUGHUACONST;
//					break;
//			}
			
			if(huaArr.indexOf(cardIdx) != -1)
			{
				return true;
			}
			
			return false;
		}
		
		public function checkHaveHua(pos:int):Boolean
		{
			var cards:Array = allCardsVec[pos];
			for(var i:int=0;i<cards.length;i++)
			{
				if(judgeHua(cards[i]) == true)
				{
					return true;
				}
			}
			
			return false;
		}
		
		
		/**
		 * 庄家 1 5 9 东  春  梅
下家 2 6 中 南  夏  兰
对家 3 7 发 西  秋  竹
上家 4 8 白 北  冬  菊
		 * */
		public static var GangtouCardArr:Array = [
			
		[[1,257,513],[65,321,577],[129,385,641],[769],[1537],[1281]],//庄家
		[[17,273,529],[81,337,593],[1025],[785],[1553],[1297]],
		[[33,289,545],[97,353,609],[1041],[801],[1569],[1329]],
		[[49,305,561],[113,369,625],[1057],[817],[1584],[1313]]
		
		];
		
		/**根据pos获取杠头的参照列表*/
		public function getGangtouRefArr(pos:int):Array
		{
			return GangtouCardArr[(pos + chairNum  - zhuangpos)%chairNum];
		}
		
		/**根据庄家的位置获取上下家的位置 0zhuang 1xia 2dui 3shang*/
		public function getRefZhuangPos(pos):int
		{
			return (pos + chairNum  - zhuangpos)%chairNum;
		}
		
//		public function compareByZhuang(A:int,B:int):int
//		{
//			if(getRefZhuangPos(A)<getRefZhuangPos(B))
//			{
//				return -1;
//			}
//			else
//			{
//				return 1;
//			}
//		}
		
		
		public function getGangtouCardImg(cardIdx:int,isHave:Boolean=true):String
		{
			var cardRef:String = "";//"1-1"
			
			var base1:int = 1;
			var base2:int = 19;
			var base3:int = 10;
			
			switch(cardIdx)
			{
				case base1:case base2:case base3:
					cardRef = "1";
					break;
				case base1+1:case base2+1:case base3+1:
					cardRef = "2";
					break;
				case base1+1*2:case base2+1*2:case base3+1*2:
					cardRef = "3";
					break;
				case base1+1*3:case base2+1*3:case base3+1*3:
					cardRef = "4";
					break;
				case base1+1*4:case base2+1*4:case base3+1*4:
					cardRef = "5";
					break;
				case base1+1*5:case base2+1*5:case base3+1*5:
					cardRef = "6";
					break;
				case base1+1*6:case base2+1*6:case base3+1*6:
					cardRef = "7";
					break;
				case base1+1*7:case base2+1*7:case base3+1*7:
					cardRef = "8";
					break;
				case base1+1*8:case base2+1*8:case base3+1*8:
					cardRef = "9";
					break;
				case 769://东  春  梅
					cardRef = "东";
					break;
				case 1537:
					cardRef = "春";
					break;
				case 1281:
					cardRef = "梅";
					break;
				case 1025://中 南  夏  兰
					cardRef = "中";
					break;
				case 785:
					cardRef = "南";
					break;
				case 1553:
					cardRef = "夏";
					break;
				case 1297:
					cardRef = "兰";
					break;
				case 1041://发 西  秋  竹
					cardRef = "发";
					break;
				case 801:
					cardRef = "西";
					break;
				case 1569:
					cardRef = "秋";
					break;
				case 1329:
					cardRef = "竹";
					break;
				case 1057://白 北  冬  菊
					cardRef = "白";
					break;
				case 817:
					cardRef = "北";
					break;
				case 1584:
					cardRef = "冬";
					break;
				case 1313:
					cardRef = "菊";
					break;
			}
			
			if(isHave == false)
			{
				cardRef += "-1"
			}
			
			return "gametable/zhuama/"+cardRef+".png";
		}
		
		public var zhuangpos:int = 0;
		
//		public function get zhuangpos():int
//		{
//			return 	this.majiangMsgs.control_game_operation_tableinfo_Info.BankerPos;
//		}
			
		//*************
		/**别的麻将要换成对应的*/
		public static var all_Cards:Array = [
			
			1,2,3,4,5,6,7,8,9,
			
			10,11,13,14,15,16,17,18,
			
			19,20,21,22,23,24,25,26,27,
			
			28,29,30,31,
			
			32,33,34
			
//			35:"h春.png",36:"h夏.png",37:"h秋.png",38:"h冬.png",39:"h梅.png",40:"h兰.png",41:"h竹.png",42:"h菊.png"
			
		];
		
		/**获取出某张牌的时候可以胡哪些牌
		 * 
		 * -1表示没有百搭
		 * */
		public function getHuTipArr(popCard:int,baidaCard:int=-1):Array
		{
			var retArr:Array = [];
			var tempArr:Array;
			
			if(theFourteenCardVec[selfChairPos] != -1)
			{
				tempArr = allCardsVec[selfChairPos].concat(theFourteenCardVec[selfChairPos]);
			}
			else
			{
				tempArr = allCardsVec[selfChairPos].concat();
			}
			
			var idx:int = tempArr.indexOf(popCard);
			
			if(idx != -1)
			{
				tempArr.splice(idx,1);
			}
			else
			{
				//return retArr;
			}
			
			var i:int,len:int = all_Cards.length;
			for(i=0;i<len;i++)
			{
				if(judgeHu(tempArr.concat(all_Cards[i]),baidaCard) == true)
				{
					retArr.push(all_Cards[i]);
				}
			}
			
			return retArr;
		}
		
		
		/**从一个牌组里把百搭和不是百搭的牌分两个数组取出*/
		public function getSplitBaidaCard(cardArr:Array,baidaCard:int):Array
		{
			var returnAarr:Array = [];
			
			var i:int,len:int= cardArr.length;
			
			var baidaCardArr:Array = [];
			var notBaidaCardArr:Array = [];
			
			for(i=0;i<len;i++)
			{
				if(cardArr[i] == baidaCard)
				{
					baidaCardArr.push(cardArr[i]);
				}
				else
				{
					notBaidaCardArr.push(cardArr[i]);
				}
			}
			
			return returnAarr;
			
		}
		
		
		
		/**判断牌组能不能胡 -1表示 */
		public function judgeHu(paiArr:Array,baidaCard:int=-1):Boolean
		{
			paiArr.sort(compareFunction);
			
			var i:int,len:int = paiArr.length;
			
			var canHu:Boolean = false;
			if(len%3 != 2)
			{
				return false;
			}
			if(UserData.roomtype == 11  || UserData.roomtype == 10)
			{
				if(len == 14)//判断是不是七小队
				{
					var isTrue:Boolean = true;
					for(i=0;i<7;i++)
					{
						if(paiArr[i*2] != paiArr[i*2+1])
						{
							isTrue = false;
						}
					}
					if(isTrue == true)
					{
						return true;
					}
				}
			}
			
			//正常判断
			//能不能找出一对
			
			var duiziArr:Array = getPaiduizi(paiArr);
			if(duiziArr.length == 0)
			{
				return false;
			}
			
			//判断在每一种对子的情况下是否能胡
			var j:int;
			var idx:int;
			var num:int;
			
			var paiArrTemp:Array;
			for(j=0;j<duiziArr.length;j++)
			{
				paiArrTemp = paiArr.concat();
				idx = paiArrTemp.indexOf(duiziArr[j])
				if(idx != -1)
				{
					paiArrTemp.splice(idx,1);
				}
				
				idx = paiArrTemp.indexOf(duiziArr[j])
				if(idx != -1)
				{
					paiArrTemp.splice(idx,1);
				}
				
				if(getCan33(paiArrTemp) == true)
				{
					canHu = true;
					break;
				}
			}
			return canHu;
		}
		
		
		/**判断能不能组成3*/
		public function getCan33(paiArr:Array):Boolean
		{
			paiArr.sort(compareFunction);
			
			if(paiArr.length == 0)
			{
				return true;
			}
			
			var result:Boolean = false;
			
			var idx1:int;
			var idx2:int;
			if(paiArr[0] == paiArr[1] && paiArr[1]== paiArr[2])
			{
				var tempArr:Array = paiArr.concat();
				paiArr.splice(0,3);
				result = getCan33(paiArr);
				if(result == false)
				{
					paiArr = tempArr;
					var tempCard:int = paiArr[0];
					
					if(tempCard == 32 || tempCard == 33 || tempCard == 34 || tempCard == 28 || tempCard == 29 || tempCard == 30 || tempCard == 31 || tempCard == 8 || tempCard == 9 ||
						tempCard == 17 || tempCard == 18 || tempCard == 26 || tempCard == 27)
					{
						return false;
					}
					
					idx1 = paiArr.indexOf(tempCard+1);
					idx2 = paiArr.indexOf(tempCard+2);
					
					if(idx1 != -1 && idx2 != -1)
					{
						paiArr.splice(0,1);
						paiArr.splice(paiArr.indexOf(tempCard+1),1);
						paiArr.splice(paiArr.indexOf(tempCard+2),1);
						result = getCan33(paiArr);
					}
					else
					{
						return false;
					}
				}
			}
			else
			{
//				var tempCard:int = paiArr[0];
				if(tempCard == 32 || tempCard == 33 || tempCard == 34 || tempCard == 28 || tempCard == 29 || tempCard == 30 || tempCard == 31 || tempCard == 8 || tempCard == 9 ||
					tempCard == 17 || tempCard == 18 || tempCard == 26 || tempCard == 27)
				{
					return false;
				}
				
				idx1 = paiArr.indexOf(tempCard+1);
				idx2 = paiArr.indexOf(tempCard+2);
				
				if(idx1 != -1 && idx2 != -1)
				{
					paiArr.splice(0,1);
					paiArr.splice(paiArr.indexOf(tempCard+1),1);
					paiArr.splice(paiArr.indexOf(tempCard+2),1);
					result = getCan33(paiArr);
				}
				else
				{
					return false;
				}
				
				
			}
			return result;
		}
		
		
		/**找出牌组里面的所有对子*/
		public function getPaiduizi(paiArr:Array):Array
		{
			var returnArr:Array = [];
			
			var i:int,len:int = paiArr.length;
			var allPai:Object = new Object();
			var tempPai:int=-1;
			
			
			for(i=0;i<paiArr.length;i++)
			{
				if(paiArr[i] == tempPai)
				{
					allPai[tempPai] += 1;
					
					if(allPai[tempPai] == 2)
					{
						returnArr.push(tempPai);
					}
				}
				else
				{
					tempPai = paiArr[i];
					allPai[tempPai] = 1;
				}
				
			}
			
			return returnArr;
		}
		
		public var canLiCards:Array = [];
		public var appendDownCards:Array = [];
		
		/**根据听哪张牌（可以知道胡哪几张张牌），求出哪些牌应该倒下来*/
		public function getTingDownCards(tingCard:int,kouCards:Array):Object
		{
			var paiArr:Array = allCardsVec[selfChairPos].concat();//取自己手里牌的一个副本
			
			if(theFourteenCardVec[selfChairPos] != -1)//如果有第十四张，加上
			{
				paiArr = paiArr.concat(theFourteenCardVec[selfChairPos]);
			}
			
			var idx:int = paiArr.indexOf(tingCard);//去掉听的那张牌
			if(idx != -1)
			{
				paiArr.splice(idx,1);
			}
			
			var i:int=0;
			for(i=0;i<kouCards.length;i++)//把扣的牌去掉
			{
				
				idx = paiArr.indexOf(kouCards[i]);
				
				if(idx != -1)
				{
					paiArr.splice(idx,1);
				}
				idx = paiArr.indexOf(kouCards[i]);
				
				if(idx != -1)
				{
					paiArr.splice(idx,1);
				}
				idx = paiArr.indexOf(kouCards[i]);
				
				if(idx != -1)
				{
					paiArr.splice(idx,1);
				}
			}
			
			canLiCards = [];
			var canDownCards:Array = [];
			var huArr:Array = this.gethuCards(tingCard);//取胡的那些牌
			
			var haveQixiaodui:Boolean = false;
			
			if(huArr.length == 1)
			{
				if(UserData.roomtype == 11 || UserData.roomtype == 10)
				{
					if(isHuqixiaodui(paiArr.concat(huArr[0])))
					{
						return {canDownCards:[huArr[0]],isHaveJiang:false,jiangpai:0};
					}
				}
			}
			else
			{
				for(i=0;i<huArr.length;i++)
				{
					if(UserData.roomtype == 11 || UserData.roomtype == 10)
					{
						if(isHuqixiaodui(paiArr.concat(huArr[i])))
						{
							haveQixiaodui = true;
						}
					}
				}
				
				if(haveQixiaodui == true)
				{
					return {canDownCards:allCardsVec[selfChairPos],isHaveJiang:false,jiangpai:0};
				}
				
			}
			
			judgeHuZhidingCards(huArr,paiArr);//我们把可以立起来的33组合取出来
			
			
			for(i=0;i<canLiCards.length;i++)
			{
				idx = paiArr.indexOf(canLiCards[i]);
				
				if(idx != -1)
				{
					paiArr.splice(idx,1);
				}
			}
			
			canDownCards = paiArr.concat();
			
			//我们对 剩下的paiArr 扣除将判断能不能胡
			
			var duiziArr:Array = getPaiduizi(paiArr);
			
			var isHaveJiang:Boolean = false;
			var jiangpai:int = 0;
			
			//判断在每一种对子的情况下是否能胡
			var j:int;;
			var num:int;
			var can33:Boolean = true;
			
			var paiArrTemp:Array;
			for(j=0;j<duiziArr.length;j++)
			{
				paiArrTemp = paiArr.concat();
				
				idx = paiArrTemp.indexOf(duiziArr[j])
				if(idx != -1)
				{
					paiArrTemp.splice(idx,1);
				}
				
				idx = paiArrTemp.indexOf(duiziArr[j])
				if(idx != -1)
				{
					paiArrTemp.splice(idx,1);
				}
				
				var allTrue:Boolean = true;
				
				for(var k:int =0;k<huArr.length;k++)
				{
					if(getCan33(paiArrTemp.concat(huArr[k])) == false)
					{
						allTrue = false;
					}
				}
				
				if(allTrue == true)//最多有一个将
				{
					can33 = true;
					paiArr = paiArrTemp;
					
					isHaveJiang = true;
					jiangpai = duiziArr[j];
					
					break;
				}
			}
			
			canDownCards = paiArr.concat(appendDownCards);
			
			return {canDownCards:canDownCards,isHaveJiang:isHaveJiang,jiangpai:jiangpai};
		}
		
		
		/**判断是不是胡七小队*/
		public function isHuqixiaodui(paiArr:Array):Boolean
		{
			
			paiArr.sort(compareFunction);
			
			var i:int,len:int = paiArr.length;
			
			var canHu:Boolean = false;
			if(len%3 != 2)
			{
				return false;
			}
			
			if(len == 14)//判断是不是七小队
			{
				var isTrue:Boolean = true;
				for(i=0;i<7;i++)
				{
					if(paiArr[i*2] != paiArr[i*2+1])
					{
						isTrue = false;
					}
				}
				if(isTrue == true)
				{
					return true;
				}
			}
			
			return false;
		}
		
		/**判断当前的手里的牌能不能胡指定的几张牌 */
		public function judgeHuZhidingCards(huCards:Array,paiArr:Array):void
		{
			appendDownCards = [];
			
			var paizu33Arr:Array = getPaizu(paiArr);
			
			var i:int,len:int = paizu33Arr.length;
			
			var tempArr:Array = paiArr.concat();
			
			var idx:int;
			for(i=0;i<len;i++)
			{
				idx = tempArr.indexOf(paizu33Arr[i][0])
				if(idx != -1)
				{
					tempArr.splice(idx,1);
				}
				
				idx = tempArr.indexOf(paizu33Arr[i][1])
				if(idx != -1)
				{
					tempArr.splice(idx,1);
				}
				
				idx = tempArr.indexOf(paizu33Arr[i][2])
				if(idx != -1)
				{
					tempArr.splice(idx,1);
				}
				
				var allRight:Boolean = true;
				
				var j:int;
				
				for(j=0;j<huCards.length;j++)
				{
					if(judgeHu(tempArr.concat(huCards[j])) == false)
					{
						allRight = false;
					}
				}
				
				if(allRight == true)//这个要去掉之后重新计算
				{
					canLiCards.push(paizu33Arr[i][0],paizu33Arr[i][1],paizu33Arr[i][2]);
					judgeHuZhidingCards(huCards,tempArr);
					
					return;
				}
				else//不行的话要加回去
				{
					tempArr.push(paizu33Arr[i][0],paizu33Arr[i][1],paizu33Arr[i][2]);
				}
			}
			
			
		}
		
		public function getPaizu(paiArr:Array):Array
		{
			paiArr.sort(compareFunction);
			var returnArr:Array = getPaizuKe(paiArr).concat(getPaizuShun(paiArr));
			
			return returnArr;
		}
		
		public function getPaizuKe(paiArr:Array):Array
		{
			var returnArr:Array = [];
			
			var i:int,len:int = paiArr.length;
			var allPai:Object = new Object();
			var tempPai:int=-1;
			
			
			for(i=0;i<paiArr.length;i++)
			{
				if(paiArr[i] == tempPai)
				{
					allPai[tempPai] += 1;
					
					if(allPai[tempPai] == 3)
					{
						returnArr.push([tempPai,tempPai,tempPai]);
					}
				}
				else
				{
					tempPai = paiArr[i];
					allPai[tempPai] = 1;
				}
				
			}
			
			return returnArr;
		}
		
		
		public function getPaizuShun(paiArr:Array):Array//这个是不对的哦
		{
			var returnArr:Array = [];
			
			var i:int,len:int = paiArr.length;
			var allPai:Object = new Object();
			var tempCard:int;
			
			var idx1:int
			
			var idx2:int
			for(i=0;i<paiArr.length-2;i++)
			{
				
				tempCard = paiArr[i];
				
				if(tempCard != 32 && tempCard != 33 && tempCard != 34 && tempCard != 28 && tempCard != 29 && tempCard != 30 && tempCard != 31 && tempCard != 8 && tempCard != 9 &&
					tempCard != 17 && tempCard != 18 && tempCard != 26 && tempCard != 27)
				{
					idx1 = paiArr.indexOf(tempCard+1);
					idx2 = paiArr.indexOf(tempCard+2);
					
					if(idx1 !=-1 && idx2 != -1)
					{
						returnArr.push([tempCard,tempCard+1,tempCard+2]);
					}
				}
			}
			
			return returnArr;
		}

		public function checkAllBuhuaComp():Boolean
		{
			var isAllOver:Boolean = true;
			for(var i:int = 0; i <overHuaVec.length; i ++){
				if(overHuaVec[i] > 0)
				{
					isAllOver = false;
				}
			}
			return isAllOver;
		}
		
		public function getRandomFourValue():Array
		{
			var retArr:Array = [];
			
			var arr:Array = [2,3,4,5,6,7,8,9,10,11,12];
			var i:int,idx:int;
			
			for(i=0;i<4;i++)
			{
				idx = Math.floor(Math.random()*arr.length);
				retArr.push(arr[idx]);
				arr.splice(idx,1);
			}
			
			retArr.sort(function (A:int,B:int):int
			{
				if(A>B)
				{
					return -1;
				}
				else if(A==B)
				{
					return 0;
				}
				else
				{
					return 1;
				}
			}
			);//从大到小
			
			return retArr;
			
			
		}
		
		public function getChengbaoNumRefNum(pos:int,fromPos:int):int
		{
			var retNum:int = 0;
			var i:int;
			for(i=0;i<chiFromVec[pos].length;i++)
			{
				if(chiFromVec[pos][i] == fromPos)
				{
					retNum += 1;
				}
			}
			
			for(i=0;i<pengFromVec[pos].length;i++)
			{
				if(pengFromVec[pos][i] == fromPos)
				{
					retNum += 1;
				}
			}
			
			for(i=0;i<mingGangFromVec[pos].length;i++)
			{
				if(mingGangFromVec[pos][i] == fromPos)
				{
					retNum += 1;
				}
			}
			
			for(i=0;i<anGangFromVec[pos].length;i++)
			{
				if(anGangFromVec[pos][i] == fromPos)
				{
					retNum += 1;
				}
			}
			
			trace("getChengbaoNumRefNum::" + retNum + "  pos:" + pos + " frompos:" + fromPos);
			
			return retNum;
		}
		
		public function getPengGangNum(pos:int):int
		{
			return chiVec[pos].length + pengVec[pos].length + anGangVec[pos].length + mingGangVec[pos].length;
		}
		
		public function judgeMenqing(pos:int):Boolean
		{
			var num:int = chiVec[pos].length + pengVec[pos].length + mingGangVec[pos].length;
			if(num == 0)
			{
				return true;
			}
			else
			{
				return false;
			}
		}
		
		/**获取一张最没有用的牌*/
		public function getUseless():int
		{
			var level0:Array = [];
			var level1:Array = [];
			var level2:Array = [];
			var level3:Array = [];
			var level4:Array = [];
			var level5:Array = [];
			var level6:Array = [];
			
			var tempCards:Array = allCardsVec[selfChairPos];
			if(theFourteenCardVec[selfChairPos]!=-1)
			{
				tempCards = tempCards.concat(theFourteenCardVec[selfChairPos]);
			}
			
			tempCards.sort(compareFunction);
			
			var i:int,len:int=tempCards.length;
			
			var duiziArr:Array = getPaiduizi(tempCards);
			var shunziArr:Array = getPaizuShun(tempCards);
			
			var havedui:Boolean = false;
			var haveshun:Boolean = false;
			
			for(i=0;i<len;i++)
			{
				if(judgeHua(tempCards[i]))
				{
					break;
				}
				
				havedui = checkduizi(tempCards[i],duiziArr);
				haveshun = checkshunzi(tempCards[i],shunziArr);
				
				if(getHuTipArr(tempCards[i]).length > 0)
				{
					if(getHuTipArr(tempCards[i]).length > 2)
					{
						level4.push(tempCards[i]);
					}
					else if(getHuTipArr(tempCards[i]).length > 1)
					{
						level5.push(tempCards[i]);
					}
					else
					{
						level6.push(tempCards[i]);
					}
					
				}
				else
				if(havedui == false && haveshun == false)
				{
					level0.push(tempCards[i]);
				}
				else if(haveshun == false)
				{
					level1.push(tempCards[i]);
				}
				else if(havedui == false)
				{
					level2.push(tempCards[i]);
				}
				else
				{
					level3.push(tempCards[i]);
				}
			}
			
			if(level4.length > 0)
			{
				return level4[0];
			}
			else
			if(level5.length > 0)
			{
				return level5[0];
			}
			else
			if(level6.length > 0)
			{
				return level6[0];
			}//需要添加判断
			else if(level3.length>0)
			{
				for(i=0;i<level3.length;i++)
				{
					if(checkTwoAndMidShun(level3[i],shunziArr,tempCards) == true)
					{
						trace("检查中间牌是否应该出，应该出了牌：：" + level3[i]);
						return level3[i];
					}
				}
			}
			else if(level0.length > 0)//对子和顺子都组成不了
			{
				var card:int = getGuliPai(level0,tempCards);
				trace("机器人检测返回了孤立牌：：" + card);
				
				return card;
			}
			else if(level1.length > 0)
			{
				if(level1.length == 1)
				{
					if(level2.length == 0)
					{
						trace("机器人检测返回了对子：：" + level1[0]);
						return level1[0];
						
					}
					else
					{
						trace("机器人检测返回了顺子：：" + level2[0]);
						return level2[0];//
					}
				}
				else
				{
					trace("机器人检测返回了对子：：" + level1[0]);
					return level1[0];
					
				}
			}
			else if(level2.length > 0)
			{
				trace("机器人检测返回了顺子：：" + level2[0]);
				return level2[0];
			}
			else if(level3.length > 0)
			{
				trace("机器人检测返回了对子顺子：：" + level2[0]);
				return level3[0];
			}
			
			return allCardsVec[selfChairPos][0];
		}
		
		/**判断某张牌是否是两张并且在顺子的中间*/
		public function checkTwoAndMidShun(cardIdx:int,shunziArr:Array,cards:Array):Boolean
		{
			return false;
			
			var preNum:int =0;
			var haveNum:int = 0;
			var nextNum:int = 0;
			
			
			var i:int;
			for(i;i<shunziArr.length;i++)
			{
				if(shunziArr[i][1] == cardIdx)//中间的
				{
					preNum = 0;
					haveNum = 0;
					nextNum = 0;
					
					for(i=0;i<cards.length;i++)
					{
						if(cards[i] == cardIdx)
						{
							haveNum += 1;
						}
						if(cards[i] == cardIdx-1)
						{
							preNum += 1;
						}
						if(cards[i] == cardIdx+1)
						{
							nextNum += 1;
						}
						
					}
					
					if(haveNum > preNum && haveNum > nextNum)
					{
						return true;
					}
				}
			}
			
			return false;
		}
		
		
		public function checkduizi(cardIdx:int,paizu:Array):Boolean
		{
			for(var i:int=0;i<paizu.length;i++)
			{
				if(paizu[i] == cardIdx)
				{
					return true;
				}
			}
			return false;
		}
		
		/**检测某张牌在手里是不是孤立的一张*/
		public function checkshunzi(cardIdx:int,paizu:Array):Boolean
		{
			for(var i:int=0;i<paizu.length;i++)
			{
				if(paizu[i][0] == cardIdx || paizu[i][1] == cardIdx || paizu[i][2] == cardIdx)
				{
					return true;
				}
			}
			
			return false;
		}
		
		/**获取单张里面最孤立的牌*/
		public function getGuliPai(arr:Array,fromArr:Array):int
		{
			var result:Array = [];
			result[0] = 0;
			result[1] = 0;
			result[2] = 0;
			result[3] = 0;
			var i:int=0,len:int;
			
			var level0:Array = [];
			var level1:Array = [];
			var level2:Array = [];
			var level3:Array = [];
			var level4:Array = [];
			var level5:Array = [];
			
			var lv0:Array = [];
			var lv1:Array = [];
			var lv2:Array = [];
			
			len=fromArr.length;
			for(i=0;i<len;i++)
			{
				result[BaseCard.getTypeByCardIndex(fromArr[i])] += 1;
			}
			
			len = arr.length;
			for(i=0;i<len;i++)
			{
//				if(arr[i] > 27)
//				{
//					level0.push(arr[i]);
//				}
				
				if(result[BaseCard.getTypeByCardIndex(arr[i])] < 2)
				{
					if(arr[i] <= 27)
					{
						level0.push(arr[i]);
					}
					else
					{
						level1.push(arr[i]);
					}
				}
				else if(result[BaseCard.getTypeByCardIndex(arr[i])] < 3)
				{
					if(arr[i] <= 27)
					{
						level2.push(arr[i]);
					}
					else
					{
						level3.push(arr[i]);
					}
				}
				else
				{
					if(arr[i] <= 27)
					{
						level4.push(arr[i]);
					}
					else
					{
						level5.push(arr[i]);
					}
				}
				
				
//				if(arr[i] > 27)
//				{
//					level0.push(arr[i]);
//				}
//				else
//				{
//					if(result[BaseCard.getTypeByCardIndex(arr[i])] < 2)
//					{
//						level1.push(arr[i]);
//					}
//					else
//					{
//						level2.push(arr[i]);
//					}
//				}
			}
			
			if(level0.length > 0)
			{
				return level0[0];
			}
			else if(level1.length > 0)
			{
				return level1[0];
			}
			else if(level2.length > 0)
			{
				return level2[0];
			}
			else if(level3.length > 0)
			{
				lv0=[];
				lv1=[];
				lv2=[]
				
				len = level3.length;
				for(i=0;i<len;i++)
				{
					if(fromArr.indexOf(level3[i]-1) != - 1 && BaseCard.getTypeByCardIndex(level3[i]-1) == BaseCard.getTypeByCardIndex(level3[i]))
					{
						lv2.push(level3[i]);
					}
					else if(fromArr.indexOf(level3[i]+1) != - 1 && BaseCard.getTypeByCardIndex(level3[i]+1) == BaseCard.getTypeByCardIndex(level3[i]))
					{ 
						lv2.push(level3[i]);
					}
					else if(fromArr.indexOf(level3[i]-2) != - 1 && BaseCard.getTypeByCardIndex(level3[i]-2) == BaseCard.getTypeByCardIndex(level3[i]))
					{
						lv1.push(level3[i]);
					}
					else if(fromArr.indexOf(level3[i]+2) != - 1 && BaseCard.getTypeByCardIndex(level3[i]+2) == BaseCard.getTypeByCardIndex(level3[i]))
					{ 
						lv1.push(level3[i]);
					}
					else
					{
						lv0.push(level3[i]);
					}
				}
				
				if(lv0.length > 0)
				{
					return lv0[0];
				}
				else if(lv1.length > 0)
				{
					return lv1[0];
				}
				else 
				{
					return lv2[0];
				}
				
			}
			else if(level4.length > 0)
			{
				return level4[0];
			}
			else if(level5.length > 0)
			{
				
				lv0=[];
				lv1=[];
				lv2=[]
				 
				len = level5.length;
				for(i=0;i<len;i++)
				{
					if(fromArr.indexOf(level5[i]-1) != - 1 && BaseCard.getTypeByCardIndex(level5[i]-1) == BaseCard.getTypeByCardIndex(level5[i]))
					{
						lv2.push(level5[i]);
					}
					else if(fromArr.indexOf(level5[i]+1) != - 1 && BaseCard.getTypeByCardIndex(level5[i]+1) == BaseCard.getTypeByCardIndex(level5[i]))
					{ 
						lv2.push(level5[i]);
					}
					else if(fromArr.indexOf(level5[i]-2) != - 1 && BaseCard.getTypeByCardIndex(level5[i]-2) == BaseCard.getTypeByCardIndex(level5[i]))
					{
						lv1.push(level5[i]);
					}
					else if(fromArr.indexOf(level5[i]+2) != - 1 && BaseCard.getTypeByCardIndex(level5[i]+2) == BaseCard.getTypeByCardIndex(level5[i]))
					{ 
						lv1.push(level5[i]);
					}
					else
					{
						lv0.push(level5[i]);
					}
				}
				
				if(lv0.length > 0)
				{
					return lv0[0];
				}
				else if(lv1.length > 0)
				{
					return lv1[0];
				}
				else 
				{
					return lv2[0];
				}
			}
			
			return arr[0];
		}
		
		public var replayAllStepData:Array = [];
		
		/**保存单步数据，有特殊的地方请自己继承实现*/
		public function saveStepData():void
		{
			var replayObj:Object = new Object();
			replayObj.userData = playerInfoVec.concat();
			
			//回复玩家的牌
			replayObj.outputCardsVec = new Vector.<Array>(chairNum);
			replayObj.allCardsVec = new Vector.<Array>(chairNum);
			replayObj.chiVec = new Vector.<Array>(chairNum);
			replayObj.chiFromVec = new Vector.<Array>(chairNum);
			replayObj.pengVec = new Vector.<Array>(chairNum);
			replayObj.pengFromVec = new Vector.<Array>(chairNum);
			replayObj.mingGangVec = new Vector.<Array>(chairNum);
			replayObj.mingGangFromVec = new Vector.<Array>(chairNum);
			replayObj.anGangVec = new Vector.<Array>(chairNum);
			replayObj.anGangFromVec = new Vector.<Array>(chairNum);
			replayObj.theFourteenCardVec = new Vector.<int>(chairNum);
			
			replayObj.huaVec = new Vector.<Array>(chairNum);
			
			
			var i:int,len:int = chairNum;
			for(i=0;i<len;i++)
			{
				
				replayObj.allCardsVec[i] = allCardsVec[i].concat();
				replayObj.theFourteenCardVec[i] = theFourteenCardVec[i];
				replayObj.outputCardsVec[i] = outputCardsVec[i].concat();
				replayObj.chiVec[i] = chiVec[i].concat();
				replayObj.chiFromVec[i] = chiFromVec[i].concat();
				replayObj.pengVec[i] = pengVec[i].concat();
				replayObj.pengFromVec[i] = pengFromVec[i].concat();
				replayObj.mingGangVec[i] = mingGangVec[i].concat();
				replayObj.mingGangFromVec[i] = mingGangFromVec[i].concat();
				replayObj.anGangVec[i] = anGangVec[i].concat();
				replayObj.anGangFromVec[i] = anGangFromVec[i].concat();
				
				replayObj.huaVec[i] = huaVec[i].concat();
				
			}
			
			replayObj.curHandlePos = curHandlePos;
			replayObj.reconnect = 1;
			replayObj.leftDesktopCardsNum = leftDesktopCardsNum;
			replayObj.curOutPutPos = curOutPutPos;
			
			replayAllStepData[replayCurStep] = replayObj;
		}
		
		/**恢复单步数据*/
		public function recoveryByReplayData(replayData:Object):void
		{
			var i:int,len:int=chairNum;
			
			for(i=0;i<len;i++)
			{
				allCardsVec[i] = replayData.allCardsVec[i].concat();
				theFourteenCardVec[i] = replayData.theFourteenCardVec[i];
				huaVec[i] = replayData.huaVec[i].concat();
				
				outputCardsVec[i] = replayData.outputCardsVec[i].concat();
				chiVec[i] = replayData.chiVec[i].concat();
				chiFromVec[i] = replayData.chiFromVec[i].concat();
				pengVec[i] = replayData.pengVec[i].concat();
				pengFromVec[i] = replayData.pengFromVec[i].concat();
				mingGangVec[i] = replayData.mingGangVec[i].concat();
				mingGangFromVec[i] = replayData.mingGangFromVec[i].concat();
				anGangVec[i] = replayData.anGangVec[i].concat();
				anGangFromVec[i] = replayData.anGangFromVec[i].concat();
			}
			
			curHandlePos = replayData.curHandlePos;
			curOutPutPos = replayData.curOutPutPos;
			//replayData.reconnect;
			leftDesktopCardsNum = replayData.leftDesktopCardsNum;
			
		}
	}
}