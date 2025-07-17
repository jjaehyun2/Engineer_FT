class dynresetbtn extends MovieClip {
	
	public function dynresetbtn(){
			//trace('setting reset button');
		}
	public function onPress(){
		_root.TwFX.changeWH(this, 187, 44);
		_root.gamecase.resetPoleGround();		
	}
	
	public function onRelease(){
		_root.TwFX.changeWH(this, 177, 34);
		}
	
	public function onRollOut(){
		_root.TwFX.fadeTo(this,100);
		}
		
	public function onRollOver(){
		_root.TwFX.fadeTo(this,15);
		}	
		
	}