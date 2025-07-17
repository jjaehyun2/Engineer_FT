package com.playtika.samples.loadup.model
{

	import com.playtika.samples.loadup.ApplicationFacade;
	import com.playtika.samples.loadup.model.vo.SectionVO;

	import flash.events.*;
	import flash.net.URLLoader;
	import flash.net.URLRequest;

	import org.puremvc.as3.multicore.utilities.loadup.interfaces.ILoadupProxy;


	public class SiteDataProxy extends EntityProxy implements ILoadupProxy
	{
		public static const NAME:String = "SiteDataProxy";
		public static const SRNAME:String = "SiteDataSRProxy";

		public function SiteDataProxy()
		{
			super(NAME);
		}

		public function load():void
		{
			sendNotification(ApplicationFacade.SITE_DATA_LOADING);

			var request:URLRequest = new URLRequest("classes/data.xml");
			var loader:URLLoader = new URLLoader();

			loader.addEventListener(IOErrorEvent.IO_ERROR, errorHandler);
			loader.addEventListener(Event.COMPLETE, loaderCompleteHandler);

			loader.load(request);
		}

		private function loaderCompleteHandler(event:Event):void
		{
			var xml:XML = new XML(event.target.data);
			xml.ignoreWhitespace = true;

			var title:String = xml.title.children().toXMLString();
			var sections:Array = [];
			var sectionsXMLList:XMLList = xml.sections.section;

			for (var i:uint = 0; i < sectionsXMLList.length(); i++)
			{
				var section:XML = sectionsXMLList[i];
				var id:uint = section.@id;
				var sectionVO:SectionVO = new SectionVO(id, section.@label, section.content);
				sections.push(sectionVO);
			}

			data = {};
			data.title = title;
			data.sections = sections;

			sendLoadedNotification(ApplicationFacade.SITE_DATA_LOADED, NAME, SRNAME);
		}

		private function errorHandler(e:IOErrorEvent):void
		{
			sendLoadedNotification(ApplicationFacade.SITE_DATA_FAILED, NAME, SRNAME);
		}

		public function get title():String
		{
			return data.title as String;
		}

		public function get sections():Array
		{
			return data.sections as Array;
		}

	}
}