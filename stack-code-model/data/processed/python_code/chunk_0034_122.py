package models
{
	
	
	import utils.strings.Strings;
	
	public class PropParser
	{
		
		private const S_COMMENT:String = "/*";
		private const E_COMMENT:String = "*/";
		private const NEWLINE:String = "\n";
		private const RETURN:String = "\r";
		private const SPACE:String = " ";
		private const DELIMITER:String = "=";
		private const TAB:String = "\t";
		
		
		
		
		/**
		 * Constructor 
		 * @param onReturn - Callback for calling class
		 */		
		
		public function PropParser() {
		}
		
		
		
		
		public function removeComments(s:String):String {
			var ns:String = new String();
			for(var start:int = 0; start<s.length;++start) {
				if(s.charAt(start)==S_COMMENT.charAt(0) && s.charAt(start+1)==S_COMMENT.charAt(1)) {
					ns=s.substring(0,start);
					for(var end:int=start;end<s.length;++end){
						if(s.charAt(end) == E_COMMENT.charAt(0) && s.charAt(end+1) == E_COMMENT.charAt(1)) {
							ns+=s.substr(end+2);
							return ns;
						}
					}
					
					// If the loop gets here then the whole line was commented
					ns += s.substr(end);
					return ns;
				} else {
					ns+=s.charAt(start);
				}
			}
			return ns;
		}
		
		
		public function parse(data:String):Array {
			var s:String = data;
			var d:Array = s.split(NEWLINE);
			var t:Array = [];
			
			for(var l:int = 0; l<d.length;++l) {
				// Clean up any "\r"
				d[l] = utils.strings.Strings.removeChar(d[l],RETURN);
				
				var _Error:Boolean = false;
				while(d[l] = removeComments(d[l])) {
					if(d[l].indexOf(S_COMMENT) == -1) {
						var i1:int = d[l].indexOf(E_COMMENT);
						if(i1 > -1) {
							_Error=true;
							// Comment Syntax Error */
							var e:String = d[l].substring(0,i1)+" >> "+d[l].substr(i1);
							trace("Syntax Error missing \" /* \": "+e);	
						}
						break;
					}
				}
				
				if(!_Error) {
					// Clean up Spaces
					d[l] = utils.strings.Strings.removeChar(d[l],SPACE);
					// Verify if the array element is blank, if so remove it from the array
					if(d[l] != "") {
						// If string is not blank then add to new array
						t.push(d[l]);
					}
				}
			
			
			var d1:Array = [];
			for(var i:int = 0; i<t.length; ++i) {
					var sp:Array = t[i].toString().split(DELIMITER);
					var jn:String = "";
					
					if(sp.length>2) {
						for(var j:int=1;j<sp.length;++j) jn+=sp[j]+DELIMITER;		
						jn = jn.substring(0,jn.length-1);
					} else {
						jn=sp[1];
					}
					
					sp[0] = utils.strings.Strings.removeChar(sp[0],TAB);
					jn = utils.strings.Strings.removeChar(jn,TAB);
					d1.push({name:sp[0], value:jn});
				}
			}
			
			
			for(var ck:int = 0; ck<d1.length; ++ck) {
				//trace("e: "+ck+" name: "+d1[ck].name+" value: "+d1[ck].value);	
			}
			
			return d1;
		}
		
		public function testData():String {
			//var d:String = "/* My nice comment */\n var1=https://www.a.com/something/abc123.htm#helloworld\n var2=http://www.b.com/somethingelse/efg456/\n var3=http://www.c.com/lskdjf/sdlkjf?a=1&b=2\n /* My nice comment */\n var4=https://www.d.com/sldkjf/12341234#lskdjf?a=1&b=2%20%helloworld\n var5=http://www.e.com";
			var d:String = "#MAIN SITE LINKS \nvzw=http://wmsvzwpreprod.ddc.vzwcorp.com\nvzw-secure=https://wmsvzwpreprod.ddc.vzwcorp.com \nbusiness=http://b2b-uat.idc.vzwcorp.com \nmyverizon=https://wmsvzwpreprod.ddc.vzwcorp.com \nmblogin=https://tmblogin.verizonwireless.com/amserver/UI/Login?realm=vzwmb\nespanol=http://espanol.vzw.com/enes\nvzwBusiness=https://business.verizonwireless.com\n\n#OMNITURE\naboutus=http://stage-aboutus.vzw.com\nb2b=http://stage-b2b.vzw.com\nsupport=http://stage-support.vzw.com\nnews=http://stage-news.vzw.com\nsearch=http://search.vzw.com?q=phones&stage=1\n\n#ASPs\nalerts=https://vmeqa1.pdi.vzw.com\nanimated=https://vgeqa1.pdi.vzw.com/vge\nblackBerryDownload=http://vzamredesign.smithmicro.net/blackberry\ncareers=http://www.vzwcareers.com\ndashboard=http://dashboard.vzw.com\nenterprizeMsg=http://enterprisemessaging.vzw.com\nentertainment=http://stage.products.verizonwireless.com\nestore=http://stage.phones.verizonwireless.com\nfamilyLocator=http://familylocatorstage.vzw.com\nforums=http://community.vzw.com\nhub=http://hubstg.vzw.com/hub/members/\nlocationMgmt=http://vzwlocmanagement.vzw.com/\nmobileWeb=http://demomobileweb.vzw.com\npictures=https://testpix.vzw.com\npushtotalk=http://pushtotalk.vzw.com\nrebates=https://wwww.yourwirelessrebatecenter.com\nsatellite=http://www.vzwsatellite.com\nsmartphoneRC=http://stage.smartphones.verizonwireless.com\ntextInt=http://text1.vzw.com\ntextMessaging=https://stagingwig.vzw.com\nvcastMusic=http://vzamredesign.smithmicronet/vcastmusic\nvzEmail=http://vzemail.vzw.com\nvzNavigator=http://stg5-vznav.vzw.com\nvskins=http://www.vskins.com\n\n#VZW\nmedia=https://mobilemediatest-east.verizonwireless.com\nscu=http://myacctqa2web1.odc.vzwcorp.com:8080/imageFiles/Myacct/gn/TEST_qa2\nasu=http://myacctqa2web1.odc.vzwcorp.com:9443/vzwsvc/asc\nusu=http://myacctqa2web1.odc.vzwcorp.com:9443/vzwsvc/usc\nclp=https://wmsvzwpreprod.ddc.vzwcorp.com:443/clp/login?redirect=\n\n#Other\nvzBusiness=http://business.verizon.net";
			return d;
		}
		
	}
}