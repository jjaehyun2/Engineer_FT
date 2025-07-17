package com.grantech.panels
{
	import feathers.controls.LayoutGroup;
	import feathers.layout.HorizontalAlign;
	import feathers.layout.VerticalAlign;
	import feathers.layout.VerticalLayout;
	import feathers.layout.VerticalLayoutData;

	public class SidebarPanel extends LayoutGroup
	{
		public function SidebarPanel()
		{
			super();
		}

		override protected function initialize():void
		{
			super.initialize();
			
			var containerLayout:VerticalLayout = new VerticalLayout();
			containerLayout.horizontalAlign = HorizontalAlign.JUSTIFY;
			containerLayout.verticalAlign = VerticalAlign.JUSTIFY;
			this.layout = containerLayout;

			var inspectorPanel:InspectorPanel = new InspectorPanel();
			inspectorPanel.layoutData = new VerticalLayoutData(NaN, 60);
			this.addChild(inspectorPanel);

			var layersPanel:LayersPanel = new LayersPanel();
			layersPanel.layoutData = new VerticalLayoutData(NaN, 40);
			this.addChild(layersPanel);
		}
	}
}