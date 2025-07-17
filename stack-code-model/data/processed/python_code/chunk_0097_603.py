package framework.controllers
{
	import flash.display.DisplayObject;
	import flash.geom.Point;
	
	import mx.core.FlexGlobals;
	import mx.managers.PopUpManager;
	
	import framework.views.events.EditCreateTaskEvent;
	import framework.views.ui.CreateTaskView;
	
	import michaPau.utils.geom.SimplePoint;
	
	import robotlegs.bender.bundles.mvcs.Command;
	import robotlegs.bender.extensions.viewManager.api.IViewManager;
	
	public class EditCreateTaskCommand extends Command {
		
		[Inject] public var event:EditCreateTaskEvent;
		[Inject] public var viewManager:IViewManager;
		
		public override function execute():void {
			
			var createTask:CreateTaskView = new CreateTaskView();
			
			switch(event.editType) {
				case "create":
					createTask.startPoint = new SimplePoint(FlexGlobals.topLevelApplication.width/2 - 90, -120);
					createTask.title = "Create a new task";
					break;
				case "update":
					createTask.startPoint = event.globalPoint;
					createTask.title = "Update the task";
					createTask.task = event.task;
					break;
			}
			
			createTask.currentState = event.editType;
			createTask.width = 180;
			createTask.height = 110;
			createTask.x = createTask.startPoint.x;
			createTask.y = createTask.startPoint.y;
			createTask.rotation = event.rotation;
			
			createTask.startRotation = event.rotation;
			createTask.endPoint = new SimplePoint(FlexGlobals.topLevelApplication.width/2 - 200, FlexGlobals.topLevelApplication.height/2 - 150);
			viewManager.addContainer(createTask);
			
			PopUpManager.addPopUp(createTask, FlexGlobals.topLevelApplication as DisplayObject, true);
			//PopUpManager.centerPopUp(createTask);
			
			
			
			
		}
	}
}