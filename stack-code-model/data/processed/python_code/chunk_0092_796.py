package modules.sddzGame.sddzInerGame.model.data
{
	import modules.sddzGame.sddzInerGame.view.pockerPart.card.BasePocker;

	public class PaixingLogic
	{
		public function PaixingLogic()
		{
		}
		
		/**获取牌型*/
		public static function  getPaixing(cards:Array,jishuArr:JishuArrData=null,needSort:Boolean=true):int
		{
			if(needSort)
			{
				cards.sort(compCardsFun);
			}
			if(jishuArr == null)
			{
				jishuArr = JishuArrData.getJishuArrData(cards);
			}
			
			
			if(isDanzhang(cards) == true)
			{
				return BasePocker.PAIXING_DAN;
			}
			else if(isDuizi(cards) == true)
			{
				return BasePocker.PAIXING_DUIZI;
			}
			else if(isSan(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_SAN;
			}
			else if(isSanYi(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_SANYI;
			}
			else if(isSanEr(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_SANER;
			}
			else if(isLiandui(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_LIANDUI;
			}
			else if(isShunzi(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_SHUNZI;
			}
			else if(isFeiji(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_FEIJI;
			}
			else if(isSidaier(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_SIDAIER;
			}
			else if(isZhadan(cards,jishuArr) == true)
			{
				return BasePocker.PAIXING_ZHADAN;
			}
			else if(isDuiwang(cards) == true)
			{
				return BasePocker.PAIXING_DUIWANG;
			}
			return BasePocker.PAIXING_NON;
		}
		
		/**是否是单张*/
		public static function isDanzhang(cards:Array):Boolean
		{
			if(cards.length == 1)
			{
				return true;
			}
			
			return false;
		}
		
		/**是否是对子*/
		public static function isDuizi(cards:Array):Boolean
		{
			if(cards.length == 2)
			{
				if(BasePocker.getV(cards[0]) == BasePocker.getV(cards[1]))//值相同的两张牌
				{
					return true;
				}
			}
			return false;
		}
		
		/**是否是三个*/
		public static function isSan(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			var i:int,len:int = cards.length;
			
			if(len == 3)
			{
				if(jishuData == null)
				{
					jishuData = JishuArrData.getJishuArrData(cards);
				}
				if(jishuData.threeArr.length == 1)
				{
					return true;
				}
				
			}
			return false;
		}
		
		/**是否是三个带1 前三个相同或者后三个相同 并且第一个不等于最后一个*/
		public static function isSanYi(cards:Array,jishuData:JishuArrData=null):Boolean
		{	
			var i:int,len:int=cards.length;
			
			if(len == 4)
			{
				if(jishuData == null)
				{
					jishuData = JishuArrData.getJishuArrData(cards);
				}
				
				if(jishuData.threeArr.length == 1 && jishuData.danArr.length == 1)
				{
					return true;
				}
			}
			return false;
		}
		
		/**是否是三个带二*/
		public static function isSanEr(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			if(cards.length == 5)
			{
				if(jishuData == null)
				{
					jishuData = JishuArrData.getJishuArrData(cards);
				}
				
				if(jishuData.threeArr.length == 1 && jishuData.twoArr.length == 1)
				{
					return true;
				}
			}
			
			return false;
		}
		
		/**是都是连对*/
		public static function isLiandui(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			var i:int;
			var len:int = cards.length;
			
			if(len >= 6 && len%2 == 0)
			{
				if(jishuData == null)
				{
					jishuData = JishuArrData.getJishuArrData(cards);
				}
				
				if(jishuData.fourArr.length == 0 && jishuData.threeArr.length == 0 && jishuData.twoArr.length >= 3 && jishuData.danArr.length == 0)
				{
					if(JishuArrData.checkValuelian(jishuData.twoArr) == true)//对子数量大于等于三并且是连着的
					{
						return true;
					}
				}
			}
			else
			{
				return false;
			}
			
			return false;
		}
		
		/**是否是顺子*/
		public static function isShunzi(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			var i:int,len:int=cards.length;
			
			if(len < 5)
			{
				return false;
			}
			else
			{
				if(jishuData == null)
				{
					jishuData = JishuArrData.getJishuArrData(cards);
				}
				
				if(jishuData.fourArr.length == 0 && jishuData.threeArr.length == 0 && jishuData.twoArr.length == 0 && jishuData.danArr.length >= 5)
				{
					if(JishuArrData.checkValuelian(jishuData.danArr) == true)
					{
						return true;
					}
				}
				
			}
			return false;
		}
		
		/**是否是飞机*/
		public static function isFeiji(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			if(cards.length < 6)
			{
				return false;
			}
			if(jishuData == null)
			{
				jishuData = JishuArrData.getJishuArrData(cards);
			}
			var feijiData:FeijiData = FeijiData.getFeiji(jishuData);
			if(feijiData != null)
			{
				return true;
			}
			return false;
		}
		
		/**是否是四带二*/
		public static function  isSidaier(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			if(cards.length < 6)
			{
				return false;
			}
			
			if(jishuData == null)
			{
				jishuData = JishuArrData.getJishuArrData(cards);
			}
			
			var sidaiData:SidaierData = SidaierData.getSidaierData(jishuData);
			
			if(sidaiData != null)
			{
				return true;
			}
			
			return false;
		}
		
		/**是否是炸弹*/
		public static function isZhadan(cards:Array,jishuData:JishuArrData=null):Boolean
		{
			if(cards.length != 4)
			{
				return false;
			}
			
			if(jishuData == null)
			{
				jishuData = JishuArrData.getJishuArrData(cards);
			}
			
			if(jishuData.fourArr.length == 1 && jishuData.threeArr.length ==0 && jishuData.twoArr.length ==0 && jishuData.danArr.length == 0)
			{
				return true;
			}
			return false;
		}
		
		/**是否是对王*/
		public static function isDuiwang(cards:Array):Boolean
		{
			if(cards.length == 2)
			{
				if(BasePocker.getT(cards[0]) == BasePocker.TYPE_WANG && BasePocker.getT(cards[1]) == BasePocker.TYPE_WANG)//两张都是王
				{
					return true;
				}
			}
			return false;
		}
		
		/**我们这里采用升序 a>b return 1 交换位置，升序*/
		public static function compCardsFun(A:int,B:int):int
		{
			if(A== 0 || B == 0)//没有值得牌直接返回
			{
				return 0;
			}
			var typeA:int = BasePocker.getT(A);
			var typeB:int = BasePocker.getT(B);
			
			var valueA:int = BasePocker.getV(A);
			var valueB:int = BasePocker.getV(B);
			
			if(valueA > valueB)
			{
				return 1;
			}
			else if(valueA == valueB)
			{
				if(typeA > typeB)//红桃在先
				{
					return 1;
				}
				else
				{
					return -1;
				}
			}
			else
			{
				return -1;
			}
		}
		
		/**从一组牌里面找出大于当前牌的的牌*/
		public static function getBigThan(fromCards:Array,targetCards:Array):Array
		{
			
			var retArr:Array = [];
			
			if(targetCards.length == 0)//目标牌没有就给最小的第一张
			{
				retArr.push(fromCards[0]);
				return retArr;
			}
			
			fromCards.sort(compCardsFun);
			targetCards.sort(compCardsFun);
			
			var tjishu:JishuArrData = JishuArrData.getJishuArrData(targetCards);
			var tPaixing:int = getPaixing(targetCards,tjishu,false);
			
//			if(tPaixing == -1)//没有牌型
//			{
//				return retArr;
//			}
			
			var fjishu:JishuArrData = JishuArrData.getJishuArrData(fromCards);
			
			var tempV:int;
			var i:int;
			var lianLen:int ;
			var tempArr:Array;
			
			switch(tPaixing)
			{
				case BasePocker.PAIXING_NON:
					alert("打出的牌型不合法！");
					return retArr;
					break;
				
				case BasePocker.PAIXING_DAN://单张
					tempV =  tjishu.danArr[0];//只有一张嘛
					//先从单张里面找一张
					for(i=0;i<fjishu.danArr.length;i++)
					{
						if(fjishu.danArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.danArr[i]]);
							return retArr;
						}
					}
					//单张没有找到
					for(i=0;i<fjishu.twoArr.length;i++)
					{
						if(fjishu.twoArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.twoArr[i]]);
							return retArr;
						}
					}
					//对子没找到
					for(i=0;i<fjishu.threeArr.length;i++)
					{
						if(fjishu.threeArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i]]);
							return retArr;
						}
					}
					//三个也没找到
					for(i=0;i<fjishu.fourArr.length;i++)
					{
						if(fjishu.fourArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.fourArr[i]]);
							return retArr;
						}
					}
					//单张都没有找到
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					
					//对王不需要 如果有 一个王就干过了
					
					return retArr;//空的表示没有找到咯
					
					break;
				case BasePocker.PAIXING_DUIZI:
					tempV =  tjishu.twoArr[0];//只有一个对子嘛
					//从自己的对子里面找
					for(i=0;i<fjishu.twoArr.length;i++)
					{
						if(fjishu.twoArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.twoArr[i],fjishu.twoArr[i]]);
							return retArr;
						}
					}
					
					for(i=0;i<fjishu.threeArr.length;i++)
					{
						if(fjishu.threeArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i]]);
							return retArr;
						}
					}
					
					//找一个炸弹来
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					
					break;
				
				
				case BasePocker.PAIXING_SAN:
					tempV =  tjishu.threeArr[0];//只有一个三个嘛
					//从自己的三个里面找
					for(i=0;i<fjishu.threeArr.length;i++)
					{
						if(fjishu.threeArr[i] > tempV)//就这张了
						{
							retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i]]);
							return retArr;
						}
					}
					//找一个炸弹来
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					
					break;
				
				case BasePocker.PAIXING_SANYI://
					tempV =  tjishu.threeArr[0];//只有一个三个带1
					//从自己的三个里面找
					for(i=0;i<fjishu.threeArr.length;i++)
					{
						if(fjishu.threeArr[i] > tempV)//就这张了
						{
							if(fjishu.danArr.length > 0)
							{
								retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.danArr[0]]);
								return retArr;
							}
							else if(fjishu.twoArr.length > 0)
							{
								retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.twoArr[0]]);
								return retArr;
							}
							else if(fjishu.threeArr.length > 1)
							{
								if(i==0)//当前第0个取第一个里面的一张
								{
									retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[1]]);
									return retArr;
								}
								else//不是第0个就取第0个
								{
									retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[0]]);
									return retArr;
								}
							}
						}
					}
					//找一个炸弹来
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_SANER:
					tempV =  tjishu.threeArr[0];//只有一个三个带2
					//从自己的三个里面找
					for(i=0;i<fjishu.threeArr.length;i++)
					{ 
						if(fjishu.threeArr[i] > tempV)//就这张了
						{
							if(fjishu.twoArr.length > 0)//给一个三带2就行了
							{
								retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.twoArr[0],fjishu.twoArr[0]]);
								return retArr;
							}
							else if(fjishu.threeArr.length > 1)
							{
								if(i==0)//当前第0个取第一个里面的一张
								{
									retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[1],fjishu.threeArr[1]]);
									return retArr;
								}
								else//不是第0个就取第0个
								{
									retArr = getCardsFromValues(fromCards,[fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[i],fjishu.threeArr[0],fjishu.threeArr[0]]);
									return retArr;
								}
							}
						}
					}
					//找一个炸弹来
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_LIANDUI:
					tempV = tjishu.twoArr[tjishu.twoArr.length-1];
					lianLen = tjishu.twoArr.length;
					
					var moreTwoArr:Array = [];//fjishu.fourArr.concat() 四个的不要拆了
					moreTwoArr = moreTwoArr.concat(fjishu.threeArr);
					moreTwoArr = moreTwoArr.concat(fjishu.twoArr);
					
					moreTwoArr.sort(compCardsFun);
					for(i=0;i<moreTwoArr.length;i++)//去除不符合的对子
					{
						if(moreTwoArr[i] < tempV - (lianLen-2))// 789 9-1=8 <8的都不行    34567        7-(5-2) = 4 45678是可以的哦           
						{
							moreTwoArr.splice(i,1);
							i--;
						}
					}
					
					if(moreTwoArr.length >= lianLen)//剩下的长度要大于连队的长度 从中找出一个连续的长度
					{
						tempArr= getFromVlauesLenThan(moreTwoArr,lianLen);
						if(tempArr != null && tempArr.length > 0)//找到咯
						{
							tempArr = tempArr.concat(tempArr);
							tempArr.sort(compCardsFun);
							retArr = getCardsFromValues(fromCards,tempArr.reverse());
							return retArr;
						}
					}
					
					//
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_SHUNZI:
					tempV = tjishu.danArr[tjishu.danArr.length-1];
					lianLen = tjishu.danArr.length;
					
					var moreOneArr:Array = [];// fjishu.fourArr.concat() 四个的不要拆了
					moreOneArr = moreOneArr.concat(fjishu.threeArr);
					moreOneArr = moreOneArr.concat(fjishu.twoArr);
					moreOneArr = moreOneArr.concat(fjishu.danArr);
					
					moreOneArr.sort(compCardsFun);
					for(i=0;i<moreOneArr.length;i++)//去除不符合的对子
					{
						if(moreOneArr[i] < tempV - (lianLen-2))// 56789 9-3=6 <6的都不行
						{
							moreOneArr.splice(i,1);
							i--;
						}
					}
					
					if(moreOneArr.length >= lianLen)//剩下的长度要大于连队的长度 从中找出一个连续的长度
					{
						tempArr = getFromVlauesLenThan(moreOneArr,lianLen);
						if(tempArr != null && tempArr.length > 0)//找到咯
						{
							retArr = getCardsFromValues(fromCards,tempArr.reverse());
							return retArr;
						}
					}
					
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_FEIJI:
					var feiji:FeijiData = FeijiData.getFeiji(tjishu);
					if(feiji == null)//说明牌型判断有误
					{
						return retArr;
					}
					
					var threeArr:Array = fjishu.threeArr.concat();
					var spliceArr:Array = [];
					
					for(i=0;i<threeArr.length;i++)//去除不符合的对子
					{
						if(threeArr[i] < feiji.bigValue - (feiji.length-2))// 56789 9-3=6 <6的都不行
						{
							spliceArr.push(threeArr[i]);
							threeArr.splice(i,1);
							i--;
						}
					}
					
					if(threeArr.length >= feiji.length)
					{
						tempArr = getFromVlauesLenThan(threeArr,feiji.length);
						var ctempArr:Array = tempArr.concat();
						//将三个剩余的继续加入删除的备用数组
						for(i=0;i<threeArr.length;i++)
						{
							var idx:int = ctempArr.indexOf(threeArr[i]);
							if(idx != -1)
							{
								ctempArr.splice(idx,1);
								threeArr.splice(i,1);
								i--;
							}
						}
						spliceArr = spliceArr.concat(threeArr);
						
						
						if(tempArr != null  && tempArr.length > 0)
						{
							switch(feiji.type)
							{
								case FeijiData.FEIJI_NON://飞机不带翅膀
									tempArr = tempArr.concat(tempArr).concat(tempArr);
									tempArr.sort(compCardsFun);
									retArr = getCardsFromValues(fromCards,tempArr);
									return retArr;
									break;
								case FeijiData.FEIJI_DAN://飞机带一个翅膀
									if(feiji.length <= spliceArr.length*3 + fjishu.twoArr.length*2 + fjishu.danArr.length)
									{
										tempArr = tempArr.concat(tempArr).concat(tempArr);
										tempArr.sort(compCardsFun);
										
										var tuiArr:Array = [];
										for(i=0;i<fjishu.danArr.length;i++)//拿单张补腿
										{
											tuiArr.push(fjishu.danArr[i]);
											if(tuiArr.length == feiji.length)
											{
												break;
											}
										}
										if(tuiArr.length  < feiji.length)//拿对子来补腿
										{
											for(i=0;i<fjishu.twoArr.length;i++)
											{
												tuiArr.push(fjishu.twoArr[i]);
												if(tuiArr.length == feiji.length)
												{
													break;
												}
												tuiArr.push(fjishu.twoArr[i]);
												if(tuiArr.length == feiji.length)
												{
													break;
												}
											}
										}
										
										if(tuiArr.length < feiji.length)//拿三个来补
										{
											for(i=0;i<spliceArr.length;i++)
											{
												tuiArr.push(spliceArr[i]);
												if(tuiArr.length == feiji.length)
												{
													break;
												}
												tuiArr.push(spliceArr[i]);
												if(tuiArr.length == feiji.length)
												{
													break;
												}
												tuiArr.push(spliceArr[i]);
												if(tuiArr.length == feiji.length)
												{
													break;
												}
											}
										}
										
										if(tuiArr.length == feiji.length)
										{
											tuiArr.sort(compCardsFun);
											
											retArr = getCardsFromValues(fromCards,tempArr.concat(tuiArr));
											return retArr;
										}
										
									
									}
									break;
								case FeijiData.FEIJI_DUIZI:
									if(feiji.length <= spliceArr.length + fjishu.twoArr.length)//剩余的三张和对子的数量还够用啊
									{
										tempArr = tempArr.concat(tempArr).concat(tempArr);
										tempArr.sort(compCardsFun);
										
										var tuiDuiArr:Array = [];
										for(i=0;i<fjishu.twoArr.length;i++)
										{
											tuiDuiArr.push(fjishu.twoArr[i]);
											if(tuiDuiArr.length == feiji.length)
											{
												break;
											}
										}
										
										if(tuiDuiArr.length < feiji.length)
										{
											for(i=0;i<spliceArr.length;i++)
											{
												tuiDuiArr.push(spliceArr[i]);
												if(tuiDuiArr.length == feiji.length)
												{
													break;
												}
											}
										}
										
										if(tuiDuiArr.length == feiji.length)
										{
											tuiDuiArr = tuiDuiArr.concat(tuiDuiArr);
											tuiDuiArr.sort(compCardsFun);
											retArr = getCardsFromValues(fromCards,tempArr.concat(tuiDuiArr));
											return retArr;
										}	
									}	
									break;
							}
						}
					}
					
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_SIDAIER:
					var tsier:SidaierData = SidaierData.getSidaierData(tjishu);
					//这个直接选炸弹还好点吧，大多数情况下
					var fsier:SidaierData = SidaierData.getSidaierData(fjishu);
					
					if(fsier != null && fsier.type == tsier.type && fsier.value > tsier.value)
					{
						retArr = fromCards.concat();
						return retArr;
					}
					
					if(fjishu.fourArr.length > 0)//有炸弹啊 随便找个炸弹嘛
					{
						retArr = getCardsFromValues(fromCards,[fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0],fjishu.fourArr[0]]);
						return retArr;
					}
					
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_ZHADAN:
					tempV = tjishu.fourArr[0];	
					if(fjishu.fourArr.length > 0)
					{
						for(i=0;i<fjishu.fourArr.length;i++)
						{
							if(fjishu.fourArr[i] > tempV)
							{
								retArr = getCardsFromValues(fromCards,[fjishu.fourArr[i],fjishu.fourArr[i],fjishu.fourArr[i],fjishu.fourArr[i]]);
								return retArr;
							}
						}
					}
					//看看有没有对王
					if(checkHaveDuiWang(fromCards) == true)
					{
						retArr = [551,552];
					}
					return retArr;//空的表示没有找到咯 
					break;
				case BasePocker.PAIXING_DUIWANG:
					return retArr;//哎，没有大过对王的啊
					break;
			}
			
			return retArr;
		}
		
		/**检测一组牌里面有没有对王*/
		public static function checkHaveDuiWang(cards:Array):Boolean
		{
			var idxXW:int = cards.indexOf(551);
			var idxDW:int = cards.indexOf(552);
			if(idxXW != -1 && idxDW != -1)
			{
				return true;
			}
			
			
			return false;
		}
		
		/**从一组牌获得values对应cards*/
		public static function getCardsFromValues(fromCards:Array,values:Array):Array
		{
			var retArr:Array = [];
			var tempArr:Array = fromCards.concat();
			var i:int,j:int;
			
			for(i=0;i<values.length;i++)
			{
				for(j=0;j<tempArr.length;j++)
				{
					if(BasePocker.getV(tempArr[j]) == values[i])//值相同
					{
						retArr.push(tempArr[j]);
						tempArr.splice(j,1);
						break;
					}
				}
			}
			
			return retArr;
		}
		
		/**从一组数值中找出一个连续的长度等于指定的长度*/
		public static function getFromVlauesLenThan(values:Array,tLen:int):Array
		{
			var retArr:Array = [];
			var i:int;
			var num:int = 0;
			for(i=0;i<values.length-1;i++)
			{
				if(values[i+1] == values[i] +1)
				{
					if(num == 0)
					{
						retArr.push( values[i],values[i+1]);
						num += 2;
					}
					else
					{
						retArr.push( values[i+1]);
						num += 1;
					}
					
				}
				else
				{
					num = 0;
					retArr = [];
				}
				
				if(num ==tLen)
				{
					break;
				}
			}
			if(retArr.length < tLen)//没有达到要求
			{
				retArr.length = 0;
			}
			return retArr;
		}
		
		
		/**给手里的牌进行排序*/
		public static function sortHandleCards(cards:Array):void
		{
			cards.sort(compCardsFun);
		}
		
		/**给打出去的牌排序*/
		public static function sortOutputCards(cards:Array):Array
		{
			var retCards:Array;
			
			sortHandleCards(cards);//排序
			var jishuData:JishuArrData = JishuArrData.getJishuArrData(cards);
			var paixing:int = getPaixing(cards);
			
			var valueCards:Array = [];
			var tempValues:Array = [];
			
			var i:int;
			var temp:int;
			var idx:int;
			
			switch(paixing)
			{
				case BasePocker.PAIXING_SANYI:
					valueCards = [jishuData.threeArr[0],jishuData.threeArr[0],jishuData.threeArr[0],jishuData.danArr[0]];//3331
					cards = getCardsFromValues(cards,valueCards);
					break;
				case BasePocker.PAIXING_SANER:
					valueCards = [jishuData.threeArr[0],jishuData.threeArr[0],jishuData.threeArr[0],jishuData.twoArr[0],jishuData.twoArr[0]];//33322
					cards = getCardsFromValues(cards,valueCards);
					break;
				case BasePocker.PAIXING_FEIJI:
					var feiji:FeijiData = FeijiData.getFeiji(jishuData);//333444555778899
					
					for(i=0;i<feiji.length;i++)
					{
						temp = feiji.bigValue - (feiji.length-1 - i);
						tempValues.push(temp,temp,temp);
						
						for(var j:int=0;j<3;j++)
						{
							idx = jishuData.valueArr.indexOf(temp);
							if(idx != -1)
							{
								jishuData.valueArr.splice(idx,1);
							}
						}
					}
					valueCards = tempValues.concat(jishuData.valueArr);
					cards = getCardsFromValues(cards,valueCards);
					break;
				case BasePocker.PAIXING_SIDAIER:
					temp = jishuData.fourArr[0];
					tempValues.push(temp,temp,temp,temp);
					for(i=0;i<4;i++)//0123
					{
						idx = jishuData.valueArr.indexOf(temp);
						if(idx != -1)
						{
							jishuData.valueArr.splice(idx);
						}
					}
					valueCards = tempValues.concat(jishuData.valueArr);
					cards = getCardsFromValues(cards,valueCards);
					break;
			}
			
			return retCards = cards.concat();
		}
		
	}
}