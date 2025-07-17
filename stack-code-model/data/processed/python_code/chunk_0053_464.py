package com.adobe.tabletdashboard.view.components
{
	import skins.buttons.RightToggleButtonSkin;

	import spark.components.ButtonBarButton;

	public class DashboardRightButtonBarButton extends ButtonBarButton
	{
		public function DashboardRightButtonBarButton()
		{
			super();
			this.setStyle("skinClass", RightToggleButtonSkin);
			this.width=100;
		}
	}
}