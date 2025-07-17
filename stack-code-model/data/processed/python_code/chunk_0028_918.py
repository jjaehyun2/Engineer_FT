package services.vo.profiles
{
	[RemoteClass(alias="MapProfilePersonView")]
	public class ProfilePersonViewVO
	{
		/**
		 *  This property contain id of profile.
		 */
		public var lId:Number = 0;
		/**
		 *  This property contain main id of profile.
		 */
		public var lMainId:Number = 0;
		/**
		 *  This property contain first name of person in
		 *  profile.
		 */
		public var sName:String;
		/**
		 *  This property contain last name of person in
		 *  profile.
		 */
		public var sSurname:String;
		/**
		 *  This property contain company name of person in
		 *  profile.
		 */
		public var sCompany:String;
		/**
		 *  This property contain phone of person in profile.
		 */
		public var sPhone:String;
		/**
		 *  This property contain e-mail of person in profile.
		 */
		public var sEmail:String;
		/**
		 *  If this property is <code>true</code>, the person
		 *  is disabled.
		 */
		public var bIsReserved:Boolean = false;		
	}
}