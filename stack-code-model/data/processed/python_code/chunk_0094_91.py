/**
 * Created by newkrok on 16/10/16.
 */
package net.fpp.pandastory.game.service.websocketservice.parser
{
	import flash.utils.Dictionary;

	import net.fpp.common.starling.module.IParser;
	import net.fpp.pandastory.config.CharacterDataSyncConfig;
	import net.fpp.pandastory.game.service.websocketservice.vo.CharacterModuleSyncDataVO;

	public class SyncDataParser implements IParser
	{
		private var _syncKeys:Dictionary;

		public function SyncDataParser( characterDataSyncConfig:CharacterDataSyncConfig )
		{
			this._syncKeys = characterDataSyncConfig.getSyncKeyConfig();
		}

		public function parse( rawData:Object ):Object
		{
			var characterModuleSyncDataVO:CharacterModuleSyncDataVO = new CharacterModuleSyncDataVO();

			for( var key:String in rawData )
			{
				characterModuleSyncDataVO[ _syncKeys[ key ] ] = rawData[ key ];
			}

			return characterModuleSyncDataVO;
		}
	}
}