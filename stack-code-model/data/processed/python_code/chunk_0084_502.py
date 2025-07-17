package vo
{
	//[RemoteClass]
	public class ProductTodayVO
	{
		public var date:Number;
		public var categoryId:int;
		public var productId:int;
		public var weight:Number;
		
		public function ProductTodayVO(date:Number, categoryId:int, productId:int,weight:Number)
		{
			this.date = date;
			this.categoryId = categoryId;
			this.productId = productId;
			this.weight = weight;
		}
	}
}