package some.useful.classes
{
	import mx.graphics.SolidColorStroke;
	
	import spark.components.HGroup;
	import spark.primitives.Line;

	public class LineGroup extends HGroup
	{
		public function draw(x1:Number, x2:Number, y1:Number, y2:Number):void
		{
			var l:Line = new Line();
			l.stroke = new SolidColorStroke();
			l.xFrom = x1;
			l.xTo = x2;
			l.yFrom = y1;
			l.yTo = y2;
			this.addElement(l);
		}

		public function sayHello():void
		{

		}

		public function sayGoodBye():void
		{

		}
	}
}