package framework.views
{
	import framework.events.DeleteCategoryEvent;
	import framework.events.UpdateCategoryEvent;
	import framework.views.ui.LegendItem;
	
	import robotlegs.bender.bundles.mvcs.Mediator;
	
	public class LegendItemMediator extends Mediator {
		
		[Inject] public var view:LegendItem;
		
		public override function initialize():void {
			//trace("LegendItemMediator::initialize");
			this.addViewListener(UpdateCategoryEvent.UPDATE_CATEGORY, dispatch);
			this.addViewListener(DeleteCategoryEvent.DELETE, dispatch);
		}
	}
}