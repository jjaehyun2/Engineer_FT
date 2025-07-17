package com.playtika.samples.loadup.controller
{
	import com.playtika.samples.loadup.model.SiteDataProxy;
	import com.playtika.samples.loadup.model.StyleSheetProxy;
	import com.playtika.samples.loadup.view.StageMediator;

	import flash.display.Stage;

	import org.puremvc.as3.multicore.interfaces.ICommand;
	import org.puremvc.as3.multicore.interfaces.INotification;
	import org.puremvc.as3.multicore.patterns.command.SimpleCommand;
	import org.puremvc.as3.multicore.utilities.loadup.interfaces.ILoadupProxy;
	import org.puremvc.as3.multicore.utilities.loadup.model.LoadupMonitorProxy;
	import org.puremvc.as3.multicore.utilities.loadup.model.LoadupResourceProxy;


	public class StartupCommand extends SimpleCommand implements ICommand
	{
		private var _monitor:LoadupMonitorProxy;

		override public function execute(note:INotification):void
		{
			var stage:Stage = note.getBody() as Stage;
			facade.registerMediator(new StageMediator(stage));

			_monitor = new LoadupMonitorProxy();
			facade.registerProxy(_monitor);

			//_monitor.defaultTimeout = 30;

			//var styleSheetProxy:ILoadupProxy = new StyleSheetProxy();
			//var siteDataProxy:ILoadupProxy = new SiteDataProxy();

			var styleSheetProxy:StyleSheetProxy = new StyleSheetProxy();
			var siteDataProxy:SiteDataProxy = new SiteDataProxy();

			facade.registerProxy(styleSheetProxy);
			facade.registerProxy(siteDataProxy);

			var rStyleSheetProxy:LoadupResourceProxy = makeAndRegisterStartupResource(StyleSheetProxy.SRNAME, styleSheetProxy);
			var rSiteDataProxy:LoadupResourceProxy = makeAndRegisterStartupResource(SiteDataProxy.SRNAME, siteDataProxy);

			rSiteDataProxy.requires = [ rStyleSheetProxy ];

			_monitor.loadResources();
		}

		private function makeAndRegisterStartupResource(proxyName:String, appResourceProxy:ILoadupProxy):LoadupResourceProxy
		{
			var r:LoadupResourceProxy = new LoadupResourceProxy(proxyName, appResourceProxy);
			facade.registerProxy(r);
			_monitor.addResource(r);
			return r;
		}
	}
}