/*
 *	Temple Library for ActionScript 3.0
 *	Copyright © MediaMonks B.V.
 *	All rights reserved.
 *	
 *	Redistribution and use in source and binary forms, with or without
 *	modification, are permitted provided that the following conditions are met:
 *	1. Redistributions of source code must retain the above copyright
 *	   notice, this list of conditions and the following disclaimer.
 *	2. Redistributions in binary form must reproduce the above copyright
 *	   notice, this list of conditions and the following disclaimer in the
 *	   documentation and/or other materials provided with the distribution.
 *	3. All advertising materials mentioning features or use of this software
 *	   must display the following acknowledgement:
 *	   This product includes software developed by MediaMonks B.V.
 *	4. Neither the name of MediaMonks B.V. nor the
 *	   names of its contributors may be used to endorse or promote products
 *	   derived from this software without specific prior written permission.
 *	
 *	THIS SOFTWARE IS PROVIDED BY MEDIAMONKS B.V. ''AS IS'' AND ANY
 *	EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 *	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 *	DISCLAIMED. IN NO EVENT SHALL MEDIAMONKS B.V. BE LIABLE FOR ANY
 *	DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 *	(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *	LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 *	ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 *	(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 *	SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *	
 *	
 *	Note: This license does not apply to 3rd party classes inside the Temple
 *	repository with their own license!
 */

