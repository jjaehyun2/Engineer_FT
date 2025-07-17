import pl.drawing.Rysowanie
import menu_tree.mvctemplate.*
import menu_tree.mvc.*
import menu_tree.I.*
import flash.display.BitmapData
import menu_tree.util.Observable

import mx.transitions.Tween
import mx.transitions.easing.*


  

class menu_tree.mvctemplate.BackgroundView extends AbstractItem {


var background:MovieClip
var title:TextField
	
////////////////////////////////////////////////////////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new BackgroundController(model)
 }
 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////

function BackgroundView(){

}
 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function onLoad() {
		var m:TreeModel=TreeModel(this.getModel())
	this.onResize()	
	this.enabled = false
	
	NewColor.setColor(background, m.COLOR_BACKGROUND_MENU.split(",")[0])
	background._alpha=m.COLOR_BACKGROUND_MENU.split(",")[1]
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////	

function onResize(){
	var m:TreeModel=TreeModel(this.getModel())
	this.background._width=m.width
	this.background._height = m.height
	
	/////title
	setTitle()
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////////

function setTitle() {
	var m:TreeModel=TreeModel(this.getModel())
	title.autoSize = true
	title.text = m.TITLE_MENU
	title.textColor=Number(m.COLOR_TITLE_MENU)
	this.title._x=int(m.width-this.title._width)
	this.title._y=int(m.height/2-title._width/2)
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////	

function onChangedSize(){
   this.onResize()	
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////	

}