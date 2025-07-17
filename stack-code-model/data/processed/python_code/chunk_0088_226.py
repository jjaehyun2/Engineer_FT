package ccomps.interfaces 
{
	import ccomps.interfaces.IComponentModifier;
	
	/**
	 * ...
	 * @author Gimmick
	 */
	public interface IMutator extends IComponentModifier
	{
		function action(action:Function, thisObj:Object):IMutator
	}
	
}