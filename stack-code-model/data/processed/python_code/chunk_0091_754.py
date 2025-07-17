package services.vo.rates.companyRates
{
	import mx.collections.ArrayCollection;

	[RemoteClass(alias="MapCompanyRateItem")]
	[Bindable]
	public class CompanyRateItemVO
	{
	  //TODO
	  public var iId:int;
	  public var iItemId:int;
	  public var fPrice:Number;
	  public var bPerPerson:Boolean;
	  public var sDescription:String;	    
	  
	  //these are for output only:
	  public var sCode:String;
	  public var sCodeDirect:String;
	  public var sName:String;	  
	  
	   //list of arrangement code assigned to this item
	  public var aCodeArrangement:Array;//int	  
	  
	  //included to Logis or not
  	  public var bRctIsIncluded:Boolean;  	  
  	  
	}
	
}