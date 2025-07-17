package hud {
	
	import net.flashpunk.FP;
	import game.Constants;
	
	public class ProceduralMessage extends AnimatedMessage {
		
		protected var subjects:Array;
		protected var verbs:Array;
		protected var objects:Array;
		
		public function ProceduralMessage(subjects:Array, verbs:Array, objects:Array, color:uint) {
			this.subjects = subjects;
			this.verbs = verbs;
			this.objects = objects;
			
			var title:String = "";
			title += subjects[uint(Math.random() * 4)];
			title += ", YOU " + verbs[uint(Math.random() * 4)];
			title += " THAT " + objects[uint(Math.random() * 4)];
			
			super(FP.halfWidth, FP.halfHeight, title, 16, color, 0x000000, Constants.SEESAW_ANIMATION);
		}
	}

}