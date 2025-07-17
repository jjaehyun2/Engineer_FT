package services.vo.rates.companyRates
{
	import mx.collections.ArrayCollection;

	[RemoteClass(alias="MapCompanyRateGroup")]
	[Bindable]
	public class CompanyRateGroupVO
	{
	  public var iRateId:int = 0; // id quality
	  public var iCompanyId:int;
	  public var aHotelIds:Array;
	  public var sDateFrom:String = "1985-10-22";
	  public var sDateTo:String = "1985-10-22";
	  public var sName:String; 
	  public var aPricesForRoomTypes:Array = []; //include arrays of CompanyPricesVO
	  public var bBreakfastIncluded:Boolean;
	  public var fBreakfastPrice:Number = 0;
	  public var sCompanyName:String;
	  [Transient]
	  public var bIsSelected:Boolean = false;
	  public var aTransactionList:Array;
	  
	    //contain arrangement code id by which this item was merged as included
  	  public var iArgIdIncluded:int;
  	  //contain arrangement code id by which this item was merged as non-included
  	  public var iArgIdExcluded:int;
	}
	
}