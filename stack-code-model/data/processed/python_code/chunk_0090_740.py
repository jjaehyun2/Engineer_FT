package com.illuzor.otherside.controllers.resource {
	
	import com.illuzor.otherside.errors.ControllerError;
	import com.illuzor.otherside.errors.ResourceControllerError;
	import com.illuzor.otherside.events.ResourceControllerEvent;
	import com.illuzor.otherside.interfaces.IResourceController;
	import com.illuzor.otherside.Settings;
	import com.illuzor.otherside.tools.AssetsFlash;
	import com.illuzor.otherside.utils.intArrayToVector;
	import flash.media.SoundChannel;
	import starling.events.EventDispatcher;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	import starling.utils.AssetManager;

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	internal final class ResourceControllerFlash extends EventDispatcher implements IResourceController {
		
		private var _isMobile:Boolean = false;
		private var assetManager:AssetManager;
		
		public function initialLoad():void {
			assetManager = new AssetManager();
			assetManager.enqueue(AssetsFlash);
			assetManager.loadQueue(onLoad);
		}
		
		private function onLoad(aspect:Number):void {
			if (aspect >= 1) {
				dispatchEvent(new ResourceControllerEvent(ResourceControllerEvent.INITIAL_LOAD_COMPLETE));	
			}
		}
		
		public function loadResources(data:Object):void {}
		
		public function getAtlas(atlasName:String):TextureAtlas {
			var atlas:TextureAtlas = assetManager.getTextureAtlas(atlasName);
			if (!atlas) {
				throw new ControllerError("ResourceControllerMobile.getAtlas(). Incorrect atlas: " + atlasName);
				return null;
			}
			return atlas;
		}
		
		public function getTexture(atlasName:String, textureName:String):Texture {
			var atlas:TextureAtlas = assetManager.getTextureAtlas(atlasName);
			if (!atlas) {
				throw new ControllerError("ResourceControllerMobile.getTexture(). Incorrect atlas: " + atlasName + "texture: " + textureName);
				return null;
			}
			return atlas.getTexture(textureName);
		}
		
		public function getLevelConfig(zone:uint = 1, level:uint = 1):Object {
			return assetManager.getObject("zone" + String(zone)+"level" + String(level));
		}
		
		public function getCurve(id:String):Object {
			if (assetManager.getObject("curves").hasOwnProperty[id]) {
				var curve:Object = assetManager.getObject("curves")[id];
				curve.x = intArrayToVector(curve.x);
				curve.y = intArrayToVector(curve.y);
				return curve;
			}
			throw new ResourceControllerError("getCurve(): curve id " + id + " is not exist");
			return null;
		}
		
		public function getCurves(ids:Array):Object {
			var curves:Object = new Object();
			for (var i:int = 0; i < ids.length; i++) {
				var id:String = String(ids[i]);
				if (assetManager.getObject("curves").hasOwnProperty(id)) {
					curves[id] = assetManager.getObject("curves")[id];
					curves[id].x = intArrayToVector(curves[id].x);
					curves[id].y = intArrayToVector(curves[id].y);
				} else {
					throw new ResourceControllerError("getCurves(): curve id " + id + " is not exist");
					return null;
				}
			}
			return curves;
		}
		
		public function playMusic(musicName:String):void {
			
		}
		
		public function pauseMusic():void {
			
		}
		
		public function playSound(soundName:String, loops:uint = 0):SoundChannel {
			return null;
		}
		
		public function get isMobile():Boolean {
			return _isMobile;
		}
		
		public function get lang():Object {
			return assetManager.getObject(Settings.lang);
		}
		
	}
}