import mx.transitions.easing.Strong;
import mx.transitions.Tween;
import templateMove.mvcFLV.*;
import templateMove.I.*
import templateMove.util.Observable
import flash.display.BitmapData
import mx.events.EventDispatcher
import templateMove.Configuration
import mx.utils.Delegate



class templateMove.mvcFLV.FLVModel extends Observable {
	var tweenW:Tween
	var tweenH:Tween
	var tweenX:Tween
	var tweenY:Tween
	var __allArea:Boolean=false
	var __hitTestTools:Boolean=true
	private var __oldHitTest:Boolean
 	var __flv:FLV
	var __interProgress:Number
	var __total:Number
	///size move
    var __maxWidthMove:Number //// width move 
	var __maxHeightMove:Number /// height move 
	/////size flv
	var __widthOrginal:Number       /////////  orginal width move
	var __heightOrginal:Number	    /////////  orginal height move
	var __newWidth:Number  
	var __newHeight:Number
	var __oldWidth:Number
	var __oldHeight:Number
	public var __width:Number   /////////width 
	public var __height:Number  /////////height 
	var __x:Number
	var __y:Number
	var __nc:NetConnection
	var __ns:NetStream
	var __sound:Sound
	var __volume:Number=100   /////////first Volume
	var __position
	var __soundEnabled:Boolean=true    ///////////
	var __stan:String="stop"   ///  STANY TO: play,stop,pause
	var __index:Number
	var __init:Boolean
	////////////////////////////////////////margin Image
	var __marginImageX1:Number=0
	var __marginImageX2:Number=0
	var __marginImageY1:Number=0
	var __marginImageY2:Number=0
	///////////////////first position
	var __firstGlobalX:Number
	var __firstGlobalY:Number
	///////////////////////////////toools
	var __marginToolsX1:Number=0
	var __marginToolsX2:Number=0
	var __marginToolsY2:Number = 0
	var __toolsSymbolPosition:Number=6
	var __toolsHeight:Number=40
	///////////////////////////////////////////////
	var __url:String                //////url move
	var __preview:String           ////////url thumb image
	private var __date:XML                ////date xml
	
	var __fullScreen:Boolean=true   ////button full screen enabled nad disabled
	var __xmlConfig:XML
	var __autoPlay:Boolean
	var __autoReplay:Boolean
	var __bufferSize:Number
	var __sound_rol:Sound
	var __alphaAreaFull:Number = 80
	var __alphaAreaNormal:Number = 0
		
	/////////////////////color tools
	var FLV_BACKGROUND_TOOLS
	var FLV_BACKGROUND_PLAYER
	var FLV_BACKGROUND_PLAYER_ALPHA
	var FLV_COLOR_SYMBOL_BUTTON_ROLLOVER
	var FLV_COLOR_SYMBOL_BUTTON_ROLLOUT
	var FLV_COLOR_NUMBER
	var FLV_COLOR_LINE_SOUND
	var FLV_COLOR_LINE_PROGRESS
	var FLV_COLOR_LINE_PROGRESS_PRELOADER
	var FLV_COLOR_CIRCLE
	var FLV_CURRENT_PROGRESS_LINE
	var FLV_CURRENT_SOUND_LINE
	var FLV_SOUND_ROLL_SAMPLE
    var FLV_COLOR_BACKGROUND_BUFFER
	
	
/////////////////////////////////////////////////////////////////////////////

