package com.appfw.view.unit
{
	import starling.display.MovieClip;
	import starling.textures.TextureAtlas;
	
	public class ArmyUnit
	{
		private var _mc:MovieClip;
		
		public function ArmyUnit()
		{
		}
		
		public function resetTextureAtlas(tas:TextureAtlas):void
		{
			if(_mc)
			{
//				_mc = new MovieClip(
			}
		}

		public function get mc():MovieClip
		{
			return _mc;
		}

	}
}