class AddButton { 
	
	// public vars
	var button:MovieClip;
	var buttonURL:String;
	var fileTitle:String;

	// constructor
	public function AddButton(buttonName:String, targetClip:MovieClip, xPos:Number, yPos:Number, btnTitle:String, btnURL:String, fileName:String) {
		var depth:Number = targetClip.getNextHighestDepth();
		button = targetClip.attachMovie(buttonName, "button" + depth + "_mc", depth);
		button._x = xPos;
		button._y = yPos;
		
		button.buttonText_mc.button_txt.autoSize = true;
		button.buttonText_mc.button_txt.text = btnTitle;
		buttonURL = btnURL;
		fileTitle = fileName;
		
		setButtonStates(buttonURL, fileTitle);
	};
	
	public function destroy():Void {
		button.removeMovieClip();
	};
	
	private function setButtonStates(buttonURL:String, fileTitle:String):Void {
		button.onRollOver = function():Void {
			this.buttonText_mc.colorTo(_level0.navHighlight, 0);
		}
		
		button.onRollOut = function():Void {
			this.buttonText_mc.colorTo(null);
		}
		
		button.onRelease = function():Void {
			_level0.fileRef.download(buttonURL,fileTitle);
		}
	};
};