package flexmvcs.patterns.facade {

	import asunit.framework.TestCase;
	
	import flash.events.MouseEvent;
	
	import flexmvcs.interfaces.IFlexFacade;
	import flexmvcs.interfaces.IService;
	
	import mx.controls.Label;
	
	import mx.core.IPropertyChangeNotifier;
	import org.puremvc.interfaces.IProxy;
	import org.puremvc.patterns.observer.Notification;
	import org.puremvc.interfaces.IMediator;
	import flash.events.Event;
	import mx.events.FlexEvent;
	import flash.utils.setTimeout;

	public class FlexFacadeTest extends TestCase {
		public static const DEFAULT_DESCRIPTION:String = "Default Description";
		public static const MODIFIED_DESCRIPTION:String = "Modified Description";
		
		[Bindable]
		public var label:Label;
		private var facade:IFlexFacade;

		public function FlexFacadeTest(methodName:String=null) {
			super(methodName)
		}

		override protected function setUp():void {
			super.setUp();
			facade = new StubFacade();
			label = new Label();
			label.text = "Foo Bar";
			label.setStyle("color", 0xFFCC00);
			label.addEventListener(FlexEvent.CREATION_COMPLETE, addAsync(creationCompleteHandler));
			addChild(label);
		}

		override protected function tearDown():void {
			super.tearDown();
			removeChild(label);
			label = null;
			facade = null;
		}
		
		protected function creationCompleteHandler(event:Event):void {
			facade.initialize(this);
		}
		
		protected function sendModifyDescription():void {
			facade.notifyObservers(new Notification(StubConstants.SET_DESCRIPTION, MODIFIED_DESCRIPTION));
		}
		
		public function testService():void {
			var service:IService = facade.retrieveService(StubConstants.STUB_SERVICE);
			assertNotNull(service);
		}
		
		public function testProxy():void {
			var proxy:IProxy = facade.retrieveProxy(StubConstants.STUB_PROXY);
			assertNotNull(proxy);
			assertEquals("Description is default value", DEFAULT_DESCRIPTION, StubProxy(proxy).description);
		}
		
		public function testCommand():void {
			var proxy:StubProxy = facade.retrieveProxy(StubConstants.STUB_PROXY) as StubProxy;
			sendModifyDescription();
			assertEquals("Description was changed", MODIFIED_DESCRIPTION, proxy.description);
		}
		
		public function testMediator():void {
			sendModifyDescription();
			assertEquals("Label.text should be modified", MODIFIED_DESCRIPTION, label.text);
		}
		
		public function testCompositeFacade():void {
//			var childFacade:StubChildFacade = new StubChildFacade();
//			childFacade.initialize(this);
			
		}
	}
}