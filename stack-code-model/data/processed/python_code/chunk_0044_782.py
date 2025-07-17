package devoron.sdk.aslc.core.utils.compare
{
	
	/**
	 * MethodNodeCompareResult
	 * @author Devoron
	 */
	public class MethodNodeCompareResult implements IScriptNodeCompareResult
	{
		public var result:Boolean;
		
		private var _returnTypesEquals:Boolean;
		private var _staticEquals:Boolean;
		private var _visibilityEquals:Boolean;
		//public var paramsEquals:Boolean = compareParams(newMethod.parameters, oldMethod.parameters);
		private var _paramsEquals:Boolean;
		private var _statementsEquals:Boolean;
		
		//public static var LANGUAGE_VERSION:String = "ActionScript3.0";
		
		public function MethodNodeCompareResult()
		{
		
		}
		
		public function get returnTypesEquals():Boolean
		{
			return _returnTypesEquals;
		}
		
		public function set returnTypesEquals(b:Boolean):void
		{
			if (!b)
				result = false;
			_returnTypesEquals = b;
		}
		
		public function get staticEquals():Boolean
		{
			return _staticEquals;
		}
		
		public function set staticEquals(b:Boolean):void
		{
			if (!b)
				result = false;
			_staticEquals = b;
		}
		
		public function get visibilityEquals():Boolean
		{
			return _visibilityEquals;
		}
		
		public function set visibilityEquals(b:Boolean):void
		{
			if (!b)
				result = false;
			_visibilityEquals = b;
		}
		
		public function get paramsEquals():Boolean
		{
			return _paramsEquals;
		}
		
		public function set paramsEquals(b:Boolean):void
		{
			if (!b)
				result = false;
			_paramsEquals = b;
		}
		
		public function get statementsEquals():Boolean
		{
			return _statementsEquals;
		}
		
		public function set statementsEquals(b:Boolean):void
		{
			if (!b)
				result = false;
			_statementsEquals = b;
		}
	
	}

}