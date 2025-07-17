package flexmvcs.patterns.facade {
	
	import org.puremvc.interfaces.IFacade;
	import org.puremvc.interfaces.IProxy;
	
	public class StubProxy implements IProxy {

		[Bindable]
		public var description:String;
		public var proxyName:String;
		private var _facade:IFacade;
		
		public function StubProxy() {
			description = FlexFacadeTest.DEFAULT_DESCRIPTION;
		}
		
		public function getProxyName():String {
			return proxyName;
		}
		
		public function setFacade(facade:IFacade):void {
			_facade = facade;
		}
		
		public function getFacade():IFacade {
			return _facade;
		}
	}
}