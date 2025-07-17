/**
 * Created by Dukobpa3 on 12/22/13.
 */
package gd.eggs.samples.simpleserver.model
{
	import org.puremvc.as3.multicore.patterns.proxy.Proxy;


	public class DataProxy extends Proxy
	{
		public function DataProxy(proxyName:String = null, data:Object = null)
		{
			super(proxyName, data);
		}
	}
}