import templateLoader.mvctemplate.*
import templateLoader.mvc.*
import templateLoader.I.*
import flash.display.BitmapData
import templateLoader.util.Observable

import mx.transitions.Tween
import mx.transitions.easing.*
import TextField.StyleSheet


 
  

class templateLoader.mvctemplate.FooterView extends AbstractView {
		

var t:TextField	
var main_menu:MovieClip
var positionY:Number
var tween
var bcg:MovieClip
var container:MovieClip
var button:MovieClip
var __show:Boolean
var currentDepths:Number

///////////////////////////////////////////////////////////

function FooterView() {
	this._visible=false
	
	
	if (ConfigurationSite.FOOTER_VISIBLE == "true") {
		//bcg._visible=true
	}else {
		//bcg._visible=false
	}
	
	//this._alpha = 0	
	///this.tween('_alpha',100,.5,'easeOutCubic',0)	
}

////////////////////////////////////////////////////////////

function onLoadMenuTree() {
	
	
	
}

/////////////////////////////////////////////////////////////

function onIntroEnd() {
	 var m:LoaderModel = LoaderModel(this.getModel())
	 
	 if(positionY==undefined){
	this._visible=true
	this.tween('_y', m.height - m.__footerHeightHide, 1, 'easeOutElastic')	
	positionY = 1
	 }
	

}

///////////////////////////////////////////////////////////////


function onIntroStart() {
	
	
}

////////////////////////////////////////////////////////////

function onLoad(){
	  var m:LoaderModel = LoaderModel(this.getModel())
	  this._y=m.height+20
	  currentDepths = this.getDepth()

	  
	  /////color button shov/hide player
	  if(ConfigurationSite.COLOR_BUTTON_SHOV_HIDE_PLAYER.length){
	  NewColor.setColor(container.button, ConfigurationSite.COLOR_BUTTON_SHOV_HIDE_PLAYER.split(",")[0])
	  container.button._alpha = ConfigurationSite.COLOR_BUTTON_SHOV_HIDE_PLAYER.split(",")[1]
	  }
	  
	  
	  ///color
	  if(ConfigurationSite.FOOTER_COLOR.split(",")[0].length){
	  NewColor.setColor(container.bcg, ConfigurationSite.FOOTER_COLOR.split(",")[0])
	  }
	  if(ConfigurationSite.FOOTER_COLOR.split(",")[1].length){
	  container.bcg._alpha = ConfigurationSite.FOOTER_COLOR.split(",")[1]
	  }
	  
	 
     	////add Desc
		this.container.t.styleSheet = m.getCss()
		container.bcg._height = m.__footerHeightShow * 2///m.__footerHeightHide
		container.t.embedFonts=true
        this.container.t.htmlText = ConfigurationSite.FOOTER_DESC
		this.container.t.autoSize=true
					
		///add Event
		if (ConfigurationSite.MP3_VISIBLE == "true") {
			container.button._visible=true
		}else {
			container.button._visible=false
		}
		container.button.onPress = Delegate2.create(this, onPressButton)
		container.bcg.onPress = function() { }
		container.bcg.useHandCursor=false
		
		this.onResize()
		mask()
	
}

///////////////////////////////////////////////////////////////////////////////////////////

function onPressButton() {
      if (__show == true) {
		  onRollOutFooter()
	  }else {
		  onRollOverFooter()
	  }
}

///////////////////////////////////////////////////////////////////////////////////////////

function onRollOverFooter() {
	var m:LoaderModel=LoaderModel(this.getModel())
	this.swapDepths(132422543)
	__show=true
	this.container.tween('_y', -m.__footerHeightShow+m.__footerHeightHide, 0.5, 'easeInOutCubic')
	container.button.gotoAndStop(2)
	container.button.symbol.play()
}

///////////////////////////////////////////////////////////////////////////////////////////

function onRollOutFooter() {
   container.button.gotoAndStop(1)
   container.button.symbol.play()
   
	__show=false
	this.container.tween('_y',0,0.5,'easeInOutCubic',0,{scope:this,func:onFadeOutEnd})
}

//////////////////////////////////

function onFadeOutEnd() {
		this.swapDepths(currentDepths)
}

///////////////////////////////////////////////////////////////////////////////////////////

function mask() {
	var m:LoaderModel=LoaderModel(this.getModel())
	var mcMask:MovieClip = this.createEmptyMovieClip("mcMaskClip", 435435)
	Drawing.rectangle(mcMask, 0, -500, m.width, m.__footerHeightHide + 500, ["0xFF0000", 50])
	this.setMask(mcMask)
}

////////////////////////////////////////////////////////////

public function defaultController (model:Observable):Controller {
  return new FooterController(model)
 }
 
////////////////////////////////////////////////////////////



/////////////////////////////////////////////////////////////////////////

function onResize(){
	var m:LoaderModel=LoaderModel(this.getModel())
	this._y = m.height - m.__footerHeightHide
		
	this.container.button._x = m.width - container.button._width-32//// m.width - container.button._width - 10
	this.container.button._y=9
	
	mask()
	
}

/////////////////////////////////////////////////////////////////////////




}