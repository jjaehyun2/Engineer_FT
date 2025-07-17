////////////////////////////////////////////////////////////////////////////////
//
// © 2016 BlooDHounD
//
////////////////////////////////////////////////////////////////////////////////

package avmplus {

	import flash.errors.IllegalOperationError;
	import flash.utils.getQualifiedClassName;

	[ExcludeClass]
	/**
	 * Object describer.
	 * 
	 * @author					BlooDHounD
	 * @version					2.0
	 * @playerversion			Flash 10.1
	 * @langversion				3.0
	 */
	public final class DescribeType {

		public static const HIDE_NSURI_METHODS:uint =	0x0001; // avmplus.HIDE_NSURI_METHODS;
		public static const INCLUDE_BASES:uint =		0x0002; // avmplus.INCLUDE_BASES;
		public static const INCLUDE_INTERFACES:uint =	0x0004; // avmplus.INCLUDE_INTERFACES;
		public static const INCLUDE_VARIABLES:uint =	0x0008; // avmplus.INCLUDE_VARIABLES;
		public static const INCLUDE_ACCESSORS:uint =	0x0010; // avmplus.INCLUDE_ACCESSORS;
		public static const INCLUDE_METHODS:uint =		0x0020; // avmplus.INCLUDE_METHODS;
		public static const INCLUDE_METADATA:uint =		0x0040; // avmplus.INCLUDE_METADATA;
		public static const INCLUDE_CONSTRUCTOR:uint =	0x0080; // avmplus.INCLUDE_CONSTRUCTOR;
		public static const INCLUDE_TRAITS:uint =		0x0100; // avmplus.INCLUDE_TRAITS;
		public static const USE_ITRAITS:uint =			0x0200; // avmplus.USE_ITRAITS;
		public static const HIDE_OBJECT:uint =			0x0400; // avmplus.HIDE_OBJECT;

		public static const FLASH10_FLAGS:uint =		INCLUDE_BASES | // avmplus.FLASH10_FLAGS
														INCLUDE_INTERFACES |
														INCLUDE_VARIABLES |
														INCLUDE_ACCESSORS |
														INCLUDE_METHODS |
														INCLUDE_METADATA |
														INCLUDE_CONSTRUCTOR |
														INCLUDE_TRAITS |
														HIDE_NSURI_METHODS |
														HIDE_OBJECT;

		/**
		 * Produces an <code>Object</code> that describes the ActionScript object named
		 * as the parameter of the method. This method implements the programming concept
		 * of reflection for the ActionScript language. 
		 * 
		 * @param	o		The object for which a type description is desired.
		 * 					Any ActionScript value may be passed to this method
		 * 					including all available ActionScript types, object
		 * 					instances, primitive types such as uint, and
		 * 					class objects.
		 * 
		 * @param	flags	Filtering properties.
		 */
		public static const get:Function = ( function():Function {
			var result:Function;
			try {
				result = describeTypeJSON;
			} catch ( e:Error ) {
				result = function(o:*, flags:int):Object {
					throw new IllegalOperationError( e.message, e.errorID );
				}
			}
			return result;
		}() );
		
		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------
		
		/**
		 * @private
		 * Constructor
		 */
		public function DescribeType() {
			Error.throwError( ArgumentError, 2012, flash.utils.getQualifiedClassName( this ) );
		}
		
	}

}