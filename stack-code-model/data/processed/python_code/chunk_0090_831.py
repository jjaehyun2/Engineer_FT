/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.skinbuilder{

import org.aswing.plaf.basic.BasicComboBoxUI;
import devoron.aswing3d.*;
import org.aswing.Insets;
import org.aswing.JButton;

public class SkinComboBoxUI extends BasicComboBoxUI{
	
	public function SkinComboBoxUI(){
		super();
	}
	
	override protected function createDropDownButton():Component{
		var btn:JButton = new JButton();
		btn.setFocusable(false);
		btn.setBorder(null);
		btn.setOpaque(false);
		btn.setMargin(new Insets());
		btn.setBackgroundDecorator(null);
		var ico:SkinButtonIcon = new SkinButtonIcon(-1, -1, getPropertyPrefix()+"arrowButton.", box);
		btn.setIcon(ico);
		return btn;
	}
}
}