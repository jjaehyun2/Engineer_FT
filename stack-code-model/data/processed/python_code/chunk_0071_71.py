package framework.models.vo
{
	[Bindable]
	public class CategoryVO 
	{
		public var id:uint;
		public var title:String;
		public var color:uint;
		public var boardId:uint;
		
		public function CategoryVO(_id:uint = 0, _boardId:uint = 0, _color:uint = 0, _title:String = "") {
			
			id = _id;
			boardId = _boardId;
			color = _color;
			title = _title;
		}
	}
}