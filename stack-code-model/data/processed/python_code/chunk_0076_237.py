/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.components.darktable { 

import org.aswing.AbstractCellEditor;
import org.aswing.ASColor;
import org.aswing.Component;
import org.aswing.Container;
import org.aswing.decorators.ColorDecorator;
import org.aswing.geom.IntRectangle;
import org.aswing.JNumberStepper;
import org.aswing.JTextField;

/**
 * The default editor for table and tree cells, use a textfield.
 * <p>
 * @author iiley
 */
public class DarkTableNumberCellEditor extends AbstractCellEditor{
	
	protected var stepper:JNumberStepper;
	
	public function DarkTableNumberCellEditor (){
		super();
		setClickCountToStart(2);
	}
	
	public function getStepper():JNumberStepper{
		if(stepper == null){
			stepper = new JNumberStepper();
			//stepper.setBackground(new ASColor(0x262F2B, 1));
			stepper.setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), null, 0));
			//var cbd:ColorDecorator = new ColorDecorator(new ASColor(0x262F2B, 1), new ASColor(0, 0.2), 2);
			//cbd.setGaps(0, 0, 0, -4);
			//stepper.setBackgroundDecorator(cbd);
		}
		return stepper;
	}
	
	override public function startCellEditing(owner:Container, value:*, bounds:IntRectangle):void 
		{
			//bounds.y += 1;
			//bounds.height -= 1;
			bounds.x -= 1.48;
			bounds.width += 5;
			super.startCellEditing(owner, value, bounds);
			//popup.setBackgroundDecorator(new ColorDecorator(new ASColor(0x262F2B, 1), new ASColor(0, 0.14), 2));
		}
	
	/**
	 * Subclass override this method to implement specified value transform
	 */
	protected function transforValueFromText(text:String):*{
		return text;
	}
	
 	override public function getEditorComponent():Component{
 		return getStepper();
 	}
	
	override public function getCellEditorValue():* {		
		return stepper.getValue();
	}
	
   /**
    * Sets the value of this cell. 
    * @param value the new value of this cell
    */
	override protected function setCellEditorValue(value:*):void{
		//getTextField().setText(value+"");
		//getTextField().selectAll();
		stepper.setValue(Number(value));
	}
	
	public function toString():String{
		return "DarkTableNumberCellEditor[]";
	}
}
}