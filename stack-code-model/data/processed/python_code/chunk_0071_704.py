package pl.cdaction.view.page
{
	import flash.text.TextFormat;
	
	import pl.cdaction.common.Constants;
	import pl.cdaction.common.Globals;
	import pl.cdaction.view.customizable.BaseCustomizableObject;
	
	public class PageContainer extends BaseCustomizableObject
	{
		public function PageContainer(containerWidth : Number, containerHeight : Number)
		{
			super(containerWidth, containerHeight);
		}
		
		public function getPageObject() : Object
		{
			var pageObject : Object = {};
			
			if(getBgColour() != Constants.DEFAULT_BG_COLOUR)
				pageObject.bg = getBgColour();
			
			if(getText() != "")
			{
				pageObject.text = getText();
				
				var textFormat : TextFormat = getTextFormat();
				if(textFormat.font == Globals.DEFAULT_TEXT_FORMAT.font && textFormat.size == Globals.DEFAULT_TEXT_FORMAT.size && textFormat.color == Globals.DEFAULT_TEXT_FORMAT.color)
				{
					// All default, skip this one
				}
				else
				{
					if(textFormat.font != Globals.DEFAULT_TEXT_FORMAT.font)
						pageObject.font = textFormat.font;
					
					if(textFormat.size != Globals.DEFAULT_TEXT_FORMAT.size)
						pageObject.size = textFormat.size;
					
					if(textFormat.color != Globals.DEFAULT_TEXT_FORMAT.color)
						pageObject.color = textFormat.color;
				}
			}
			
			return pageObject;
		}
		
		public function setPageData(pageData : Object) : void
		{
			if(pageData.text)
			{
				_tf.text = pageData.text;
				
				var textFormat : TextFormat = getTextFormat();
				
				if(pageData.font)
					textFormat.font = pageData.font;
				
				if(pageData.size)
					textFormat.size = pageData.size;
				
				if(pageData.color)
					textFormat.color = pageData.color;
				
				setTextFormat( textFormat );
			}
			
			if(pageData.bg)
				setBgColour( pageData.bg );
		}
	}
}