package framework.controllers
{
	
	import spark.components.Alert;
	
	import framework.events.GlobalErrorEvent;
	
	import robotlegs.bender.bundles.mvcs.Command;
	
	public class ShowErrorCommand extends Command {
		
		[Inject] public var event:GlobalErrorEvent;
		
		public override function execute():void {
			
			var alertText:String = "Details: \n" + event.details + "\n\n" + "Info:\n" + event.extraInfo;
			Alert.show(alertText, "Error", Alert.OK);
		}
	}
}