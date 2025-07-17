package  
{
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.external.ExternalInterface;
	/**
	 * ...
	 * @author Jake
	 */
	public class PrinterTable extends Sprite
	{
		private var currentX:int;
		private var currentY:int = -45;
		
		private var cellsPerRow:int = 6;
		private var cellsPerColumn:int = 20;
		
		private var pageStage:Stage;
		private var blocks:int;
		private var blockWidth:Number;
		private var blockHeight:Number;
		
		private var tableWidth:int;
		private var tableHeight:int;
		
		public function PrinterTable(stage:Stage,width:int,height:int) 
		{
			pageStage = stage;
			tableWidth = width;
			tableHeight = height;
		}
			
		public function buildPrinter(printer:PrinterObject):void
		{
			if (blocks % 7 == 0) 
			{
				blocks = 0;
				currentX = 2;
				currentY += 50;
			}
			blocks += 1;
			var newPrinter:Printer = new Printer(currentX, currentY,printer);
			currentX += 97;
			addChild(newPrinter);
			
		}
		
		
	}

}