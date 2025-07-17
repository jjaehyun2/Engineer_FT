package com.illuzor.airlab.screens.mainScreens {
	
	import com.illuzor.airlab.constants.Screens;
	import feathers.controls.Button;
	import feathers.controls.Header;
	import feathers.controls.List;
	import feathers.controls.Screen;
	import feathers.data.ListCollection;
	import feathers.skins.StandardIcons;
	import starling.display.DisplayObject;
	import starling.events.Event;
	import starling.textures.Texture;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	internal class Section extends Screen {
		
		private var list:List;
		private var header:Header;
		private var backbutton:Button;

		override protected function initialize():void {
			header = new Header();
			header.title = Screens.currentScreenName;
			addChild(header);
			
			backbutton = new Button();
			backbutton.label = "Back";
			backbutton.addEventListener(Event.TRIGGERED, onBack);
			header.rightItems = new <DisplayObject>[backbutton];
	
			list = new List();
			addChild(list);
			fillList();
		}
		
		override protected function draw():void {
			header.width = actualWidth;
			list.y = header.height;
			list.width = actualWidth;
			list.height = actualHeight - header.height;
			
			backbutton.x = actualWidth - backbutton.width - 20;
		}
		
		private function fillList():void {
			var extensions:Array = Screens.currentSelectedScreen;
			list.dataProvider = new ListCollection(extensions);
			list.itemRendererProperties.labelField = "name";
			list.itemRendererProperties.accessoryTextureFunction = function(item:Object):Texture {
				return StandardIcons.listDrillDownAccessoryTexture;
			}
			list.addEventListener(Event.CHANGE, listChanged);
		}
		
		private function onBack(e:Event):void {
			dispatchEventWith("goBack");
		}
		
		private function listChanged(e:Event):void {
			list.removeEventListener(Event.CHANGE, listChanged);
			//dispatchEventWith("sectionSelected", false, list.selectedItem);
		}
		
	}

}