package ro.ciacob.desktop.skins.cherry {
	
	
	
	/**
	 *  The skin for the close button in the TitleBar
	 *  of a WindowedApplication or Window.
	 * 
	 *  
	 *  @langversion 3.0
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public class WindowCloseButtonSkin extends ImageButtonSkin {		
		//--------------------------------------------------------------------------
		//
		//  Class assets
		//
		//--------------------------------------------------------------------------
		
		[Embed(source="../../../../../SourCherry/Window/close-up.png")]
		private const UP_SKIN:Class;
		
		[Embed(source="../../../../../SourCherry/Window/close-over.png")]
		private const OVER_SKIN:Class;
		
		[Embed(source="../../../../../SourCherry/Window/close-down.png")]
		private const DOWN_SKIN:Class;
		
		[Embed(source="../../../../../SourCherry/Window/close-disabled.png")]
		private const DISABLED_SKIN:Class;
		
		override protected function get upSkin() : Class {
			return UP_SKIN;
		}
		
		override protected function get overSkin() : Class {
			return OVER_SKIN;
		}
		
		override protected function get downSkin() : Class {
			return DOWN_SKIN;
		}
		
		override protected function get disabledSkin() : Class {
			return DISABLED_SKIN;
		}
	}
	
}