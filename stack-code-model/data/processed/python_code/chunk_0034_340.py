import mx.utils.Delegate;
import templateLoader.mvctemplate.LoaderModel;
import templateNewsy.text_area.Scroll 
import TextField.StyleSheet;
import templateNewsy.Configuration

class templateNewsy.text_area.TextArea extends MovieClip {
	var __width:Number=200  
	var __height:Number=300  
	var t:TextField
	var __scroll:Scroll
	var __styleSheet
	var __text:String
	//////////////////////////////////////color
	var __colorScrollBackground:String="0xCCCCCC"  ///color background scroll
	var __colorScroll:String="0xFF0000"    ////color scroll
	///////////////param
	var __speedScroll:Number=1
	var tween
	var model
	//var setMask	
///////////////////////////////////////////////////
	
	function TextArea(){
	
	}
	
///////////////////////////////////////////////////

 function setSelectedId(id_:Number) {
	 var m:LoaderModel = LoaderModel(LoaderModel.getInstance())
	 m.setSelectedId(id_)
 }

///////////////////////////////////////////////////

    function onLoad(){
      Mouse.addListener(this);
    }

///////////////////////////////////////////////////

function addScroll() {
	
	
	__scroll=Scroll(this.attachMovie("_scroll", "_scroll_", 1))
	
	colorScrollBackground=Configuration.BACKGROUND_SCROLL_COLOR//colorScrollBackground
	colorScroll=Configuration.SCROLL_COLOR
		
	__scroll.height = this.t._height+1
	__scroll.x =this.t._x+this.t._width+8
	__scroll.y = this.t._y+__scroll.spaceArrowY
	
	
     var proportion=t.bottomScroll/(t.maxscroll+t.bottomScroll)
	__scroll.limit = [1,this.t.maxscroll,proportion];
	__scroll.onChange=Delegate.create(this,onChange)
	
	
	
	}
	
///////////////////////////////////////////////////////

function removeScroll(){
	this.__scroll.removeMovieClip()	
}

////////////////////////////////////////////////////////////////////////////////////////////////////

	function onChange(value){
	///	trace("onchange = "+value+"  /  "+t.maxscroll)
	this.t.scroll=value
	}
	
/////////////////////////////////////////////////////////////////////////////////////////////////////

function setSize(w_:Number,h_:Number){
	this.t._width=w_
	this.t._height=h_
	this.text = this.text
	
	///enabled_disabled_scroll
}
	
///////////////////////////////////////////////////////////////////////////////////////////////////////

	function set text(tekst_){
		//trace("set text = !!! = "+tekst_+newline)
		__text=tekst_
	if(t.styleSheet==undefined){
	t.styleSheet=Configuration.CSS_STYLE
	}
	 this.t.scroll = 0
	 t.embedFonts=true
	 this.t.htmlText=tekst_.split("\n").join("")
	
	enabled_disabled_scroll()
  }
  
//////////////////////////////////////////////////////////////////////////////////////////////////////

function enabled_disabled_scroll(){
	
	if(this.t.maxscroll>1){
     addScroll()
    }else{
		this.removeScroll()
    }
}
	
///////////////////////////////////////////////////////////////////////////////////////////////////////

function get text(){
	return this.__text
}
	
//////////////////////////////////////////////////////////	
	
function set colorScrollBackground(color_){
	__colorScrollBackground=color_
	this.__scroll.setColorScrollBackground(color_)
}

/////////////////////////////////////////////

function get colorScrollBackground(){
	return __colorScrollBackground
}

//////////////////////////////////////////////////////////	
	
function set colorScroll(color_){
	__colorScroll=color_
	this.__scroll.setColorScroll(color_)
}

/////////////////////////////////////////////

function get colorScroll(){
	return __colorScroll
}

/////////////////////////////////////////

   function set border(value_:Boolean){
	   this.t.border=value_	   
   }
   
/////////////////////////////////////////////// 
 
   function set borderColor(color_){
	this.t.borderColor=color_
   }
   
///////////////////////////////////////////////

 function set textColor(color_){
	this.t.textColor=color_
   }
   
///////////////////////////////////////////////

   function onMouseWheel(delta:Number) {
	   
   var value=(delta/3)*this.__speedScroll
	 
	if(this.hitTest(_root._xmouse,_root._ymouse,true)){
	var value2=__scroll.getScrollPosition()-value
	this.__scroll.setScrollPosition(value2)   
	} 
	 
    };
	
///////////////////////////////////////////////
	
	
	
}