package
{

	import com.playtika.samples.loadup.ApplicationFacade;

	import flash.display.Sprite;


	public class LoadupUtilAppSkeleton extends Sprite
	{
		public function LoadupUtilAppSkeleton()
		{
			var facade:ApplicationFacade = ApplicationFacade.getInstance();
			facade.startup(this.stage);

		}
	}
}