package application
{
    import domain.model.Quiz;
    import domain.model.vo.Question;
    import domain.model.vo.Answer;

    import flash.events.Event;
    import flash.events.EventDispatcher;

    import org.swizframework.storage.ISharedObjectBean;

    public class AppModel extends EventDispatcher
	{
		[Inject]
		public var quizzSoBean:ISharedObjectBean;


        private var _quiz:Quiz = null;

        private var _currentQuestion:Question;

        public function get quiz():Quiz
        {
            return _quiz;
        }

        public function set quiz(value:Quiz):void
        {
            _quiz = value;

            _currentQuestion = _quiz.firstQuestion;

            dispatchEvent(new Event("currentQuestionChanged"));
            dispatchEvent(new Event("correctAnswerChanged"));
            dispatchEvent(new Event("correctAnswerIndexChanged"));
            dispatchEvent(new Event("isPreviousQuestionPossibleChanged"));
            dispatchEvent(new Event("isNextQuestionPossibleChanged"));
        }

		[Bindable(event="currentQuestionChanged")]
		public function get currentQuestion():Question
		{
			return _currentQuestion;
		}

        [Bindable(event="correctAnswerChanged")]
        public function get correctAnswer():Answer
        {
            return _currentQuestion.correctAnswer;
        }

        [Bindable(event="correctAnswerIndexChanged")]
        public function get correctAnswerIndex():Number
        {
            return _currentQuestion.possibleAnwers.getItemIndex(
                _currentQuestion.correctAnswer
            );
        }

        [Bindable(event="isPreviousQuestionPossibleChanged")]
        public function get isPreviousQuestionPossible():Boolean
        {
            return _quiz.isPreviousQuestionPossible;
        }

        [Bindable(event="isNextQuestionPossibleChanged")]
        public function get isNextQuestionPossible():Boolean
        {
            return _quiz.isNextQuestionPossible;
        }

        public function goToPreviousQuestion():void
        {
            _currentQuestion = _quiz.previousQuestion;

            dispatchEvent(new Event("currentQuestionChanged"));
            dispatchEvent(new Event("correctAnswerChanged"));
            dispatchEvent(new Event("correctAnswerIndexChanged"));
            dispatchEvent(new Event("isPreviousQuestionPossibleChanged"));
            dispatchEvent(new Event("isNextQuestionPossibleChanged"));
        }

        public function goToNextQuestion():void
        {
            _currentQuestion = _quiz.nextQuestion;

            dispatchEvent(new Event("currentQuestionChanged"));
            dispatchEvent(new Event("correctAnswerChanged"));
            dispatchEvent(new Event("correctAnswerIndexChanged"));
            dispatchEvent(new Event("isPreviousQuestionPossibleChanged"));
            dispatchEvent(new Event("isNextQuestionPossibleChanged"));
        }

        public function get isQuizResumable():Boolean
        {
            return _quiz !== null;
        }

        public function set selectedAnswerIndex(answerIndex:Number):void
        {
            _currentQuestion.selectedAnswer = _currentQuestion.possibleAnwers.getItemAt(answerIndex) as Answer;

            dispatchEvent(new Event("currentQuestionChanged"));
        }
    }
}