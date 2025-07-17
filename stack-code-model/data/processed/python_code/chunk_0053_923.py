/**
 *        __       __               __
 *   ____/ /_ ____/ /______ _ ___  / /_
 *  / __  / / ___/ __/ ___/ / __ `/ __/
 * / /_/ / (__  ) / / /  / / /_/ / /
 * \__,_/_/____/_/ /_/  /_/\__, /_/
 *                           / /
 *                           \/
 * http://distriqt.com
 *
 * @author 		Michael (https://github.com/marchbold)
 * @created		15/6/21
 */
package com.apm.data.packages
{
	public class PackageParameter
	{
		////////////////////////////////////////////////////////
		//  CONSTANTS
		//
		
		private static const TAG:String = "PackageParameter";
		
		
		////////////////////////////////////////////////////////
		//  VARIABLES
		//
		
		public var name:String;
		public var required:Boolean = false;
		public var defaultValue:String = "";
		
		private var _singleLineOutput:Boolean = false;
		
		
		////////////////////////////////////////////////////////
		//  FUNCTIONALITY
		//
		
		public function PackageParameter( name:String = "", required:Boolean = false )
		{
			this.name = name;
			this.required = required;
		}
		
		
		public function toString():String
		{
			return name;
		}
		
		
		public function toObject( forceObjectOutput:Boolean=false ):Object
		{
			if (_singleLineOutput && !forceObjectOutput)
			{
				if (required)
					return name + ":required";
				else
					return name;
			}
			else
			{
				return {
					name:     name,
					required: required,
					defaultValue: defaultValue
				};
			}
		}
		
		
		public function fromObject( data:Object ):PackageParameter
		{
			if (data != null)
			{
				if (data is String)
				{
					// single line format paramName:required
					this._singleLineOutput = true;
					if (String( data ).indexOf( ":" ) > 0)
					{
						// "parameterName:required"
						var vals:Array = String( data ).split( ":" );
						this.name = vals[ 0 ];
						this.required = (vals.length > 1 && vals[ 1 ] == "required");
					}
					else
					{
						// "parameterName"
						this.name = String( data );
					}
				}
				else
				{
					if (data.hasOwnProperty( "name" )) this.name = data[ "name" ];
					if (data.hasOwnProperty( "required" )) this.required = data[ "required" ];
					if (data.hasOwnProperty( "defaultValue" )) this.defaultValue = data[ "defaultValue" ];
				}
			}
			return this;
		}
		
	}
	
}