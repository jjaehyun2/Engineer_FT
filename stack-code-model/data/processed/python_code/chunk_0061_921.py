import mx.data.encoders.Num;
import mx.transitions.easing.Strong;
import mx.transitions.Tween;
import mx.utils.Delegate;
import templateText.Scroll  
import templateLoader.mvctemplate.LoaderModel;
 
class templateText.TextArea extends MovieClip {
	var __width:Number
	var __height:Number
	var t:TextField
	var __scroll:Scroll
	var __styleSheet
	var __text:String
	//////////////////////////////////////color
	var __colorScrollBackground:String="0x000000"  ///color background scroll
	var __colorScroll:String="0xFF0000"    ////color scroll
	/////////////Png
	var __background:Boolean
	var __backgroundColor
	///////////////param
	var __speedScroll:Number=1
	var __backgroundPng:Boolean
    var containerBackground:MovieClip
	var __spaceBackground:Number
	var spaceXScroll:Number = 24
	var scrollAreaWidth:Number=0
	
///////////////////////////////////////////////////
	
	function TextArea(){
	
	}
	
//////////////////////////////////////////////////

 function setSelectedId(id_:Number) {
	 var m:LoaderModel = LoaderModel(LoaderModel.getInstance())
	 m.setSelectedId(id_)
 }


///////////////////////////////////////////////////

function onLoad(){
 Mouse.addListener(this);
 
}

///////////////////////////////////////////////////////

function refresh(){
	
	this.t._width=width
	this.t._height=height
	this.t._x=spaceBackground
	this.t._y=spaceBackground
	
	containerBackground._width=width+spaceBackground*2+scrollAreaWidth
	containerBackground._height=height+spaceBackground*2
	
	this.text=this.text
}

//////////////////////////////////////////////////////

function set spaceBackground(value_:Number){
	__spaceBackground=value_
	refresh()
}

//////////////////////////////////////////////////////

function get spaceBackground(){
	return __spaceBackground
}

/////////////////////////////////////////////////////

function setColorBcg(color_,alpha_){
		
	containerBackground._visible=true	
	containerBackground.attachMovie("_background_png", "_background_png_", 102)
	
	if(color_&&alpha_){
	NewColor.setColor(containerBackground, color_)
	containerBackground._alpha=alpha_
	}
	
	
	refresh()
	
}

/////////////////////////////////////////////////////

function get backgroundPng(){
	return __backgroundPng
}

///////////////////////////////////////////////////

function addScroll(){
	__scroll=Scroll(this.attachMovie("_scroll", "_scroll_", 1))
	
	colorScrollBackground=colorScrollBackground
	colorScroll=colorScroll
		
	__scroll.height = this.t._height+1
	__scroll.x =this.t._x+this.t._width+spaceXScroll
	__scroll.y =this.t._y+__scroll.spaceArrowY
     var proportion=t.bottomScroll/(t.maxscroll+t.bottomScroll)
	__scroll.limit = [1, this.t.maxscroll, proportion];
	//trace("max scroll = "+t.maxscroll)
	__scroll.onChange=Delegate.create(this,onChange)
	
	
	}
	
///////////////////////////////////////////////////////

function removeScroll(){
	this.__scroll.removeMovieClip()	
}

////////////////////////////////////////////////////////////////////////////////////////////////////

	function onChange(value) {
			this.t.scroll=Math.ceil(value)
	}
	
/////////////////////////////////////////////////////////////////////////////////////////////////////	
	
function set background(background_:Boolean){
   __background=background_	
   t.background=__background
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

function set backgroundColor(color_){
	__backgroundColor=color_
	t.backgroundColor=__backgroundColor
}

/////////////////////////////////////////////////////////////////////////////////////////////////////

function setSize(w_:Number,h_:Number){
	width=w_
	height=h_
}

///////////////////////////////////////////////////////////////////////////////////////////////////

function set width(value_:Number){
	__width=value_-(2*spaceBackground+scrollAreaWidth)
	this.refresh()
}

/////////////////////////////////////////////////////////////////////////////////////////////////

function get width(){
	return __width
}

///////////////////////////////////////////////////////////////////////////////////////////////////

function set height(value_:Number){
	__height=value_-spaceBackground*2
	this.refresh()
}

/////////////////////////////////////////////////////////////////////////////////////////////////

function get height(){
	return __height
}
	
////////////////////////////////////////////////////////////////////////////////////////////////////

	function set text(tekst_){
		__text=tekst_
		
	  styleSheet=styleSheet
	  this.t.scroll=0
   
      this.t.background=__background
      this.t.backgroundColor=__backgroundColor

	  this.t.embedFonts=true
	  this.t.htmlText = tekst_.split("\n").join("") 
	  ///t.htmlText+="<br><br><br><br><br><br>"
	  if(this.t.maxscroll>1){
       addScroll()
       }else{
	   this.removeScroll()
      }
	 	 

////////////////////////////////////////////////

	var array=[]
	for(var i in t){
		if(t[i] instanceof MovieClip){
		array.push(t[i])
		}
	}

  for(var i=0;i<array.length;i++){
    var mc:MovieClip=array[i]
	mc._alpha = 0
	mc.tween.stop()
	mc.tween=new Tween(mc,'_alpha',Strong.easeOut,0,100,1,true)
   }
	  

////////////////////////////////////////////////	  
	  
	  
	}
	
///////////////////////////////////////////////////////////////////////////////////////////////////

function get text(){
	return this.__text
}
	
/////////////////////////////////////////////////////////////////////////////////////////////////////

function set styleSheet(styleSheet_){
	__styleSheet=styleSheet_
	this.t.styleSheet=__styleSheet
}

///////////////////////////////////////////////////////////////////////////////////////////////////

function get styleSheet(){
	return __styleSheet
	
}

	
//////////////////////////////////////////////////////////////////////////////////////////////	
	
function set colorScrollBackground(color_){
	__colorScrollBackground=color_
	this.__scroll.setColorScrollBackground(color_)
}

/////////////////////////////////////////////////////////////////////////////////////////////////

function get colorScrollBackground(){
	return __colorScrollBackground
}

//////////////////////////////////////////////////////////////////////////////////////////////
	
function set colorScroll(color_) {
	__colorScroll=color_
	this.__scroll.setColorScroll(color_)
}

////////////////////////////////////////////////////////////////////////////////////////////////////

function get colorScroll(){
	return __colorScroll
}

////////////////////////////////////////////////////////////////////////////////////////

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
	this.t.scroll-=value
	this.__scroll.setScrollPosition(this.t.scroll,false)   
	} 
	 
    };
	
///////////////////////////////////////////////
	
	
	
}