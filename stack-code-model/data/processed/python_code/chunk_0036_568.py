/**
 * Created by Dukobpa3 on 12/21/13.
 */
package gd.eggs.samples.simpleserver.app
{
	import flash.display.Sprite;

	import org.puremvc.as3.multicore.patterns.facade.Facade;


	public class MainFacade extends Facade
	{
		public static const NAME:String = "appFacade";

		private static var instance:MainFacade;

		public function MainFacade()
		{
			super(NAME);
		}

		public static function getInstance():MainFacade
		{
			return instance ||= new MainFacade();
		}

		public function startup(main:Sprite):void {}

	}
}