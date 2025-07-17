package com.lowoui_as.config
{
	import com.lowoui_as.sample.config.lang.Lang;
	import com.lowoui_as.sample.config.lang.LangTyp;
	import com.lowoui_as.sample.config.lang.ZH_CN;
	//import com.lowoui_as.sample.config.lang.EN_US;

	public class ConfigLang
	{
		public static var curTyp:String = LangTyp.Lang_ZH_CN;

		public static function get Type():Lang {
			var t = null;

			switch (curTyp)
			{
				case LangTyp.Lang_ZH_CN:
					t = ZH_CN.ins;
					break;
				default:
					break;
			}

			return t;
		}

		//public static var Common          = Type["Common_"];
		//public static var Charpters       = Type["Charpters_"];
	}
}