class Note extends MovieClip {
	//Create Note Names
	public var direction:String = "";
	
	public var isHit:Boolean = false;
	public var _value = 0;

	function onLoad(){
		this._y = 0;
		this.points.gotoAndStop(1);
	}
	
	function onUnload(){
		trace("Note Unloaded");
	}
	
	function arrowHit(){
		_root.vocals.isMiss = false;
		this.isHit = true;
		this._value = 0;
				
		//Animate Speaker GOOD
		_root.game.speaker.gotoAndPlay(36);
		
		if(this.points._currentframe == 2){
			this._value = 300;
			_root.game.combo_counter.points.gotoAndStop(1);
		}else if(this.points._currentframe == 3){
			this._value = 600;
			_root.game.combo_counter.points.gotoAndStop(2);
		}else if(this.points._currentframe == 4){
			this._value = 200;
			_root.game.combo_counter.points.gotoAndStop(3);
		}
		
		_root.game.combo += 1;
		_root.game.combo_counter.gotoAndPlay(1);
		_root.game.combo_counter.combo_left.gotoAndPlay(1);
		_root.game.combo_counter.combo_right.gotoAndPlay(1);
		_root.game.combo_counter.combo_x.gotoAndPlay(1);
			
		trace("Combo: " + _root.game.combo);
		
		_root.game.score += (this._value * _root.game.combo);
		trace("Score: " + _root.game.score);
		
		this.gotoAndPlay(2);
	}

	function onEnterFrame(){		
		if(this.isHit){
			this._y = 1060;
		}
	
		//Unload Notes on Final Frame
		if(this._currentframe == 5){
			this.swapDepths(0)
			this.removeMovieClip();
		}
		
		/*
		//Calculate Score
		Perfect = 600 points
		Early = 300 points
		Late = 200 points

		//Score is multiplied by combo each note, compounded
		//(e.g. (600 * 1 + 300 * 2 + 300 * 3... + 300 * 7 in the combo)
		*/
		
		if(!isHit){
			//Move down the screen, takes 60 frames or 1 second
			this._y += 18;
		
			if(this._y > 1024){
				//Early
				if(this._y < 1056){
					this.points.gotoAndStop(2);
					
					//Left Arrow
					if(this.direction == "L"){
						if(_root.game._left.isPressed){
							trace("+ MEDIUM FRIES");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(1);
							_root.game._left.gotoAndPlay(3);
							arrowHit();
						}
					}
					//Down Arrow
					if(this.direction == "D"){
						if(_root.game._down.isPressed){
							trace("+ MEDIUM SODA");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(2);
							arrowHit();
						}
					}
					//Up Arrow
					if(this.direction == "U"){
						if(_root.game._up.isPressed){
							trace("+ CINNAMON STICKS");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(3);
							arrowHit();
						}
					}
					//Right Arrow
					if(this.direction == "R"){
						if(_root.game._right.isPressed){
							trace("+ GOOD BOY MEAL");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(4);
							arrowHit();
						}
					}
				}
				//Perfect
				else if(this._y < 1080){
					this.points.gotoAndStop(3);
				
					//Left Arrow
					if(this.direction == "L"){
						if(_root.game._left.isPressed){
							trace("+ LARGE FRIES");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(5);
							_root.game._left.gotoAndPlay(3);
							arrowHit();
						}
					}
					//Down Arrow
					if(this.direction == "D"){
						if(_root.game._down.isPressed){
							trace("+ LARGE SODA");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(6);
							arrowHit();
						}
					}
					//Up Arrow
					if(this.direction == "U"){
						if(_root.game._up.isPressed){
							trace("+ EXTRA CINNAMON STICKS");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(7);
							arrowHit();
						}
					}
					//Right Arrow
					if(this.direction == "R"){
						if(_root.game._right.isPressed){
							trace("+ JOYFUL MEAL");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(8);
							arrowHit();
						}
					}
				}
				//Late
				else if(this._y < 1128){
					this.points.gotoAndStop(4);
				
					//Left Arrow
					if(this.direction == "L"){
						if(_root.game._left.isPressed){
							trace("+ SMALL FRIES");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(9);
							_root.game._left.gotoAndPlay(3);
							arrowHit();
						}
					}
					//Down Arrow
					if(this.direction == "D"){
						if(_root.game._down.isPressed){
							trace("+ SMALL SODA");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(10);
							arrowHit();
						}
					}
					//Up Arrow
					if(this.direction == "U"){
						if(_root.game._up.isPressed){
							trace("+ BREADSTICKS");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(11);
							arrowHit();
						}
					}
					//Right Arrow
					if(this.direction == "R"){
						if(_root.game._right.isPressed){
							trace("+ SADLY MEAL");
							_root.game.menu.food.gotoAndPlay(1);
							_root.game.menu.food.food_name.gotoAndStop(12);
							arrowHit();
						}
					}
				//Miss
				}else if(this._y < 1150){
					this.points.gotoAndStop(5);
					
					_root.vocals.isMiss = true;
					trace("Miss");
					
					//Animate Speaker BAD
					_root.game.speaker.gotoAndPlay(77);
					
					//Medal
					if(this.direction == "U"){
						_root.NG.cinnamonMedal = false;
						trace("cinnamonMedal: " + _root.NG.cinnamonMedal);
					}
				}else if(this._y > 1280){
					this.swapDepths(0)
					this.removeMovieClip();
				}
			}
		}
	}
}