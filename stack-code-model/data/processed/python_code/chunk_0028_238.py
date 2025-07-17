/**
 * Created by newkrok on 21/08/16.
 */
package net.fpp.pandastory.menu.handler
{
	import net.fpp.common.starling.module.AHandler;
	import net.fpp.common.starling.module.IApplicationContext;
	import net.fpp.pandastory.config.character.EvilPandaCharacterVO;
	import net.fpp.pandastory.config.character.PandaCharacterVO;
	import net.fpp.pandastory.vo.PlayerInfoVO;

	import starling.display.Button;
	import starling.events.Event;

	public class StartGameHandler extends AHandler
	{
		[Inject]
		public var applicationContext:IApplicationContext;

		[Inject]
		public var playerInfoVO:PlayerInfoVO;

		private var _startGameButtonA:Button;
		private var _startGameButtonB:Button;

		public function StartGameHandler( startGameButtonA:Button, startGameButtonB:Button )
		{
			this._startGameButtonA = startGameButtonA;
			this._startGameButtonA.addEventListener( Event.TRIGGERED, this.onStartGameButtonATriggered );

			this._startGameButtonB = startGameButtonB;
			this._startGameButtonB.addEventListener( Event.TRIGGERED, this.onStartGameButtonBTriggered );
		}

		private function onStartGameButtonATriggered( e:Event ):void
		{
			this.playerInfoVO.characterVO = new PandaCharacterVO;

			this.applicationContext.dispose();
		}

		private function onStartGameButtonBTriggered( e:Event ):void
		{
			this.playerInfoVO.characterVO = new EvilPandaCharacterVO;

			this.applicationContext.dispose();
		}

		override public function dispose():void
		{
			this._startGameButtonA.removeEventListener( Event.TRIGGERED, this.onStartGameButtonATriggered );
			this._startGameButtonA = null;

			this._startGameButtonB.removeEventListener( Event.TRIGGERED, this.onStartGameButtonBTriggered );
			this._startGameButtonB = null;

			this.applicationContext = null;
		}
	}
}