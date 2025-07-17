/*
   Copyright aswing.org, see the LICENCE.txt.
 */

package devoron.components.darktable
{
	
	import devoron.components.CompoundComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.color.CompositeColorComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.color.ConstColorComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.fourD.FourDCompositeWithOneDComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.fourD.FourDCompositeWithThreeDComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.oneD.OneDValueComponent;
	import devoron.gameeditor.particleeditor.nodeforms.components.threeD.ThreeDValueComponent;
	import flash.display.Sprite;
	import org.aswing.AbstractCellEditor;
	import org.aswing.ASColor;
	import org.aswing.border.LineBorder;
	import org.aswing.Component;
	import org.aswing.Container;
	import org.aswing.ext.Form;
	import org.aswing.geom.IntRectangle;
	import org.aswing.JNumberStepper;
	import org.aswing.JTextField;
	
	/**
	 * The default editor for table and tree cells, use a textfield.
	 * <p>
	 * @author iiley
	 */
	public class DarkTableCompoundCellEditor extends AbstractCellEditor
	{
		protected var compoundComponent:CompoundComponent;
		
		public function DarkTableCompoundCellEditor()
		{
			super();
			setClickCountToStart(2);
		}
		
		override public function startCellEditing(owner:Container, value:*, bounds:IntRectangle):void
		{
			//bounds.y += 1;
			bounds.width = 300;
			bounds.height = 250;
			//bounds.x -= 1.48;
			
			super.startCellEditing(owner, value, bounds);
		}
		
		/**
		 * Subclass override this method to implement specified value transform
		 */ /*protected function transforValueFromText(text:String):*{
		   return text;
		 }*/
		
		override public function getEditorComponent():Component
		{
			if (compoundComponent == null)
			{
				compoundComponent = new CompoundComponent();
			}
			return compoundComponent;
		}
		
		override public function getCellEditorValue():*
		{
			return compoundComponent.getValue();
		}
		
		/**
		 * Sets the value of this cell.
		 * @param value the new value of this cell
		 */
		override protected function setCellEditorValue(value:*):void
		{
			compoundComponent.setValue(value);
		}
		
		public function toString():String
		{
			return "DarkTableCompoundCellEditor[]";
		}
	}
}