package com.losttemple.assets
{
	import com.fw.view.comps.style.StyleDef;
	
	import flash.geom.Rectangle;
	import flash.text.TextFormat;
	import flash.text.TextFormatAlign;
	
	import feathers.textures.Scale9Textures;
	
	import starling.textures.Texture;
	import starling.utils.AssetManager;
	
	public class Assets
	{
		private static var _instance:Assets;
		
		public var assetMgr:AssetManager;
		
		// 以下为文本格式
		public var defTextFmt:TextFormat;
		
		// 以下为资源命名
		public var ui_head_bar_bg_Texture:Texture;
		public var ui_head_bar_bg_S9Texture:Scale9Textures;
		public var ui_btn2_normal_Texture:Texture;
		public var ui_btn2_normal_S9Texture:Scale9Textures;
		public var ui_btn2_selected_Texture:Texture;
		public var ui_btn2_selected_S9Texture:Scale9Textures;
		public var ui_tab_bg_Texture:Texture;
		public var ui_tab_bg_S9Texture:Scale9Textures;
		public var ui_wnd_back_normal_Texture:Texture;
		public var ui_wnd_back_selected_Texture:Texture;
		public var ui_info_bg_Texture:Texture;
		public var ui_info_bg_S9Texture:Scale9Textures;
		public var ui_battle_stage_info_bg_Texture:Texture;
		public var ui_battle_stage_info_bg_S9Texture:Scale9Textures;
		
		public function Assets()
		{
		}
		
		public static function get instance():Assets
		{
			return _instance ||= new Assets();
		}
		
		private function initTextformat():void
		{
			defTextFmt = new TextFormat(StyleDef.FONT_NAME_FZY4, StyleDef.FONT_SIZE_16, StyleDef.FONT_COLOR_WHITE,
				true, false, false, "", "", TextFormatAlign.LEFT, 0, 0, 0 , 0);
		}
		
		private function initTexture():void
		{
			ui_head_bar_bg_Texture = assetMgr.getTexture("ui_head_bar_bg");
			ui_head_bar_bg_S9Texture = new Scale9Textures(ui_head_bar_bg_Texture, new Rectangle(130, 0, 20, 105));
			ui_btn2_normal_Texture = assetMgr.getTexture("ui_btn2_normal");
			ui_btn2_normal_S9Texture = new Scale9Textures(ui_btn2_normal_Texture, new Rectangle(30, 0, 30, 86));
			ui_btn2_selected_Texture = assetMgr.getTexture("ui_btn2_selected");
			ui_btn2_selected_S9Texture = new Scale9Textures(ui_btn2_selected_Texture, new Rectangle(30, 0, 30, 86));
			ui_tab_bg_Texture = assetMgr.getTexture("ui_tab_bg");
			ui_tab_bg_S9Texture = new Scale9Textures(ui_tab_bg_Texture, new Rectangle(10, 20, 6, 6));
			ui_wnd_back_normal_Texture = assetMgr.getTexture("ui_btn_to_right_normal");
			ui_wnd_back_selected_Texture = assetMgr.getTexture("ui_btn_to_right_selected");
			ui_info_bg_Texture = assetMgr.getTexture("ui_info_bg");
			ui_info_bg_S9Texture = new Scale9Textures(ui_info_bg_Texture, new Rectangle(20, 20, 6, 6));
			ui_battle_stage_info_bg_Texture = assetMgr.getTexture("ui_battle_stage_info_bg");
			ui_battle_stage_info_bg_S9Texture = new Scale9Textures(ui_battle_stage_info_bg_Texture, new Rectangle(20, 30, 6, 6));
		}
		
		public function init():void
		{
			initTextformat();
			initTexture();
		}
	
	}
}