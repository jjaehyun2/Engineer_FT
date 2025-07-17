package devoron.components.labels
{
	import net.kawa.tween.easing.Linear;
	import net.kawa.tween.KTween;
	import org.aswing.AssetIcon;
	import org.aswing.geom.IntDimension;
	import org.aswing.JDropDownButton;
	import org.aswing.JLabel;
	
	/**
	 * WarningLabel
	 * @author Devoron
	 */
	public class WarningLabel extends JDropDownButton
	{
		[Embed(source="../../../../assets/icons/managers/FileChooser/warning_icon16.png")]
		private static const WARNING_ICON:Class;
		
		public function WarningLabel()
		{
			super("", new AssetIcon(new WARNING_ICON));
			setPreferredSize(new IntDimension(24, 24));
			setSize(new IntDimension(24, 24));
			getDropDownButtonUI().getDropDownButton().removeFromContainer();
		}
		
		override public function setVisible(v:Boolean):void
		{
			/*if (!transtions)
			   {
			   super.setVisible(v);
			   }
			   else
			 {*/
			if (v)
			{
				alpha = 0;
				super.setVisible(true);
				KTween.to(this, 0.15, {alpha: 1}, Linear.easeIn).init();
			}
			else
			{
				//super.setVisible(false);
				KTween.to(this, 0.08, {alpha: 0}, Linear.easeIn, onCompile).init();
			}
		
			//}
		}
		
		private function onCompile():void
		{
			super.setVisible(false);
		}
	
	}

}