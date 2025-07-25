package model.vo
{
	import com.adobe.cairngorm.vo.IValueObject;
	
	import mx.collections.ArrayCollection;
	
	[Bindable]
	public class SiteVO implements IValueObject
	{
		public var locationName:String;
		public var xPosition:Number;
		public var yPosition:Number;
		public var sourceDir:String;
		public var people:PeopleVO;
		public var profileImagePath:String;
		public var galleryImagePaths:ArrayCollection;
		public var videoPath:String;
	}
}