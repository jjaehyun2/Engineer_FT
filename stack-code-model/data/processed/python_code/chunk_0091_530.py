package flexmvcs.interfaces {
	import flexmvcs.interfaces.IService;
	
	import org.puremvc.interfaces.IFacade;

	public interface IFlexFacade extends IFacade {

		function initialize(context:Object=null):void;
		function registerService(service:IService):void;
		function removeService(id:String):void;
		function retrieveService(id:String):IService;
	}
}