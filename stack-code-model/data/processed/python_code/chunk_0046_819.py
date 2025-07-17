package com.losttemple.templates
{
	import com.engine.templates.ITemplate;
	import com.losttemple.templates.base.Template;

	public class SkillTemplate extends Template
	{
		public static const TYPE:String = "skill";
		
		/**
		 * eg:SkillTemplate.getTemplate(10001).name
		 */		
		public function SkillTemplate()
		{
			super();
		}
		
		public function get desctxt():String
		{
			return crtData["desctxt"];
		}
		
		public function get costmp():Number
		{
			return Number(crtData["costmp"]);
		}
		
		public function get dhp():Number
		{
			return Number(crtData["dhp"]);
		}
		
		public function get ddef():Number
		{
			return Number(crtData["ddef"]);
		}
		
		public function get targettype():Number
		{
			return Number(crtData["targettype"]);
		}
		
		public function get rounds():Number
		{
			return Number(crtData["rounds"]);
		}
		
		public function get prop():Number
		{
			return Number(crtData["prop"]);
		}
		
		public static function getTemplate(id:Number):SkillTemplate
		{
			var temp:ITemplate = Template.getTemp(TYPE);
			return temp.getTempById(id) as SkillTemplate;
		}
	}
}