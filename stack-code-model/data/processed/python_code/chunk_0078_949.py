/*
* Copyright 2010-2011 Research In Motion Limited.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
package webworks.loadingScreen
{
	import flash.display.Bitmap;
	import flash.display.Graphics;
	import flash.display.Loader;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.geom.Rectangle;
	import flash.net.URLRequest;
	
	import qnx.media.QNXStageWebView;
	
	import webworks.config.ConfigConstants;
	import webworks.config.ConfigData;
	import webworks.config.TransitionConstants;
	import webworks.uri.URI;
	import webworks.util.Utilities;
	import webworks.webkit.WebkitControl;
	
	public class LoadingScreen extends Sprite
	{
		private var bgImageLoader:Loader;
		private var fgImageLoader:Loader;
		private var source:Bitmap;
		private var foreground:Bitmap;
		private var rect:Rectangle;
		
		private var backgroundColor:uint = 0xFFCC00;
		private var backgroundImage:String = "bg.jpg";
		private var foregroundImage:String = "loading.gif";

		private var isFirstLaunch:Boolean = true;
		private var onFirstLaunch:Boolean = false;
		private var onLocalPageLoad:Boolean  = false;
		private var onRemotePageLoad:Boolean = false;
		private var canMoveAhead:Boolean;
		
		private var app:WebWorksAppTemplate;
		private var webView:QNXStageWebView;

		public function LoadingScreen( x:int, y:int, width:int, height:int) 
		{	
			loadProperties();			
			createLoadingScreen(new Rectangle(x,y,width,height));
		}

		private function createLoadingScreen(rrect:Rectangle):void
		{
			rect = rrect;
			setBackgroundColor();
			canMoveAhead = false;
			
			if (backgroundImage.length > 0) 
			{
				bgImageLoader = new Loader();
				bgImageLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, backgroundImageLoadComplete);
				bgImageLoader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, imageIOError);
				addChild(bgImageLoader);
				bgImageLoader.load(new URLRequest(backgroundImage));
			}
			
			if (foregroundImage.length > 0) 
			{
				fgImageLoader = new Loader();
				fgImageLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, foregroundImageLoadComplete);
				fgImageLoader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, imageIOError);
				addChild(fgImageLoader);
				fgImageLoader.load(new URLRequest(foregroundImage));
			}
		}

		private function imageIOError(event:Event):void
		{
			trace("Image load error:" + event.toString());
		}
		
		private function loadProperties():void
		{
			try
			{
			    var configData:ConfigData = ConfigData.getInstance();
			    backgroundColor = configData.getLoadingScreenColor(); 
			    var obj:Object = configData.getProperty(ConfigConstants.BACKGROUNDIMAGE);
			    if ( obj != null )
    				backgroundImage = obj as String;
	    		obj = configData.getProperty(ConfigConstants.FOREGROUNDIMAGE);
		    	if ( obj != null )
			    	foregroundImage = obj as String;
				obj = configData.getProperty(ConfigConstants.ONFIRSTLAUNCH);
			    if ( obj != null )
				    onFirstLaunch = obj as Boolean;
			    obj = configData.getProperty(ConfigConstants.ONLOCALPAGELOAD);
			    if ( obj != null )
				    onLocalPageLoad  = obj as Boolean;
			    obj = configData.getProperty(ConfigConstants.ONREMOTEPAGELOAD);
			    if ( obj != null )
    				onRemotePageLoad = obj as Boolean;
	    		obj = configData.getProperty(ConfigConstants.ENV_APPLICATION);
		    	if ( obj != null )
			    {	
				    app = obj as WebWorksAppTemplate;
			    }
			    obj = configData.getProperty(ConfigConstants.ENV_WEBVIEW);
			    if ( obj != null )
			    {	
				    webView = obj as QNXStageWebView;
			    }
			}
			catch(error:Error)
			{
				throw new Error("config data errors:" + error.message);
			}
		}
		
		private function foregroundImageLoadComplete(event:Event):void
		{
		  	foreground = event.target.content;
			//position the bitmap in the center of the stage
			if ( foreground != null )
			{
				foreground.x = (rect.width - foreground.width)/2;
				foreground.y = (rect.height - foreground.height)/2;
			}
		}
		private function backgroundImageLoadComplete(event:Event):void
		{
			source = event.target.content;
			resize(rect.width, rect.height, false);
		}
		
		private function setBackgroundColor():void
		{
			var graphic:Graphics = this.graphics;
			graphic.beginFill(backgroundColor);
			graphic.drawRect(rect.x, rect.y, rect.width, rect.height);
			graphic.endFill();
		}
				
		private function resize(maxW:Number, maxH:Number=0, constrainProportions:Boolean=true):void
		{
			maxH = maxH == 0 ? maxW : maxH;
			source.width = maxW;
			source.height = maxH;
			if (constrainProportions) {
				source.scaleX < source.scaleY ? source.scaleY = source.scaleX : source.scaleX = source.scaleY;
			}
		}
		
		public function isLoadingScreenRequired(url:String):Boolean 
		{
			// Skip the first time because it's controlled by onFirstLaunch
			if (!isFirstLaunch)
			{
				var uri:URI = new URI(url);
				if (onLocalPageLoad && (Utilities.isLocalURI(uri) || Utilities.isFileURI(uri))) {
					return true;
				}
				if (onRemotePageLoad && (Utilities.isHttpURI(uri) || Utilities.isHttpsURI(uri))) {
					return true;
				}
			}
			return false;
		}
		
		public function show(url:String):void
		{
			if (showOnFirstLaunch || isLoadingScreenRequired(url)) {
				app.addChild(this);
				webView.zOrder = -1;
				
				if (app.transitionEffect.transitionType != TransitionConstants.TRANSITION_NONE && isLoadingScreenRequired(url)) {
					canMoveAhead = false;
					app.transitionEffect.createEffect();
				} else {
					canMoveAhead = true;
				}
			}
		}
		
		public function hide():void
		{
			if (app.contains(this))
			{
				app.transitionEffect.resetEffect();
		        app.removeChild(this);
				webView.zOrder = 0;
			}
		}
		
		public function hideIfNecessary():void{
			trace("hide necessary");
			if (canMoveAhead) {
				hide();
			} else {
				canMoveAhead = true;
			}
		}

		public function get showOnFirstLaunch():Boolean
		{	
			return onFirstLaunch;
		}
		
		public function get firstLaunchFlag():Boolean
		{
			return isFirstLaunch;
		}
		
		public function clearFirstLaunchFlag():void
		{
			isFirstLaunch = false;
		}		
		
		public function setLoadingScreenArea(rrect:Rectangle):void
		{
			this.x = rrect.x;
			this.y = rrect.y;
			this.width = rrect.width;
			this.height = rrect.height;
		}
	}
}