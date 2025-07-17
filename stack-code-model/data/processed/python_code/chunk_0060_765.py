package com.demy._test.textures 
{
	import com.demy._test.TestMain;
	import com.demy._test.listenerview.StarlingAsync;
	import com.demy.waterslide.textures.TextureListPanel;
	import org.flexunit.Assert;
	import org.flexunit.async.Async;
	import flash.events.Event;
	import starling.events.Event;
	/**
	 * ...
	 * @author 
	 */
	public class TextureListPanelTest 
	{
		private var list:TextureListPanel;
		
		public function TextureListPanelTest() 
		{
			
		}
		
		[Before]
		public function setup():void
		{
			list = new TextureListPanel();
			TestMain.container.addChild(list);
		}
		
		[After]
		public function cleanup():void
		{
			list.removeFromParent(true);
			list = null;
		}
		
		[Test]
		public function isLoadingFlaseOnCreation():void
		{
			Assert.assertFalse(list.isLoading);
		}
		
		[Test]
		public function whenLoadThenIsLoading():void
		{
			list.load();
			Assert.assertTrue(list.isLoading);
		}
		
		[Test(async, timeout=1000)]
		public function whenLoadThenDispatchedCompleteAfterLoading():void
		{
			var eventHandler:StarlingAsync = new StarlingAsync(list, starling.events.Event.COMPLETE);
			list.load();
			Async.handleEvent(this, eventHandler, flash.events.Event.COMPLETE, checkIsLoadingFalse, 1000);
		}
		
		private function checkIsLoadingFalse(event:flash.events.Event, data:*):void 
		{
			Assert.assertFalse(list.isLoading);
		}
		
	}

}