import mx.core.UIComponent
import mx.controls.NumericStepper

class NumericRenderer extends UIComponent
{
	var stepper_cont : MovieClip;
	var stepper : MovieClip;
	var listOwner : MovieClip; // the reference we receive to the list
	var getCellIndex : Function; // the function we receive from the list
	var	getDataLabel : Function; // the function we receive from the list

	function NumericRenderer()
	{
	}

	function createChildren(Void) : Void
	{
		stepper = stepper_cont.stepper
		size();
	}

	// note that setSize is implemented by UIComponent and calls size(), after setting
	// __width and __height
	function size(Void) : Void
	{
		stepper.setSize(80, __height);
		stepper._x = (__width-80)/2;
		stepper._y = (__height-22)/2;
	}

	function setValue(str:String, item:Object, sel:Boolean) : Void
	{
		if(item[getDataLabel()] == undefined){
			stepper_cont._visible = false
		} else {
			stepper_cont._visible = true
		}
		stepper_cont.value = item[getDataLabel()];
	}

	function getPreferredHeight(Void) : Number
	{
		return 22;
	}

	function getPreferredWidth(Void) : Number
	{
		return 80;
	}

	function change()
	{
		listOwner.dataProvider.editField(getCellIndex().itemIndex, getDataLabel(), stepper_cont.stepper.value);
		listOwner.selectedIndex = getCellIndex().itemIndex
		listOwner.dispatchEvent({ type:"cellEdit"});
	}

}