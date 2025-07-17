import pl.drawing.Rysowanie
import template_form.mvctemplate.*
import template_form.mvc.*
import template_form.I.*
import flash.display.BitmapData
import template_form.util.Observable

import mx.transitions.Tween
import mx.transitions.easing.*

import template_form.Configuration

 

class template_form.mvctemplate.SendView extends AbstractView {
	
var t:TextField
var background:MovieClip
	 
/////////////////////////////////////////////////////////	

public function defaultController (model:Observable):Controller {
  return new SendController(model)
 }
 
//////////////////////////////////////////////////////////////////


function onRelease(){
	var m:FormModel=FormModel(this.getModel())
	m.check()
}

//////////////////////////////////////////////////////////////////

function onLoad(){
	var m:FormModel = FormModel(this.getModel())
	
	NewColor.setColor(background, Configuration.BUTTON_BCG_COLOR.split(",")[0])
	background._alpha=Configuration.BUTTON_BCG_COLOR.split(",")[1]
	
	t.embedFonts=true
	this.t.text = m.__buttonSend	
	this.t.textColor=m.__buttonTextColor
	//setColorBackground()
}

//////////////////////////////////////////////////////////////////
 
function setColorBackground(){
	var m:FormModel=FormModel(this.getModel())
	var color:Color = new Color(this.background)
	color.setRGB(m.__buttonBackgroundColor)
	
	
}

//////////////////////////////////////////////////////////////////

function onRollOver() {
	background.background2.gotoAndPlay(2)
}

////////////////////////////////////////////////////////////////////

function onRollOut() {
	background.background2.gotoAndPlay(11)
}

}