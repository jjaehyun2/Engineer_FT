package flexUnit.tests
{
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import flexUnit.BaseTestCase;
	
	import services.business.common.CommonDelegate;
	import services.cairngorm.BaseEvent;
	import services.vo.GlobalStorage;

	public class CommonDictionaryTest extends BaseTestCase
	{	
		public function testCommonDictionary():void
		{
			addCallBack(CommonDelegate.GET_COMMON_DICTIONARY, commonDictionaryCallBack);
		}
		
		private function commonDictionaryCallBack(event:BaseEvent):void
		{
			assertTrue("vip total is empty", GlobalStorage.vipTotal.length != 0);	
			assertTrue("mailing list is empty", GlobalStorage.mailings.length != 0);
			assertTrue("source code is empty", GlobalStorage.sourceCodes.length != 0);
			assertTrue("vip total is empty", GlobalStorage.vipTotal.length != 0);
			assertTrue("vip total is empty", GlobalStorage.vipTotal.length != 0);
			assertTrue("vip total is empty", GlobalStorage.vipTotal.length != 0);	
		}		
	}
}