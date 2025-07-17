package com.nigelyang.bootstrapstyle.spark.RichEditText
{
	import mx.core.mx_internal;
	
	import spark.components.RichEditableText;
	
	use namespace mx_internal;
	
	public class RichEditableTextClass extends RichEditableText
	{
		public function RichEditableTextClass()
		{
			super();
			super.passwordChar = "●";
		}
	}
}