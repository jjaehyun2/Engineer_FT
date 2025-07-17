package interfaces.container
{
	import application.event.QuizEvent;
	import application.event.ViewEvent;

	import flash.events.MouseEvent;

	import interfaces.AbstractView;

	import interfaces.component.ValueButton;

	import spark.components.Label;


	[ResourceBundle("menu_view")]
	public class MenuView extends AbstractView
	{
		private var _isQuizResumable:Boolean = false;
		private var _isQuizResumableDirty:Boolean;

		[SkinPart(required="true")]
		public var txt_caption:Label;
		
		[SkinPart(required="true")]
		public var txt_info:Label;
		
		[SkinPart(required="true")]
		public var btn_startQuiz:ValueButton;
		
		[SkinPart(required="true")]
		public var btn_showAbout:ValueButton;
		
		public function MenuView()
		{
			super();
			
			this.resourceBundleName = "menu_view";
			
			this.title = resourceManager.getString(resourceBundleName, "title");
			//this.actionContent = [getLogoutButton()];
		}


		[Inject(source="model.isQuizResumable", bind="true")]
		public function set currentUser(value:Boolean):void
		{
			_isQuizResumable = value;
			_isQuizResumableDirty = true;
			
			invalidateProperties();
		}


		override protected function partAdded(partName:String, instance:Object):void
		{
			super.partAdded(partName, instance);
			
			if (instance == btn_startQuiz)
			{
				btn_startQuiz.label = _isQuizResumable ?
					resourceManager.getString(resourceBundleName, "btn_resumeQuiz.label") :
					resourceManager.getString(resourceBundleName, "btn_startQuiz.label");

				btn_startQuiz.value = '►';
				btn_startQuiz.addEventListener(MouseEvent.CLICK, btn_startQuiz_clickHandler);
			}
			if (instance == btn_showAbout)
			{
				btn_showAbout.label = resourceManager.getString(resourceBundleName, "btn_showAbout.label");
				btn_showAbout.value = '►';
				btn_showAbout.addEventListener(MouseEvent.CLICK, btn_showAbout_clickHandler);
			}
		}
		
		override protected function partRemoved(partName:String, instance:Object):void
		{
			super.partRemoved(partName, instance);
			
			if (instance == btn_startQuiz)
			{
				btn_startQuiz.removeEventListener(MouseEvent.CLICK, btn_startQuiz_clickHandler);
			}
			if (instance == btn_showAbout)
			{
				btn_showAbout.removeEventListener(MouseEvent.CLICK, btn_showAbout_clickHandler);
			}
		}
		
		override protected function commitProperties():void
		{
			super.commitProperties();

			if (_isQuizResumableDirty)
			{
				btn_startQuiz.label = _isQuizResumable ?
					resourceManager.getString(resourceBundleName, "btn_resumeQuiz.label") :
					resourceManager.getString(resourceBundleName, "btn_startQuiz.label");

				_isQuizResumableDirty = false;
			}
		}
		
		protected function btn_startQuiz_clickHandler(event:MouseEvent):void
		{
			_isQuizResumable ?
				dispatchEvent(new QuizEvent(QuizEvent.RESUME_QUIZ)) :
                dispatchEvent(new QuizEvent(QuizEvent.START_QUIZ))
        }

		protected function btn_showAbout_clickHandler(event:MouseEvent):void
		{
			dispatchEvent(new ViewEvent(ViewEvent.DISPLAY_ABOUT_VIEW));
		}

		private function check():Boolean
		{
			return true;
		}
	}
}