package application.event
{
	import flash.events.Event;
	
	public class AnswerSelectedEvent extends Event
	{
		public static const ANSWER_SELECTED:String = 'AnswerEvent.ANSWER_SELECTED';

		private var _answerIndex:Number;

		public function AnswerSelectedEvent(answerIndex:Number, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super(ANSWER_SELECTED, bubbles, cancelable);

			_answerIndex = answerIndex;
		}

		public function get answerIndex():Number
		{
			return _answerIndex;
		}
	}
}