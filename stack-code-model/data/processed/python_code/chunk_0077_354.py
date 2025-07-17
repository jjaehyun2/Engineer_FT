package devoron.components.hidebuttons
{
	import org.aswing.AssetIcon;
	import org.aswing.Component;
	import org.aswing.event.AWEvent;
	import org.aswing.geom.IntDimension;
	import org.aswing.JToggleButton;
	
	/**
	 * RightHideButton
	 * @author Devoron
	 */
	public class RightHideButton extends HideButton
	{
		[Embed(source="../../../../assets/icons/commons/Hide_arrowLeft_defaultImage.png")]
		private var hideIcon:Class;
		
		[Embed(source="../../../../assets/icons/commons/Hide_arrowLeft_pressedImage.png")]
		private var pressedIcon:Class;
		
		[Embed(source="../../../../assets/icons/commons/Hide_arrowLeft_rolloverImage.png")]
		private var rolloverIcon:Class;
		
		[Embed(source="../../../../assets/icons/commons/Hide_arrowRight_defaultImage.png")]
		private var selectedIcon:Class;
		
		[Embed(source="../../../../assets/icons/commons/Hide_arrowRight_pressedImage.png")]
		private var selectedPressedIcon:Class;
		
		[Embed(source="../../../../assets/icons/commons/Hide_arrowRight_rolloverImage.png")]
		private var selectedRolloverIcon:Class;
		
		public function RightHideButton(hideTarget:Component = null, hideTargetContainer:Component = null)
		{
			super(hideTarget, hideTargetContainer);
			setIcon(new AssetIcon(new hideIcon, 6, 32));
			setPressedIcon(new AssetIcon(new pressedIcon, 6, 32));
			setBackgroundDecorator(null);
			setRollOverIcon(new AssetIcon(new rolloverIcon, 6, 32));
			setSelectedIcon(new AssetIcon(new selectedIcon, 6, 32));
			setRollOverSelectedIcon(new AssetIcon(new selectedRolloverIcon, 6, 32));
			setSize(new IntDimension(6, 32));
			
			addActionListener(onStateChange);
		}
		
		private function onStateChange(e:AWEvent):void
		{
			if (isSelected())
				setPressedIcon(new AssetIcon(new selectedPressedIcon, 6, 32));
			else
				setPressedIcon(new AssetIcon(new pressedIcon, 6, 32));
		}
	
	}

}