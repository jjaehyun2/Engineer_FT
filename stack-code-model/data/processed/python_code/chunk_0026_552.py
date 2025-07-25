#set( $symbol_pound = '#' )
#set( $symbol_dollar = '$' )
#set( $symbol_escape = '\' )
package ${package}.business
{
import org.ow2.kerneos.common.business.AbsDelegateResponder;

import ${package}.MyModule

public class ModuleDelegate extends AbsDelegateResponder implements IModuleDelegate
{
    ////////////////////////////////////////////////////////////////////
    //                                                                //
    //             Function that does the requested operation         //
    //                                                                //
    ////////////////////////////////////////////////////////////////////
    
    

    // Put here the method that will trigger the code to execute following a dispatched event
    // in the cairngorm architecture.
    // Example :
    public function callServerSide(parameters : Object) : void
    {
        // find the service
        // "hello_service" is defined in kerneos-module.xml as
        // <service id="hello_service"/>
       var service : Object = MyModule.getInstance().getServices().getRemoteObject("hello_service");

       // Make the service call. The method called on service is the method name
       // of the java class bound with the remote object, with its parameters.
       var call : Object = service.sayHello(parameters);

       // add responder to handle the callback
       call.addResponder(this.responder);
    }
}
}