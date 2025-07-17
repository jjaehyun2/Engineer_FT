package devoron.components.multicontainers.table 
{
	import flash.geom.Matrix;
	import org.aswing.ASColor;
	import org.aswing.decorators.GradientBackgroundDecorator;
	import org.aswing.table.JTableHeader;
	import org.aswing.table.TableColumnModel;
	/**
	 * ...
	 * @author Devoron
	 */
	public class TableHeaderCustom extends JTableHeader
	{
		
		public function TableHeaderCustom(cm:TableColumnModel) 
		{
			super(cm);
			setBackgroundChild(null);
			
				var colors:Array = [0x000000, 0x000000, 0x000000, 0x000000, 0x000000];
			var alphas:Array = [0.24, 0.14, 0.08, 0.04, 0.01];
			var ratios:Array = [0, 70, 145, 200, 255];
			var matrix:Matrix = new Matrix();
			matrix.createGradientBox(270, 22, 0, 0, 0);
			//super.getTableHeader().set
			setBackgroundChild(null);
			setBackgroundDecorator(new GradientBackgroundDecorator(GradientBackgroundDecorator.LINEAR, colors, alphas, ratios, matrix, "pad", "rgb", 0, new ASColor(0xFFFFFF, 0), 2));
		}
		
	}

}