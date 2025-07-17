package RiddleStrip 
{
	/**
	 * ...
	 * @author jk
	 */
	public class Riddles 
	{
		
		public function Riddles() 
		{
			Reset();
		}
		
		public function Reset():void {
			m_Riddles = new Array();
			m_CurrentRiddle = null;
			
			var riddle:Riddle;
			riddle = new Riddle();
			riddle.m_Text = "<p>Evolution erfolgt (A)zielgerichtet (B)iterativ (C)nur zufällig</p>"
			riddle.m_NumberResponses = 3;
			riddle.m_Response = 1;
			m_Riddles.push(riddle);
			
			/*riddle = new Riddle();
			riddle.m_Text = "<p>Wenn du einmal mit einem Würfel würfelst, wie hoch ist die Wahrscheinlichkeit mindestens eine 4 zu werfen:</p>"
			+ " <p>(A)50%</p> <p>(B)66%</p> <p>(C)17%</p> <p>(D)25%</p>"
			riddle.m_Response = 0;
			riddle.m_NumberResponses = 4;
			m_Riddles.push(riddle);
			
			riddle = new Riddle();
			riddle.m_Text = "<p>Die Sonnenscheindauer pro Tag ist am Äquator gegenüber den gemäßigten Breiten immer</p>"
			+ " <p>(A)equal</p> <p>(B)kürzer</p> <p>(C)länger</p>"
			riddle.m_Response = 0;
			riddle.m_NumberResponses = 3;
			m_Riddles.push(riddle);
			
			riddle = new Riddle();
			riddle.m_Text = "<p>Du hast 9 gleich große Kugeln und eine Digitalwaage. Eine ist etwas schwerer. Wie oft musst du die Waage benutzen um damit die schwere Kugel zu finden ?"
			+"(Du kannst mehrere Kugeln gleichzeitig wiegen.)</p> "
			+ " <p>(A)8</p> <p>(B)6</p> <p>(C)5</p> <p>(D)2</p>"
			riddle.m_Response = 3;
			riddle.m_NumberResponses = 4;
			m_Riddles.push(riddle);
			
			riddle = new Riddle();
			riddle.m_Text = "<p>A riddle</p> "
			+ " <p>(A)8</p> <p>(B)6</p> <p>(C)5</p> <p>(D)2</p>"
			riddle.m_Response = 0;
			riddle.m_NumberResponses = 4;
			m_Riddles.push(riddle);
			
			riddle = new Riddle();
			riddle.m_Text = "<p>A riddle</p> "
			+ " <p>(A)8</p> <p>(B)6</p> <p>(C)5</p> <p>(D)2</p>"
			riddle.m_Response = 0;
			riddle.m_NumberResponses = 4;
			m_Riddles.push(riddle);
			
			riddle = new Riddle();
			riddle.m_Text = "<p>A riddle</p> "
			+ " <p>(A)8</p> <p>(B)6</p> <p>(C)5</p> <p>(D)2</p>"
			riddle.m_Response = 0;
			riddle.m_NumberResponses = 4;
			m_Riddles.push(riddle);*/
			
			m_Solved = 0;
			m_Failed = 0;
			m_ToSolve = Math.min(m_Riddles.length,10);
		}
		
		public function GetNextRiddle():void {
				var i:int = m_Riddles.length-1;
				i *= Math.random();//randomize
				m_CurrentRiddle = m_Riddles.splice(i,1)[0];  
		}
		public function GetRiddleText():String {
			if (m_CurrentRiddle == null) return "start a riddle first";
			return m_CurrentRiddle.m_Text;
		}
		public function GetPossibleChoices():int {
			if (m_CurrentRiddle == null) return 0;
			return m_CurrentRiddle.m_NumberResponses;
		}
		public function GuessAnswer(index:int):Boolean {
			if (m_CurrentRiddle == null) return false;
			var result:Boolean = false;
			result = ( m_CurrentRiddle.m_Response==(index));
			m_Solved += result ? 1:0;
			m_Failed += result ? 0:1;
			m_ToSolve--;
			return result;
		}
		public function GetRiddlesLeft():int {
			return m_ToSolve;
		}
		public function GetRiddlesSolved():int {
			return m_Solved;
		}
		public function GetRiddlesFailed():int {
			return m_Failed;
		}
		private var m_ToSolve:int = 0; 
		private var m_Solved:int = 0;
		private var m_Failed:int = 0;
		private var m_CurrentRiddle:Riddle;
		private var m_Riddles:Array = null;
	}

}