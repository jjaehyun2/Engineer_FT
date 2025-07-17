/*
 Copyright aswing.org, see the LICENCE.txt.
*/
package devoron.aswing3d.util
{
import flash.utils.getDefinitionByName;
import flash.utils.getQualifiedClassName;
import flash.net.registerClassAlias;
import flash.utils.ByteArray;


public class ObjectUtils
{
	/**
	 * Deep clone object using thiswind@gmail.com 's solution
	 */
	public static function baseClone(source:*):*{
		var typeName:String = getQualifiedClassName(source);
        var packageName:String = typeName.split("::")[1];
        var type:Class = Class(getDefinitionByName(typeName));

        registerClassAlias(packageName, type);
        
        var copier:ByteArray = new ByteArray();
        copier.writeObject(source);
        copier.position = 0;
        return copier.readObject();
	}
	
	public static function cloneObject(source:Object, destination:Object = null):Object {
		var dest:Object = destination == null ? new Object() : destination;
		for (var prop:String in source) {
				if (typeof(source[prop]) == "object") {
					if ( ("clone" in source[prop]) ) dest[prop] = source[prop].clone();
					else dest[prop] = cloneObject(source[prop]);
				}
				else {
					try{
					dest[prop] = source[prop];
					}
					catch (e:Error) {
					}
				}
				/*if ( ("clone" in source[prop]) ) dest[prop] = source[prop].clone();
				else dest[prop] = source[prop];*/
		}
		return dest;
	}
	
	public static function isEmpty(obj:Object):Boolean {
		for (var prop:String in obj) {
			return false;
		}
		return true;
	}
	
	/**
	 * Checks wherever passed-in value is <code>String</code>.
	 */
	public static function isString(value:*):Boolean {
		return ( typeof(value) == "string" || value is String );
	}
	
	/**
	 * Checks wherever passed-in value is <code>Number</code>.
	 */
	public static function isNumber(value:*):Boolean {
		return ( typeof(value) == "number" || value is Number );
	}

	/**
	 * Checks wherever passed-in value is <code>Boolean</code>.
	 */
	public static function isBoolean(value:*):Boolean {
		return ( typeof(value) == "boolean" || value is Boolean );
	}

	/**
	 * Checks wherever passed-in value is <code>Function</code>.
	 */
	public static function isFunction(value:*):Boolean {
		return ( typeof(value) == "function" || value is Function );
	}

	
}
}