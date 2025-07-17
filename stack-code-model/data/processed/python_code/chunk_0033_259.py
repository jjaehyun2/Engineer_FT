package services.vo.common
{
	[RemoteClass(alias="MapContact")]
	public class ContactVO
	{
		public static const CONTACT_WORK_PHONE:int = 1;
		public static const CONTACT_WORK_FAX:int = 2;
		public static const CONTACT_WORK_EMAIL:int = 3;
		public static const CONTACT_WWW:int = 4;
		public static const CONTACT_HOME_PHONE:int = 5;
		public static const CONTACT_MOBILE_PHONE:int = 6;
		public static const CONTACT_PERSONAL_EMAIL:int = 7;
		public static const CONTACT_WHITE_MAIL:int = 8;
		/**
		 *  This property contain type of contact.
		 */
		public var iContactType:int;
		/**
		 *  This property contain view of contact data
		 *  as String.
		 */
		public var sContactData:String;
	}
}