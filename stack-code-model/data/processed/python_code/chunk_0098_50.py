package services.vo.common.wishes
{
	[RemoteClass(alias="MapSettingsWish")]
	public class SettingsWishVO
	{
		/**
		 *  This property contain id of settings wish.
		 */
		public var lId:Number;
		/**
		 *  This property contain name of settings wish.
		 */
		public var sName:String;
		/**
		 *  This property contain desription of settings wish.
		 */
		public var sDescription:String;
		/**
		 *  This property contain type of settings wish.
		 *  
		 *  @see framework.vo.profiles.ProfileSpecialWishesVO.SETTING_WISHES
		 *  
		 *  @default 2
		 */
		public var iType:int = 2;
		
		[Transient]
		/**
		 *  This property is <code>true</code> if item is selected
		 *  to attach it to check out guest. 
		 *  
		 *  @default false
		 */
		public var bIsSelected:Boolean = false;
	}
}