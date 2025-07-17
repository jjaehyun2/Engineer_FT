package  
{
	/**
	 * ...
	 * @author Andy Chase
	 */
	public class Assets 
	{
		// Resources
		[Embed(source = 'assets/tiles.png')] public static const TILES:Class;
		[Embed(source = 'assets/player.png')] public static const PLAYER:Class;
		[Embed(source = 'assets/heads.png')] public static const HEADS:Class;
		[Embed(source = 'assets/chat.png')] public static const CHAT:Class;
		[Embed(source = 'assets/map.json', mimeType = "application/octet-stream")]
			public static const MAP:Class;
		
		// Chats
		public static const staphonSays:Array = new Array(
			"Check out this picture of SUPERMAN i'm drawing.",
			"Check out this picture of SUPERMAN i'm drawing.",
			"Check out this picture of SUPERMAN i'm drawing.",
			"Check out this picture of SPIDERMAN i'm drawing",
			"Check out this picture of SPIDERMAN i'm drawing",
			"Have you seen the new SONIC game?",
			"Have you seen that new episode of SONIC?",
			"Have you checked your TINY VILLAGE lately?",
			"Have you checked your TINY VILLAGE lately?",
			"Where's PERRY?",
			"*busy drawing*"
		);
			
		public static const steveSays:Array = new Array (
			"Make sure you turn in your paychecks!!!",
			"Make sure you turn in your paychecks before SUMMER",
			"Make sure you turn in your paychecks before VACATION",
			"Hey man are you going to get the new EVO?",
			"Hey man are you going to get the new EVO?",
			"Hey man are you going to get the new EVO?",
			"Hey man are you going to get the new EVO?",
			"Hey man, what's up?",
			"Hey man, what's up?",
			"Ah man, my transmission broke on the way to work",
			"I really gotta trash this junker",
			"Have you seen the new GOOGLE PRODUCT?"
		);
		
		public static const meganSays:Array = new Array (
			"1 day until FLORIDA!",
			"2 days until FLORIDA!",
			"5 days until FLORIDA!",
			"7 days until FLORIDA!",
			"Don't talk to me.",
			"Don't talk to me.",
			"Don't talk to me.",
			"So my roomates...",
			"OMG my roomates...",
			"OMG my roomates...",
			"Don, me and Andy are best friends now.",
			"Don, can we take out the wii?",
			"I hate you",
			"I hate you"
		);
		
		public static const courtneySays:Array = new Array (
			"I hate talking on the phone",
			"So my cats",
			"ANDY!!!!!!!! YOU DIDN'T ______",
			"I missed you guys",
			"RIA: CHIPOTLE!!",
			"So my cats tried to eat me today",
			"I couldn't sleep... like ever"
		);
		
		public static const dennisSays:Array = new Array (
			"Hey man...",
			"Hey man...",
			"Hey man...",
			"Like if you're gunna do that you gotta at least...",
			"...",
			"*Squaky Dianna Impression* I'm sOoOoOo cOold :X",
			"*Squaky Dianna Impression* I'm sOoOoOo cOold :X",
			"The giants beat the patriots?"
		);
		
		public static const dianaSays:Array = new Array (
			"It's so cOOOOOLD in here!!!",
			"It's so cOOOOOLD in here!!",
			"It's so cOOOOOLD in here!",
			"It's so cOOOOOLD in here.",
			"Hey can you check on an email for me?",
			"Assign that to me, I'll take care of it"
		);

		public static const ssSays:Array = new Array (
			"...",
			"...",
			"There's like 50 of us",
			"There's like 50 of us",
			"I only open up to customers",
			"I only open up to customers",
			"No thanks",
			"What's the work order number?",
			"I'm calling the MOD",
			"I don't know how"
		);
		
		public static const customerSays:Array = new Array (
			"[HINT] Although most of the things I say are convaluted, the workflow is always the same.",
			"[HINT] Key words like 'it says' means that it's a password reset.",
			"[HINT] Work orders work every time, but you risk The Wrath of Steve (or Courtney) for dumb requests",
			"[HINT] Smile :-))))))))",
			"[HINT] You don't get paid to make me happy, you get paid to get a high FCR %. Resolve or hang up!",
			"[HINT] Sales calls can be tricky, a giveaway is someone asking for someone wierd that doesn't work here anymore.",
			"[HINT] Go to the empty cubical to start"
		);
		
		public static const minigameSays:Array = new Array (
			"Return to Game... [Q]\nExplore with arrow keys or mouse"
		)
			
			
		public static const chatWords:Array = new Array ();
		chatWords["staphon"] = staphonSays;
		chatWords["steve"] = steveSays;
		chatWords["megan"] = meganSays;
		chatWords["courtney"] = courtneySays;
		chatWords["dennis"] = dennisSays;
		chatWords["diana"] = dianaSays;
		chatWords["customer"] = customerSays;
		chatWords["ss"] = ssSays;
		chatWords["minigame"] = minigameSays;
			
	}

}