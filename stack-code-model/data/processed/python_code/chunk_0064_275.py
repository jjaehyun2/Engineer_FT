package entities
{
	import entities.Bullets;
	
	import flash.display.BitmapData;
	import flash.geom.Point;
	import flash.net.LocalConnection;
	
	import net.flashpunk.Entity;
	import net.flashpunk.FP;
	import net.flashpunk.Sfx;
	import net.flashpunk.World;
	import net.flashpunk.graphics.Image;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.utils.Input;
	import net.flashpunk.utils.Key;
	
	import worlds.GameWorld;
	import worlds.Level;
	import worlds.MainMenuWorld;
	
	
	
	
	public class Player extends Entity
	{
		[Embed(source = '../assets/jump2.mp3')]
		private const JUMPSOUND:Class;
		public var jumpsound:Sfx = new Sfx(JUMPSOUND);
		
		
		[Embed(source = '../assets/click1.mp3')]
		private const CLICKSOUND:Class;
		public var clicksound:Sfx = new Sfx(CLICKSOUND);
		
		[Embed(source = '../assets/hurt.mp3')]
		private const HURTSOUND:Class;
		public var hurtsound:Sfx = new Sfx(HURTSOUND);
		
		[Embed(source = '../assets/Concerto.mp3')]
		private const CONCERTOSOUND:Class;
		public var concertosound:Sfx = new Sfx(CONCERTOSOUND);
		
		[Embed(source = '../assets/powerup1.mp3')]
		private const POWERUPSOUND:Class;
		public var powerupsound:Sfx = new Sfx(POWERUPSOUND);
		
		
		//protected var scoreText:Text;
	
		
		protected var playerImage:Image;
		protected const PLAYER_HSPEED:int = 40;
		protected var gravity:int = 24;  //the greater the number, the bigger the gravity
		protected var JUMP:int = 700;
		protected var a:Point;
		protected var v:Point;
		protected var bGravityFlipped:Boolean;  //This is used to flip the gravity on up-down direction.
		protected var cGravityFlipped:Boolean;  //this is used to flip gravity to right.
		protected var dGravityFlipped:Boolean;  //used to flip gravity to left.
		
		protected var playerHealth:Number = 50;
		protected var playerScore:Number = 0;
		protected var roundNumber:Number = 0;
		
		
		
		protected var hitcount:int = 0;  //ok, eli alussa on hitcount 0, if updown direction there are hits to walls, then hitcount is increased by one,
		// if on the other way (leftright direction), then it is decreased by one. So basically this number tells me what shape the player is, 0 is the basic shape.
		
	
	
		
		
		public function Player()
		{
			
			
			
			
			

			
			
			
			playerImage = new Image(new BitmapData(16, 24));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(16,24);
			a = new Point();
			v = new Point();
			bGravityFlipped = false;  //muuntaa normipainovoiman kohti kattoa
			cGravityFlipped = false;
			dGravityFlipped = false;
			x = 320;  //the player's starting position.
			y = 440;
			
			
		//	transformationminus1 = false;
		//	transformationplus1 = false;
		//	transformationplus2 = false;
	
		}
		
		public override function update():void
		{
		
			
			
			/*
			if(collide("exit", x, y))
			{
				FP.world = new Level(2);
			}*/
			
			if (Input.check(Key.M)) {
				concertosound.loop();
			}
			
			
			if (collide("ball",x,y)) {
				
				//playerHealth = playerHealth - 1;
				
				var d:Ball= collide("ball",x,y) as Ball;	
				if (d) {
					hurtsound.play();
					//this.playerImage.color = 0x000026.;
					graphic = playerImage;
					playerHealth = playerHealth - 0.5;
					//trace(playerHealth);
					
					if (playerHealth <= 0 ) {
						//FP.world.end();
						FP.world = new MainMenuWorld(0, this.playerScore, this.roundNumber);
					}
					
				}
			}
			
			
			//WORKING!
		//
			if(collide("bullet", x, y) && hitcount == -2 || hitcount ==3 && collide("bullet", x, y))
			{
				
				powerupsound.play();
				var c:Bullets = collide("bullet",x,y) as Bullets;	
				
				if (c)
				{
					
					this.playerScore = this.playerScore + 10000;
					this.roundNumber = this.roundNumber + 1;
					//FP.world.end();
					FP.world = new Level(this.playerScore, this.playerHealth, this.roundNumber);
				}
				
				
				//FP.world = new Level(2);
			}
			
			
			
			//THIS IS WORKING!!!!!!!!!!!!!
			/*
			if(Input.check(Key.SPACE))
			{
				FP.world.removeAll();
				FP.world = new Level(2);
			}*/
			
			
			//Collision with bullet
			if (collide("bullet", x, y))  //bullet is not the best name to describe these, maybe pills they are, but whatever, could be bullets too, just player thinks that they are pills :P
			{
			//	playerScore = playerScore + 1000;
				
				// Player is colliding with a "bullet" type.
			}
			
			// Assign the collided Bullet Entity to a temporary var.
			var b:Bullets = collide("bullet", x, y) as Bullets;
			
			// Check if b has a value (true if a Bullet was collided with).
			if (b && hitcount == -1 || b && hitcount == 2)
			{
				this.playerScore = this.playerScore + 30;
				
				// Call the Bullet's destroy() function.
				b.destroy();
			}
			
			if (b && hitcount == 0 || b && hitcount == 1)
			{
				this.playerScore = this.playerScore + 10;
				
				// Call the Bullet's destroy() function.
				b.destroy();
			}
			
			
			
			
			if (hitcount ==-2 && isOnGround && !cGravityFlipped && !dGravityFlipped) {
				JUMP = 1000;
				
			}
			
			else if (hitcount ==-1 && isOnGround && !cGravityFlipped && !dGravityFlipped) {
				JUMP = 700;
			}
			
			else if (hitcount == 3 && isOnGround3 && dGravityFlipped  || hitcount == 3 && isOnGround3 && cGravityFlipped ) { //if the tall player is jumping, its jumping higher
				JUMP = 1000;
				
			}
			
			else if (hitcount == 2 && isOnGround3 && dGravityFlipped|| hitcount == 2 && isOnGround3 && cGravityFlipped) { //need here many conditions, so that it works on all special occassions too correctly.
				JUMP = 700;
			}
			
			else if (hitcount == 1 && isOnGround3 && dGravityFlipped || hitcount == 1 && isOnGround3 && cGravityFlipped) {
				JUMP = 400;
				
			}
			
			else {
				JUMP = 400;
			}
			
			// Checking player input.
			var hInput:int = 0;

			if (!cGravityFlipped && !bGravityFlipped) {	 //gravity pulls down, the normal condition, just like we are used to the gravity! :)
			if(Input.check(Key.LEFT)) hInput -= 8; // MOVE LEFT
			if(Input.check(Key.RIGHT)) hInput += 8; // MOVE RIGHT	
			if(Input.pressed(Key.UP)) jump();    //painamalla ylos tai alas niin gravity filppaa ylos-alas suunnassa
			if (Input.pressed(Key.W)) flipGravity();		
			//if(Input.pressed(Key.DOWN)) flipGravity();
			if (Input.pressed(Key.D))  {
				v.x = 0;
				a.x = 0;
				flipToRightLeftGravity();
			}
			
			if (Input.pressed(Key.A)) {
				v.x = 0;
				a.x = 0;
				dGravityFlipped = true;   //this dGravityFlipped is used to turn gravity pulling to right to pull to left, so it can be used here like this if we want now gravity to left.
				flipToRightLeftGravity();
			}

			
			}
			
			
			if (!cGravityFlipped && bGravityFlipped) {	  //situation is here that the gravity pulls up now.
				if(Input.check(Key.LEFT)) hInput -= 8; // MOVE LEFT
				if(Input.check(Key.RIGHT)) hInput += 8; // MOVE RIGHT	
				if(Input.pressed(Key.DOWN)) jump();    //painamalla ylos tai alas niin gravity filppaa ylos-alas suunnassa
				if (Input.pressed(Key.S)) flipGravity();		
				//if(Input.pressed(Key.DOWN)) flipGravity();
				if (Input.pressed(Key.D)) {
					flipToRightFromUp();		//created this method here to work right specifically in this situation.
				}
				if (Input.pressed(Key.A)) {
					flipToLeftFromUp();
				}
				
				
				
				
			}
			
			
			
			
			
			

			
			 //gravity is pulling now to right here.
			if (cGravityFlipped && !dGravityFlipped) {
				
				
				if(Input.check(Key.UP)) hInput -= 8; // MOVE LEFT
				if(Input.check(Key.DOWN)) hInput += 8; // MOVE RIGHT	
				if (Input.check(Key.LEFT)) jumpLeftRight();
				if (Input.pressed(Key.A)) {
					
					if (isOnRight) {
						v.x=0;   //failsafe , to make sure that the horizontal speed and acceleration is at zero now, because soon we are going to flip those around on "leftflipGravity()"
						a.x = 0; 	
					}
					
					rightToLeftflipGravity();
				}
				
				if (Input.pressed(Key.S)) {
					
					if (isOnRight) {
						bGravityFlipped = false;
						cGravityFlipped = false;	
					}
				}
				if (Input.pressed(Key.W)) {
					if (isOnRight) {
						bGravityFlipped = true;
						cGravityFlipped = false;
					}

				}
				
				
			}
			if (cGravityFlipped && dGravityFlipped) {  //gravity is pulling to left here.
				if(Input.check(Key.UP)) hInput -= 8; // MOVE LEFT
				if(Input.check(Key.DOWN)) hInput += 8; // MOVE RIGHT	
				if (Input.check(Key.RIGHT)) jumpLeftRight();
				if (Input.pressed(Key.D)) {
					
					if (isOnLeft) {
						v.x = 0; //failsafe , to make sure that the horizontal speed and acceleration is at zero now, because soon we are going to flip those around on "leftflipGravity()"
						a.x = 0;
					}
				
					rightToLeftflipGravity();
				}
				
				
				if (Input.pressed(Key.W)) {
					if (isOnLeft) {
						
						bGravityFlipped = true;
						cGravityFlipped = false;
						dGravityFlipped = false;
					}
				}
				
				
				if (Input.pressed(Key.S)) {
					v.y = 0;
					a.y = 0;
					
					if (isOnLeft) {
						
						bGravityFlipped = false;
						cGravityFlipped = false;
						dGravityFlipped = false;
					}
				}
				
				
				
			}
	
			
			
			
			
			
		//	if (Input.pressed(Key.ENTER)) gravityToggle();  here the gravity can be changed.
			
			//ok, hmm. this could be fun addition, but yeah..
			//not using it for now.
			
			
			
			
			
			if (!cGravityFlipped) { // Jos tilanne on se, etta painovoima on ylos-alas suuntainen.
				
				
				// Update physics.
				v.x = PLAYER_HSPEED * hInput;	
			
				if(bGravityFlipped) {
					a.y = -gravity;
				}
				else {
					a.y =gravity;
				}
		
				v.y += a.y;
			
				// Apply physics.
				x += v.x * FP.elapsed;
				y += v.y * FP.elapsed;
				
				
				
				
				
				
				
				/*
				//this third one of these shapetransformations need to come last, after the two has happened.
				if (v.y >= 1100 && shapetransformationUpDown3 == false && shapetransformationUpDown == true && shapetransformationUpDown2 == true && y + height >= FP.screen.height || y <= 1 && v.y <= -1100 && shapetransformationUpDown3 == false && shapetransformationUpDown == true && shapetransformationUpDown2 == true) {
					transform3();
				}*/
				
				if (v.y >= 1100 && hitcount == 2 && y + height >= FP.screen.height || y <= 0 && v.y <= -1100  && hitcount == 2 ) {
					transform3();
				}
				
				
				
				
				if (v.y >= 1100 && y + height >= FP.screen.height && hitcount == 1 || y <= 0 && v.y <= -1100 && hitcount == 1) {
					//trace(v.y);
					transform2();
					
				}
				
				
				//trace(v.y);
				
				/*
				if (v.y >= 1100 && shapetransformationUpDown == false && y + height >= FP.screen.height   && shapetransformationUpDown2 == false || y <= 1 && v.y <= -1100 && shapetransformationUpDown == false && shapetransformationUpDown2 == false ) {
					transform1();
					
					
				}*/

				if (v.y >= 1150 && y + height >= FP.screen.height   && hitcount == 0 || y <= 0 && v.y <= -1150 && hitcount == 0  ) {
					transform1();
					//trace(v.y);
					
				}
				
				
			
				if (v.y >= 1100 &&  y + height >= FP.screen.height   && hitcount == -1  || y <= 0 && v.y <= -1100 && hitcount == -1  ) {
					transform0();
					//trace(v.y);
					
				}
				
				if (v.y >= 1100 &&  y + height >= FP.screen.height   && hitcount == -2  || y <= 0 && v.y <= -1100 && hitcount == -2  ) {
					transform00();
					
					
				}
				

				
			
				
			
				// Simple collision with boundries.
				if(y + height > FP.screen.height)
				{
					v.y = 0;
					y = FP.screen.height - height;
				}
			
				if (y<0) {
					v.y = 0;
					y=0;
				}
			
			
				if(x > FP.screen.width-width)
				{	
					v.x = 0;
					x = FP.screen.width-width;
				}
				else if(x < 0)
				{
					v.x = 0;
					x = 0;
				}
			
			}
			
			if (cGravityFlipped) { //jos painovoima on oikea-vasen suuntainen
				
				
				
				v.y = PLAYER_HSPEED * hInput;	
				if(dGravityFlipped) {
					a.x = -gravity;
				}
				
				else {
					a.x =gravity;
				}
				v.x += a.x;
			
				
				// Apply physics.
				x += v.x * FP.elapsed;
				y += v.y * FP.elapsed;
				
				
				
				
				
				
				
				//this third one of these shapetransformations need to come last, after the two has happened.
			//	if (v.y >= 1100 && shapetransformationUpDown3 == false && shapetransformationUpDown == true && shapetransformationUpDown2 == true && y + height >= FP.screen.height || y <= 1 && v.y <= -1100 && shapetransformationUpDown3 == false && shapetransformationUpDown == true && shapetransformationUpDown2 == true) {
		//			transform1();
		//		}
				
				
				
				
				
				
				
				if (v.x >= 1174 && x + width >= FP.screen.width && hitcount ==-1 || x <= 0 && v.x <= -1174 && hitcount ==-1) {
					transform000();
	
				//	trace(v.x);
					//hitcount = -1;	
					
				}
				

				
				
				
				if (v.x >= 1174 && x + width >= FP.screen.width && hitcount ==0 || x <= 0 && v.x <= -1174 && hitcount ==0) {
					transform00();

					//trace(v.x);
					//hitcount = -1;
					
					
					
				}
				
				
				
				
				if (v.x >= 1174 && x + width >= FP.screen.width && hitcount ==1 || x <= 0 && v.x <= -1174 && hitcount == 1) {
					transform0();
	
					//trace(v.x);
					
					//hitcount = hitcount -2;
					
					
				}

				
				
				if (v.x >= 1174 && x + width  >= FP.screen.width && hitcount == 2 || x <= 0 && v.x <= -1174 && hitcount ==2) {
					transform1();
		
				//	trace(v.x);
					//hitcount = hitcount -2;
				}
				
				
				/*

				
				*/
				
				
				if (v.x >= 1174 && x + width >= FP.screen.width && hitcount == 3 || x <= 0 && v.x <= -1174 && hitcount == 3 ) {
					transform2();
			
					//trace(v.x);
					//hitcount = hitcount -2;
					
					
					
				}
				
				
				
				
						
				//trace(v.y);
				
				
			
				
				
				
				
				
				
				
				
				// Simple collision with boundries.
				if(y + height > FP.screen.height)
				{
					// if it's wanted that there is some "glue" on the walls, there could be some modifiers here.
					//for example press first A and then down button during the gravitation transformation.
					v.y = 0;
					y = FP.screen.height - height;
				}
				
				if (y<0) {
					
					v.y = 0;
					y=0;
				}
				
				
				if(x > FP.screen.width-width)
				{	
					v.x = 0;
					x = FP.screen.width-width;
				}
				else if(x < 0)
				{	
					v.x = 0;
					x = 0;
				}
				
				
			}
			
			
			// Update parent shit.
			super.update();
		}
		
		protected function jump():void
		{
			
			
			//jos pelaaja on ruudun alareunalla ja ei ole gravityflipped tai toisinpäin
			if(isOnGround)
			
			{
				jumpsound.play();
				
				if (bGravityFlipped) {
					v.y = JUMP; //jos hyppy 
					
				} else {
					v.y = -JUMP;
				}
				
			}
		}
		
		
		
		protected function jumpLeftRight():void
		{
			
			
			
			//jos pelaaja on ruudun alareunalla ja ei ole gravityflipped tai toisinpäin
			if(isOnGround2 || isOnGround3)
				
			{
				
				jumpsound.play();
				
				if (dGravityFlipped) {
					v.x = JUMP; //jos hyppy 
					
				} else {
					v.x = -JUMP;
				}
				
			}
		}
		
		
		
		
		
		
		
		
		protected function flipGravity():void {
			
			if (isOnGround) {
				bGravityFlipped = !bGravityFlipped;
			}
			
		}
		
		protected function flipToRightLeftGravity():void {
				
			if (isOnGround2) {
				cGravityFlipped = !cGravityFlipped;
			}
			
		}
		
		protected function flipToRightFromUp():void {
			
			if (isOnGround) {
				bGravityFlipped = !bGravityFlipped;
				cGravityFlipped = !cGravityFlipped;
			}
			
		}
		
		protected function flipToLeftFromUp():void {
			
			if (isOnGround) {
				bGravityFlipped = !bGravityFlipped;
				cGravityFlipped = !cGravityFlipped;
				dGravityFlipped = !dGravityFlipped;
			}
			
		}
		
		
		
		
		protected function rightToLeftflipGravity():void {
			
			if (isOnGround3) {
				dGravityFlipped = !dGravityFlipped;
			}
			
		}
		
		
	/*	protected function gravityToggle():void {  //fun stuff, but not included in the final game for now
			if (gravity >=4) {
				gravity = 3;
			}
			else if (gravity ==3) {
				gravity = 2;
				
			}
			
			else {
				gravity =4;
			}
			
		}
		*/
		
		//checks if player is on the DOWN OR UP.
		public function get isOnGround():Boolean { 
			return (y + height >= FP.screen.height && !bGravityFlipped) || (y <=0 && bGravityFlipped);
		}
		
		//checks if the player is on DOWN OR RIGHT
		public function get isOnGround2():Boolean {
			return (y + height >= FP.screen.height && !cGravityFlipped) || (x + width >= FP.screen.width && cGravityFlipped) ;
		}
		
		//checks if the plaeyr is RIGHT or LEFT
		public function get isOnGround3():Boolean { 
			return (x + width >= FP.screen.width && !dGravityFlipped) || (x <= 0 && dGravityFlipped);
		}
		
		public function get isOnLeft(): Boolean {
			//v.x = 0;
			return (x <= 0 && dGravityFlipped);
		}
		
		public function get isOnRight(): Boolean {
			//v.x = 0;
			return (x + width >= FP.screen.width && !dGravityFlipped);
		}
		
		
		
		
		
		
		
		
		
		
		
		
		protected function transform000():void {
			//trace(v.y);
			clicksound.play();
			playerImage = new Image(new BitmapData(7, 55));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(7,55);
			width = 7;
			height = 55;

			
			hitcount = -2;
			//trace(-2);
			
			
			
		}
		
		
		
		
		
		
		
		
		
		
		
		
		protected function transform00():void {
			//trace(v.y);
			clicksound.play();
			playerImage = new Image(new BitmapData(11, 36));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(11,36);
			width = 11;
			height = 36;

			
			hitcount = -1;
			///trace(-1);
		}
		
		
		
		
		protected function transform0():void {
			//trace(v.y);
			clicksound.play();
			playerImage = new Image(new BitmapData(16, 24));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(16,24);
			width = 16;
			height = 24;
			


			
			hitcount = 0;
			//trace(0);
		}
		
		
		
		
		
		protected function transform1():void {
			
			clicksound.play();
			playerImage = new Image(new BitmapData(26, 15));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(26,15);
			width = 26;
			height = 15;

			
			hitcount = 1;
			//trace(1);
			
			
		}
		
		protected function transform2():void {
			clicksound.play();
			playerImage = new Image(new BitmapData(36, 11));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(36,11);
			width = 36;
			height = 11;
			
	
			hitcount = 2;
			
			
			
		}
		
		protected function transform3():void {
			
			clicksound.play();
			playerImage = new Image(new BitmapData(55, 7));
			playerImage.color = 0xf0c826;
			graphic = playerImage;
			setHitbox(55,7);
			width = 55;
			height = 7;

			hitcount = 3;
			
		}
		
		
		public function getScore():Number {
			return this.playerScore;
		}
		
		public function setScore(e:Number): void {
			this.playerScore = e;
		}
		
		
		public function getHealth():Number {
			return this.playerHealth;
		}
		
		public function setHealth(e:Number): void {
			this.playerHealth = e;
		}
		
		public function getRound():Number {
			return this.roundNumber;
		}
		
		public function setRound(e:Number): void {
			this.roundNumber = e;
		}
		

		
		

		
		

		
		
	}
}