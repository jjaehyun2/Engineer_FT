package net.sfxworks.dataVisualiser 
{
	import flash.display.Bitmap;
	import flash.display.Sprite;
	/**
	 * ...
	 * @author Samuel Walker
	 */
	public class Node extends Sprite
	{
		
		/*
		* @infotip The name of the node. Optional but used by visualisers on focus.
		public var name:String;
		*/
		
		/**
		* @infotip Data pertaining to the node. Field data would go in here with 'f1' and 'f2' being the defaults.
		* Any other data would only be visualised by ObjectVisualiser and is otherwise irrelivant.
		* 
		* Other default values are img and must be of type Bitmap for display.
		*/ 
		public var data:Object;
		
		/**
		* @infotip All nodes this node is linked to. This will usually contain either one or no nodes. However this is a vector for future use for visualising mulitple links between different data.
		* Nodes will be considered a parent whatever they're linked to.
		*/ 
		public var link:Vector.<Node>
		
		public var internalData:Object;
		
		public var image:Bitmap;
		
		
		/**
		* @infotip A node is your basic individual data object that is a core part of display and processing. Nodes can be linked with other nodes and contain properties to display and alter.
		*/ 
		public function Node() 
		{
			super();
			data = new Object();
			link = new Vector.<Node>();
			internalData = new Object();
		}
		
		
	}

}