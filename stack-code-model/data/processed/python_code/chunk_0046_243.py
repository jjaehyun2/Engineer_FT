package services.vo.profiles
{
	import services.vo.common.ContactVO;
	
	[RemoteClass(alias="MapCompanyContact")]
	public class CompanyContactVO
	{
		public var bIsPrimary:Boolean = false;
		public var oMapContact:ContactVO = new ContactVO();
	}
}