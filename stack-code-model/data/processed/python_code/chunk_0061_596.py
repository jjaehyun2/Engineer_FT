package modules.game.majiangGame.model
{
	/**西周专用，如果是其他麻将，需要自己和象山麻将一样的做法去实现*/ 
	public class ReplayMajiangModel extends MajiangModel
	{
		
		public var isShowOtherCards:Boolean = true;
		
		
		public function ReplayMajiangModel()
		{
			super();
		}
		
		override public function saveStepData():void
		{
			//回复玩家作为的数据、
			super.saveStepData();
			
//			var userobj:Object = new Object();						
//			
//			var userinfo:Array = new Array();
//			for(var i:int=0;i < chairNum;i++)
//			{
//				var obj:Object = new Object();
//				userinfo.push(obj);
//				obj.uid = getPlayerUidByPos(i);
//				obj.pos = i;
//				obj.vip = 0;
//				obj.sex = playerInfoVec[i].sex;
//				obj.sign = 0;
//				obj.nickname = playerInfoVec[i].nickname;
//				obj.level = playerInfoVec[i].level;
//				obj.golds = playerInfoVec[i].golds;
//				obj.readystate = 1;
//				obj.isTing =  isTingVec[i];
//				obj.card = new Array();
//				
//				var tempArr:Array;
//				if(theFourteenCardVec[i] != -1)
//				{
//					tempArr = allCardsVec[i].concat(theFourteenCardVec[i]);
//				}
//				else
//				{
//					tempArr = allCardsVec[i].concat();
//				}
//				
//				var idx:int = -1;
//				
//				for( j=0;j < kouVec[i].length;j++)
//				{
//					obj.card.push({"type":5,"card":kouVec[i][j],"isPeng":0});
//					obj.card.push({"type":5,"card":kouVec[i][j],"isPeng":0});
//					obj.card.push({"type":5,"card":kouVec[i][j],"isPeng":0});
//					
//					idx = tempArr.indexOf(kouVec[i][j]);
//					if(idx != -1)
//					{
//						tempArr.splice(idx,1);
//					}
//					
//					idx = tempArr.indexOf(kouVec[i][j]);
//					if(idx != -1)
//					{
//						tempArr.splice(idx,1);
//					}
//					
//					idx = tempArr.indexOf(kouVec[i][j]);
//					if(idx != -1)
//					{
//						tempArr.splice(idx,1);
//					}
//				}
//				
//				//去掉扣的 和 听倒的
//				
//				for(var j:int=0;j < tempArr.length;j++)
//				{
//					obj.card.push({"type":3,"card":tempArr[j],"isPeng":0});
//				}
//				
//				for( j=0;j < anGangVec[i].length;j++)
//				{
//					obj.card.push({"type":2,"card":anGangVec[i][j],"isPeng":0});
//				}
//				for( j=0;j < mingGangVec[i].length;j++)
//				{
//					obj.card.push({"type":1,"card":mingGangVec[i][j],"isPeng":0});
//				}
//				for( j=0;j < pengVec[i].length;j++)
//				{
//					obj.card.push({"type":0,"card":pengVec[i][j],"isPeng":0});
//				}
//				for( j=0;j < outputCardsVec[i].length;j++)
//				{
//					obj.card.push({"type":4,"card":outputCardsVec[i][j],"isPeng":0});
//				}
//				
//				for( j=0; j< TingHuCardVec[i].length;j++)
//				{
//					obj.card.push({"type":6,"card":TingHuCardVec[i][j],"isPeng":0});
//				}
//				
//				//7吃的牌 8花
//				for(j=0; j< chiVec[i].length;j++)
//				{
//					obj.card.push({"type":7,"card":chiVec[i][j].chicard,"chicards":chiVec[i][j].chicards,"isPeng":0});
//				}
//				
//				
//				for(j=0;j<huaVec[i].length;j++)
//				{
//					obj.card.push({"type":8,"card":huaVec[i][j],"isPeng":0});
//				}
//				
//				
//			}
//			
//			userobj.user = userinfo;
//			userobj.handlepos = curHandlePos;
//			userobj.reconnect = 1;
//			userobj.remaincard = leftDesktopCardsNum;
//			replayAllStepData[replayCurStep] = userobj;	
			
		}
		
		override public function reset():void
		{
			super.reset();
			
			isStrictShowCalc = false;
		}
		
		public function replayReset():void
		{
			super.reset();
		}
		
		/**从手里的牌里面去掉一张碰掉的牌*/
		override public function cutPengCard(pos:int,cardIdx:int):void
		{
			if(isShowOtherCards)
			{
				var tempArr:Array = [cardIdx,cardIdx];
				
				var i:int;
				var len:int = tempArr.length;
				
				var idx:int =0;
				
				for(i=0;i<len;i++)
				{
					idx = allCardsVec[pos].indexOf(tempArr[i]);
					
					if(idx != -1)
					{
						allCardsVec[pos].splice(idx,1);
					}
				}
			}
			else
			{
				super.cutPengCard(pos,cardIdx);
			}
		}
		
		/**杠了之后刷新手里的牌
		 * 
		 * @param type 0补杠 1暗杠 2明杠
		 * */
		override public function cutGangCard(pos:int,cardIdx:int,type:int):void
		{
			if(isShowOtherCards)
			{
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
						if(theFourteenCardVec[pos] == cardIdx)
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
							}
						}
						
						break;
					default : break;
				}
			}
			else
			{
				super.cutGangCard(pos,cardIdx,type);
			}
			
			
		}
		
		/**玩家出牌更新玩家数据*/
		override public function outputCard(pos:int,cardIdx:int):void
		{
			curOutPutPos = pos;
			if(isShowOtherCards)
			{
				outputCardsVec[pos].push(cardIdx);
				
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
			else
			{
				super.outputCard(pos,cardIdx);
			}
		}
		
		/**更新所有牌(游戏开始后的第一次发牌）*/
		override public function updateAllCardsVecByGameStart(allCards:Array):void
		{
			var i:int;
			var len:int = allCards.length;
			
			for(i=0;i<len;i++)
			{
				var pos:int = getPlayerPosByUid(allCards[i].uid);
				
				updateOneAllCardsVecByGameStart(allCards[i].nusercard,pos);
			}
		}
		
		protected function updateOneAllCardsVecByGameStart(cards:Array,pos:int):void
		{
			var i:int;
			allCardsVec[pos] = new Array();
			var len:int = cards.length;
			for(i=0;i<len;i++)
			{
				(allCardsVec[pos] as Array).push(cards[i].card);
			}
			sortAllCards(pos);
		}

	}
}