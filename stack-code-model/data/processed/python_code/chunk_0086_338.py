package domain.model
{
    import domain.model.vo.Question;

    import flash.events.Event;

    import mockolate.nice;
    import mockolate.prepare;
    import mockolate.stub;

    import mx.collections.ArrayCollection;

    import org.flexunit.asserts.assertTrue;
    import org.flexunit.async.Async;

    public class QuizFactoryTest
    {
        [Before(async, timeout=5000)]
        public function prepareMockolates():void
        {
            Async.proceedOnEvent(this, prepare(QuestionPool), Event.COMPLETE);
        }

        [Before]
        public function setUp():void {  }

        [After]
        public function tearDown():void {  }

        [Test]
        public function testCreateQuiz():void
        {
            var questionPool:QuestionPool = nice(QuestionPool);
            stub(questionPool).method("getRandomQuestions").args(3).returns(getQuestionsArrayCollectionFixture());

            var quizFactory:QuizFactory = new QuizFactory(questionPool);
            var quiz:Quiz = quizFactory.createQuiz(3);

            assertTrue(quiz.questions.length === 3);
        }

        private function getQuestionsArrayCollectionFixture():ArrayCollection
        {
            return new ArrayCollection([
                new Question(1, 'firstQuestion', null, null),
                new Question(2, 'secondQuestion', null, null),
                new Question(3, 'thirdQuestion', null, null),
            ]);
        }
    }
}