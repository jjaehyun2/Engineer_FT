package com.macys.marketing.sema.vo.tools
{
	
	import com.adobe.cairngorm.vo.ValueObject;
	
	import mx.collections.ArrayCollection;

	[Bindable]
	public class GenerateKeywordsVO implements ValueObject
	{
		private var _seedKeyword : String;
		private var _matchType : String;
		private var _negativeFlag : Boolean;
		private var _useSynonym : Boolean;
			
		private var _relatedKeywords : ArrayCollection;
		private var _alsoToConsiderKeywords : ArrayCollection;
			
		
		public function get seedKeyword() : String {
			return _seedKeyword;
		} 
		
		public function set seedKeyword(seedKeyword:String) : void {
			_seedKeyword = seedKeyword;
		}

		public function get matchType() : String {
			return _matchType;
		} 
		
		public function set matchType(matchType:String) : void {
			_matchType = matchType;
		}

		public function get negativeFlag() : Boolean {
			return _negativeFlag;
		} 
		
		public function set negativeFlag(negativeFlag:Boolean) : void {
			_negativeFlag = negativeFlag;
		}
		
		public function get useSynonym() : Boolean {
			return _useSynonym;
		} 
		
		public function set useSynonym(useSynonym:Boolean) : void {
			_useSynonym = useSynonym;
		}
		
		
		public function get relatedKeywords() : ArrayCollection {
			return _relatedKeywords;
		} 
		
		public function set relatedKeywords(relatedKeywords:ArrayCollection) : void {
			_relatedKeywords = relatedKeywords;
		}
		
		public function get alsoToConsiderKeywords() : ArrayCollection {
			return _alsoToConsiderKeywords;
		} 
		
		public function set alsoToConsiderKeywords(alsoToConsiderKeywords:ArrayCollection) : void {
			_alsoToConsiderKeywords = alsoToConsiderKeywords;
		}

	}
}