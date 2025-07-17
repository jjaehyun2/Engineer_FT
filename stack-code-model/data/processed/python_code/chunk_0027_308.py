package  
{
	import net.flashpunk.FP;
	/**
	 * ...
	 * @author Andy Chase
	 * This class generates the phone caller's story
	 * and answer
	 */
	public class PersonStory 
	{
		public var richText:String;
		public var correctResponse:String;
		public var userChoice:String;
		
		private var starters:Array = new Array (
			"I don't wanna die",
			"My dog died",
			"Fiddle my biscits",
			"My daughers eating a doughnut",
			"I just got back from the beach",
			"300 ways to start a fire stuch a good book",
			"I know 90 ways to pet a chicken",
			"I am a robot",
			"Don't get me started",
			"I've been talking to like 5 different people",
			"I don't remember my fingernails being so long",
			"how tall are you,",
			"I dropped my computer into acid, burned it, drove over it twice, "
			);
			
			private var keywords:Array = new Array (
				new Array (
					" and I'm <e>having trouble</e> functining,",
					" and I really <e>can't get in</e> this,",
					" and I'm <e>unable</e> to get email,",
					" and it says my <e>credentials</e> cannot something,"
				),
				new Array(
					" and I need some <e>toner</e>,",
					" and my hand is jammed in the <e>printer</e>,",
					" and I need a to get a <e>microphone</e>, projecter and dancer,",
					" and I want to set my <e>voicemail</e> password to 666,"
				),
				new Array (
					" and I was wondering <e>what time</e> you're open?",
					" hmm.. <e>can I</e> make it before you close?",
					" and <e>what's</e> my <e>status</e> on this number thingy,",
					" and can you hear me? I'm <e>testing</e> my phone.",
					" and <e>if I come in</e>, can you make magic happen?"
				),
				new Array (
					"Marty Grah",
					"Dennis",
					"Fisher Price",
					"Abe Lincoln",
					"Sean Connery",
					"Jack Lemmon",
					"Dudley Moore",
					"Gregory Peck",
					"Van Damme",
					"Omar Epps",
					"Kevin Bacon",
					"Dennis Quaid"
				)
			);
			
			private var enders:Array = new Array(
				" my face really hurts so that would great",
				" I'm not sure if I exist.",
				" what if I'm just a recording?",
				" are you listening to me?",
				" my anger increases by the minute.",
				" I really wish I could be smarter.",
				" can you teach me to do the google?",
				" this phone looks wierd upside down",
				" I'm just not sure if I'm human",
				" so can you call me maybe?"
			);
		
		public function PersonStory() 
		{
			
		}
		
		public function NewStory():void {
			userChoice = "";
			var choice:int = FP.rand(5);
			if (choice >= 4) choice = 0;
			switch(choice) {
				case 0: correctResponse = "Q"; break;
				case 1: correctResponse = "W"; break;
				case 2: correctResponse = "E"; break;
				case 3: correctResponse = "R"; break;
			}
			if (choice < 3) {
				richText = starters[FP.rand(starters.length)]
							+ keywords[choice][FP.rand(keywords[choice].length)]
							+ enders[FP.rand(enders.length)];
			} else {
				richText = "Hello. What is your name? Okay. Can I talk to <e>" + keywords[3][FP.rand(keywords[3].length)] + "</e>? Thanks.";
			}
		}
		
		public function WasRight():Boolean {
			return userChoice == correctResponse;
		}
	}

}