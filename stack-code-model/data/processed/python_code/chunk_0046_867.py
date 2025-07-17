package net.sfxworks.dataVisualiser.types 
{
	/**
	 * ...
	 * @author Samuel Walker
	 */
	public class NodeType 
	{
		/**
		* @infotip Indent is for creating a node listing of linked nodes that indents by level.
		* Parent nodes will lie to the left and above of children nodes.
		*/ 
		public static const INDENT:String = "indent";
		
		/**
		* @infotip Hirarchy is for creating a node listing of linked nodes similar to a bracket style.
		* Example: A tournament bracket.
		*/ 
		public static const HIRARCHY:String = "hirarchy";
		
		/**
		* @infotip NodeTypes contains arguments for the NodeVisualiser to consume.
		* Nodes in this value will need to have parents and children for the visualiser to properly process. Nodes with no links will float.
		* 
		*/ 
		public function NodeType() 
		{
			
		}
		
	}

}