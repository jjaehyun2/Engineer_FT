package flexUnit.tests
{
	import com.adobe.cairngorm.control.CairngormEventDispatcher;
	
	import framework.core.utils.UtilsGolobal;
	import framework.core.utils.UtilsSecurity;
	import framework.model.AppModelLocator;
	
	import mx.collections.ArrayCollection;
	
	import services.cairngorm.BaseEvent;
	import services.controller.AppController;
	import services.events.frontend.LoginEvent;
	
	import flexUnit.BaseTestCase;

	public class SecurityTest extends BaseTestCase
	{
		
		public function testRoleLis(event:BaseEvent = null):void
		{
			var permissions:ArrayCollection = new ArrayCollection();
			var classInfo:XML = UtilsGolobal.getClassInfo(UtilsSecurity);
			var classElements:XMLList = classInfo.elements();
			
			for each(var node:XML in classElements)
			{
				if(node.name() == "constant")
				{
					permissions.addItem({name:node.@name.toString(),value:UtilsSecurity[node.@name],selected:false});
				}
			}
			assertTrue(model.currentUser.oRole.aPermission.length == permissions.length);
		}

	}
}