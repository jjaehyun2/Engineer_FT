/*	
__       _____   ____    ______      ______   __  __     
/\ \     /\  __`\/\  _`\ /\__  _\    /\__  _\ /\ \/\ \    
\ \ \    \ \ \/\ \ \,\L\_\/_/\ \/    \/_/\ \/ \ \ `\\ \   
\ \ \  __\ \ \ \ \/_\__ \  \ \ \       \ \ \  \ \ , ` \  
\ \ \L\ \\ \ \_\ \/\ \L\ \ \ \ \       \_\ \__\ \ \`\ \ 
\ \____/ \ \_____\ `\____\ \ \_\      /\_____\\ \_\ \_\
\/___/   \/_____/\/_____/  \/_/      \/_____/ \/_/\/_/
	                                                          
	                                                          
______  ____    ______  ______   _____   __  __  ____    ____     ____    ______   ____    ______   
/\  _  \/\  _`\ /\__  _\/\__  _\ /\  __`\/\ \/\ \/\  _`\ /\  _`\  /\  _`\ /\__  _\ /\  _`\ /\__  _\  
\ \ \L\ \ \ \/\_\/_/\ \/\/_/\ \/ \ \ \/\ \ \ `\\ \ \,\L\_\ \ \/\_\\ \ \L\ \/_/\ \/ \ \ \L\ \/_/\ \/  
\ \  __ \ \ \/_/_ \ \ \   \ \ \  \ \ \ \ \ \ , ` \/_\__ \\ \ \/_/_\ \ ,  /  \ \ \  \ \ ,__/  \ \ \  
\ \ \/\ \ \ \L\ \ \ \ \   \_\ \__\ \ \_\ \ \ \`\ \/\ \L\ \ \ \L\ \\ \ \\ \  \_\ \__\ \ \/    \ \ \ 
\ \_\ \_\ \____/  \ \_\  /\_____\\ \_____\ \_\ \_\ `\____\ \____/ \ \_\ \_\/\_____\\ \_\     \ \_\
\/_/\/_/\/___/    \/_/  \/_____/ \/_____/\/_/\/_/\/_____/\/___/   \/_/\/ /\/_____/ \/_/      \/_/

    
Copyright (c) 2008 Lost In Actionscript - Shane McCartney

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

 */
package com.lia.utils {
	import flash.display.*;
	import flash.events.*;
	import flash.net.*;
	import flash.system.*;
	import flash.text.*;	

	/**
	 * @author flashdynamix
	 */
	public class SWFLoader extends Sprite {

		public var txtBx : TextField;
		private var loader : Loader;
		private var swfUrl : *;

		public function SWFLoader() {
			loader = new Loader();
			var loadInfo : LoaderInfo = loader.contentLoaderInfo;
			
			loadInfo.addEventListener(Event.COMPLETE, onLoaded);			loadInfo.addEventListener(ErrorEvent.ERROR, onLoadError);
			loadInfo.addEventListener(IOErrorEvent.IO_ERROR, onLoadError);			loadInfo.addEventListener(IOErrorEvent.NETWORK_ERROR, onLoadError);			loadInfo.addEventListener(IOErrorEvent.VERIFY_ERROR, onLoadError);			loadInfo.addEventListener(IOErrorEvent.DISK_ERROR, onLoadError);
			loadInfo.addEventListener(ProgressEvent.PROGRESS, onLoadProgress);
			
			init();
		}

		private function onLoadProgress(event : ProgressEvent) : void {
			if(event.bytesLoaded < 10) return;
			
			txtBx.text = Math.round(event.bytesLoaded / event.bytesTotal * 100).toString() + "%";
		}

		private function onLoadError(event : Event) : void {
			trace("On load error for swf file :" + swfUrl);
		}

		private function onLoaded(event : Event) : void {
			addChild(loader.content);
			
			txtBx.visible = false;
		}

		private function onResize(event : Event = null) : void {
			txtBx.x = 0;
			txtBx.y = stage.stageHeight / 2 - txtBx.height / 2;
			txtBx.width = stage.stageWidth;
		}

		public function init() : void {
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			stage.addEventListener(Event.RESIZE, onResize);
			onResize();
			
			swfUrl = root.loaderInfo.parameters["url"];
			
			loader.load(new URLRequest(swfUrl), new LoaderContext(false, ApplicationDomain.currentDomain));
		}
	}
}