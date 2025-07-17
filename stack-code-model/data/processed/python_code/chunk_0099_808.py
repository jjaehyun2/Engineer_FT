package org.openPyro.collections
{
	import flash.events.Event;
	import flash.events.EventDispatcher;
	
	/**
	 * The XMLNodeDescriptor class represents an XML node
	 * and maintains some extra properties like depth, parent
	 * and whether its open or closed.
	 */ 
	public class XMLNodeDescriptor extends EventDispatcher
	{
		public var node:XML;
		public var depth:int;
		
		public var parent:XMLNodeDescriptor;
		
		public static const BRANCH_VISIBILITY_CHANGED:String = "branchVisibilityChanged"
		
		public function XMLNodeDescriptor()
		{
		}
		
		private var _open:Boolean = true;
		
		public function set open(b:Boolean):void{
			_open = b;
			dispatchEvent(new Event(BRANCH_VISIBILITY_CHANGED))
		}
		
		public function get open():Boolean{
			return _open
		}
		
		public function isLeaf():Boolean{
			if(!node) return false;
			if (node.hasComplexContent()){
				return false
			}
			return true;
		}
		
		public function get nodeString():String{
			return node.toXMLString();
		}

	}
}