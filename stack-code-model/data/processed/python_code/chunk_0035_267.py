//------------------------------------------------------------------------------
//
//   Anthony Henderson   Copyright 2012  
//   All rights reserved. 
//
//------------------------------------------------------------------------------

/**
 * File: StringUtils.as
 * @Author: Tony Henderson
 * Purpose:

 */

package ahhenderson.core.util
{
	import flash.utils.Dictionary;
	
	import mx.utils.UIDUtil;

	public class StringUtil
	{
		
		public static function generateUniqueConstant(constantName:String):String{
			
			return substitute("{0}_{1}", constantName, GuidUtil.createUID());
			
		}

		public static function objectPropertyToString(property:String, item:Object ):String {
			
			var result:String;
			
			if ( property != null && item && item.hasOwnProperty( property )) {
				result = item[ property ];
				
				if ( result is String ) {
					return result as String;
				}
				
				if(result)
					return result.toString();
				
			} else if ( item is String ) {
				return item as String;
			} else if ( item ) {
				return item.toString();
			}
			return "";
		}
		
		
		/**
		 * Replace all of the parameters in the str argument. Placeholders are defined like {0},{1},etc
		 * @param str
		 * @param rest
		 * @return
		 */
		public static function substitute(str:String, ... rest):String {
			if (str == null) {
				return '';
			}
			
			var len:uint = rest.length;
			var args:Array;
			if (len == 1 && rest[0] is Array) {
				args = rest[0];
				len = args.length;
			} else {
				args = rest;
			}
			
			for (var i:int = 0; i < len; i++) {
				var item:* = args[i];
				str = str.split('{' + i.toString() + '}').join((item != null) ? item.toString() : "[null]");
			}
			
			return str;
		}
		
		public static function getTimestampUID():String
		{		
			return UIDUtil.createUID().toString() + "_" + DateUtil.toRFC802(new Date());
		}
		
		/**
		 *	Replaces multiple values in a string
		 *
		 *	@param targetString The string data in which values will be replaced.
		 *
		 *	@param valuesDict The dictionary object containing the values to be replaced (key) and replacment values (value)
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function replaceMultipleValues(targetString:String, valuesDict:Dictionary):String
		{
			if(!targetString || !valuesDict)
				return null;
			
			for(var k:String in valuesDict)
			{
				var key:String = k;
				var value:String = valuesDict[k];

				targetString = targetString.replace(key, value);
			}

			return targetString;
		}

		
		/**
		 *	Replaces a specified character in a string with a new values.
		 *
		 *	@param targetString The string data in which characters will be replaced.
		 *
		 *	@param charToMatch The character to match in the target string.
		 *
		 *  @param replaceStr The replacement value for all matched instances of the specified character..
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function replaceChar(targetString:String, charToMatch:String, replaceStr:String):String
		{
			var tempString:String = '';

			for(var i:Number = 0; i < targetString.length; i++)
			{
				if(charToMatch.charAt(0) == targetString.charAt(i))
				{
					tempString += replaceStr;
				}
				else
				{
					tempString += targetString.charAt(i);
				}
			}
			return tempString;
		}
		
		
		/**
		 *	Returns everything after the first occurrence of the provided character in the string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_begin The character or sub-string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function afterFirst(p_string:String, p_char:String):String {
			if (p_string == null) { return ''; }
			var idx:int = p_string.indexOf(p_char);
			if (idx == -1) { return ''; }
			idx += p_char.length;
			return p_string.substr(idx);
		}
		
		/**
		 *	Returns everything after the last occurence of the provided character in p_string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_char The character or sub-string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function afterLast(p_string:String, p_char:String):String {
			if (p_string == null) { return ''; }
			var idx:int = p_string.lastIndexOf(p_char);
			if (idx == -1) { return ''; }
			idx += p_char.length;
			return p_string.substr(idx);
		}
		
		/**
		 *	Determines whether the specified string begins with the specified prefix.
		 *
		 *	@param p_string The string that the prefix will be checked against.
		 *
		 *	@param p_begin The prefix that will be tested against the string.
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function beginsWith(p_string:String, p_begin:String):Boolean {
			if (p_string == null) { return false; }
			return p_string.indexOf(p_begin) == 0;
		}
		
		/**
		 *	Returns everything before the first occurrence of the provided character in the string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_begin The character or sub-string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function beforeFirst(p_string:String, p_char:String):String {
			if (p_string == null) { return ''; }
			var idx:int = p_string.indexOf(p_char);
			if (idx == -1) { return ''; }
			return p_string.substr(0, idx);
		}
		
		/**
		 *	Returns everything before the last occurrence of the provided character in the string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_begin The character or sub-string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function beforeLast(p_string:String, p_char:String):String {
			if (p_string == null) { return ''; }
			var idx:int = p_string.lastIndexOf(p_char);
			if (idx == -1) { return ''; }
			return p_string.substr(0, idx);
		}
		
		/**
		 *	Returns everything after the first occurance of p_start and before
		 *	the first occurrence of p_end in p_string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_start The character or sub-string to use as the start index.
		 *
		 *	@param p_end The character or sub-string to use as the end index.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function between(p_string:String, p_start:String, p_end:String):String {
			var str:String = '';
			if (p_string == null) { return str; }
			var startIdx:int = p_string.indexOf(p_start);
			if (startIdx != -1) {
				startIdx += p_start.length; // RM: should we support multiple chars? (or ++startIdx);
				var endIdx:int = p_string.indexOf(p_end, startIdx);
				if (endIdx != -1) { str = p_string.substr(startIdx, endIdx-startIdx); }
			}
			return str;
		}
		
		/**
		 *	Description, Utility method that intelligently breaks up your string,
		 *	allowing you to create blocks of readable text.
		 *	This method returns you the closest possible match to the p_delim paramater,
		 *	while keeping the text length within the p_len paramter.
		 *	If a match can't be found in your specified length an  '...' is added to that block,
		 *	and the blocking continues untill all the text is broken apart.
		 *
		 *	@param p_string The string to break up.
		 *
		 *	@param p_len Maximum length of each block of text.
		 *
		 *	@param p_delim delimter to end text blocks on, default = '.'
		 *
		 *	@returns Array
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function block(p_string:String, p_len:uint, p_delim:String = "."):Array {
			var arr:Array = new Array();
			if (p_string == null || !contains(p_string, p_delim)) { return arr; }
			var chrIndex:uint = 0;
			var strLen:uint = p_string.length;
			var replPatt:RegExp = new RegExp("[^"+escapePattern(p_delim)+"]+$");
			while (chrIndex <  strLen) {
				var subString:String = p_string.substr(chrIndex, p_len);
				if (!contains(subString, p_delim)){
					arr.push(truncate(subString, subString.length));
					chrIndex += subString.length;
				}
				subString = subString.replace(replPatt, '');
				arr.push(subString);
				chrIndex += subString.length;
			}
			return arr;
		}
		
		/**
		 *	Capitallizes the first word in a string or all words..
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_all (optional) Boolean value indicating if we should
		 *	capitalize all words or only the first.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function capitalize(p_string:String, ...args):String {
			var str:String = trimLeft(p_string);
			trace('capl', args[0])
			if (args[0] === true) { return str.replace(/^.|\b./g, _upperCase);}
			else { return str.replace(/(^\w)/, _upperCase); }
		}
		
		/**
		 *	Determines whether the specified string contains any instances of p_char.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_char The character or sub-string we are looking for.
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function contains(p_string:String, p_char:String):Boolean {
			if (p_string == null) { return false; }
			return p_string.indexOf(p_char) != -1;
		}
		
		/**
		 *	Determines the number of times a charactor or sub-string appears within the string.
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_char The character or sub-string to count.
		 *
		 *	@param p_caseSensitive (optional, default is true) A boolean flag to indicate if the
		 *	search is case sensitive.
		 *
		 *	@returns uint
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function countOf(p_string:String, p_char:String, p_caseSensitive:Boolean = true):uint {
			if (p_string == null) { return 0; }
			var char:String = escapePattern(p_char);
			var flags:String = (!p_caseSensitive) ? 'ig' : 'g';
			return p_string.match(new RegExp(char, flags)).length;
		}
		
		/**
		 *	Levenshtein distance (editDistance) is a measure of the similarity between two strings,
		 *	The distance is the number of deletions, insertions, or substitutions required to
		 *	transform p_source into p_target.
		 *
		 *	@param p_source The source string.
		 *
		 *	@param p_target The target string.
		 *
		 *	@returns uint
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function editDistance(p_source:String, p_target:String):uint {
			var i:uint;
			
			if (p_source == null) { p_source = ''; }
			if (p_target == null) { p_target = ''; }
			
			if (p_source == p_target) { return 0; }
			
			var d:Array = new Array();
			var cost:uint;
			var n:uint = p_source.length;
			var m:uint = p_target.length;
			var j:uint;
			
			if (n == 0) { return m; }
			if (m == 0) { return n; }
			
			for (i=0; i<=n; i++) { d[i] = new Array(); }
			for (i=0; i<=n; i++) { d[i][0] = i; }
			for (j=0; j<=m; j++) { d[0][j] = j; }
			
			for (i=1; i<=n; i++) {
				
				var s_i:String = p_source.charAt(i-1);
				for (j=1; j<=m; j++) {
					
					var t_j:String = p_target.charAt(j-1);
					
					if (s_i == t_j) { cost = 0; }
					else { cost = 1; }
					
					d[i][j] = _minimum(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+cost);
				}
			}
			return d[n][m];
		}
		
		/**
		 *	Determines whether the specified string ends with the specified suffix.
		 *
		 *	@param p_string The string that the suffic will be checked against.
		 *
		 *	@param p_end The suffix that will be tested against the string.
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function endsWith(p_string:String, p_end:String):Boolean {
			return p_string.lastIndexOf(p_end) == p_string.length - p_end.length;
		}
		
		/**
		 *	Determines whether the specified string contains text.
		 *
		 *	@param p_string The string to check.
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function hasText(p_string:String):Boolean {
			var str:String = removeExtraWhitespace(p_string);
			return !!str.length;
		}
		
		/**
		 *	Determines whether the specified string contains any characters.
		 *
		 *	@param p_string The string to check
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function isEmpty(p_string:String):Boolean {
			if (p_string == null) { return true; }
			return !p_string.length;
		}
		
		/**
		 *	Determines whether the specified string is numeric.
		 *
		 *	@param p_string The string.
		 *
		 *	@returns Boolean
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function isNumeric(p_string:String):Boolean {
			if (p_string == null) { return false; }
			var regx:RegExp = /^[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?$/;
			return regx.test(p_string);
		}
		
		/**
		 * Pads p_string with specified character to a specified length from the left.
		 *
		 *	@param p_string String to pad
		 *
		 *	@param p_padChar Character for pad.
		 *
		 *	@param p_length Length to pad to.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function padLeft(p_string:String, p_padChar:String, p_length:uint):String {
			var s:String = p_string;
			while (s.length < p_length) { s = p_padChar + s; }
			return s;
		}
		
		/**
		 * Pads p_string with specified character to a specified length from the right.
		 *
		 *	@param p_string String to pad
		 *
		 *	@param p_padChar Character for pad.
		 *
		 *	@param p_length Length to pad to.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function padRight(p_string:String, p_padChar:String, p_length:uint):String {
			var s:String = p_string;
			while (s.length < p_length) { s += p_padChar; }
			return s;
		}
		
		/**
		 *	Properly cases' the string in "sentence format".
		 *
		 *	@param p_string The string to check
		 *
		 *	@returns String.
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function properCase(p_string:String):String {
			if (p_string == null) { return ''; }
			var str:String = p_string.toLowerCase().replace(/\b([^.?;!]+)/, capitalize);
			return str.replace(/\b[i]\b/, "I");
		}
		
		/**
		 *	Escapes all of the characters in a string to create a friendly "quotable" sting
		 *
		 *	@param p_string The string that will be checked for instances of remove
		 *	string
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function quote(p_string:String):String {
			var regx:RegExp = /[\\"\r\n]/g;
			return '"'+ p_string.replace(regx, _quote) +'"'; //"
		}
		
		/**
		 *	Removes all instances of the remove string in the input string.
		 *
		 *	@param p_string The string that will be checked for instances of remove
		 *	string
		 *
		 *	@param p_remove The string that will be removed from the input string.
		 *
		 *	@param p_caseSensitive An optional boolean indicating if the replace is case sensitive. Default is true.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function remove(p_string:String, p_remove:String, p_caseSensitive:Boolean = true):String {
			if (p_string == null) { return ''; }
			var rem:String = escapePattern(p_remove);
			var flags:String = (!p_caseSensitive) ? 'ig' : 'g';
			return p_string.replace(new RegExp(rem, flags), '');
		}
		
		/**
		 *	Removes extraneous whitespace (extra spaces, tabs, line breaks, etc) from the
		 *	specified string.
		 *
		 *	@param p_string The String whose extraneous whitespace will be removed.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function removeExtraWhitespace(p_string:String):String {
			if (p_string == null) { return ''; }
			var str:String = trim(p_string);
			return str.replace(/\s+/g, ' ');
		}
		
		/**
		 *	Returns the specified string in reverse character order.
		 *
		 *	@param p_string The String that will be reversed.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function reverse(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.split('').reverse().join('');
		}
		
		/**
		 *	Returns the specified string in reverse word order.
		 *
		 *	@param p_string The String that will be reversed.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function reverseWords(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.split(/\s+/).reverse().join('');
		}
		
		/**
		 *	Determines the percentage of similiarity, based on editDistance
		 *
		 *	@param p_source The source string.
		 *
		 *	@param p_target The target string.
		 *
		 *	@returns Number
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function similarity(p_source:String, p_target:String):Number {
			var ed:uint = editDistance(p_source, p_target);
			var maxLen:uint = Math.max(p_source.length, p_target.length);
			if (maxLen == 0) { return 100; }
			else { return (1 - ed/maxLen) * 100; }
		}
		
		/**
		 *	Remove's all < and > based tags from a string
		 *
		 *	@param p_string The source string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function stripTags(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.replace(/<\/?[^>]+>/igm, '');
		}
		
		/**
		 *	Swaps the casing of a string.
		 *
		 *	@param p_string The source string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function swapCase(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.replace(/(\w)/, _swapCase);
		}
		
		/**
		 *	Removes whitespace from the front and the end of the specified
		 *	string.
		 *
		 *	@param p_string The String whose beginning and ending whitespace will
		 *	will be removed.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function trim(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.replace(/^\s+|\s+$/g, '');
		}
		
		/**
		 *	Removes whitespace from the front (left-side) of the specified string.
		 *
		 *	@param p_string The String whose beginning whitespace will be removed.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function trimLeft(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.replace(/^\s+/, '');
		}
		
		/**
		 *	Removes whitespace from the end (right-side) of the specified string.
		 *
		 *	@param p_string The String whose ending whitespace will be removed.
		 *
		 *	@returns String	.
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function trimRight(p_string:String):String {
			if (p_string == null) { return ''; }
			return p_string.replace(/\s+$/, '');
		}
		
		/**
		 *	Determins the number of words in a string.
		 *
		 *	@param p_string The string.
		 *
		 *	@returns uint
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function wordCount(p_string:String):uint {
			if (p_string == null) { return 0; }
			return p_string.match(/\b\w+\b/g).length;
		}
		
		/**
		 *	Returns a string truncated to a specified length with optional suffix
		 *
		 *	@param p_string The string.
		 *
		 *	@param p_len The length the string should be shortend to
		 *
		 *	@param p_suffix (optional, default=...) The string to append to the end of the truncated string.
		 *
		 *	@returns String
		 *
		 * 	@langversion ActionScript 3.0
		 *	@playerversion Flash 9.0
		 *	@tiptext
		 */
		public static function truncate(p_string:String, p_len:uint, p_suffix:String = "..."):String {
			if (p_string == null) { return ''; }
			p_len -= p_suffix.length;
			var trunc:String = p_string;
			if (trunc.length > p_len) {
				trunc = trunc.substr(0, p_len);
				if (/[^\s]/.test(p_string.charAt(p_len))) {
					trunc = trimRight(trunc.replace(/\w+$|\s+$/, ''));
				}
				trunc += p_suffix;
			}
			
			return trunc;
		}
		
		
		public static function containsExclusion(input:String, exclusions:Array, strictMatch:Boolean=false):Boolean{
			
			if(!exclusions || !input || exclusions.length == 0)
				return false;
			
			if(strictMatch) 
				return ArrayUtil.isExcluded(exclusions, input);
			 
				
			for(var i:int=0;i<exclusions.length;i++){
				
				// verify item is stringt
				if (typeof exclusions[i] == "string")   
					if(input.search(exclusions[i]) >=0 )
						return true;
						
			}
			 
			return false;
			
		}
		
		/**
		 *  Removes "unallowed" characters from a string.
		 *  A "restriction string" such as <code>"A-Z0-9"</code>
		 *  is used to specify which characters are allowed.
		 *  This method uses the same logic as the <code>restrict</code>
		 *  property of TextField.
		 *
		 *  @param str The input string.
		 *
		 *  @param restrict The restriction string.
		 *
		 *  @return The input string, minus any characters
		 *  that are not allowed by the restriction string.
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 1.5
		 *  @productversion Flex 4.1
		 */
		public static function restrict(str:String, restrict:String):String
		{
			// A null 'restrict' string means all characters are allowed.
			if (restrict == null)
				return str;
			
			// An empty 'restrict' string means no characters are allowed.
			if (restrict == "")
				return "";
			
			// Otherwise, we need to test each character in 'str'
			// to determine whether the 'restrict' string allows it.
			var charCodes:Array = [];
			
			var n:int = str.length;
			for (var i:int = 0; i < n; i++)
			{
				var charCode:uint = str.charCodeAt(i);
				if (testCharacter(charCode, restrict))
					charCodes.push(charCode);
			}
			
			return String.fromCharCode.apply(null, charCodes);
		}
		
		
		/**
		 *  Returns a string consisting of a specified string
		 *  concatenated with itself a specified number of times.
		 *
		 *  @param str The string to be repeated.
		 *
		 *  @param n The repeat count.
		 *
		 *  @return The repeated string.
		 *  
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 1.5
		 *  @productversion Flex 4.1
		 */
		public static function repeat(str:String, n:int):String
		{
			if (n == 0)
				return "";
			
			var s:String = str;
			for (var i:int = 1; i < n; i++)
			{
				s += str;
			}
			return s;
		}
		
		/* **************************************************************** */
		/*	These are helper methods used by some of the above methods.		*/
		/* **************************************************************** */
		private static function escapePattern(p_pattern:String):String {
			// RM: might expose this one, I've used it a few times already.
			return p_pattern.replace(/(\]|\[|\{|\}|\(|\)|\*|\+|\?|\.|\\)/g, '\\$1');
		}
		
		private static function _minimum(a:uint, b:uint, c:uint):uint {
			return Math.min(a, Math.min(b, Math.min(c,a)));
		}
		
		private static function _quote(p_string:String, ...args):String {
			switch (p_string) {
				case "\\":
					return "\\\\";
				case "\r":
					return "\\r";
				case "\n":
					return "\\n";
				case '"':
					return '\\"';
				default:
					return '';
			}
		}
		
		private static function _upperCase(p_char:String, ...args):String {
			trace('cap latter ',p_char)
			return p_char.toUpperCase();
		}
		
		private static function _swapCase(p_char:String, ...args):String {
			var lowChar:String = p_char.toLowerCase();
			var upChar:String = p_char.toUpperCase();
			switch (p_char) {
				case lowChar:
					return upChar;
				case upChar:
					return lowChar;
				default:
					return p_char;
			}
		}
		/**
		 *  @private
		 *  Helper method used by restrict() to test each character
		 *  in the input string against the restriction string.
		 *  The logic in this method implements the same algorithm
		 *  as in TextField's 'restrict' property (which is quirky,
		 *  such as how it handles a '-' at the beginning of the
		 *  restriction string).
		 */
		private static function testCharacter(charCode:uint,
											  restrict:String):Boolean
		{
			var allowIt:Boolean = false;
			
			var inBackSlash:Boolean = false;
			var inRange:Boolean = false;
			var setFlag:Boolean = true;
			var lastCode:uint = 0;
			
			var n:int = restrict.length;
			var code:uint;
			
			if (n > 0)
			{
				code = restrict.charCodeAt(0);
				if (code == 94) // caret
					allowIt = true;
			}
			
			for (var i:int = 0; i < n; i++)
			{
				code = restrict.charCodeAt(i)
				
				var acceptCode:Boolean = false;
				if (!inBackSlash)
				{
					if (code == 45) // hyphen
						inRange = true;
					else if (code == 94) // caret
						setFlag = !setFlag;
					else if (code == 92) // backslash
						inBackSlash = true;
					else
						acceptCode = true;
				}
				else
				{
					acceptCode = true;
					inBackSlash = false;
				}
				
				if (acceptCode)
				{
					if (inRange)
					{
						if (lastCode <= charCode && charCode <= code)
							allowIt = setFlag;
						inRange = false;
						lastCode = 0;
					}
					else
					{
						if (charCode == code)
							allowIt = setFlag;
						lastCode = code;
					}
				}
			}
			
			return allowIt;
		}

	}
}