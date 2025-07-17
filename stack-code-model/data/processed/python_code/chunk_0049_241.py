/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.table{

/**
 * Texts in this cell is selectable.
 */
public class SelectablePoorTextCell extends PoorTextCell{
	
	public function SelectablePoorTextCell(){
		super();
		textField.mouseEnabled = true;
		textField.selectable = true;
	}
	
}
}