package com.vini123.utils
{
	import flash.utils.ByteArray;
	

	public class StringTool
	{
		
		public static const REGEX_UNSAFE_CHARS:String = "\\-^[]";
		
		public static const TRIM_RIGHT_REGEX:RegExp = /[\s]+$/g;
		
		public function StringTool()
		{
		}
		
		/**
		 *       Removes whitespace from the front of the specified string.
		 *
		 *       @param value The String whose beginning whitespace will will be removed.
		 *
		 *       @returns A String with whitespace removed from the begining
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function ltrim(value:String):String {
			var out:String = "";
			
			if(value) {
				out = value.replace(/^\s+/, "");
			}
			
			return out;
		}
		
		
		/**
		 *       Removes whitespace from the end of the specified string.
		 *
		 *       @param value The String whose ending whitespace will will be removed.
		 *
		 *       @returns A String with whitespace removed from the end
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function rtrim(value:String):String {
			var out:String = "";
			
			if(value) {
				out = value.replace(/\s+$/, "");
			}
			
			return out;
		}
		
		/**
		 *       Removes whitespace from the front and the end of the specified
		 *       string.
		 *
		 *       @param value The String whose beginning and ending whitespace will
		 *       will be removed.
		 *
		 *       @returns A String with whitespace removed from the begining and end
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function trim(value:String):String {
			var out:String = "";
			
			if(value) {
				out = value.replace(/^\s+|\s+$/g, "");
			}
			
			return out;
		}
		
		/**
		 * Extreme Trim: remove whitespace, line feeds, carriage returns from string
		 */
		public static function xtrim(str:String = null):String {
			str = (!str) ? "" : str;
			
			var o:String = new String();
			var TAB:Number = 9;
			var LINEFEED:Number = 10;
			var CARRIAGE:Number = 13;
			var SPACE:Number = 32;
			
			for(var i:int = 0; i < str.length; i++) {
				if(str.charCodeAt(i) != SPACE && str.charCodeAt(i) != CARRIAGE && str.charCodeAt(i) != LINEFEED && str.charCodeAt(i) != TAB) {
					o += str.charAt(i);
				}
			}
			
			return o;
		}
		
		/**
		 * Search for key in string.
		 */
		public static function search(str:String, key:String, caseSensitive:Boolean = true):Boolean
		{
			if (!caseSensitive)
			{
				str = str.toUpperCase();
				key = key.toUpperCase();
			}
			return (str.indexOf(key) <= -1) ? false : true;
		}
		
		
		/**
		 * Returns the truncated string with an appended ellipsis (...) if the length of <code>str</code> is greater than <code>len</code>.
		 * If the length of <code>str</code> is less than or equal to <code>len</code>, the method returns <code>str</code> unaltered.
		 * @param str the string to truncate
		 * @param len the length to limit the string to
		 * @return
		 */
		public static function truncate(str:String, len:int):String
		{
			// return the string if str is null, empty, or the length of str is less than or equal to len
			if (!str || str.length <= len)
				return str;
			
			// short str to len
			str = str.substr(0, len);
			
			// trim the right side of whitespace
			str = str.replace(StringTool.TRIM_RIGHT_REGEX, "");
			
			// append the ellipsis
			return str + "...";
		}
		
		/**
		 * Returns a String truncated to a specified length with optional suffix.
		 * @param value Input String
		 * @param length Length the String should be shortened to
		 * @param suffix (optional, default="...") String to append to the end of the truncated String
		 * @returns String String truncated to a specified length with optional suffix
		 */
		public static function truncate2(value:String, length:uint, suffix:String = "..."):String {
			var out:String = "";
			var l:uint = length;
			
			if(value) {
				l -= suffix.length;
				
				var trunc:String = value;
				
				if(trunc.length > l) {
					trunc = trunc.substr(0, l);
					
					if(/[^\s]/.test(value.charAt(l))) {
						trunc = rtrim(trunc.replace(/\w+$|\s+$/, ""));
					}
					
					trunc += suffix;
				}
				
				out = trunc;
			}
			
			return out;
		}
		
		
		/**
		 * Determines the number of words in a String.
		 * @param value Input String
		 * @returns Number of words in a String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function wordCount(value:String):uint {
			var out:uint = 0;
			
			if(value) {
				out = value.match(/\b\w+\b/g).length;
			}
			
			return out;
		}
		
		
		/** 双引号转成单引号
		 * Convert double quotes to single quotes.
		 */
		public static function toSingleQuote(str:String):String
		{
			var sq:String = "'";
			var dq:String = String.fromCharCode(34);
			return str.split(dq).join(sq);
		}
		
		/**单引号转成双引号
		 * Convert single quotes to double quotes.
		 */
		public static function toDoubleQuote(str:String):String
		{
			var sq:String = "'";
			var dq:String = String.fromCharCode(34);
			return str.split(sq).join(dq);
		}
		
		
		/**
		 * Remove all formatting and return cleaned numbers from string.
		 * @example <listing version="3.0">
		 *      StringUtils.toNumeric("123-123-1234"); // returns 1221231234
		 * </listing>
		 */
		public static function toNumeric(str:String):String
		{
			var len:Number = str.length;
			var result:String = "";
			for (var i:int = 0; i < len; i++)
			{
				var code:Number = str.charCodeAt(i);
				if (code >= 48 && code <= 57)
				{
					result += str.substr(i, 1);
				}
			}
			return result;
		}
		
		/**大写字母
		 * Transforms source String to per word capitalization.
		 */
		public static function toTitleCase(str:String):String
		{
			var lstr:String = str.toLowerCase();
			return lstr.replace(/\b([a-z])/g, function($0:*):*
			{
				return $0.toUpperCase();
			});
		}
		
		
		/**
		 *       Does a case insensitive compare or two strings and returns true if
		 *       they are equal.
		 *
		 *       @param s1 The first string to compare.
		 *
		 *       @param s2 The second string to compare.
		 *
		 *       @returns A boolean value indicating whether the strings' values are
		 *       equal in a case sensitive compare.
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function stringsAreEqual(s1:String, s2:String,caseSensitive:Boolean):Boolean
		{
			if (caseSensitive)
			{
				return (s1 == s2);
			}
			else
			{
				return (s1.toUpperCase() == s2.toUpperCase());
			}
		}
		
		/**
		 *       Specifies whether the specified string is either non-null, or contains
		 *       characters (i.e. length is greater that 0)
		 *
		 *       @param s The string which is being checked for a value
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function stringHasValue(s:String):Boolean
		{
			return (s != null && s.length > 0);
		}
		
		/**
		 * Sanitize <code>null</code> strings for display purposes.
		 */
		public static function sanitizeNull(str:String):String
		{
			return (str == null || str == "null") ? "" : str;
		}
		
		
		/**反转
		 * Returns the specified String in reverse word order.
		 * @param value String that will be reversed
		 * @returns Output String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function reverseWords(value:String):String {
			var out:String = "";
			
			if(value) {
				out = value.split(/\s+/).reverse().join("");
			}
			
			return out;
		}
		
		/**
		 * Returns the specified String in reverse character order.
		 * @param value String that will be reversed
		 * @returns Output String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function reverse(value:String):String {
			var out:String = "";
			
			if(value) {
				out = value.split("").reverse().join("");
			}
			
			return out;
		}
		
		
		/**
		 *       Replaces all instances of the replace string in the input string
		 *       with the replaceWith string.
		 *
		 *       @param input The string that instances of replace string will be
		 *       replaces with removeWith string.
		 *
		 *       @param replace The string that will be replaced by instances of
		 *       the replaceWith string.
		 *
		 *       @param replaceWith The string that will replace instances of replace
		 *       string.
		 *
		 *       @returns A new String with the replace string replaced with the
		 *       replaceWith string.
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function replace(input:String, replace:String, replaceWith:String):String
		{
			return input.split(replace).join(replaceWith);
		}
		
		
		/**
		 * Remove tabs from string.
		 */
		public static function removeTabs(str:String):String
		{
			return replace(str, "  ", "");
		}
		
		/**
		 * Remove spaces from string.
		 * @param str (String)
		 * @return String
		 */
		public static function removeSpaces(str:String):String
		{
			return replace(str, " ", "");
		}
		
		/**
		 * Removes extraneous whitespace (extra spaces, tabs, line breaks, etc) from the specified String.
		 * @param value String whose extraneous whitespace will be removed
		 * @returns Output String
		 */
		public static function removeExtraWhitespace(value:String):String {
			var out:String = "";
			
			if(value) {
				var str:String = trim(value);
				
				out = str.replace(/\s+/g, " ");
			}
			
			return out;
		}
		
		/**
		 *       Removes all instances of the remove string in the input string.
		 *
		 *       @param input The string that will be checked for instances of remove
		 *       string
		 *
		 *       @param remove The string that will be removed from the input string.
		 *
		 *       @returns A String with the remove string removed.
		 *
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function remove(input:String, remove:String):String
		{
			return replace(input, remove, "");
		}
		
		/**
		 * Generate a set of random Special and Number characters.
		 */
		public static function randomSpecialCharacters(amount:Number):String
		{
			var str:String = "";
			for (var i:int = 0; i < amount; i++)
				str += String.fromCharCode(Math.round(Math.random() * (64 - 33)) + 33);
			return str;
		}
		
		
		/**
		 * Get random sentence.
		 * @param maxLength Max chars
		 * @param minLength Min chars
		 * @return Random sentence
		 * @author Vaclav Vancura (http://vancura.org, http://twitter.com/vancura)
		 */
		public static function randomSequence(maxLength:uint = 50, minLength:uint = 10):String {
			return randomCharacters(NumberTool.randomIntegerWithinRange(minLength, maxLength), "            abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789");
		}
		
		/**
		 * Generate a set of random Number characters.
		 */
		public static function randomNumberString(amount:Number):String
		{
			var str:String = "";
			for (var i:int = 0; i < amount; i++)
				str += String.fromCharCode(Math.round(Math.random() * (57 - 48)) + 48);
			return str;
		}
		
		/**
		 * Generate a set of random LowerCase characters.
		 */
		public static function randomLowercaseCharacters(amount:Number):String
		{
			var str:String = "";
			for (var i:int = 0; i < amount; i++)
				str += String.fromCharCode(Math.round(Math.random() * (122 - 97)) + 97);
			return str;
		}
		
		/**
		 * Generate a random String.
		 * @param amount String length (default 10)
		 * @param charSet Chars used (default "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
		 * @return Random String
		 */
		public static function randomCharacters(amount:Number, charSet:String = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):String {
			var alphabet:Array = charSet.split("");
			var alphabetLength:int = alphabet.length;
			var randomLetters:String = "";
			
			for(var j:uint = 0; j < amount; j++) {
				var r:Number = Math.random() * alphabetLength;
				var s:int = Math.floor(r);
				randomLetters += alphabet[s];
			}
			
			return randomLetters;
		}
		
		
		/**
		 * Pads value with specified padChar character to a specified length from the right.
		 * @param value Input String
		 * @param padChar Character for pad
		 * @param length Length to pad to
		 * @returns Padded String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function padRight(value:String, padChar:String, length:uint):String {
			var s:String = value;
			
			while(s.length < length) {
				s += padChar;
			}
			
			return s;
		}
		
		/**
		 * Pads value with specified padChar character to a specified length from the left.
		 * @param value Input String
		 * @param padChar Character for pad
		 * @param length Length to pad to
		 * @returns Padded String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function padLeft(value:String, padChar:String, length:uint):String {
			var s:String = value;
			
			while(s.length < length) {
				s = padChar + s;
			}
			
			return s;
		}
		
		
		/**
		 * Encode HTML.
		 */
		public static function htmlEncode(s:String):String
		{
			s = replace(s, "&", "&amp;");
			
			s = replace(s, " ", "&nbsp;");
			s = replace(s, "<", "&lt;");
			s = replace(s, ">", "&gt;");
			s = replace(s, "�", '&trade;');
			s = replace(s, "�", '&reg;');
			s = replace(s, "�", '&copy;');
			s = replace(s, "�", "&euro;");
			s = replace(s, "�", "&pound;");
			s = replace(s, "�", "&mdash;");
			s = replace(s, "�", "&ndash;");
			s = replace(s, "�", "&hellip;");
			s = replace(s, "�", "&dagger;");
			s = replace(s, "�", "&middot;");
			s = replace(s, "�", "&micro;");
			s = replace(s, "�", "&laquo;");
			s = replace(s, "�", "&raquo;");
			s = replace(s, "�", "&bull;");
			s = replace(s, "�", "&deg;");
			s = replace(s, '"', "&quot;");
			return s;
		}
		
		
		/**
		 * Decode HTML.
		 */
		public static function htmlDecode(s:String):String
		{
			s = replace(s, "&nbsp;", " ");
			s = replace(s, "&amp;", "&");
			s = replace(s, "&lt;", "<");
			s = replace(s, "&gt;", ">");
			s = replace(s, "&trade;", '�');
			s = replace(s, "&reg;", "�");
			s = replace(s, "&copy;", "�");
			s = replace(s, "&euro;", "�");
			s = replace(s, "&pound;", "�");
			s = replace(s, "&mdash;", "�");
			s = replace(s, "&ndash;", "�");
			s = replace(s, "&hellip;", '�');
			s = replace(s, "&dagger;", "�");
			s = replace(s, "&middot;", '�');
			s = replace(s, "&micro;", "�");
			s = replace(s, "&laquo;", "�");
			s = replace(s, "&raquo;", "�");
			s = replace(s, "&bull;", "�");
			s = replace(s, "&deg;", "�");
			s = replace(s, "&ldquo", '"');
			s = replace(s, "&rsquo;", "'");
			s = replace(s, "&rdquo;", '"');
			s = replace(s, "&quot;", '"');
			return s;
		}
		
		public static  function getLettersFromString(source:String):String
		{
			var pattern:RegExp = /[^A-Z^a-z]/g;
			return source.replace(pattern, '');
		}
		
		/**
		 * Capitalize the first character in the string.
		 */
		public static function firstToUpper(str:String):String
		{
			return str.charAt(0).toUpperCase() + str.substr(1);
		}
		
		
		/**
		 * Does a case insensitive compare or two strings and returns true if they are equal.
		 */
		public static function equals(s1:String, s2:String, caseSensitive:Boolean = false):Boolean
		{
			return (caseSensitive) ? (s1 == s2) : (s1.toUpperCase() == s2.toUpperCase());
		}
		
		
		/**
		 *       Determines whether the specified string ends with the specified suffix.
		 *       @param input The string that the suffix will be checked against.
		 *       @param suffix The suffix that will be tested against the string.
		 *       @returns True if the string ends with the suffix, false if it does not.
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function endsWith(input:String, suffix:String):Boolean {
			return (suffix == input.substring(input.length - suffix.length));
		}
		
		
		/**
		 * Returns everything after the first occurrence of begin and before the first occurrence of end in String.
		 * @param value Input String
		 * @param start Character or sub-string to use as the start index
		 * @param end Character or sub-string to use as the end index
		 * @returns Everything after the first occurrence of begin and before the first occurrence of end in String.
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function between(value:String, start:String, end:String):String {
			var out:String = "";
			
			if(value) {
				var startIdx:int = value.indexOf(start);
				
				if(startIdx != -1) {
					startIdx += start.length; // RM: should we support multiple chars? (or ++startIdx);
					
					var endIdx:int = value.indexOf(end, startIdx);
					
					if(endIdx != -1) {
						out = value.substr(startIdx, endIdx - startIdx);
					}
				}
			}
			
			return out;
		}
		
		/**
		 *       Determines whether the specified string begins with the specified prefix.
		 *       @param input The string that the prefix will be checked against.
		 *       @param prefix The prefix that will be tested against the string.
		 *       @returns True if the string starts with the prefix, false if it does not.
		 *       @langversion ActionScript 3.0
		 *       @playerversion Flash 9.0
		 *       @tiptext
		 */
		public static function beginsWith(input:String, prefix:String):Boolean {
			return (prefix == input.substring(0, prefix.length));
		}
		
		
		/**
		 * Returns everything before the last occurrence of the provided character in the String.
		 * @param value Input String
		 * @param ch Character or sub-string
		 * @returns Everything before the last occurrence of the provided character in the String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function beforeLast(value:String, ch:String):String {
			var out:String = "";
			
			if(value) {
				var idx:int = value.lastIndexOf(ch);
				
				if(idx != -1) {
					out = value.substr(0, idx);
				}
			}
			
			return out;
		}
		
		
		/**
		 * Returns everything before the first occurrence of the provided character in the String.
		 * @param value Input String
		 * @param ch Character or sub-string
		 * @returns Everything before the first occurence of the provided character in the String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function beforeFirst(value:String, ch:String):String {
			var out:String = "";
			
			if(value) {
				var idx:int = value.indexOf(ch);
				
				if(idx != -1) {
					out = value.substr(0, idx);
				}
			}
			
			return out;
		}
		
		
		/**
		 * Returns everything after the last occurrence of the provided character in value.
		 * @param value Input String
		 * @param ch Character or sub-string
		 * @return Output String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function afterLast(value:String, ch:String):String {
			var out:String = "";
			
			if(value) {
				var idx:int = value.lastIndexOf(ch);
				
				if(idx != -1) {
					idx += ch.length;
					out = value.substr(idx);
				}
			}
			
			return out;
		}
		
		
		/**
		 * Returns everything after the first occurrence of the provided character in the String.
		 * @param value Input String
		 * @param ch Character or sub-string
		 * @returns Output String
		 * @author Aaron Clinger
		 * @author Shane McCartney
		 * @author David Nelson
		 */
		public static function afterFirst(value:String, ch:String):String {
			var out:String = "";
			
			if(value) {
				var idx:int = value.indexOf(ch);
				
				if(idx != -1) {
					idx += ch.length;
					out = value.substr(idx);
				}
			}
			return out;
		}
		
		/**
		 *得到字符串长度 
		 */		
		public	static function GetStringLength(thisString : String):uint{
			var thisStringBytsLength:ByteArray = new ByteArray();
			thisStringBytsLength.writeMultiByte(thisString,"gb2312");
			return thisStringBytsLength.length;
		}
		
		/**
		 *裁剪字符串 
		 * @param str
		 * @param length
		 * @param endStr
		 * @return 
		 * 
		 */		
		public static function splickNickName(str:String, length:uint = 15, endStr:String = "..."):String
		{
			if(!str){
				return null;
			}
			var newNickName:String = "";
			if (str.length > length)
			{
				newNickName = str.substr(0, str.length-3) + endStr;
			}
			else
			{
				newNickName = str;
			}
			return newNickName;
		}
		
		public static function formatThousands(value:Number):String {
			var numStr:String = Math.abs(value).toString();
			var numArr:Array = new String(numStr).split(".");
			
			var numLen:int = String(numArr[0]).length;
			
			if (numLen > 3) {
				var numSep:int = int(Math.floor(numLen / 3));
				
				if ((numLen % 3) == 0) {
					numSep--;
				}
				
				var b:int = numLen;
				var a:int = b - 3;
				
				var arr:Array = [];
				for (var i:int = 0; i <= numSep; i++) {
					arr[i] = numArr[0].slice(a, b);
					a = int(Math.max(a - 3, 0));
					b = int(Math.max(b - 3, 1));
				}
				arr.reverse();
				numArr[0] = arr.join(",");
			}
			numStr = numArr.join(".");
			return numStr.toString();
		}
		
		public static function formatLt(value:String):String{
			var exp:RegExp = /&/g;
			value = value.replace(exp, "&amp;");
			exp = /</g;
			value = value.replace(exp, "&lt;");
			exp = />/g;
			value = value.replace(exp, "&gt;");
			return value;
		}
		
		public static function formatReLt(value:String):String{
			var exp:RegExp = /&lt;/g;
			value = value.replace(exp, "<");
			exp = /&gt;/g;
			value = value.replace(exp, ">");
			exp = /&amp;/g;
			value = value.replace(exp, "&");
			exp = /&quot;/g;
			value = value.replace(exp, "\"");
			exp = new RegExp("<br>", "g");
			value = value.replace(exp, "\n");
			exp = new RegExp("<br/>", "g");
			value = value.replace(exp, "\n");
			return value;
		}
		
		public static function serializeRandom(temp:Array):Array{
			var cc:Array = [];
			while(temp.length){
				var r:uint = Math.random() * temp.length;
				cc.push(temp[r]);
				temp.splice(r, 1);
			}
			temp.length = 0;
			temp = null;
			return cc;
		}
		
		public static function transHttpUrl(http:String):String{
			var p:RegExp = new RegExp("^[www]", "g");
			var result:String;
			if(p.test(http)){
				result = "http://" + http;
			}else result = http;
			return result;
		}
		
		/**
		 * 
		 * 将str转换成html 
		 * @param value
		 * @return 
		 * 
		 */		
		public static function transHtmlStr(value:String):String
		{
			var reg:RegExp = new RegExp("(((www\\.)|(http://)|(https://))[^\\s\\(\\)]+)");
			var index:int = 0;
			var str:String = "";
			var matchStr:String = "";
			
			while(reg.test(value))
			{
				index = value.search(reg);
				str += value.substr(0 , index);
				matchStr = value.match(reg)[0];
				str += Sprintf("<a color='#0099ff' target='_blank' href='%s'>%s</a>", matchStr, matchStr);
				value = value.substr(index + matchStr.length);
			}
			return str + value;
		}
	}
}