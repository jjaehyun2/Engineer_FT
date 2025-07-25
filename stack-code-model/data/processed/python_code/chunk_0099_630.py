﻿/**
 * This code is part of the Bumpslide Library maintained by David Knape
 * Fork me at http://github.com/tkdave/bumpslide_as3
 * 
 * Copyright (c) 2010 by Bumpslide, Inc. 
 * http://www.bumpslide.com/
 *
 * This code is released under the open-source MIT license.
 * See LICENSE.txt for full license terms.
 * More info at http://www.opensource.org/licenses/mit-license.php
 */

package com.bumpslide.util {
	/**	 * String Utility functions	 * 	 * @author David Knape	 */	public class StringUtil {
		/**		 * Make text fit by cutting it off and adding ellipsis to the end		 */		static public function abbreviate( origStr:String, maxLength:Number = 50, moreIndicator:String = '...', splitChar:String = ' '):String {						if(origStr == null) return "";						if(origStr.length < maxLength) {				return origStr;			}					var str:String = '';			var n:int = 0;			var pieces:Array = origStr.split(splitChar);	
			// split string into pieces			var charCount:int = pieces[n].length;			
			// running total of char count					// put pieces back together as long as the charCount doesn't exceed the max length			while(charCount < maxLength && n < pieces.length) {				str += pieces[n] + splitChar;					
				// put the space back as we add the piece to our new string				charCount += pieces[++n].length + splitChar.length ;	    // increase the character count			}					// do extra stuff if we now have an abbreviated string			if(n < pieces.length) {				// remove any chars from the end that are not letters or numbers				var badChars:Array = ['-', '—', ',', '.', ' ', ':', '?', '!', ';', "\n", ' ', String.fromCharCode(10), String.fromCharCode(13)];				while( badChars.indexOf(str.charAt(str.length - 1)) != -1 ) {					// trace("[StringUtil.abbreviate] Chopping bad char before ellipsis: '"+str.charAt(str.length-1)+"'");					str = str.slice(0, -1);				}				// add an ellipsis to the end				str = trim(str) + moreIndicator;			}						// first word is longer than max length...			if(n == 0) {				str = origStr.slice(0, maxLength) + moreIndicator;			}						return str;		}
		/**		 *  Removes whitespace from ends of string		 */					public static function trim(input:String):String {			return StringUtil.ltrim(StringUtil.rtrim(input));		}
		/**		 *  Removes whitespace from the front of a string		 */			public static function ltrim(s:String):String {			var len:Number = s.length;			for(var i:Number = 0;i < len; i++) if(s.charCodeAt(i) > 32) return s.substring(i);			return "";		}
		/**		 *  Removes whitespace from the end of a string		 */			public static function rtrim(s:String):String {			var len:Number = s.length;			for(var i:Number = len;i > 0; i--) if(s.charCodeAt(i - 1) > 32) return s.substring(0, i);			return "";		}		/**		 * Format a number as a string.		 */
		public static function formatNumber(num:Number, decimals:uint = 0, thousandsSeparator:String = ",", decimalSeparator:String = "."):String {			if(isNaN(num)) return "NaN";			if(num == Number.POSITIVE_INFINITY) return "Infinity";			if(num == Number.NEGATIVE_INFINITY) return "-Infinity";			// First Round the number to the right decimal places			var factor:int = Math.pow(10, decimals);			num = Math.round(num * factor) / factor;			//	convert num to string for formatting			//  we split it at the decimal point first			var pieces:Array = num.toString().split('.');			var before:Array = pieces[0].split('');  			var after:String = pieces[1] != undefined ? pieces[1] : '';						// pad with zeroes after the decimal point				while(after.length < decimals) { 				after += '0'; 			}			// add thousands separator						var len:int = before.length;						var before_formatted:Array = [];						for( var i:uint = 0;i < len; ++i) {				if(i % 3 == 0 && i != 0) before_formatted.unshift(thousandsSeparator);				before_formatted.unshift(before[len - 1 - i]);			}						var result:String = before_formatted.join('');			if(decimals > 0) { 				result += decimalSeparator + after;			}			return result;		} 	}}