package devoron.components.hidebuttons
{
	import org.aswing.Component;
	import org.aswing.JPanel;
	import org.aswing.layout.CenterLayout;
	import org.aswing.layout.HorizontalCenterLayout;
	
	/**
	 * HideButtonPanel
	 * @author Devoron
	 */
	public class HideButtonPanel extends JPanel
	{
		public static const LEFT:String = "left";
		public static const RIGHT:String = "right";
		public static const BOTTOM:String = "bottom";
		public static const TOP:String = "top";
		
		public var hideBtn:HideButton;
		
		public function HideButtonPanel(type:String, hideTarget:Component = null, hideTargetContainer:Component = null)
		{
			super(new CenterLayout());
			setPreferredWidth(10);
			
			switch (type)
			{
				case "left": 
					hideBtn = new LeftHideButton(hideTarget, hideTargetContainer);
					break;
				case "right": 
					hideBtn = new RightHideButton(hideTarget, hideTargetContainer);
					break;
				case "bottom": 
					hideBtn = new BottomHideButton(hideTarget, hideTargetContainer);
					break;
				case "top": 
					hideBtn = new BottomHideButton(hideTarget, hideTargetContainer);
					break
			}
			append(hideBtn);
		}
		
		public function getHideTarget():Component
		{
			return hideBtn.getHideTarget();
		}
		
		public function setHideTarget(c:Component):void
		{
			hideBtn.setHideTarget(c);
		}
		
	}

}