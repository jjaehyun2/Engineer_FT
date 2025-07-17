package com.illuzor.gaftest {
	
	import com.catalystapps.gaf.data.GAFGFXData;
	import starling.core.Starling;
	import starling.display.MovieClip;
	import starling.display.Sprite;
	import starling.events.Event;
	import starling.textures.Texture;
	import starling.textures.TextureAtlas;
	

	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class Game extends Sprite {
		
		public function Game() {
			addEventListener(Event.ADDED_TO_STAGE, onAdded);
		}
		
		private function onAdded(e:Event):void {
			removeEventListener(Event.ADDED_TO_STAGE, onAdded);
			makeMovieClip();
			makeGaf();
		}
		
		private function makeMovieClip():void {
			var atlas:TextureAtlas = new TextureAtlas(Texture.fromBitmap(Assets.beeMcBitmap), Assets.xml);
			trace(atlas);
			var mc:MovieClip = new MovieClip(atlas.getTextures("bee_mc"));
			Starling.juggler.add(mc);
			addChild(mc);
			mc.play();
			mc.fps = 30;
		}
		
		private function makeGaf():void {
			trace(Assets.gafBitmap, Assets.gafConfig);
			var gfxData:GAFGFXData = new GAFGFXData();
			gfxData.addImage(1)
		}
		
	}
}