package core.procedure
{
	import com.component.menu.Selection;

	public interface IMenu
	{
		function getSelection():Vector.<Selection>;
		function get x():Number;
		function get y():Number;
	}
}