/*

Copyright (c) 2014, GlassLab, Inc.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the FreeBSD Project.

*/


/**
* glsdk_json.as
* GlassLab SDK
*
* JSON wrapper allows for Flash Player 10+ compliance.
* Flash Player 10 uses as3corelib for JSON, which includes "encode" and "decode"
* Flash Player 11+ uses a native JSON library, which includes "stringify" and "parse"
*
* @author Ben Dapkiewicz
*
* Copyright (c) 2014 GlassLab. All rights reserved.
*/
package GlassLabSDK {
	
	import com.adobe.serialization.json.JSON;

	
	public class glsdk_json {
		
		// Singleton instance
		private static var m_instance : glsdk_json;
		public static function instance() : glsdk_json {
			if( m_instance == null ) {
				m_instance = new glsdk_json();
			}
			return m_instance;
		}
		
		
		// Stringify and parse functions
		public var stringify : Function;
		public var parse : Function;
		
		
		/**
		 * Constructor sets the correct encode and decode methods, based on supported runtime version.
		 */
		public function glsdk_json() {
			// Flash Player 10
			if( JSON[ "encode" ] ) {
				stringify = JSON[ "encode" ];
				parse = JSON[ "decode" ];
			}
			// Flash Player 11+
			else {
				stringify = JSON[ "stringify" ];
				parse = JSON[ "parse" ];
			}
		}
	}
}