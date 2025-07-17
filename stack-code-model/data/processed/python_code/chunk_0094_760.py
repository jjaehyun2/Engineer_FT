
class dynpole extends MovieClip{
	public var astas_mc:MovieClip;
	public var angle:Array;
	private var poleRotation:Number;
	private var randomAngle:Number;
	public var mynum:Number;
	public var hitedTimes:Number;
	public var maxhitedtimes:Number;
	
	public function dynpole() {
			this.hitedTimes = 0;
			this.maxhitedtimes = 2;
			this.setAngleValues();
	}
	
	public function onEnterFrame(){
		if(_root.started == 1){
			if (this.hitTest(_root.apuntador_mc)) {
				_root.started = 2;
				this.rotatePole();
			}
		}
	}
	
	public function rotatePole(){
			this.setRandomAngle();
			_root.TwFX.changeRotation(this.astas_mc,this.randomAngle,this,"poleHit");
		}
	
	public function setPole(xpos:Number, ypos:Number) {
		this.setRandomAngle();
		this.astas_mc._rotation = this.randomAngle;//poleRotation;
		this._y = ypos;
		this._x = xpos;
	}
	
	public function poleHit(){
			var i:Number;
			var polename:String;
			if(this.hitedTimes < this.maxhitedtimes){
				for(i=0;i<_root.gamecase.poleAmount;i++){
					polename = "pole"+i+"_mc";
					if (this.hitTest(_root[polename]) && this.hitedTimes < this.maxhitedtimes) {
						_root.gamecase.poles[i].rotatePole();
						this.hitedTimes ++;
						this.rotatePole();
						this.createExplosion(this._x,this._y,3,1);
						this._alpha -= 20;
						if(this.hitedTimes == 2){
							_root.TwFX.gotoXY(this,this._x,this._y - 200,this,"destruct");
						}
					}
				}
			}
		}
	
	private function setAngleValues(){		
			this.angle = new Array();
			this.angle[0] = 0;
			//this.angle[1] = 90;
			this.angle[1] = 180;
			//angle[2] = 270;
			this.angle[2] = 360;
		}
		
	private function setRandomAngle(){
			this.poleRotation = random(3);			
			this.randomAngle = this.angle[this.poleRotation];
		}
		
	public function createExplosion(x,y,max,sameColor){
		var currentParticle = 0;
		var colors = new Array("0xFF0000","0×00FF00","0×0000FF","0xFFFF00","0xFF00FF","0×00FFFF");
        var c;
        if(sameColor){
			c = colors[int(Math.random()*colors.length)];
		}
		for(var i=0; i < max; i++){
			if(!sameColor){
				c = colors[int(Math.random()*colors.length)];
			}
			_root.attachMovie("Particle","P"+currentParticle,_root.getNextHighestDepth(),{_x:x,_y:y,rgbValue:c});
			currentParticle++;
		}
	}

	public function destruct(){
		_root.points += 1;
		this.removeMovieClip();
		}
}