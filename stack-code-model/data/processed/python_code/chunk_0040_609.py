/*
** Source code Copyright 2006, Andrew Rapo
** May be used in non-commercial and commercial applications
** as long as the author is credited
*/
package org.rapo.games.astro {

	import org.rapo.games.astro.AudioController;
	import org.rapo.games.astro.SoundtrackXML;
	import flash.xml.XMLNode;
	import flash.net.*;
	import flash.events.*;
	
	public class SoundtrackController extends AudioController {
		
		
		public var xmlDoc:SoundtrackXML;
		public var xmlFile:String;
		public var phases:Object;
		
		public function SoundtrackController(xml_file:String) {
			
			xmlFile = xml_file;
			
			phases = new Object();
			xmlDoc = new SoundtrackXML(this);
			xmlDoc.ignoreWhite = true;
			loadXML();
		}
		
		public function loadXML() {
			
			//xmlDoc.onLoad = function(success:Boolean) {	
			//	this.owner.parseXML();	
			//}
			//xmlDoc.load(xmlFile);
			
			var loader:URLLoader = new URLLoader();
            configureListeners(loader);

            var request:URLRequest = new URLRequest("soundtrack.xml");
            try {
                loader.load(request);
            } catch (error:Error) {
                trace("Unable to load requested document.");
            }
        }

        private function configureListeners(dispatcher:IEventDispatcher):void {
            dispatcher.addEventListener(Event.COMPLETE, completeHandler);
            dispatcher.addEventListener(Event.OPEN, openHandler);
            dispatcher.addEventListener(ProgressEvent.PROGRESS, progressHandler);
            dispatcher.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
            dispatcher.addEventListener(HTTPStatusEvent.HTTP_STATUS, httpStatusHandler);
            dispatcher.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
        }

        private function completeHandler(event:Event):void {
            var loader:URLLoader = URLLoader(event.target);
            trace("completeHandler: ");
			
			xmlDoc.parseXML(loader.data);
			parseXML();
        }

        private function openHandler(event:Event):void {
            trace("openHandler: " + event);
        }

        private function progressHandler(event:ProgressEvent):void {
            trace("progressHandler loaded:" + event.bytesLoaded + " total: " + event.bytesTotal);
        }

        private function securityErrorHandler(event:SecurityErrorEvent):void {
            trace("securityErrorHandler: " + event);
        }

        private function httpStatusHandler(event:HTTPStatusEvent):void {
            trace("httpStatusHandler: " + event);
        }

        private function ioErrorHandler(event:IOErrorEvent):void {
            trace("ioErrorHandler: " + event);
        }

		
		public function parseXML() {
			for (var prop:String in xmlDoc.firstChild.childNodes) {
				trace(prop + ' ' + xmlDoc.firstChild.childNodes[prop].nodeName);
				if (xmlDoc.firstChild.childNodes[prop].nodeName == "phase") {
					parsePhase(xmlDoc.firstChild.childNodes[prop]);
				}
			}
		}
		
		public function parsePhase(node:XMLNode) {
			for (var prop:String in node.childNodes) {
				trace("  " + prop + ' ' + node.childNodes[prop].nodeName + ", " + node.attributes["id"]);
				if (node.childNodes[prop].nodeName == "track") {
					parseTrack(node.childNodes[prop], node.attributes["id"]);
				}
			}
		}
			
		public function parseTrack(node:XMLNode, phase:String) {
			trace("    " + node.firstChild.nodeValue);
			
			if (phases[phase] == undefined) {
				phases[phase] = new Array();
			}
	
			phases[phase].push(node.firstChild.nodeValue);
		}
		
		public function playTrack(phase:String, loop:Boolean) {
			
			var randomIndex = Math.floor(Math.random() * phases[phase].length);
			trace("PlayTrack: " + phase + ", " + randomIndex + ", " + phases[phase][randomIndex]);
			
			
			loadSound(phase, phases[phase][randomIndex], false, true);
			playSound(phase, loop);
			setSoundVolume(phase, 40);
		}	
	}
}