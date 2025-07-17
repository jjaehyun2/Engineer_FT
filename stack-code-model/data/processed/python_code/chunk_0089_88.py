/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.skinbuilder{

public class SkinRadioButtonIcon extends SkinButtonIcon{
	
	public function SkinRadioButtonIcon(){
		super();
	}
	
	override protected function getPropertyPrefix():String {
        return "RadioButton.";
    }
}
}