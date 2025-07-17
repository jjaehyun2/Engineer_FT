import templateGallery.mvcgallery.*
import templateGallery.mvc.*
import templateGallery.I.*
import flash.display.BitmapData
import templateGallery.util.Observable
import mx.transitions.Tween
import mx.transitions.easing.*
import TextField.StyleSheet;
import templateGallery.Configuration
import templateGallery.text_area.TextArea



class templateGallery.mvcgallery.DescView extends AbstractView {
	
var mcArea:TextArea
var bcg:MovieClip
var mcClose:MovieClip
var __itsDesc:Boolean
/////////////////////////////////////////////////////////////////////////////////////////

function DescView() {
	
	 ///BUTTON CLOSE
	 NewColor.setColor(mcClose, Configuration.COLOR_BUTTON_CLOSE_DESC.split(",")[0])
	 mcClose._alpha = Configuration.COLOR_BUTTON_CLOSE_DESC.split(",")[1]
	 
	 
	 ///COLOR BACGROUND DESC
	 NewColor.setColor(bcg.bcg, Configuration.COLOR_BCG_DESC.split(",")[0])
	 bcg.bcg._alpha = Configuration.COLOR_BCG_DESC.split(",")[1]
	
	 
	 
	
	bcg._visible=false
   hide()
   
   
}

/////////////////////////////////////////////////////////////////////////////////////////

 public function defaultController (model:Observable):Controller {
   return new ImageController(model)
  }
  
/////////////////////////////////////////////////////////////////////////////////////////  
  
function create_area(){
	mcArea = TextArea( this.attachMovie("_gallery_big_image", "_gallery_big_image_", 2))
	mcArea.border = false
	mcArea.borderColor = 0xFF0000
	mcArea.colorScrollBackground = 0x727272
	mcArea.colorScroll = 0xAEAEAE
	mcArea.__speedScroll = 1
	mcArea.setSize(500,500)
	hide()
}

/////////////////////////////////////////////////////////////////////////////////////////

function onShovInfo() {
shov()	
}
	
/////////////////////////////////////////////////////////////////////////////////////////

  function onPressClose(){
  this.hide()	
  }
  
////////////////////////////////////////////////////////////////////////////////////////

function onChangedIndex(){
	__itsDesc = itsDesc()
		
}
  
/////////////////////////////////////////////////////////////////////////////////////////

function onLoad() {
	//////bcg
	bcg.onPress = function() { }
	bcg.useHandCursor=false
	
	////close
	mcClose.onPress=Delegate2.create(this,onPressButClose)
	
	bcg._visible=false	
	hide()
}

//////////////////////////////////////////////////////////////////////////////////////

function onPressButClose() {
	this.hide()
}

/////////////////////////////////////////////////////////////////////////////////////////

function onResize(){
	
}

/////////////////////////////////////////////////////////////////////////////////////////

function onImageResize(){
	this.setPosition()
}

/////////////////////////////////////////////////////////////////////////////////////////


private function setPosition(){
	var model:GalleryModel=GalleryModel(this.getModel())
	var gallery:Gallery=model.__target
	var image:ImageView = gallery.__image
	
	setSize(Stage.width-300,Stage.height-300)
		
	var space:Number = 0
	bcg._x = space
	bcg._y = space
	this.bcg._width = Stage.width-space*2
	this.bcg._height = Stage.height-space*2
	
	var container:MovieClip = model.__target.__target
		
	var obj:Object=Converter.convert( { x:container._x, y:container._y }, container._parent, _root)
	this._x = -obj.x
	this._y = -obj.y
	
	this.mcArea._x=Stage.width/2-mcArea._width/2
	this.mcArea._y = Stage.height / 2 -mcArea._height/2
}

/////////////////////////////////////////////////////////////////////////////////////////

function itsDesc():Boolean {
		var desc = this.getDesc()
		if (desc != undefined && desc.length) {
			return true
		}else {
			return false
		}
}

/////////////////////////////////////////////////////////////////////////////////////////

function shov() {
	var m:GalleryModel=GalleryModel(this.getModel())
var desc = this.getDesc()
if(itsDesc()){
create_area()
setPosition()
this.text=desc
mcClose._visible = true
mcClose._x = m.width - 50
mcClose._y=50

bcg._alpha = 0
bcg.tween('_alpha', 100, 1, 'easeOutCubic')
bcg._visible=true
this.mcArea._visible = true
}
}

/////////////////////////////////////////////////////////////////////////////////////////

function hide(){
	this.mcArea._visible = false
	mcClose._visible = false
	bcg.tween('_alpha',0,1,'easeOutCubic',0,{scope:this,func:'onEndHideBcg'})
}

////////////////////////////////////////////////////////////////////////////////////////////

function onEndHideBcg() {
	bcg._visible=false
}

/////////////////////////////////////////////////////////////////////////////////////////

function onIntroEnd() {

}

////////////////////////////////////////////////////////////////////////////////////////

function set text(value_:String){
	mcArea.text=value_	
}

///////////////////////////////////////////////////////////////////////////////////////

function setSize(w_:Number,h_:Number){
	mcArea.setSize(w_,h_)	
}

/////////////////////////////////////////////////////////////////////////////////////////

function getDesc(){
var model:GalleryModel=GalleryModel(this.getModel())
var attributes:Object=model.getAttributes()
return attributes.child.firstChild.nodeValue
}

/////////////////////////////////////////////////////////////////////////////////////////

function onExitStart(){
this.hide()	
}

/////////////////////////////////////////////////////////////////////////////////////////
	
}