package net.guttershark.util 
{
	import flash.display.DisplayObject;	
	import flash.display.DisplayObjectContainer;
	
	/**
	 * The DisplayListUtils class has utility methods for working with the Display list.
	 */
	public class DisplayListUtils 
	{
		
		/**
		 * Remove all children from a sprite.
		 * 
		 * @example Removing all children from a sprite.
		 * <listing>	
		 * var container:Sprite = new Sprite();
		 * addChild(container);
		 * var child1:Sprite = new Sprite();
		 * car child2:Sprite = new Sprite();
		 * container.addChild(child1);
		 * container.addChild(child2);
		 * DisplayListUtils.RemoveAllChildren(container);
		 * </listing>
		 * 
		 * @param	sprite	The sprite to remove all children from.
		 */
		public static function RemoveAllChildren(doc:DisplayObjectContainer):void
		{
			Assert.NotNull(doc, "Parameter doc cannot be null.");
			try
			{
				while(doc.removeChildAt(0)){}
			}
			catch(re:RangeError){}
		}
		
		/**
		 * Add multiple children onto a display object container.
		 * @param	doc	The display object container to add children too.
		 * @param	children	The children display objects to add to the container.
		 */
		public static function AddChildren(doc:DisplayObjectContainer, children:Array):void
		{
			Assert.NotNull(doc, "Parameter doc cannot be null.");
			Assert.NotNullOrEmpty(children, "Parameter children cannot be null or empty.");
			var l:int = children.length;
			for(var i:int = 0; i < l; i++) doc.addChild(children[i]);
		}
		
		/**
		 * Bring a clip to the top layer in the holder.
		 * @param	holder	The display object container that contains the child to bring to front.
		 * @param	child	The child to bring to front.
		 */
		public static function BringToFront(holder:DisplayObjectContainer, child:DisplayObject):void
		{
			holder.removeChild(child);
			holder.addChild(child);
		}
	}
}