package temple.utils 
{
	import temple.core.debug.log.Log;
	import temple.core.debug.objectToString;

	/**
	 * This class is used to decode HTMLEntities
	 * 
	 * @author Thijs Broerse
	 */
	public final class HTMLEntities 
	{
		private static var _entities:Object;

		/**
		 * Replaces HTML Entities codes to Flash codes in a String
		 * @param string the String that needs to be decoded
		 * @return a decoded String with all HTMLEntities replaced
		 */
		public static function decode(string:String):String
		{
			HTMLEntities._entities ||= HTMLEntities.getEntities();
        	
			for (var entity:String in HTMLEntities._entities)
			{
				string = string.replace(new RegExp(entity, 'g'), HTMLEntities._entities[entity]);
			}
			try
			{
				return String(XML('<node>' + string + '</node>'));
			}
			catch (error:Error)
			{
				Log.error(error.message + "\n\"" + string + "\"\n" + error.getStackTrace(), HTMLEntities);
			}
			return string;
		}

		private static function getEntities():Object
		{
			var entities: Object = new Object();
			entities["&nbsp;"]   = "\u00A0"; // non-breaking space
			entities["&iexcl;"]  = "\u00A1"; // inverted exclamation mark
			entities["&cent;"]   = "\u00A2"; // cent sign
			entities["&pound;"]  = "\u00A3"; // pound sign
			entities["&curren;"] = "\u00A4"; // currency sign
			entities["&yen;"]    = "\u00A5"; // yen sign
			entities["&brvbar;"] = "\u00A6"; // broken vertical bar (|)
			entities["&sect;"]   = "\u00A7"; // section sign
			entities["&uml;"]    = "\u00A8"; // diaeresis
			entities["&copy;"]   = "\u00A9"; // copyright sign
			entities["&reg;"]    = "\u00AE"; // registered sign
			entities["&deg;"]    = "\u00B0"; // degree sign
			entities["&plusmn;"] = "\u00B1"; // plus-minus sign
			entities["&sup1;"]   = "\u00B9"; // superscript one
			entities["&sup2;"]   = "\u00B2"; // superscript two
			entities["&sup3;"]   = "\u00B3"; // superscript three
			entities["&acute;"]  = "\u00B4"; // acute accent
			entities["&micro;"]  = "\u00B5"; // micro sign
			entities["&frac14;"] = "\u00BC"; // vulgar fraction one quarter
			entities["&frac12;"] = "\u00BD"; // vulgar fraction one half
			entities["&frac34;"] = "\u00BE"; // vulgar fraction three quarters
			entities["&iquest;"] = "\u00BF"; // inverted question mark
			entities["&Agrave;"] = "\u00C0"; // Latin capital letter A with grave
			entities["&Aacute;"] = "\u00C1"; // Latin capital letter A with acute
			entities["&Acirc;"]  = "\u00C2"; // Latin capital letter A with circumflex
			entities["&Atilde;"] = "\u00C3"; // Latin capital letter A with tilde
			entities["&Auml;"]   = "\u00C4"; // Latin capital letter A with diaeresis
			entities["&Aring;"]  = "\u00C5"; // Latin capital letter A with ring above
			entities["&AElig;"]  = "\u00C6"; // Latin capital letter AE
			entities["&Ccedil;"] = "\u00C7"; // Latin capital letter C with cedilla
			entities["&Egrave;"] = "\u00C8"; // Latin capital letter E with grave
			entities["&Eacute;"] = "\u00C9"; // Latin capital letter E with acute
			entities["&Ecirc;"]  = "\u00CA"; // Latin capital letter E with circumflex
			entities["&Euml;"]   = "\u00CB"; // Latin capital letter E with diaeresis
			entities["&Igrave;"] = "\u00CC"; // Latin capital letter I with grave
			entities["&Iacute;"] = "\u00CD"; // Latin capital letter I with acute
			entities["&Icirc;"]  = "\u00CE"; // Latin capital letter I with circumflex
			entities["&Iuml;"]   = "\u00CF"; // Latin capital letter I with diaeresis
			entities["&ETH;"]    = "\u00D0"; // Latin capital letter ETH
			entities["&Ntilde;"] = "\u00D1"; // Latin capital letter N with tilde
			entities["&Ograve;"] = "\u00D2"; // Latin capital letter O with grave
			entities["&Oacute;"] = "\u00D3"; // Latin capital letter O with acute
			entities["&Ocirc;"]  = "\u00D4"; // Latin capital letter O with circumflex
			entities["&Otilde;"] = "\u00D5"; // Latin capital letter O with tilde
			entities["&Ouml;"]   = "\u00D6"; // Latin capital letter O with diaeresis
			entities["&Oslash;"] = "\u00D8"; // Latin capital letter O with stroke
			entities["&Ugrave;"] = "\u00D9"; // Latin capital letter U with grave
			entities["&Uacute;"] = "\u00DA"; // Latin capital letter U with acute
			entities["&Ucirc;"]  = "\u00DB"; // Latin capital letter U with circumflex
			entities["&Uuml;"]   = "\u00DC"; // Latin capital letter U with diaeresis
			entities["&Yacute;"] = "\u00DD"; // Latin capital letter Y with acute
			entities["&THORN;"]  = "\u00DE"; // Latin capital letter THORN
			entities["&szlig;"]  = "\u00DF"; // Latin small letter sharp s = ess-zed
			entities["&agrave;"] = "\u00E0"; // Latin small letter a with grave
			entities["&aacute;"] = "\u00E1"; // Latin small letter a with acute
			entities["&acirc;"]  = "\u00E2"; // Latin small letter a with circumflex
			entities["&atilde;"] = "\u00E3"; // Latin small letter a with tilde
			entities["&auml;"]   = "\u00E4"; // Latin small letter a with diaeresis
			entities["&aring;"]  = "\u00E5"; // Latin small letter a with ring above
			entities["&aelig;"]  = "\u00E6"; // Latin small letter ae
			entities["&ccedil;"] = "\u00E7"; // Latin small letter c with cedilla
			entities["&egrave;"] = "\u00E8"; // Latin small letter e with grave
			entities["&eacute;"] = "\u00E9"; // Latin small letter e with acute
			entities["&ecirc;"]  = "\u00EA"; // Latin small letter e with circumflex
			entities["&euml;"]   = "\u00EB"; // Latin small letter e with diaeresis
			entities["&igrave;"] = "\u00EC"; // Latin small letter i with grave
			entities["&iacute;"] = "\u00ED"; // Latin small letter i with acute
			entities["&icirc;"]  = "\u00EE"; // Latin small letter i with circumflex
			entities["&iuml;"]   = "\u00EF"; // Latin small letter i with diaeresis
			entities["&eth;"]    = "\u00F0"; // Latin small letter eth
			entities["&ntilde;"] = "\u00F1"; // Latin small letter n with tilde
			entities["&ograve;"] = "\u00F2"; // Latin small letter o with grave
			entities["&oacute;"] = "\u00F3"; // Latin small letter o with acute
			entities["&ocirc;"]  = "\u00F4"; // Latin small letter o with circumflex
			entities["&otilde;"] = "\u00F5"; // Latin small letter o with tilde
			entities["&ouml;"]   = "\u00F6"; // Latin small letter o with diaeresis
			entities["&oslash;"] = "\u00F8"; // Latin small letter o with stroke
			entities["&ugrave;"] = "\u00F9"; // Latin small letter u with grave
			entities["&uacute;"] = "\u00FA"; // Latin small letter u with acute
			entities["&ucirc;"]  = "\u00FB"; // Latin small letter u with circumflex
			entities["&uuml;"]   = "\u00FC"; // Latin small letter u with diaeresis
			entities["&yacute;"] = "\u00FD"; // Latin small letter y with acute
			entities["&thorn;"]  = "\u00FE"; // Latin small letter thorn
			entities["&yuml;"]   = "\u00FF"; // Latin small letter y with diaeresis
			entities["&ndash;"]  = "-";
			entities["&lsquo;"]  = "'";
			entities["&rsquo;"]  = "'";
			entities["&amp;"]    = "&";
			entities["&quot;"]   = '"';
			entities["&apos;"]   = "'";
			entities["&lt;"]     = "&#60;";
			entities["&gt;"]     = "&#62;";
			entities["<"]    	 = "&#60;";
			entities[">"]    	 = "&#62;";
           
            return entities;
		}
        
        /**
		 * @private
		 */
		public static function toString():String
       	{
        	return objectToString(HTMLEntities);
        }
	}
}