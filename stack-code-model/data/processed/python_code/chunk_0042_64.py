package src.game.module.help
{
	import net.fpp.common.starling.module.AModule;

	import src.game.module.help.events.HelpModuleEvent;
	import src.game.module.help.view.HelpModuleView;

	public class HelpModule extends AModule
	{
		private const HELP_TEXTS:Vector.<Vector.<String>> = new <Vector.<String>> [
			new <String> [
				"Touch right arrows to accelerate or to brake.".toUpperCase(),
				"Touch left arrows to lean back or to lean front with the car.".toUpperCase(),
				"Collect Coins to earn more score.".toUpperCase(),
				"Do back flip, front flip, wheelie or nice air time to earn more score.".toUpperCase(),
				"Good luck, have a nice ride!".toUpperCase(),
			],
			new <String> [
				'It is hard to drive on places covered with snow.'.toUpperCase(),
				'Be careful in the blizzard!'.toUpperCase(),
			],
			new <String> [
				'Watch out for the crates, they can be moved easily.'.toUpperCase()
			],
			new <String> [
				'description...'.toUpperCase()
			]
		];

		private var _onComplete:Function;

		public function HelpModule( worldId:int, onComplete:Function ):void
		{
			this._view = this.createModuleView( HelpModuleView ) as HelpModuleView;
			this._view.addEventListener( HelpModuleEvent.CLOSE_REQUEST, this.onCloseRequest );

			( this._view as HelpModuleView ).setHelpText( this.HELP_TEXTS[ worldId ] );
			( this._view as HelpModuleView ).setWorldId( worldId );

			this._onComplete = onComplete;
		}

		private function onCloseRequest( e:HelpModuleEvent ):void
		{
			this._onComplete.call( this, e );
		}

		override public function dispose():void
		{
			this._view.removeEventListener( HelpModuleEvent.CLOSE_REQUEST, this.onCloseRequest );

			this._onComplete = null;

			super.dispose();
		}
	}
}