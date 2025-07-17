import templateNewsy.mvcgallery.*
import templateNewsy.mvc.*
import templateNewsy.I.*
import flash.display.BitmapData
import templateNewsy.util.Observable
import mx.transitions.Tween
import mx.transitions.easing.*
import TextField.StyleSheet;
import templateNewsy.Configuration
import templateNewsy.text_area.TextArea


class templateNewsy.mvcgallery.DescView extends AbstractView {
	
var mcArea:TextArea
var bcg:MovieClip
var mcClose:MovieClip
var __itsDesc:Boolean
var title:TextField

//////config
var __widthArea:Number = 334
var __heightArea:Number = 345
var __positionX:Number = 500
var __positionY:Number = 28

var bcg_title



/////////////////////////////////////////////////////////////////////////////////////////

function DescView(){
   create_area()
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
	//mcArea.setSize(334,260)
	//hide()
}

/////////////////////////////////////////////////////////////////////////////////////////

function onShovInfo() {
//shov()	
}
	
/////////////////////////////////////////////////////////////////////////////////////////

  function onPressClose(){
  ///this.hide()	
  }
  
////////////////////////////////////////////////////////////////////////////////////////

function onChangedIndex(){
	__itsDesc = itsDesc()
	
	//if(__itsDesc){
	shov()	
	//}else {
	//	hide()
	//}
		
}
  
/////////////////////////////////////////////////////////////////////////////////////////

function onLoad() {
	//////bcg
	bcg.onPress = function() { }
	bcg.useHandCursor=false
	
	////close
	mcClose.onPress=Delegate2.create(this,onPressButClose)
	
	bcg._visible=false	
	//hide()
}

//////////////////////////////////////////////////////////////////////////////////////

function onPressButClose() {
	///this.hide()
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
	
	setSize(__widthArea,__heightArea)
			
	this._x = __positionX
	this._y = __positionY
	
	
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
var _title = m.getTitle()

/////title
title.styleSheet = Configuration.CSS_STYLE
title.embedFonts=true
this.title.htmlText = _title
title.autoSize=true
this.bcg_title._width=title._width+50



////desc

create_area()
setPosition()
this.text = desc


/////effect mask
var maskDesc:MovieClip = this.createEmptyMovieClip("mcMaskDesc", 23124)
var space:Number=10
maskDesc._x -= space;maskDesc._y=-space
Drawing.rectangle(maskDesc, 0, 0, __widthArea+space*2+20, __heightArea+space*2, ["0xFF0000", 50])
maskDesc._xscale = 0
maskDesc._yscale = 0
maskDesc.tween('_xscale', 100,0.5,'easeOutCubic')
maskDesc.tween('_yscale', 100,0.5,'easeOutCubic')
mcArea.setMask(maskDesc)



this.mcArea._visible = true




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
return model.getDesc()
}

/////////////////////////////////////////////////////////////////////////////////////////

function onExitStart(){
this.hide()	
}

/////////////////////////////////////////////////////////////////////////////////////////
	
}