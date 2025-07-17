/*
 * (C) Copyright 2009 by Open-Plug, All Rights Reserved
 */
package op
{
	import flash.events.EventDispatcher;
	
	import mx.events.CollectionEvent;
	import mx.events.CollectionEventKind;
	
	import openplug.elips.core.ISectionDataProvider;

	public class MyListData extends EventDispatcher implements ISectionDataProvider
	{
		private var dataArray:Array = [
			["Accessory None", "Accessory Disclosure", "Accessory Details", "Accessory Checkmark"],
			["item 1-0", "item 1-1", "item 1-2", "item 1-3", "item 1-4"],
			["item 2-0", "item 2-1", "item 2-2", "item 2-3"],
			["item 3-0", "item 3-1", "item 3-2"],
		];
		
		public function MyListData()
		{
		}

		public function getNumberOfSections():int
		{
			return dataArray.length;
		}
		
		public function getNumberOfItems(section:int):int
		{
			return (dataArray[section] as Array).length;
		}
		
		public function getTitleOfSection(section:int):String
		{
			return "Section " + section;
		}
		
		public function getData(section:int, item:int):Object
		{
			return dataArray[section][item];
		}
	}
}