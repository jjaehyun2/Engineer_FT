package interfaces.container
{
	import application.event.AnswerSelectedEvent;
	import application.event.QuizEvent;
	import application.event.ViewEvent;

	import domain.model.vo.Question;
	import domain.model.vo.Answer;

    import flash.events.MouseEvent;

	import interfaces.AbstractView;

	import interfaces.component.ValueButton;

	import spark.components.Button;
    import spark.components.Label;

    [ResourceBundle("quiz_view")]
	public class QuizView extends AbstractView
	{
        private var _currentQuestion:Question;
        private var _isCurrentQuestionDirty:Boolean;

        private var _correctAnswerIndex:Number;
        private var _correctAnswerIndexDirty:Boolean;

		private var _isPreviousQuestionPossible:Boolean;
		private var _isPreviousQuestionPossibleDirty:Boolean;

		private var _isNextQuestionPossible:Boolean;
		private var _isNextQuestionPossibleDirty:Boolean;

		[SkinPart(required="true")]
		public var txt_caption:Label;
		
		[SkinPart(required="true")]
		public var txt_question:Label;
		
		[SkinPart(required="true")]
		public var btn_answer_one:ValueButton;
		
		[SkinPart(required="true")]
		public var btn_answer_two:ValueButton;
		
		[SkinPart(required="true")]
		public var btn_answer_three:ValueButton;
		
		[SkinPart(required="true")]
		public var btn_answer_four:ValueButton;
		
		[SkinPart(required="true")]
		public var btn_previousQuestion:Button;

        [SkinPart(required="true")]
		public var btn_menu:Button;

		[SkinPart(required="true")]
		public var btn_nextQuestion:Button;

		public function QuizView()
		{
			super();
			
			this.resourceBundleName = "quiz_view";
			
			this.title = resourceManager.getString(resourceBundleName, "title");
		}

		[Inject(source="model.currentQuestion", bind="true")]
		public function set currentQuestion(value:Question):void
		{
			_currentQuestion = value;
			_isCurrentQuestionDirty = true;
			
			invalidateProperties();
		}

        [Inject(source="model.correctAnswerIndex", bind="true")]
        public function set correctAnswerIndex(value:Number):void
        {
            _correctAnswerIndex = value;
            _correctAnswerIndexDirty = true;

            invalidateProperties();
        }

		[Inject(source="model.isPreviousQuestionPossible", bind="true")]
		public function set isPreviousQuestionPossible(value:Boolean):void
		{
			_isPreviousQuestionPossible = value;
			_isPreviousQuestionPossibleDirty = true;

			invalidateProperties();
		}

		[Inject(source="model.isNextQuestionPossible", bind="true")]
		public function set isNextQuestionPossible(value:Boolean):void
		{
			_isNextQuestionPossible = value;
			_isNextQuestionPossibleDirty = true;

			invalidateProperties();
		}

		override protected function partAdded(partName:String, instance:Object):void
		{
			super.partAdded(partName, instance);

            if (instance == btn_answer_one)
            {

                btn_answer_one.addEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
            }
            if (instance == btn_answer_two)
            {
                btn_answer_two.addEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
            }
            if (instance == btn_answer_three)
            {
                btn_answer_three.addEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
            }
            if (instance == btn_answer_four)
            {
                btn_answer_four.addEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
            }

			if (instance == btn_previousQuestion)
			{
				btn_previousQuestion.label = resourceManager.getString(resourceBundleName, "btn_previousQuestion");
				btn_previousQuestion.addEventListener(MouseEvent.CLICK, btn_previousQuestion_clickHandler);
			}
			if (instance == btn_menu)
			{
				btn_menu.label = resourceManager.getString(resourceBundleName, "btn_menu");
				btn_menu.addEventListener(MouseEvent.CLICK, btn_menu_clickHandler);
			}
			if (instance == btn_nextQuestion)
			{
				btn_nextQuestion.label = resourceManager.getString(resourceBundleName, "btn_nextQuestion");
				btn_nextQuestion.addEventListener(MouseEvent.CLICK, btn_nextQuestion_clickHandler);
			}
		}
		
		override protected function partRemoved(partName:String, instance:Object):void
		{
			super.partRemoved(partName, instance);
			
			if (instance == btn_answer_one)
			{
                btn_answer_one.removeEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
			}
			if (instance == btn_answer_two)
			{
                btn_answer_two.removeEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
			}
			if (instance == btn_answer_three)
			{
                btn_answer_three.removeEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
			}
            if (instance == btn_answer_four)
            {
                btn_answer_four.removeEventListener(MouseEvent.CLICK, btn_answer_clickHandler);
            }

            if (instance == btn_previousQuestion)
            {
                btn_previousQuestion.removeEventListener(MouseEvent.CLICK, btn_previousQuestion_clickHandler);
            }
            if (instance == btn_menu)
            {
                btn_menu.removeEventListener(MouseEvent.CLICK, btn_menu_clickHandler);
            }
            if (instance == btn_nextQuestion)
            {
                btn_nextQuestion.removeEventListener(MouseEvent.CLICK, btn_nextQuestion_clickHandler);
            }
		}
		
		override protected function commitProperties():void
		{
			super.commitProperties();

			if (_isCurrentQuestionDirty)
			{
                txt_question.text = _currentQuestion.question;
				btn_answer_one.label = (_currentQuestion.possibleAnwers.getItemAt(0) as Answer).answer;
                btn_answer_one.value = '►';
                btn_answer_two.label = (_currentQuestion.possibleAnwers.getItemAt(1) as Answer).answer;
                btn_answer_two.value = '►';
                btn_answer_three.label = (_currentQuestion.possibleAnwers.getItemAt(2) as Answer).answer;
                btn_answer_three.value = '►';
                btn_answer_four.label = (_currentQuestion.possibleAnwers.getItemAt(3) as Answer).answer;
                btn_answer_four.value = '►';

                _isCurrentQuestionDirty = false;
			}

			if (_isPreviousQuestionPossibleDirty)
			{
				btn_previousQuestion.visible = _isPreviousQuestionPossible;
				_isPreviousQuestionPossibleDirty = false;
			}

			if (_isNextQuestionPossibleDirty)
			{
				btn_nextQuestion.visible = _isNextQuestionPossible;
				_isNextQuestionPossibleDirty = false;
			}
		}
		
		protected function btn_answer_clickHandler(event:MouseEvent):void
		{
            var btn_clicked:ValueButton = event.currentTarget as ValueButton;
            var answerIndex:Number = 0;

            if (btn_clicked == btn_answer_one) answerIndex = 0;
            if (btn_clicked == btn_answer_two) answerIndex = 1;
            if (btn_clicked == btn_answer_three) answerIndex = 2;
            if (btn_clicked == btn_answer_four) answerIndex = 3;

            dispatcher.dispatchEvent(new AnswerSelectedEvent(answerIndex));

            /*
            if (btn_clicked == btn_answer_one && _currentQuestion.isCorrectAnswer(_currentQuestion.possibleAnwers.getItemAt(0) as Answer))
            {
                btn_answer_one.value = '✓';
            }

            if (btn_clicked == btn_answer_two && _currentQuestion.isCorrectAnswer(_currentQuestion.possibleAnwers.getItemAt(1) as Answer))
            {
                btn_answer_two.value = '✓';
            }

            if (btn_clicked == btn_answer_three && _currentQuestion.isCorrectAnswer(_currentQuestion.possibleAnwers.getItemAt(2) as Answer))
            {
                btn_answer_three.value = '✓';
            }

            if (btn_clicked == btn_answer_four && _currentQuestion.isCorrectAnswer(_currentQuestion.possibleAnwers.getItemAt(3) as Answer))
            {
                btn_answer_four.value = '✓';
            }
            */
		}

		protected function btn_previousQuestion_clickHandler(event:MouseEvent):void
		{
            dispatcher.dispatchEvent(
				new QuizEvent(QuizEvent.GOTO_PREVIOUS_QUESTION)
            );
		}

		protected function btn_menu_clickHandler(event:MouseEvent):void
		{
			dispatcher.dispatchEvent(
				new ViewEvent(ViewEvent.DISPLAY_MENU_VIEW)
			);
		}

		protected function btn_nextQuestion_clickHandler(event:MouseEvent):void
		{
            dispatcher.dispatchEvent(
				new QuizEvent(QuizEvent.GOTO_NEXT_QUESTION)
            );
		}
    }
}