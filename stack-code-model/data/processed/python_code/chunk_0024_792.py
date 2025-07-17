/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package devoron.components.darktable
{
	import devoron.components.comboboxes.DSComboBox;
	import org.aswing.ASColor;
	import org.aswing.Container;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.DefaultComboBoxCellEditor;
	import org.aswing.geom.IntRectangle;
	import org.aswing.JComboBox;
	
	/**
	 * The default editor for table and tree cells, use a combobox.
	 * <p>
	 * @author iiley
	 */
	public class DarkTableComboBoxCellEditor extends DefaultComboBoxCellEditor
	{
		
		public function DarkTableComboBoxCellEditor()
		{
			super();
			setClickCountToStart(1);
			
		}
		
		override public function startCellEditing(owner:Container, value:*, bounds:IntRectangle):void 
		{
			bounds.y -= 1.2;
			bounds.height += 6;
			bounds.x -= 1.48;
			bounds.width += 5.1;
			super.startCellEditing(owner, value, bounds);
		}
		
		override public function getComboBox():JComboBox
		{
			if (comboBox == null)
			{
				comboBox = new DSComboBox();
				comboBox.setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), null, 0));
				comboBox.getPopupList().setSelectionBackground(new ASColor(0x000000, 0.04));
			comboBox.getPopupList().setSelectionForeground(new ASColor(0XFFFFFF, 1));
				//comboBox.setBackgroundDecorator(null);
			}
			return comboBox;
		}
		
		override public function toString():String
		{
			return "DarkTableComboBoxCellEditor[]";
		}
	}
}