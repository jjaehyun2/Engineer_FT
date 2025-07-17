package classes {
	
	import classes.Piece;
	
	public class Queen extends Piece{		
		public function Queen(X:Number,Y:Number){
			x = X;
			y = Y;
			vx = 0;
			vy = 0;
			r = 31/2;
			m = 5;
			//fric = 0.1;
			type = "Queen";
		}
	}
}