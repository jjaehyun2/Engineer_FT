/**
 * Created by newkrok on 23/10/16.
 */
package net.fpp.pandastory.helper
{
	import flash.utils.Dictionary;

	import net.fpp.pandastory.config.character.EvilPandaCharacterVO;
	import net.fpp.pandastory.config.character.PandaCharacterVO;
	import net.fpp.pandastory.vo.CharacterVO;

	public class CharacterVOHelper
	{
		private static var _instance:CharacterVOHelper;

		private var characterVOs:Dictionary;

		public function CharacterVOHelper()
		{
			this.characterVOs = new Dictionary();

			this.characterVOs['Panda'] = PandaCharacterVO;
			this.characterVOs['Evil Panda'] = EvilPandaCharacterVO;
		}

		public function getCharacterVOByName( name:String ):CharacterVO
		{
			return new this.characterVOs[name];
		}

		public static function get instance():CharacterVOHelper
		{
			if ( _instance == null )
			{
				_instance = new CharacterVOHelper();
			}

			return _instance;
		}
	}
}