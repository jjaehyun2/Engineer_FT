package services.vo.profiles
{
	[RemoteClass(alias="MapProfileSpWishes")]
	public class ProfileSpecialWishesVO
	{
		/**
		 *  This property contain list of items' wishes.
		 *  
		 *  @see framework.vo.common.wishes.ItemsWishVO
		 *  
		 *  @default []
		 */
		public var aItems:/* ItemsWishVO */Array = [];
		/**
		 *  This property contain list of items' wishes.
		 *  
		 *  @see framework.vo.common.wishes.SettingsWishVO
		 *  
		 *  @default []
		 */
		public var aSettings:/* SettingsWishVO */Array = [];
	}
}