class pole extends MovieClip{
	
		public function pole(){
				trace('dynpole');
			}
		
		public function jiji(){
			trace('jejej');
			}
		
		public function setPos(xpos:Number,ypos:Number){
trace('primero');			
			this._y = ypos;
			this._x = xpos;
trace('posicionando'+ ypos);
		}
	}