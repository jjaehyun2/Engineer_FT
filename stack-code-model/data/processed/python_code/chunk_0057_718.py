/*(c). Copyright 1990-2008, Vyper Logix Corp., All Rights Reserved.

Published under Creative Commons License 
(http://creativecommons.org/licenses/by-nc/3.0/) 
restricted to non-commercial educational use only., 

See also: http://www.VyperLogix.com and http://samples.raychorn.com for details.

THE AUTHOR VYPER LOGIX CORP DISCLAIMS ALL WARRANTIES WITH REGARD TO
THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS, IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING
FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
WITH THE USE OR PERFORMANCE OF THIS SOFTWARE !

USE AT YOUR OWN RISK.
*/
package vyperlogix.FileIO.events {
	import flash.events.Event;
	import flash.display.DisplayObject;
	import flash.geom.Point;

	public class FileUploadTermsAgreementEvent extends Event {

		public function FileUploadTermsAgreementEvent(type:String, bubbles:Boolean=true, cancelable:Boolean=false) {
			super(type, bubbles, cancelable);
		}
		
        public static const TYPE_FILE_UPLOAD_TERMS_AGREEMENT:String = "fileUploadTermsAgreement";
        
        override public function clone():Event {
            return new FileUploadTermsAgreementEvent(type);
        }
	}
}