package devoron.components.comboboxes{
	import org.aswing.Component;
	import org.aswing.geom.IntDimension;
	import org.aswing.geom.IntRectangle;
	import org.aswing.graphics.Graphics2D;
	import org.aswing.Insets;
	import org.aswing.JButton;
	import org.aswing.skinbuilder.SkinComboBoxUI;

public class TextCBUI extends SkinComboBoxUI {
		
		public function TextCBUI() {
			super();
		}
		
		override public function paint(c:Component, g:Graphics2D, b:IntRectangle):void {
			layoutCombobox();
			dropDownButton.setEnabled(true);
		}
	
		override protected function createDropDownButton():Component {
		
			var btn:JButton = new JButton("", new GrayArrowIcon());
			btn.setFocusable(false);
			btn.setPreferredSize(new IntDimension(16, 16));
			btn.setBackgroundDecorator(null);
			btn.setMargin(new Insets());
			btn.setBorder(null);
			//make it proxy to the combobox
			btn.setMideground(null);
			btn.setStyleTune(null);
			return btn;
		}
		
		
		
	}
}




import flash.display.DisplayObject;
import flash.display.Sprite;
import flash.geom.Point;
import org.aswing.ASColor;
import org.aswing.Component;
import org.aswing.graphics.Graphics2D;
import org.aswing.graphics.Pen;
import org.aswing.graphics.SolidBrush;
import org.aswing.Icon;
	
	/**
	 * Иконка стрелки.
	 */
	class GrayArrowIcon implements Icon{
	
	public function GrayArrowIcon(){
	}
	
	/* INTERFACE org.aswing.Icon */
	
	public function getIconWidth(c:Component):int 
	{
		return 5;
	}
	
	public function getIconHeight(c:Component):int 
	{
		return 5;
	}
	
	public function updateIcon(c:Component, g:Graphics2D, x:int, y:int):void 
	{
		g.beginFill(new SolidBrush(new ASColor(0x000000, 0.24)));
		//g.drawPolygon(new Pen(new ASColor(0x000000, 0)), new Array(new Point(0, 5.3), new Point(10, 5.3), new Point(5, 10)));
		g.drawPolygon(new Pen(new ASColor(0x000000, 0)), new Array(new Point(0, 6.3), new Point(10, 6.3), new Point(5, 11)));
		g.endFill();
	}
	
	public function getDisplay(c:Component):DisplayObject 
	{
		return new Sprite();
	}
}