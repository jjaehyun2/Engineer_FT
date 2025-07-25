package com {
	import com.hurlant.crypto.hash.MD5;
	import com.hurlant.util.Hex;
	
	import flash.utils.ByteArray;
	
	public class StringUtils {
		public static const illegalWindowsFileNameChars:Array = ['?','[',']','/','\\','=','+','<','>',':',';','"',"'",',','.'];
		
		public static const hex_digits:Array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f'];
		
		public static function trim(value:String):String {
			return value.match(/^\s*(.*?)\s*$/)[1];
		}
		
		public static const mode_OBSCURE_ALL:uint = 0x0000;
		public static const mode_OBSCURE_PARTIAL:uint = 0x0001;
		public static const mode_OBSCURE_ALL_SWAPPER:uint = 0x0002;
		
		private static const masks:Array = [];
		
		public static function json(content:String):String {
			var pattern:RegExp = /(\{".*)/;
			var test:* = pattern.exec(content);
			return ( (test is Array) && (test.length > 0) ) ? test[0] : test;
		}
		
		public static function isUrl(url:String):Boolean {
			var pattern:RegExp = /^http(s)?:\/\/((\d+\.\d+\.\d+\.\d+)|(([\w-]+\.)+([a-z,A-Z][\w-]*)))(:[1-9][0-9]*)?(\/([\w-.\/:%+@&=]+[\w- .\/?:%+@&=]*)?)?(#(.*))?$/i;
			var test:* = pattern.exec(url);
			var bool:Boolean = false;
			var isUrl:Boolean = (test);
			return isUrl;
		}

		public static function isIPAddress(ip:String):Boolean {
			var pattern:RegExp = /\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b/;
			var test:* = pattern.exec(ip);
			var bool:Boolean = false;
			for (var i:String in test) {
				if (int(i) > 1) {
					bool ||= StringUtils.isStringNumeric(test[i]);
				}
			}
			var isIP:Boolean = (test) ? (test.length == 5) && (bool) : false;
			return isIP;
		}

		public static function version_as_number(version:String):Number {
			var toks:Array = version.split('.');
			var demask:Function = function (ar:Array):Number {
				var num:Number = 0;
				var exp:int  = 0;
				var n:Number;
				for (var i:String in ar) {
					n = Number(ar[i]);
					n *= Math.pow(10,exp);
					num += n;
					exp--;
				}
				return (num > 0) ? num : -1;
			};
			var num:Number = demask(toks);
			num = int(num * Math.pow(10,version.length)) / Math.pow(10,version.length);
			return num;
		}
		
		public static function appendSlashIfNecessary(str:String):String {
			return str+((str.charAt(str.length-1) != '/') ? '/' : '');
		}
		
		public static function isAlpha(char:uint):Boolean {
			return ( ( (char >= 0x41) && (char <= 0x5a) ) || ( (char >= 0x61) && (char <= 0x7a) ) );
		}
		
		public static function isNumeric(char:uint):Boolean {
			return ( (char >= 0x30) && (char <= 0x39) );
		}
		
		public static function isAlphaNumeric(char:uint):Boolean {
			return (isAlpha(char) || isNumeric(char));
		}
		
		public static function numericsOnly(s:String):String {
			var i:int;
			var t:String = '';
			var c:String;
			for (i = 0; i < s.length; i++) {
				c = s.substr(i,1);
				if (isNumeric(c.charCodeAt(0))) {
					t += c;
				}
			}
			return t;
		}
		
		public static function nonNumericsOnly(s:String):String {
			var i:int;
			var t:String = '';
			var c:String;
			for (i = 0; i < s.length; i++) {
				c = s.substr(i,1);
				if (!isNumeric(c.charCodeAt(0))) {
					t += c;
				}
			}
			return t;
		}
		
		public static function isStringNumeric(s:String):Boolean {
			for (var i:int = 0; i < s.length; i++) {
				if (!isNumeric(s.charCodeAt(i))) {
					return false;
				}
			}
			return true;
		}
		
		public static function numericTokensOnly(source:String,delim:String):Array {
			var toks:Array = source.split(delim);
			var t:Array = [];
			var s:String;
			for (var i:int = 0; i < toks.length; i++) {
				s = toks[i];
				if (isStringNumeric(s)) {
					t.push(s);
				}
			}
			return t;
		}
		
		public static function replaceAll(source:String, pattern:String, newPattern:String):String {
			var ar:Array = source.split(pattern);
			return (ar.join(newPattern));
		}
		
		private static function initMasks():void {
			var m:uint = 0x8000;
			if (masks.length != 16) {
				do {
					masks.push(m);
					m >>>= 1;
				} while (m > 0);
			}
		}
		
		public static function dumpAsHexBytes(s:String):Array {
			var bytes:Array = [];
			var i:int;
			var ch:uint;
			for (i = 0; i < s.length; i++) {
				ch = s.charCodeAt(i);
				bytes.push(ch.toString(16));
			}
			return bytes;
		}
		
		public static function dumpAsHexBytesString(s:String):String {
			var bytes:String = '';
			var i:int;
			var h:String;
			for (i = 0; i < s.length; i++) {
				h = (s.charCodeAt(i) & 0xff).toString(16);
				bytes += ((h.length < 2) ? '0' : '') + h;
			}
			return bytes;
		}
		
		public static function fromHexBytesString(s:String):String {
			var bytes:String = '';
			var i:int;
			var h:uint;
			for (i = 0; i < s.length; i += 2) {
				h = parseInt('0x' + s.substr(i,2));
				bytes += String.fromCharCode(h);
			}
			return bytes;
		}
		
		private static function maskForNumBits(numBits:int):uint {
			var i:int;
			var j:int = 1;
			var mask:uint = 0;
			for (i = masks.length-1; i >= 0; i--) {
				mask |= masks[i];
				if (j == numBits) {
					break;
				}
				j++;
			}
			return mask;
		}
		
		private static function swapBits(value:uint, numBits:int):uint {
			var lsbMask:uint = maskForNumBits(numBits);
			var msbMask:uint = ~lsbMask & 0x00ff;
			var msbValue:uint = (value & msbMask) >> 4;
			var lsbValue:uint = value & lsbMask;
			var x:uint = (lsbValue << 4) | msbValue;
			return x;
		}
		
		public static function isHexDigits(s:String):Boolean {
			var i:int;
			for (i = 0; i < s.length; i++) {
				if (hex_digits.indexOf(s.substr(i,1)) == -1) {
					return false;
				}
			}
			return true;
		}
		
		public static function asHexDigits(s:String):String {
			var i:int;
			var ch:String;
			var t:String = '';
			for (i = 0; i < s.length; i++) {
				ch = s.substr(i,1);
				if (hex_digits.indexOf(ch) > -1) {
					t += ch;
				}
			}
			return t;
		}
		
		public static function obscure(value:String, mode:uint = mode_OBSCURE_PARTIAL):String {
			var i:int;
			var s:String = "";
			if (mode == mode_OBSCURE_PARTIAL) {
				for (i = 0; i < value.length; i++) {
					s += ((isAlphaNumeric(value.charCodeAt(i))) ? String.fromCharCode(value.charCodeAt(i)) : String.fromCharCode(value.charCodeAt(i) | 0x80));
				}
			} else if (mode == mode_OBSCURE_ALL_SWAPPER) {
				initMasks();
				for (i = 0; i < value.length; i++) {
					s += String.fromCharCode(swapBits(value.charCodeAt(i) | 0x80,4));
				}
			} else {
				for (i = 0; i < value.length; i++) {
					s += String.fromCharCode(value.charCodeAt(i) | 0x80);
				}
			}
			return s;
		}
		
		public static function deobscure(value:String,mode:uint=mode_OBSCURE_ALL):String {
			var i:int;
			var s:String = "";
			if (mode == mode_OBSCURE_ALL_SWAPPER) {
				initMasks();
				for (i = 0; i < value.length; i++) {
					s += String.fromCharCode(swapBits(value.charCodeAt(i),4));
				}
				
			} else {
				for (i = 0; i < value.length; i++) {
					s += String.fromCharCode(value.charCodeAt(i) & 0x7f);
				}
			}
			return s;
		}
		
		public static function removeIllegalWindowsFileNameChars(source:String, replacementChar:String='_'):String {
			var i:int;
			var s:String = source;
			var illegalChars:Array = illegalWindowsFileNameChars;
			for (i = 0; i < illegalChars.length; i++) {
				s = s.replace(illegalChars[i],replacementChar);
			}
			return s;
		}
		
		public static function dummyTranslateFunc(ch:String):String {
			return ch;
		}
		
		public static function dummyReportFunc(value:String, ch:String):String {
			return '(' + value.charCodeAt(0).toString() + ':"' + ch + '")';
		}
		
		public static function replaceCaseless(value:String, pattern:String, replacement:String):String {
			var val:String = value;
			var i:int;
			var j:int = 0;
			var lenPattern:int = pattern.length;
			var ch:String;
			var isMatched:Boolean = false;
			for (i = 0; i < value.length; i++) {
				ch = value.substr(i,1);
				if (ch.toLowerCase() == pattern.substr(j,1).toLowerCase()) {
					if (j == (lenPattern-1)) {
						isMatched = true;
						break;
					}
					j++;
				} else {
					j = 0;
				}
			}
			if (isMatched) {
				i -= (lenPattern-1);
				val = value.substr(0,i) + replacement + value.substr(i+lenPattern,value.length-lenPattern);
			}
			return val;
		}
		
		public static function reportCharCodes(value:String, reportFunc:Function=null, translateFunc:Function=null):String {
			var i:int;
			var ar:Array = [];
			var ar2:Array = [];
			var ch:String;
			translateFunc = ((translateFunc == null) ? dummyTranslateFunc : translateFunc);
			reportFunc = ((reportFunc == null) ? dummyReportFunc : reportFunc);
			for (i = 0; i < value.length; i++) {
				try { ch = translateFunc(value.substr(i,1)); } catch (err:Error) { ch = ''; }
				ar.push(reportFunc(value.substr(i,1),ch));
				ar2.push(ch);
			}
			return ar.join(' ') + '<br>' + ar2.join('');
		}
		
		public static function repeatedChars(aChar:String, num:int):String {
			var s:String = '';
			for (var i:int = 0; i < num; i++) {
				s += aChar;
			}
			return s;
		}
		
		public static function urlEncode(plaintext:String):String {
			var SAFECHARS:String = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_.!~*'()";					
			var HEX:String = "0123456789ABCDEF";
			
			var ch:String;
			var charCode:uint;
			var encoded:String = "";
			if (!!plaintext) {
				for (var i:int = 0; i < plaintext.length; i++ ) {
					ch = plaintext.charAt(i);
					if (ch == " ") { encoded += "+";} else if (SAFECHARS.indexOf(ch) != -1) {encoded += ch;
					} else {
						charCode = ch.charCodeAt(0);
						if (charCode > 255) { encoded += "+";} else {encoded += "%"; encoded += HEX.charAt((charCode >> 4) & 0xF); encoded += HEX.charAt(charCode & 0xF);}
					}
				}
			}
			
			return encoded;
		}
		
		public static function urlDecode(encoded:String):String {
			var HEXCHARS:String = "0123456789ABCDEFabcdef"; 
			var plaintext:String = "";
			var i:int = 0;
			while (i < encoded.length) {
				var ch:String = encoded.charAt(i);
				if (ch == "+") { plaintext += " "; i++;} else if (ch == "%") {
					if (i < (encoded.length-2) && (HEXCHARS.indexOf(encoded.charAt(i+1)) != -1) && (HEXCHARS.indexOf(encoded.charAt(i+2)) != -1) ) {
						plaintext += unescape( encoded.substr(i,3) ); i += 3;
					} else { plaintext += "%[ERROR]"; i++;}
				} else { plaintext += ch; i++;}
			} 
			return plaintext;
		}
		
		public static function ellipsis(str:String,len:int=-1):String {
			var n:int = ((len == -1) ? str.length : len);
			return str.substr(0,n) + ((str.length > n) ? '...' : '');
		}
		
		public static function fit_to_width(str:String,len:int):String {
			var toks:Array = str.split(' ');
			var _toks:Array = [];
			var result:String = '';
			var seps:int = 0;
			for (var i:String in toks) {
				_toks.push(toks[i]);
				seps++;
				if (_toks.join(' ').length > (len-seps)) {
					_toks.push('\n');
					result += _toks.join(' ');
					_toks = [];
					seps = 0;
				}
			}
			return result;
		}
		
		public static function uintToString(hex:uint):String {
			var hexString:* = hex.toString(16).toUpperCase();
			var cnt:int = 6 - hexString.length;
			var zeros:String = "";
			for (var i:int = 0; i < cnt; i++) {
				zeros += "0";
			}
			return "#" + zeros + hexString;
		}
		
		public static function toBoolean(str:String):Boolean {
			return (str) ? (str.toString().toLowerCase() == 'true') : false;
		}
		
		public static function toMD5(str:String):String {
			var ba:ByteArray = (new MD5).hash(Hex.toArray(Hex.fromString(str)));
			return StringUtils.dumpAsHexBytesString(ba.toString());
		}
		
	}
}