package com.fp.templates
{
	import com.engine.templates.ITemplate;
	import com.fp.templates.base.Template;

	public class HeroTemplate extends Template
	{
		public static const TYPE:String = "hero";
		
		/**
		 * eg:HeroTemplate.getTemplate(10001).getCrtProp("datas");
		 * eg2:HeroTemplate.getTemplate(10001).datas;
		 */	
		public function HeroTemplate()
		{
			super();
		}
		
		public function get desctxt():String
		{
			return getCrtProp("desctxt") + "";
		}
		
		public function get armytype():int
		{
			return int(getCrtProp("armytype"));
		}
		
		public function get basehp():int
		{
			return int(getCrtProp("basehp"));
		}
		
		public function get baseatk():int
		{
			return int(getCrtProp("baseatk"));
		}
		
		public function get basedef():int
		{
			return int(getCrtProp("basedef"));
		}
		
		public function get fighteff():int
		{
			return int(getCrtProp("fighteff"));
		}
		
		public static function getTemplate(id:Number):HeroTemplate
		{
			var temp:ITemplate = Template.getTemp(TYPE);
			return temp.getTempById(id) as HeroTemplate;
		}
	}
}