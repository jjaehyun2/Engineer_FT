package com.macys.marketing.sema.vo.tools
{
	import com.adobe.cairngorm.vo.ValueObject;

	[Bindable]
	public class KeywordVariationVO implements ValueObject
	{
		private var _advertiserCompetitionScale : Number;
		private var _generatedKeyword : String;
		private var _searchVolumeScale : Number;
		
		public function get advertiserCompetitionScale() : Number {
			return _advertiserCompetitionScale;
		} 
		
		public function set advertiserCompetitionScale(advertiserCompetitionScale:Number) : void {
			_advertiserCompetitionScale = advertiserCompetitionScale;
		}
		
		public function get generatedKeyword() : String {
			return _generatedKeyword;
		} 
		
		public function set generatedKeyword(generatedKeyword:String) : void {
			_generatedKeyword = generatedKeyword;
		}
		
		public function get searchVolumeScale() : Number {
			return _searchVolumeScale;
		} 
		
		public function set searchVolumeScale(searchVolumeScale:Number) : void {
			_searchVolumeScale = searchVolumeScale;
		}
				
          
		

	}
}