package some.external.lib
{
	import spark.components.Panel;
	
	public class Board extends Panel
	{
		public function drawBoardItem(item:BoardItem, x1:Number, x2:Number, y1:Number, y2:Number, msg:String):void
		{
			item.drawLine(x1, x2, y1, y2);
			item.drawText(msg);
			this.addElement(item);
		}
	}
}