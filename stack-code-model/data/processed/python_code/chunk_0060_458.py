package com.vmware.simplivity.citrixplugin {
import com.vmware.flexutil.ServiceUtil;
import com.vmware.flexutil.proxies.BaseProxy;

/**
 * Proxy class for the ReadCfgFileService java service
 */
public class ReadCfgFileServiceProxy extends BaseProxy {
   // Service name matching the flex:remoting-destination declared in
   // main/webapp/WEB-INF/spring/bundle-context.xml
   private static const SERVICE_NAME:String = "ReadCfgFileService";

   /**
    * Create a ReadCfgFileServiceProxy with a secure channel.
    */
   public function ReadCfgFileServiceProxy() {
      // channelUri uses the Web-ContextPath defined in MANIFEST.MF
      const channelUri:String = ServiceUtil.getDefaultChannelUri(CitrixPluginModule.contextPath);
      super(SERVICE_NAME, channelUri);
   }

   public function readcfgfile(callback:Function = null,
							   context:Object = null):void {
	   callService("readcfgfile", [], callback, context);
   }

}
}