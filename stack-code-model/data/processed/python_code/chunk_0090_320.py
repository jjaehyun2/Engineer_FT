package Infrastructure 
{
	/**
	 * ...
	 * @author Philip Ludington
	 */
	public final class MouseCursor extends Object
	{/**
		 * Used to specify that the arrow cursor should be used.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const ARROW : MouseCursor = new MouseCursor();

		/**
		 * Used to specify that the cursor should be selected automatically based on the object under the mouse.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const AUTO : MouseCursor = new MouseCursor();

		/**
		 * Used to specify that the button pressing hand cursor should be used.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const BUTTON : MouseCursor = new MouseCursor();

		/**
		 * Used to specify that the dragging hand cursor should be used.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const HAND : MouseCursor = new MouseCursor();

		/**
		 * Used to specify that the I-beam cursor should be used.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const IBEAM : MouseCursor = new MouseCursor();
		
		/**
		 * Used to specify that the no cursor should be used.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const HIDE:MouseCursor = new MouseCursor();
		
		/**
		 * This is an alias for AUTO, but makes more sense:
		 * Used to specify that the cursor should be selected automatically based on the object under the mouse.
		 * @langversion	3.0
		 * @playerversion	Flash 10
		 * @playerversion	AIR 1.5
		 */
		public static const DEFAULT:MouseCursor = new MouseCursor();		
		
		public function ToString():String
		{
			if ( this == HAND)
			{
				return "hand";
			}
			else if ( this == HIDE)
			{
				return "hide";
			}
			else if ( this == ARROW)
			{
				return "arrow";
			}
			else if ( this == BUTTON)
			{
				return "button";
			}
			else if ( this == IBEAM)
			{
				return "ibeam";
			}
			else
			{
				return "auto";
			}
		}
	}

}