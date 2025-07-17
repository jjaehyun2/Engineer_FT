package framework.view.pages.checkOut.data
{
	import services.vo.checkOut.AccountVO;

	public class AccountTreeItem extends AccountVO
	{	
		
		//в поле $sType будут такие варианты:
		public static const PMT_ACCOUNT_TYPE_GROUP:String = "PMT_ACCOUNT_TYPE_GROUP";// - группа;
		public static const PMT_ACCOUNT_TYPE_ROOM:String = "PMT_ACCOUNT_TYPE_ROOM";// - комната
		public static const PMT_ACCOUNT_TYPE_VIRTUAL:String = "PMT_ACCOUNT_TYPE_VIRTUAL";// - конференс рум
		public static const PMT_ACCOUNT_TYPE_PERSONAL:String = "PMT_ACCOUNT_TYPE_PERSONAL";// - персонал аддресс
		public static const PMT_ACCOUNT_TYPE_COMPANY:String = "PMT_ACCOUNT_TYPE_COMPANY";// - компани аддресс
		public static const PMT_ACCOUNT_TYPE_AGENCY:String = "PMT_ACCOUNT_TYPE_AGENCY";// - тревел эдженси аддресс (тот же компани, только в профиль:))		
			
		public function AccountTreeItem()
		{
			super();
		}
	
		public var children:Array;	
	}
}