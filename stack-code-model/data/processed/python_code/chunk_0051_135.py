/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package org.aswing.components.containers
{
	import org.aswing.components.Container;
	import org.aswing.layouts.FlowLayout;
	import org.aswing.layouts.LayoutManager;
	import org.aswing.plaf.basic.BasicPanelUI;
	
	/**
	 * The general container - panel.
	 * @author iiley
	 */
	public class JPanel extends Container
	{
		
		public function JPanel(layout:LayoutManager = null)
		{
			super();
			setName("JPanel");
			if (layout == null)
				layout = new FlowLayout();
			this.layout = layout;
			updateUI();
		}
		
		override public function updateUI():void
		{
			setUI(UIManager.getUI(this));
		}
		
		override public function getDefaultBasicUIClass():Class
		{
			return org.aswing.plaf.basic.BasicPanelUI;
		}
		
		override public function getUIClassID():String
		{
			return "PanelUI";
		}
	}
}