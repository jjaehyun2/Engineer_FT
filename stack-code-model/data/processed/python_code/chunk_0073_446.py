/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package devoron.aswing3d.skinbuilder{

public class SkinPopupMenuBackground extends SinglePicBackground{
	
	public function SkinPopupMenuBackground(){
		super();
		avoidBorderMargin = false;
	}
	
	override protected function getDefaltsKey():String{
		return "PopupMenu.bgImage";
	}
}
}