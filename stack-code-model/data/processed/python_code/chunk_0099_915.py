package devoron.components.darktable 
{
	import devoron.components.comboboxes.DSComboBox;
	import org.aswing.ASColor;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.JComboBox;
	/**
	 * ...
	 * @author ...
	 */
	public class TypeCellEditor extends DarkTableComboBoxCellEditor
	{
		
		public function TypeCellEditor() 
		{
			
		}
		

		override public function getComboBox():JComboBox
		{
			if (comboBox == null)
			{
				comboBox = new DSComboBox(["String", "Number", "uint", "int", "Boolean", "Array", "Date", "Error", "Function", "RegExp", "XML", "XMLList"]);
				comboBox.setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), null, 0));
				//comboBox.setBackgroundDecorator(null);
			}
			return comboBox;
		}
		
	}

}