package application
{
	import application.event.ViewEvent;

	import interfaces.container.MenuView;
	import interfaces.container.QuizView;

	import spark.components.ViewNavigator;

	public class ViewManager
	{
		[ViewNavigator]
		public var viewNavigator:ViewNavigator;
		
		[Inject(source="model", bind="true")]
		public var model:AppModel;
		
		
		[EventHandler(event="ViewEvent.RESET_VIEW")]
		public function resetView(event:ViewEvent):void
		{
			trace('resetView()');
			
			viewNavigator.popAll();
		}
		
		[EventHandler(event="ViewEvent.DISPLAY_PREVIOUS_VIEW")]
		public function displayPreviousView(event:ViewEvent):void
		{
			trace('displayPreviousView()');
			
			viewNavigator.popView();
		}
		
		[EventHandler(event="ViewEvent.DISPLAY_MENU_VIEW")]
		public function displayMenuView(event:ViewEvent):void
		{
			trace('displayMenuView()');
			
			viewNavigator.pushView(MenuView);
		}

		[EventHandler(event="ViewEvent.DISPLAY_QUIZ_VIEW")]
		public function displayQuizView(event:ViewEvent):void
		{
			trace('displayQuizView()');

			viewNavigator.pushView(QuizView);
		}

		[EventHandler(event="ViewEvent.DISPLAY_ABOUT_VIEW")]
		public function displayAboutView(event:ViewEvent):void
		{
			trace('displayAboutView()');

			//viewNavigator.pushView(AboutView);
		}
	}
}