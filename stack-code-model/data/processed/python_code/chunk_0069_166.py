package com.lowoui_as.config
{
	//import scaleform.gfx.Extensions;

	public class ConfigAsset
	{
		//image
		public static var Common:String = "img://Texture2D'ProjCommon.";
		public static var Item:String = "img://Texture2D'ProjCommonItem.";
		public static var Suit:String = "img://Texture2D'ProjCommonSuit.";
		public static var Weapon:String = "img://Texture2D'ProjCommonWeapon.";
		public static var RoleClass:String = "img://Texture2D'ProjCommonClass.";
		public static var Skill:String = "img://Texture2D'ProjCommonSkill.";
		public static var Rune:String = "img://Texture2D'ProjCommonRune.";
		public static var Pickup:String = "img://Texture2D'ProjCommonPickup.";

		public static var CommonGFxPlayer:String = "../ProjCommon/common/";
		public static var ItemGFxPlayer:String = "../ProjCommonItem/commonItem/";

		/**
		 * -----------------------------------------
		 * don't use swf source path like this ...
		 * -----------------------------------------
		 * "SwfMovie'ProjLogin.Proj_login'";
		 */
		public static var BgSWF:String = "../bg/bg.swf";
		public static var ComponentSWF:String = "../component/component.swf";
		public static var ChapterSWF:String = "../chapter/chapter.swf";
		public static var HudSWF:String = "../hud/hud.swf";
		public static var MinimapSWF:String = "../minimap/minimap.swf";

		public static var YesNoDialogSWF:String = "../Dialog/dialog_yesno.swf";
		public static var YesDialogSWF:String = "../Dialog/dialog_yes.swf";
		public static var NoticeDialogSWF:String = "../Dialog/dialog_notice.swf";

		public static function imgURL(itemClass:String, itemName:String):String
		{
			//take weapon resource for example
			//_url = "img://Texture2D'ProjCommonWeapon." + itemName + "'";
			//_url = "../ProjCommonWeapon/proj_commonWeapon/" + itemName + ".png";

			var _url:String;
			//if (Extensions.isGFxPlayer)
			//{
				//_url = AssetPath[itemClass + "GFxPlayer"] + itemName + ".png";
			//}
			//else
			//{
				_url = ConfigAsset[itemClass] + itemName + "'";
			//}

			return _url;
		}

		public static function swfURL(widgetName:String):String
		{
			var _url:String;
			_url = ConfigAsset[widgetName + "SWF"];

			return _url;
		}
	}
}