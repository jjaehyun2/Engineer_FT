package plugins.mxml.spark
{import core.base.CoreBaseClassFactory;
import core.base.CoreCallback;
import core.context.CoreContext;
import core.service.CoreServiceContainer;
import spark.components.TabbedViewNavigatorApplication;

public class GuiTabbedViewNavigatorApplication extends TabbedViewNavigatorApplication
	{
		public var sc:CoreServiceContainer;

		public var context:CoreContext;


		public var callbacks:Array=[];


		public function GuiTabbedViewNavigatorApplication()
		{
			CoreBaseClassFactory.construct(this);
		}

		public function serviceAddCallback(params:Array):void
		{
			CoreBaseClassFactory.serviceAddCallback(this, params);
		}

		public function serviceAddCallbacks(params:Array):void
		{
			CoreBaseClassFactory.serviceAddCallbacks(this, params);
		}

		protected function createCallBack(group:String):CoreCallback
		{
			return CoreBaseClassFactory.createCallBack(this, group);
		}

		protected function log(message:Object):void
		{
			CoreBaseClassFactory.log(this, message);
		}
	}
}