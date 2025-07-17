package layer.tooltip.common {
	import org.as3commons.ui.layer.tooltip.ToolTipAdapter;
	import flash.display.DisplayObject;
	import flash.geom.Point;

	public class SimpleAdapter extends ToolTipAdapter {
		override protected function onToolTip(toolTip : DisplayObject) : void {
			offset = new Point(-5, 5);
		}

		override protected function onContent(toolTip : DisplayObject, content : *) : void {
			SimpleToolTip(toolTip).text = content;
		}
	}
}