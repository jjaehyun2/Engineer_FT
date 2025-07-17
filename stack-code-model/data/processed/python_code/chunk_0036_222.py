package com.macys.marketing.sema.model.type
{
	
public class ReplicateToken
{
	
	public static const kAdKeyword:String = "adKeyword";
	public static const kAdGroup:String = "adGroup";
	public static const kAdCopy:String = "adCopy";
	public static const kAdCampaign:String = "adCampaign";
	
	private var _sourceId:Number = 0;
	private var _targetId:Number = 0;
	private var _sourceType:String = "";
	private var _targetType:String = "";
	
	private var _sourceName : String = "";
	private var _targetName : String = "";
	
	public function ReplicateToken()
	{
		super();
	}
	
  	public function get sourceId():Number 
  	{
  		return _sourceId;
  	}
  	
  	public function set sourceId(sourceId:Number):void 
  	{
  		_sourceId = sourceId;
  	}
  
  	public function get sourceType():String 
  	{
  		return _sourceType;
  	}
  	
  	public function set sourceType(sourceType:String):void 
  	{
  		_sourceType = sourceType;
  	}
  
  	public function get targetId():Number 
  	{
  		return _targetId;
  	}
  	
  	public function set targetId(targetId:Number):void 
  	{
  		_targetId = targetId;
  	}
  
  	public function get targetType():String 
  	{
  		return _targetType;
  	}
  	
  	public function set targetType(targetType:String):void 
  	{
  		_targetType = targetType;
  	}
  	
  	public function get sourceName() : String
  	{
  		return _sourceName;
  	}
  	
  	public function set sourceName(sourceName : String) : void
  	{
  		_sourceName = sourceName;
  	}
  	
  	public function get targetName() : String
  	{
  		return _targetName;
  	}
  	
  	public function set targetName(targetName : String) : void
  	{
  		_targetName = targetName;
	}
}
}