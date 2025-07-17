package vo
{
	public class CategoryVO
	{
		public var id:int;
		public var categoryName:String;
		
		public function CategoryVO(id:int, categoryName:String)
		{
			this.id = id;
			this.categoryName = categoryName;
		}
	}
}