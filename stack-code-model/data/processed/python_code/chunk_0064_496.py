package framework.models.vo
{
	[Bindable]
	public class BoardVO {
		
		public var id:int;
		public var title:String;
		public var position:uint;
		public var creationTime:String;
		public var backgroundColor:uint;
		
		public function BoardVO(_id:uint = 0, _title:String = "", _creationTime:String = "", _position:uint = 0, _backgroundColor:uint = 0x0087BD) {
			
			id = _id;
			title = _title;
			creationTime = _creationTime;
			position = _position;
			backgroundColor = _backgroundColor;
		}
	}
}