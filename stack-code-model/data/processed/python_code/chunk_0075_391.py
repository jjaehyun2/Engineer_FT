/*
 * Copyright 2007 (c) Tim Knip, ascollada.org.
 *
 * Permission is hereby granted, free of charge, to any person
 * obtaining a copy of this software and associated documentation
 * files (the "Software"), to deal in the Software without
 * restriction, including without limitation the rights to use,
 * copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the
 * Software is furnished to do so, subject to the following
 * conditions:
 *
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 * OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 * NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 * HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 */
 
package org.ascollada.core {
	import org.ascollada.ASCollada;
	import org.ascollada.core.DaeEntity;	

	/**
	 * 
	 */
	public class DaeInput extends DaeEntity
	{	
		/** */
		public var semantic:String;
		
		/** */
		public var source:String;
		
		/** */
		public var offset:uint;
		
		/** */
		public var setId:uint;
		
		/**
		 * 
		 * @param	node
		 * @return
		 */
		public function DaeInput( node:XML = null ):void
		{
			super( node );
		}
		
		/**
		 * 
		 * @param	node
		 * @return
		 */
		override public function read( node:XML ):void
		{			
			if( node.localName() != ASCollada.DAE_INPUT_ELEMENT )
				return;
				
			super.read( node );
			
			// required
			this.semantic = getAttribute(node, ASCollada.DAE_SEMANTIC_ATTRIBUTE);
			
			// required
			this.source = getAttribute(node, ASCollada.DAE_SOURCE_ATTRIBUTE);
			
			// optional
			this.offset = parseInt( getAttribute(node, ASCollada.DAE_OFFSET_ATTRIBUTE), 10 );
			this.offset = this.offset ? this.offset : 0;
			
			// optional
			this.setId = parseInt( getAttribute(node, ASCollada.DAE_SET_ATTRIBUTE), 10 );
		}
	}	
}