/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.plaf.basic{

/**
 * @private
 */
public class BasicTextAreaUI extends BasicTextComponentUI{
	
	public function BasicTextAreaUI(){
		super();
	}
	
	//override this to the sub component's prefix
	override protected function getPropertyPrefix():String {
		return "TextArea.";
	}
}
}