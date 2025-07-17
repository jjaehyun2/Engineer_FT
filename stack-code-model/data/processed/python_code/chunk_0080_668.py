package services.vo.inHouse
{
	import services.vo.MapValueObject;
	
	[RemoteClass(alias="MapPersonMessage")]
	public class PersonMessageVO extends MapValueObject
	{
		/**
		 *  This property is id of person profile of guest.
		 *  
		 *  @default 0
		 */
		public var lProfileId:Number = 0;;
		/**
		 *  This property is id of message.
		 *  
		 *  @default 0
		 */
		public var lId:Number = 0;
		/**
		 *  This property is name of person who deliver message for
		 *  guest.
		 */
		public var sFrom:String;
		/**
		 *  This property is body of message.
		 */
		public var sMsg:String;
		/**
		 *  This property is time of creation message for guest.
		 */
		public var dCreationTime:String;
		/**
		 *  This property is time of deliver message for guest.
		 */
		public var dDeliverTime:String;
		
		[Transient]
		/**
		 *  This property is <code>true</code> if message for guest
		 *  is read.
		 *  
		 *  @default false
		 */
		public var bIsRead:Boolean = false;
	}
}