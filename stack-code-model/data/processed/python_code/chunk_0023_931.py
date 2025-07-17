// (c) Alexandre Fenyo 2012, 2013, 2014, 2015, 2016 - alex@fenyo.net - http://fenyo.net - GPLv3 licensed

////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2010 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package net.fenyo.mail4hotspot.gui
{
	import spark.skins.mobile.*;

	import spark.components.ButtonBarButton;
	import spark.components.DataGroup;
	import spark.skins.mobile.supportClasses.ButtonBarButtonClassFactory;
	import spark.skins.mobile.supportClasses.TabbedViewNavigatorTabBarHorizontalLayout;

	import flash.display.*;

	/**
	 *  The default skin class for the Spark TabbedViewNavigator tabBar skin part.
	 *  
	 *  @see spark.components.TabbedViewNavigator#tabBar
	 *  
	 *  @langversion 3.0
	 *  @playerversion Flash 10
	 *  @playerversion AIR 2.5
	 *  @productversion Flex 4.5
	 */
	public class MobileTabbedViewNavigatorTabBarSkin extends ButtonBarSkin
	{
		[Bindable]
		[Embed(source="/assets/aluminium.png")] 
		private var MyGfx : Class; 

		[Bindable]
		[Embed(source="/assets/bandeau_bleu.png")] 
		private var MyGfx2 : Class; 

		//--------------------------------------------------------------------------
		//
		//  Constructor
		//
		//--------------------------------------------------------------------------
		
		/**
		 *  Constructor.
		 * 
		 *  @langversion 3.0
		 *  @playerversion Flash 10
		 *  @playerversion AIR 2.5 
		 *  @productversion Flex 4.5
		 * 
		 */
		public function MobileTabbedViewNavigatorTabBarSkin()
		{
			super();
		}
		
		//--------------------------------------------------------------------------
		//
		//  Overridden methods
		//
		//--------------------------------------------------------------------------
		
		/**
		 *  @private
		 */
		override protected function createChildren():void
		{
			if (!firstButton)
			{
				firstButton = new ButtonBarButtonClassFactory(ButtonBarButton);
				firstButton.skinClass = spark.skins.mobile.TabbedViewNavigatorTabBarFirstTabSkin;
			}
			
			if (!lastButton)
			{
				lastButton = new ButtonBarButtonClassFactory(ButtonBarButton);
				lastButton.skinClass = spark.skins.mobile.TabbedViewNavigatorTabBarLastTabSkin;
			}
			
			if (!middleButton)
			{
				middleButton = new ButtonBarButtonClassFactory(ButtonBarButton);
				middleButton.skinClass = spark.skins.mobile.TabbedViewNavigatorTabBarLastTabSkin;
			}
			
			if (!dataGroup)
			{
				// TabbedViewNavigatorButtonBarHorizontalLayout for even percent layout
				var tabLayout:TabbedViewNavigatorTabBarHorizontalLayout = 
					new TabbedViewNavigatorTabBarHorizontalLayout();
				tabLayout.useVirtualLayout = false;
				
				dataGroup = new DataGroup();
				dataGroup.layout = tabLayout;
				addChild(dataGroup);
			}
		}
		
		/**
		 *  @private
		 */
		override protected function drawBackground(unscaledWidth:Number, unscaledHeight:Number):void
		{
			super.drawBackground(unscaledWidth, unscaledHeight);
			
			// backgroundAlpha style is not supported by ButtonBar
			// TabbedViewNavigatorSkin sets a hard-coded value to support
			// overlayControls
//			var backgroundAlphaValue:* = getStyle("backgroundAlpha");
//			var backgroundAlpha:Number = (backgroundAlphaValue === undefined)
//				? 1 : getStyle("backgroundAlpha");
//			
//			graphics.beginFill(getStyle("chromeColor"), backgroundAlpha);
//			graphics.drawRect(0, 0, unscaledWidth, unscaledHeight);
//			graphics.endFill();
			var myBitmap : BitmapData;
			if (!Main.new_skin) myBitmap = new MyGfx().bitmapData;
			else myBitmap = new MyGfx2().bitmapData;
			graphics.beginBitmapFill(myBitmap);
			graphics.drawRect(0, 0, unscaledWidth, unscaledHeight);
			graphics.endFill(); 
		}
	}
}