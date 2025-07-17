package com.playtika.samples.loadup.view
{
	import com.playtika.samples.loadup.ApplicationFacade;
	import com.playtika.samples.loadup.model.SiteDataProxy;
	import com.playtika.samples.loadup.model.StyleSheetProxy;
	import com.playtika.samples.loadup.model.vo.SectionVO;
	import com.playtika.samples.loadup.view.components.SectionView;
	import com.playtika.samples.loadup.view.components.TitleView;

	import flash.display.Stage;

	import org.puremvc.as3.multicore.interfaces.IMediator;
	import org.puremvc.as3.multicore.interfaces.INotification;
	import org.puremvc.as3.multicore.patterns.mediator.Mediator;
	import org.puremvc.as3.multicore.utilities.loadup.model.LoadupMonitorProxy;


	public class StageMediator extends Mediator implements IMediator
	{
		public static const NAME:String = "StageMediator";
		private var _styleSheetProxy:StyleSheetProxy;
		private var _siteDataProxy:SiteDataProxy;

		public function StageMediator(viewComponent:Object)
		{
			super(NAME, viewComponent);
		}

		override public function listNotificationInterests():Array
		{
			return  [
				LoadupMonitorProxy.LOADING_PROGRESS,
				LoadupMonitorProxy.LOAD_RESOURCE_TIMED_OUT,
				LoadupMonitorProxy.LOADING_COMPLETE,
				LoadupMonitorProxy.LOADING_FINISHED_INCOMPLETE,
				LoadupMonitorProxy.CALL_OUT_OF_SYNC_IGNORED,
				ApplicationFacade.STYLE_SHEET_LOADING,
				ApplicationFacade.STYLE_SHEET_LOADED,
				ApplicationFacade.STYLE_SHEET_FAILED,
				ApplicationFacade.SITE_DATA_LOADING,
				ApplicationFacade.SITE_DATA_LOADED,
				ApplicationFacade.SITE_DATA_FAILED
			];
		}

		override public function handleNotification(note:INotification):void
		{
			switch (note.getName())
			{
				case ApplicationFacade.STYLE_SHEET_LOADING:
					trace("Loading StyleSheet...");
					break;
				case ApplicationFacade.STYLE_SHEET_LOADED:
					trace("StyleSheet Loaded");
					break;
				case ApplicationFacade.SITE_DATA_LOADING:
					trace("Loading Site Data...");
					break;
				case ApplicationFacade.SITE_DATA_LOADED:
					trace("Site Data Loaded");
					break;

				case LoadupMonitorProxy.CALL_OUT_OF_SYNC_IGNORED:
					trace("Abnormal State, Abort");
					break;
				case LoadupMonitorProxy.LOADING_PROGRESS:
					var perc:Number = note.getBody() as Number;
					trace("Loading Progress: " + perc + "%");
					break;
				case LoadupMonitorProxy.LOADING_COMPLETE:
					trace(">>> Loading Complete");
					initializeView();
					break;
				case LoadupMonitorProxy.LOADING_FINISHED_INCOMPLETE:
					trace("Loading Finished Incomplete");
					break;
			}
		}

		private function initializeView():void
		{
			_styleSheetProxy = facade.retrieveProxy(StyleSheetProxy.NAME) as StyleSheetProxy;
			_siteDataProxy = facade.retrieveProxy(SiteDataProxy.NAME) as SiteDataProxy;

			var titleView:TitleView = new TitleView(_siteDataProxy.title, _styleSheetProxy.css);
			stage.addChild(titleView);

			var sectionVO:SectionVO = _siteDataProxy.sections[0];
			var sectionView:SectionView = new SectionView(sectionVO, _styleSheetProxy.css);
			stage.addChild(sectionView);
		}

		public function get stage():Stage
		{
			return viewComponent as Stage;
		}

	}
}