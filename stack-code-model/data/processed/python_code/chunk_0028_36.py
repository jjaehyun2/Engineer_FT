package framework.view.pages.checkOut.data
{
	import mx.collections.ArrayCollection;
	
	public class AccountData 
	{
		public var id:Number;
		public var type:int;
		/**
		 *  This property is company name by account.
		 *  
		 *  @default ""
		 */
		public var company:String = "";
		/**
		 *  This property is guest name by account.
		 *  
		 *  @default ""
		 */
		public var guest:String = "";
		/**
		 *  This property is address of account.
		 *  
		 *  @default ""
		 */
		public var address:String = "";
		
		public function AccountData(company:String = "", guest:String = "", address:String = "")
		{
			this.company = company;
			this.guest = guest;
			this.address = address;
		}
	}
}