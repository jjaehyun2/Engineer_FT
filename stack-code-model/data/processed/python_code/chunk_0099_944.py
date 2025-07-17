package devoron.components.labels 
{
	import org.aswing.AssetIcon;
	/**
	 * ...
	 * @author Devoron
	 */
	public class WarningIcon extends AssetIcon
	{
		[Embed(source="../../../../assets/icons/warning_icon8.png")]
		private var WARNING_ICON16:Class;
		
		public function WarningIcon() 
		{
			super(new WARNING_ICON16);
		}
		
	}

}