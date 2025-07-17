package com.losttemple.templates
{
	import com.engine.templates.ITemplate;
	import com.losttemple.templates.base.Template;

	public class RaceTemplate extends Template
	{
		public static const TYPE:String = "race";
		
		public function RaceTemplate()
		{
			super();
		}
		
		public function get desctxt():String
		{
			return crtData["desctxt"];
		}
		
		public function get raceskill():Number
		{
			return Number(crtData["raceskill"]);
		}
		
		public static function getTemplate(id:Number):RaceTemplate
		{
			var temp:ITemplate = Template.getTemp(TYPE);
			return temp.getTempById(id) as RaceTemplate;
		}
	}
}