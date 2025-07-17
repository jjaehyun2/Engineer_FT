package  {
	import flash.display.MovieClip;
	import flash.events.Event;
	
	public class Scenery {
		private var grass1:MovieClip;
		private var grass2:MovieClip;
		private var s1:MovieClip;
		private var s2:MovieClip;
		private var s3:MovieClip;
		private var s4:MovieClip;
		private var s5:MovieClip;
		private var enemy:Enemy;
		private var speed:Number;
		private var sceneryFrames:Number;
		private var pause:Boolean;
		

		public function Scenery(grass1:MovieClip,grass2:MovieClip,enemy:Enemy,s1:MovieClip,s2:MovieClip,s3:MovieClip,s4:MovieClip,s5:MovieClip,set1:Number,set2:Number,set3:Number,set4:Number) {
			this.grass1 = grass1;
			this.grass2 = grass2;
			this.grass1.mouseEnabled = false;
			this.grass1.mouseChildren = false;
			this.grass2.mouseEnabled = false;
			this.grass2.mouseChildren = false;
			
			this.s1 = s1;
			this.s2 = s2;
			this.s3 = s3;
			this.s4 = s4;
			this.s5 = s5;
			this.s1.mouseEnabled = false;
			this.s1.mouseChildren = false;
			this.s2.mouseEnabled = false;
			this.s2.mouseChildren = false;
			this.s3.mouseEnabled = false;
			this.s3.mouseChildren = false;
			this.s4.mouseEnabled = false;
			this.s4.mouseChildren = false;
			this.s5.mouseEnabled = false;
			this.s5.mouseChildren = false;
			
			this.sceneryFrames = 10;
			
			this.s1.gotoAndStop(set1);
			this.s2.gotoAndStop(set2);
			this.s3.gotoAndStop(set3);
			this.s4.gotoAndStop(set4);	
			this.s5.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
			
			this.enemy = enemy;
			this.speed = enemy.getSpeed();
			this.grass1.addEventListener(Event.ENTER_FRAME,move);
			
			this.pause = false;
		}
		
		public function move(event:Event) {
			if(this.pause == false) {
				this.speed = this.enemy.getSpeed();
				this.grass1.x = this.grass1.x - this.speed;
				this.grass2.x = this.grass2.x - this.speed;
				this.s1.x = this.s1.x - this.speed/3;
				this.s2.x = this.s2.x - this.speed/3;
				this.s3.x = this.s3.x - this.speed/3;
				this.s4.x = this.s4.x - this.speed/3;
				this.s5.x = this.s5.x - this.speed/3;
				
				if(this.grass1.x <= - 960) {
					this.grass1.x = grass2.x+960;
				}
				if(this.grass2.x <= - 960) {		
					this.grass2.x = grass1.x +960;
				}
				
				if(this.s1.x <= -240) {
					this.s1.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
					this.s1.x = this.s5.x + 240;
				}
				if(this.s2.x <= -240) {
					this.s2.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
					this.s2.x = this.s1.x + 240;
				}
				if(this.s3.x <= -240) {
					this.s3.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
					this.s3.x = this.s2.x + 240;
				}
				if(this.s4.x <= -240) {
					this.s4.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
					this.s4.x = this.s3.x + 240;
				}
				if(this.s5.x <= -240) {
					this.s5.gotoAndStop(Math.floor(Math.random() * this.sceneryFrames) + 2);
					this.s5.x = this.s4.x + 240;
				}
			}
		}
		
		public function removeEventListeners():void {
			this.grass1.removeEventListener(Event.ENTER_FRAME,move);
		}
		
		public function setPause() {
			if(this.pause == false) {
				this.pause = true;
			}
			else if(this.pause) {
				this.pause = false;
			}
		}
		public function getPause():Boolean {
			return this.pause;
		}
	}
	
}