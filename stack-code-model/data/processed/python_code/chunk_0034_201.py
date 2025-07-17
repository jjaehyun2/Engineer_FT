package org.aswing 
{
	import flash.display.Shape;
	import flash.filters.DropShadowFilter;
	import org.aswing.ASColor;
	import org.aswing.JTable;
	import org.aswing.table.DefaultTextHeaderCell;
	import org.aswing.table.JTableHeader;
	import org.aswing.UIManager;
	
	/**
	 * Render для заголовочной ячейки таблицы аниматоров.
	 * @author DEVORON
	 */
	public class TableTextHeaderCell extends DefaultTextHeaderCell 
	{
		
		/**
		 * Конструктор класса.
		 */
		public function TableTextHeaderCell() {
		super();
		//setHorizontalAlignment(CENTER);
		//setBorder(UIManager.getBorder("TableHeader.cellBorder"));
		setBackgroundDecorator(UIManager.getGroundDecorator("TableHeader.cellBackground"));
		//UIManager.getGroundDecorator("TableHeader.cellBackground")
		//var sh:Shape = new Shape();
		//var pen:Pen = new Pen(sh.graphics);
		//pen.beginFill(0x313722, 0.7);
		//pen.lineStyle(0, 0, 0);
		//pen.drawRect(1, 0, 247, 15);
		//pen.endFill();
		//
		//setBackgroundChild(sh);
		//setOpaque(true);
		setTextFilters([new DropShadowFilter(1, 45, 0XD251CC, 0.2, 1, 1, 1, 1)]);
	}
	
	override public function setTableCellStatus (table:JTable, isSelected:Boolean, row:int, column:int) : void{
		var header:JTableHeader = table.getTableHeader();
		if (header != null) {
			//setBackground(header.getBackground());
			setBackground(ASColor.getASColor(57, 53, 45, 0.4));
			//setForeground(header.getForeground());
			setForeground(ASColor.getASColor(255, 255, 255, 0.8));
			setFont(header.getFont());
		}
	}
		
		
		
	}

}