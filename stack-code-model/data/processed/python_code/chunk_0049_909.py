package com.illuzor.airlab.screens.mainScreens {
	
	import com.illuzor.airlab.constants.Screens;
	import feathers.controls.Header;
	import feathers.controls.List;
	import feathers.controls.Screen;
	import feathers.data.ListCollection;
	import feathers.skins.StandardIcons;
	import starling.events.Event;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	internal class MainMenu extends Screen {
		
		private var list:List;
		private var header:Header;

		override protected function initialize():void {
			header = new Header();
			header.title = "AIR Lab";
			addChild(header);
	
			list = new List();
			addChild(list);
			fillList();
		}
		
		override protected function draw():void {
			header.width = actualWidth;
			list.y = header.height;
			list.width = actualWidth;
			list.height = actualHeight - header.height;
		}
		
		private function fillList():void {
			var extensions:Array = Screens.mainMenu;
			list.dataProvider = new ListCollection(extensions);
			list.itemRendererProperties.labelField = "name";
			list.itemRendererProperties.accessoryTextureFunction = function(item:Object):Texture {
				return StandardIcons.listDrillDownAccessoryTexture;
			}
			list.addEventListener(Event.CHANGE, listChanged);
		}
		
		private function listChanged(e:Event):void {
			list.removeEventListener(Event.CHANGE, listChanged);
			dispatchEventWith("sectionSelected", false, list.selectedItem);
		}
		
	}

}