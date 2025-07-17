package flexUnit
{
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import flexUnit.model.TestAppModel;
	
	import flexunit.framework.TestCase;
	
	import framework.model.AppModelLocator;
	
	import mx.collections.ArrayCollection;
	import mx.utils.StringUtil;
	
	import services.data.RequestInfo;

	public class BaseTestCase extends TestCase
	{
		
		[Bindable]
		public var model:AppModelLocator = AppModelLocator.getInstance();
		
		[Bindable]
		public var modelTest:TestAppModel = TestAppModel.getInstance();

		private var functionList:ArrayCollection = new ArrayCollection();
		
		public function BaseTestCase(methodName:String=null)
		{
			super(methodName);
		}
		
		public function addCallBack(eventType:String, callbackFunction:Function):void
		{
			addToQueue(eventType + "Complete", callbackFunction);
			CairngormEventDispatcher.getInstance().addEventListener(eventType + "Complete", addAsync(onCompleteTest,15000));
		}
				
		private function onCompleteTest(event:CompleteEvent):void
		{
			if(event.status == CompleteEvent.OK)
			{
				var f:Function = getFromQueue(event.type);
				if(f != null)
				{
					removeFromQueue(event.type);
					f(event);
				}
			}
			if(event.status == CompleteEvent.FAULT)
			{
				removeFromQueue(event.type);
				var info:RequestInfo = model.requestInfo;
				var message:String = StringUtil.substitute("Test is failed on {0}::{1}!",
					info.gateway, info.operation);
				assertTrue(message, false);
			}
			model.appEnabled--;
		}
		
		
		
		private function addToQueue(eventName:String, func:Function):void
		{
			if(getFromQueue(eventName) == null)
			{
				functionList.addItem({eventName:eventName,func:func});
			}
		}
		
		private function removeFromQueue(eventName:String):void
		{
			var index:int = 0;
			for each(var item:Object in functionList)
			{
				if(item.eventName == eventName)
				{
					functionList.removeItemAt(index);
					return;
				}
				index++;
			}
		}
				
		private function getFromQueue(eventName:String):Function
		{
			for each(var item:Object in functionList)
			{
				if(item.eventName == eventName)
				{
					return item.func;
				}
			}
			return null;
		}
		
	}
}