package devoron.aswing3d.plaf
{
	import org.aswing.lookandfeel.plaf.ComponentUI;
	import org.aswing.JDropDownButton;

	public interface DropDownButtonUI extends ComponentUI
	{
		function isPopupVisible (c:JDropDownButton) : Boolean;

		function setPopupVisible (c:JDropDownButton, v:Boolean) : void;
	}
}