	function FLVModel(target_:FLV){
		Stage.addListener(this)
		this.__flv=target_
		this.__flv.__container.onMouseMove=Delegate2.create(this,this.onMouseMove)
		ini()
	}
	
//////////////////////////////////////////////////////////////////////////

function setConfig(xml_:XML){
	this.__xmlConfig=xml_
	
	//////set/get
	this.fullScreen=getValueConfig("FULL_SCRENN_BUTTON")
	this.autoPlay=getValueConfig("FLV_AUTO_PLAY")
	this.autoReplay=getValueConfig("FLV_AUTO_REPLAY")
	this.newWidth=getValueConfig("NEW_WIDTH")
	this.newHeight=getValueConfig("NEW_HEIGHT")
	this.bufferSize=getValueConfig("FLV_BUFFER_SIZE")
	
	/////color
	FLV_BACKGROUND_TOOLS=getValueConfig("FLV_BACKGROUND_TOOLS")
	FLV_BACKGROUND_PLAYER = getValueConfig("FLV_BACKGROUND_PLAYER")
	FLV_BACKGROUND_PLAYER_ALPHA = getValueConfig("FLV_BACKGROUND_PLAYER_ALPHA")
	__alphaAreaFull=FLV_BACKGROUND_PLAYER_ALPHA
	
	FLV_COLOR_SYMBOL_BUTTON_ROLLOVER=getValueConfig("FLV_COLOR_SYMBOL_BUTTON_ROLLOVER")
	FLV_COLOR_SYMBOL_BUTTON_ROLLOUT=getValueConfig("FLV_COLOR_SYMBOL_BUTTON_ROLLOUT")
	FLV_COLOR_NUMBER=getValueConfig("FLV_COLOR_NUMBER")
	FLV_COLOR_LINE_SOUND=getValueConfig("FLV_COLOR_LINE_SOUND")
	FLV_COLOR_LINE_PROGRESS=getValueConfig("FLV_COLOR_LINE_PROGRESS")
	FLV_COLOR_LINE_PROGRESS_PRELOADER=getValueConfig("FLV_COLOR_LINE_PROGRESS_PRELOADER")
	FLV_COLOR_CIRCLE=getValueConfig("FLV_COLOR_CIRCLE")
	FLV_CURRENT_PROGRESS_LINE=getValueConfig("FLV_CURRENT_PROGRESS_LINE")
	FLV_CURRENT_SOUND_LINE=getValueConfig("FLV_CURRENT_SOUND_LINE")
	FLV_SOUND_ROLL_SAMPLE=getValueConfig("FLV_SOUND_ROLL_SAMPLE")
	FLV_COLOR_BACKGROUND_BUFFER=getValueConfig("FLV_COLOR_BACKGROUND_BUFFER")
	
	
	this.__flv.faceView()	
	
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////

function getValueConfig(name_:String){
	
	for(var i=0;i<__xmlConfig.firstChild.childNodes.length;i++){
		var node:XMLNode=__xmlConfig.firstChild.childNodes[i]
		if(node.nodeName==name_){
			
			    var value=node.firstChild.nodeValue		
				
				if(!isNaN(value)){
				value=Number(value)
				}
				else if(value=="true"){
				value=true
				}
				else if(value=="false"){
				value=false
				}
				else{
				value=String(value)
				}
                
                if(value=="undefined"){
					value=undefined
				}
				
				return value
			}
		}

}

////////////////////button full screen enabled nad disabled///////////////////////////////////////////////////	
		
function set fullScreen(boolean_:Boolean){
	this.__fullScreen=boolean_;
	
	this.__flv.__fullScreen._visible=this.fullScreen
	if(fullScreen){
	this.__flv.__fullScreen.create_menu()
	}
}

///////////////////////////////////////////////////////////////////////////////

function get fullScreen(){
	return this.__fullScreen;
}

///////////////////////////////////////////////////////////////////////////////

	public function ini(){
	__nc = new NetConnection();
	__nc.connect(null);
	__ns = new NetStream(__nc);
	__ns.setBufferTime(bufferSize); 
	__ns.onMetaData = Delegate.create(this,MetaData) 
	__ns.onStatus = Delegate.create(this,Status) 
	create_sound()
	//////////////////////first attributes
	this.volume=this.__volume
	soundEnabled=this.__soundEnabled
	}
	
////////////////////////////////////////////////////////////////////

function set width(width_:Number){
	this.__width=width_
	resize()
}

////////////////////////////////////////////////////////////////////

function set height(height_:Number){
	this.__height=height_	
	resize()
}

////////////////////////////////////////////////////////////////////

function get width(){
	return this.__width	
}

////////////////////////////////////////////////////////////////////

function get height(){
return this.__height
	
}

//////////////////////////auto Play/////////////////////////////////////////////

function set autoPlay(boolean_:Boolean){
	__autoPlay=boolean_
}

///////////////////////////////////////////////////////////////////////

function get autoPlay():Boolean{
	return __autoPlay
}

/////////////////////////////auto Replay//////////////////////////////////////////

function set autoReplay(boolean_:Boolean){
	__autoReplay=boolean_
}

///////////////////////////////////////////////////////////////////////

function get autoReplay():Boolean{
	return __autoReplay
}

///////////////////////////new width///////////////////////////////////////////

function set newWidth(boolean_:Number){
	__newWidth=boolean_
}

///////////////////////////////////////////////////////////////////////

function get newWidth():Number{
	return __newWidth
}

////////////////////new height///////////////////////////////////////////////////

function set newHeight(boolean_:Number){
	__newHeight=boolean_
}

///////////////////////////////////////////////////////////////////////

function get newHeight():Number{
	return __newHeight
}

///////////////////buffer size///////////////////////////////////////////////

function set bufferSize(number_:Number){
	__bufferSize=number_
	this.__ns.setBufferTime(__bufferSize)
}

///////////////////////////////////////////////////////////////////////

function get bufferSize():Number{
	return __bufferSize
}




///////////////////////////////////////////////////////////////////////
function setFirstPoint(){
	///trace("setFirstPoint (FLV Model)!")
			///first X and Y
		var myPoint:Object = {x:this.__flv.__container._x, y:this.__flv.__container._y}; // create your generic point object
        this.__flv.__container._parent.localToGlobal(myPoint);
        this.__firstGlobalX=myPoint.x
		this.__firstGlobalY=myPoint.y
}

////////////////////////////////////////////////////////////////////

function set x(x_:Number){
	this.__x=x_	
	this.__flv.__container._x=this.__x
	
    setFirstPoint()
      		
}

///////////////////////////////////////////////////////////////////

function get x(){
	return this.__x
}

////////////////////////////////////////////////////////////////////

function set y(y_:Number){
	this.__y=y_	
	this.__flv.__container._y=this.__y
	 setFirstPoint()
      		
}

///////////////////////////////////////////////////////////////////

function get y(){
	return this.__y
}

/////////////////////////////////////////////////////////////////////////

function fullArea() {
	    stopTweenResize()
	    setFirstPoint()
		var myPoint:Object = {x:0, y:0}; 
      __flv.__container._parent.globalToLocal(myPoint);	 
		__oldWidth = width
		__oldHeight = height
		////x and y tween
		tweenX = new Tween(__flv.__container, '_x', Strong.easeOut, __flv.__container._x, myPoint.x, 1, true)
		tweenY = new Tween(__flv.__container, '_y', Strong.easeOut, __flv.__container._y, myPoint.y, 1, true)
				
		/////width and height
		tweenW = new Tween(this, 'width', Strong.easeOut, width, Stage.width, 1, true)
		tweenH = new Tween(this, 'height', Strong.easeOut, height, Stage.height, 1, true)
				
		__allArea = true
		
		dispatchEvent({target:this,type:"onChangeArea"})
}

/////////////////////////////////////////////////////////////////////////

function stopTweenResize() {
	tweenH.stop()
	tweenW.stop()
	tweenX.stop()
	tweenY.stop()
}

/////////////////////////////////////////////////////////////////////////

function normalArea() {
	stopTweenResize()
	  var myPoint:Object = {x:__firstGlobalX, y:__firstGlobalY};
       __flv.__container._parent.globalToLocal(myPoint);
				 
		////x and y tween
		tweenX = new Tween(__flv.__container, '_x', Strong.easeOut, __flv.__container._x, 0, 1, true)
		tweenY = new Tween(__flv.__container, '_y', Strong.easeOut, __flv.__container._y, 0, 1, true)
				
		/////width and height
		tweenW = new Tween(this, 'width', Strong.easeOut, width, __oldWidth, 1, true)
		tweenH = new Tween(this, 'height', Strong.easeOut, height, __oldHeight, 1, true)
	
		 __allArea = false
		 
		 dispatchEvent({target:this,type:"onChangeArea"})
	
}

/////////////////////////////////////////////////////////////////////////

function onResize(){
    
	
	
    if(fullScreen!=false){
           
	if (Stage["displayState"] == "normal"||Stage["displayState"]==undefined) {
		//////////////////////////////////////normal screen
		var myPoint:Object = {x:this.__firstGlobalX, y:__firstGlobalY};
         this.__flv.__container._parent.globalToLocal(myPoint);
		 this.__flv.__container._x=0
		 this.__flv.__container._y=0
		 this.width=this.newWidth
		 this.height=this.newHeight
	}else{  ///////////////////full screen
	    setFirstPoint()
		var myPoint:Object = {x:0, y:0}; 
        this.__flv.__container._parent.globalToLocal(myPoint);	 
		this.__flv.__container._x=myPoint.x
		this.__flv.__container._y=myPoint.y
		this.width=Stage.width
		this.height=Stage.height
	
	}
		 		
    }    
		
}

/////////////////////////////////////////////////////////////////////////////////////////////////
private function resize(){
		///////////set max width and height move 
		this.__maxWidthMove=this.width-(this.__marginImageX1+this.__marginImageX2)
		this.__maxHeightMove=this.height-(this.__marginImageY1+this.__marginImageY2+this.__toolsHeight+__marginToolsY2)
		
		dispatchEvent({target:this,type:"onResize"})
}



/////////////////////////////////////////////////////////end interface////////////////////////////	
	
	function get index(){
		return this.__index		
	}
	
////////////////////////////////////////////////////////////////////////////
	
	private function create_sound(){
	var mc:MovieClip=_root.createEmptyMovieClip("v_Sound",789456654)
	mc.attachAudio(__ns)
	this.__sound=new Sound(mc)
	}
	
////////////////////////////////////////////////////////////////////////////stan
	
	function set stan(stan_){
		this.__stan=stan_
		if(this.stan=="play"){
		dispatchPlay()
		}else if(this.stan=="stop"){
			__ns.pause()
		}else if(this.stan=="pause"){
			__ns.pause()
			this.dispatchPauze()
		}
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	function get stan(){
		return this.__stan
	}
	
	
////////////volume et/get /////////////////////////////////////////////////
	
	public function set volume(volume_){
		    this.__volume=volume_
			this.__sound.setVolume(this.__volume)	
			dispatchEvent({target:this,type:"onVolume"})   ////zmiana stopnia naglosnienia
	}
	public function get volume(){
		    return this.__volume
	}
			
/////////////////////////////////////////////////////////////////////////////

	public function set soundEnabled(value_:Boolean){
		this.__soundEnabled=value_
		
		if(soundEnabled==true){
		this.__sound.setVolume(this.volume)
		dispatchEvent({target:this,type:"onSoundEnabled"})
		}else{
		this.__sound.setVolume(0)
		dispatchEvent({target:this,type:"onSoundDisabled"})
		}
		///zdarzenie zmiany stanu muzyki na wlaczona lub wylaczono
	}
	
/////////////////////////////////////////////////////////////////////////////

	function get soundEnabled(){
		return this.__soundEnabled
		
	}

/////////////////////////////////////////////////////////////////////////////
	
	public function set position(position_){   //////pozycje filmu mozemy nadac tylko wtedy kiedy zastopujemy - funkcja Stop()
		  this.__position=position_
		  if(stan=="stop"||stan=="pause"){ 
		  __ns.seek(__position)
		  }
		dispatchEvent({target:this,type:"onProgress"})	
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	public function get position(){
		  return this.__position
	}
	
///////////////////////////////////////////////////////////////////////////

public function setDateXml(xml_:XML){
  this.__date=xml_	
  setUrl(__date.firstChild.firstChild.attributes.path,__date.firstChild.firstChild.attributes.preview)  
}

//////////////////////////////////////////////////////////////////////////

public function setDateObject(object:Object){
   setUrl(object.flv,object.preview)  
}

/////////////////////////////////////////////////////////////////////////////

function getDateXml():XML{
	return __date;	
}
	
/////////////////////////////////////////////////////////////////////////////
		
public function setUrl(url_:String,preview_:String){
	    this.setPreview(preview_)
	    this.Stop()
		this.__ns.close()
		this.__url = url_
		
			this.dispatchEvent( { target:this, type:"onSetUrl" } )
		
			//if(autoPlay==true){
		//this.Start()
		///}
}

/////////////////////////////////////////////////////////////////////////////////

function getUrl(){
	return this.__url
}

/////////////////////////////////////////////////////////////////////////////////

private function setPreview(url_:String){
	this.__preview=url_	
}

//////////////////////////////////////////////////////////////////////////////

function getPreview():String{
	return __preview
}

/////////////////////////////////////////////////////////////////////////////////

	public function Start(){
	
		if(this.getUrl()){ 
		__ns.play(this.getUrl());
		stan="play"
		delete this.__url
		return;
		}
		/////////////////////////////
		if(stan=="stop"||stan=="pause"){
		__ns.pause()
		stan="play"
		}
	}
	
/////////////////////////////////////////////////////////////////////////////		
	
	public function Pause(){
		if(stan=="play"){
		stan="pause"
		}
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	public function Stop(){
		if(stan=="play"){
		stan="stop"
		}
		this.dispatchStop()
		this.position=0
	}
		
/////////////////////////////////////////////////////////////////////////////

	private function Progress(){ ////odtwarzanie
	this.position=this.__ns.time
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	private function MetaData(obj){
		this.__total=obj.duration
	
	    this.__widthOrginal=obj.width
		this.__heightOrginal=obj.height
		
		__flv.__container._visible=true
				
						
		dispatchEvent({target:this,type:"onMetaData",obj:obj})
	}
		
/////////////////////////////////////////////////////////////////////////////
	
	private function Status(info){
		if (info.code == "NetStream.Play.Stop") {

			if(this.stan!="pause"&&this.stan!="stop"){
				this.dispatchEvent({target:this,type:"onEndMove"})
			if(autoReplay==true){
			this.Stop()
			this.position=0
			this.Start()
			}else{
			  this.Stop()
			}
			}
			//////////////////////////////////
			
		////if(this.__ns.bufferLength <= this.__ns.bufferTime) {
      	}
				
		if (info.code == "NetStream.Play.Start") {
		     
		}
		
		if(info.code =="NetStream.Seek.Notify"){
				
		}
		
		if(info.code =="NetStream.Buffer.Flush"){
									
		}
		
		if (info.code == "NetStream.Buffer.Empty") {
			
			dispatchEvent({target:this,type:"onBufferStart"})			
		}
		
				
		if (info.code == "NetStream.Buffer.Full") {
			dispatchEvent({target:this,type:"onBufferStop"})	
			
		}
			
	}
	
/////////////////////////////////////////////////////////////////////////////	
	
	private function dispatchPlay(){
		clearInterval(__interProgress)
		__interProgress=setInterval(this,'Progress',1)
		dispatchEvent({target:this,type:"onStart"})
		
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	private function dispatchStop(){
		clearInterval(__interProgress)
		dispatchEvent({target:this,type:"onStop"})
			
	}
	
/////////////////////////////////////////////////////////////////////////////
	
	function dispatchPauze(){
		clearInterval(__interProgress)
		dispatchEvent({target:this,type:"onPauze"})
		
	}

/////////////////////////////////////////////////////////////////////////////

	function dispatchIndex(){
			dispatchEvent({target:this,type:"onChangedIndex"})	
	}

/////////////////////////////////////////////////////////////////////////////

	function dispatchLoadThumb(){
		dispatchEvent({target:this,type:"onLoadThumb"})
		
	}
	
	///////////////////////////////////////////////////////////////////////
	
	public function full_screen(){
		if (Stage["displayState"] == "normal") {	
			Stage["displayState"] = "fullScreen";
			this.dispatchEvent({target:this,type:"onFullScreenYes"})			
		}else{
			Stage["displayState"] = "normal";
			this.dispatchEvent({target:this,type:"onFullScreenNo"})						
		}
		
	}
	

/////////////////////////////////////////////////////////////////////////////

  function onMouseMove(){
	  var xmouse:Number=this.__flv.__container._xmouse
	  var ymouse:Number=this.__flv.__container._ymouse
	  
	  var margin:Number=20
	  
	  if(__flv.__image.hitTest(_root._xmouse,_root._ymouse,true)&&xmouse>margin&&xmouse<(width-margin)&&ymouse>margin&&ymouse<(height-(__toolsHeight+margin))){
		   setHitTestImage(true)
		  
	 }else{
		   setHitTestImage(false)
	 }
  }
  
///////////////////////////////////////////////////////////////////////////
 
 function setHitTestImage(boolean_:Boolean){
	  __hitTestTools=boolean_	
	 
	 if(__hitTestTools!=__oldHitTest){
	 
	    if(__hitTestTools==true){
		   	dispatchEvent({target:this,type:"onHitTestImageTrue"})
	   }else{
		    dispatchEvent({target:this,type:"onHitTestImageFalse"})
	   }
	   
	 }
	   
	   __oldHitTest=__hitTestTools
 }
 
 ///////////////////////////////////////////////////////////
 
 function sound_rol(mc_:MovieClip){
	 if(FLV_SOUND_ROLL_SAMPLE){
	 __sound_rol.stop()
	 __sound_rol=new Sound(this.__flv.__container)
	 __sound_rol.attachSound("_roll_tools")
	 __sound_rol.start(0,1)
	 __sound_rol.setVolume(50)
 }}
		
 ///////////////////////////////////////////////////////////
  
}