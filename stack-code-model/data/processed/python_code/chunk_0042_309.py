package fwk.text
{
	import flash.geom.ColorTransform;
	import flash.text.TextField;
	
	/**
	 * The SelectionColor class allows for a TextField to change its selection color.
	 * 
	 * @author Mark Walters
	 * @since 2007.08.13
	 */
	public class SelectionColor
	{
		
		/**
		 * Sets the field's selection color and tries to handle changing the field's background, border and text colors to maintain their initial values.
		 * 
		 * @param	field	TextField
		 * @param	color	uint
		 */
		public static function setFieldSelectionColor( field:TextField, color:uint ):void
		{
			field.backgroundColor = invert( field.backgroundColor );
			field.borderColor = invert( field.borderColor );
			field.textColor = invert( field.textColor );
				
			var colorTrans:ColorTransform = new ColorTransform();
			colorTrans.color = color;
			colorTrans.redMultiplier = -1;
			colorTrans.greenMultiplier = -1;
			colorTrans.blueMultiplier = -1;
			field.transform.colorTransform = colorTrans;
		}
		
		protected static function invert( color:uint ):uint
		{
			var colorTrans:ColorTransform = new ColorTransform();
			colorTrans.color = color;
			
			return invertColorTransform( colorTrans ).color;
		}
		
		protected static function invertColorTransform( colorTrans:ColorTransform ):ColorTransform
		{
			with( colorTrans )
			{
				redMultiplier = -redMultiplier;
				greenMultiplier = -greenMultiplier;
				blueMultiplier = -blueMultiplier;
				redOffset = 255 - redOffset;
				greenOffset = 255 - greenOffset;
				blueOffset = 255 - blueOffset;
			}
			
			return colorTrans;
		}
		
	}
	
}