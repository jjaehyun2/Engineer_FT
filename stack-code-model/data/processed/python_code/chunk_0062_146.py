package modules.srddzGame.srddzInerGame.model.data
{
	public class FeijiData
	{
		/**飞机不带翅膀*/
		public static const FEIJI_NON:int = 0;
		
		/**飞机带翅膀*/
		public static const FEIJI_DAI:int = 1;
		
		/**飞机的长度*/
		public var length:int = 0;
		
		/**飞机的类型*/
		public var type:int = 0;
		
		/**飞机的最大值*/
		public var bigValue:int = 0;
		
		public function FeijiData()
		{
		}
		
		/**请使用排好序的牌传入*/
		public static function getFeiji(jishuData:JishuArrData):FeijiData
		{
			if(jishuData.danArr.length > 0 || jishuData.fourArr.length > 0 || jishuData.fiveArr.length > 0 || jishuData.sixArr.length >0 || jishuData.sevenArr.length > 0 || jishuData.eightArr.length > 0)
			{
				return null;
			}
			
			var i:int;
			var retData:FeijiData;
			var tempJishuData:JishuArrData = new JishuArrData();
			tempJishuData.clone(jishuData);
			return getFeijiWithNoFour(tempJishuData);
		}
		
		
		
		/**请使用排好序的牌传入,四个的计数必须为零*/
		private static function getFeijiWithNoFour(jishuData:JishuArrData):FeijiData
		{
			if(jishuData.threeArr.length <2)
			{
				return null;
			}
			var feijiData:FeijiData;
			var threeLian:Boolean = JishuArrData.checkValuelian(jishuData.threeArr);
			var twoLian:Boolean = false;
			
			var needOneTwo:Boolean = UserData.needOneTwo; //表示1 2可以连
			
			//以下肯定是飞机带腿
			if(threeLian)//三个都是连续的
			{
				if( jishuData.twoArr.length == 0 && jishuData.threeArr.length > 1)
				{
					feijiData = new FeijiData();
					feijiData.bigValue = jishuData.threeArr[jishuData.threeArr.length-1];
					feijiData.length = jishuData.threeArr.length;
					feijiData.type = FeijiData.FEIJI_NON;
					return feijiData;
				}
				else if(jishuData.threeArr.length == jishuData.twoArr.length)
				{
					twoLian = JishuArrData.checkValuelian(jishuData.twoArr);
				    if(twoLian == false &&needOneTwo)
					{
						var twoArr:Array = jishuData.twoArr.concat();
						JishuArrData.conversValueArr(twoArr);
						twoLian = JishuArrData.checkValuelian(twoArr);
					}
					
					if(twoLian)
					{
						feijiData = new FeijiData();
						feijiData.bigValue = jishuData.threeArr[jishuData.threeArr.length-1];
						feijiData.length = jishuData.threeArr.length;
						feijiData.type = FeijiData.FEIJI_DAI;
						return feijiData;
					}
						
						
				}
			}
			else if(needOneTwo)
			{
				var threeArr:Array = jishuData.threeArr.concat();
				JishuArrData.conversValueArr(threeArr);
				
				threeLian = JishuArrData.checkValuelian(threeArr);
				if(threeLian)//三个都是连续的
				{
					if( jishuData.twoArr.length == 0 && threeArr.length > 1)
					{
						feijiData = new FeijiData();
						feijiData.bigValue = threeArr[threeArr.length-1];
						feijiData.length = threeArr.length;
						feijiData.type = FeijiData.FEIJI_NON;
						return feijiData;
					}
					else if(jishuData.threeArr.length == jishuData.twoArr.length)
					{
						twoLian = JishuArrData.checkValuelian(jishuData.twoArr);
						if(twoLian == false &&needOneTwo)
						{
							var twoArr:Array = jishuData.twoArr.concat();
							JishuArrData.conversValueArr(twoArr);
							twoLian = JishuArrData.checkValuelian(twoArr);
						}
						
						if(twoLian)
						{
							feijiData = new FeijiData();
							feijiData.bigValue = threeArr[threeArr.length-1];
							feijiData.length = threeArr.length;
							feijiData.type = FeijiData.FEIJI_DAI;
							return feijiData;
						}
					}
				}
			}
			
			return null;
		}
	}
}