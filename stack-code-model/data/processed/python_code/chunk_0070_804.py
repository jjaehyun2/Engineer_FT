/**
 * Created by newkrok on 16/10/16.
 */
package net.fpp.pandastory.game.service.websocketservice
{
	import net.fpp.common.starling.module.IService;

	public interface IWebSocketService extends IService
	{
		function connect():void;

		function join( characterTypeName:String ):void;

		function sync( data:Object ):void;
	}
}