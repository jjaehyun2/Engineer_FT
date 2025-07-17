package some.external.lib
{
	import spark.components.Panel;
	
	public class Board extends Panel
	{
		public function drawBoardItem(item:BoardItem, x1:Number, x2:Number, y1:Number, y2:Number):void
		{
			item.drawLine(x1, x2, y1, y2);
			this.addElement(item.getVisualElement());
		}
	}
}