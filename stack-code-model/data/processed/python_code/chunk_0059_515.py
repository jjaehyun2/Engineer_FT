import templateMp3.mvcMp3.*;
import templateMp3.I.*
import templateMp3.util.Observable
import mx.events.EventDispatcher
import mx.utils.Delegate

class templateMp3.mvcMp3.Mp3Model extends Observable{
 	var __volumeFirst:Number
	var __muteFirst:Boolean=true
	
	///////////////////////////////////////////////////
	var __muteSound:Boolean ///true/false
	var __sound:Sound  ///object Sound
	var __oldVolume:Number
	var __state:String="stop" ///// stop,pause,play
	var __volume:Number
	var __current:Number  ////current number mp3
	var __array:Array   ///// array mp3
	var __target:Mp3
	var __width:Number
	////////////////////////////////////////////inter
	var __interPreloader:Number
	var __interProgressPlay:Number
	
	var __userDisabledSound:Boolean=false
	
	
	////////////////////////configuration
	var autoPlay:Boolean
	
	////color list 
	var MP3_NUMBER_COLOR_ROL
	var MP3_NUMBER_COLOR_OUT
	
	////color tools
	var MP3_TOOLS_COLOR_ROL
	var MP3_TOOLS_COLOR_OUT
	
	
	////equalizer
	var MP3_EQUALIZER_COLOR_OLD
    var MP3_EQUALIZER_COLOR_NORMAL
	
	/////Volume
	var MP3_VOLUME_COLOR_BACKGROUND
	var MP3_VOLUME_COLOR_CURRENT
	
	/////Speaker
	var MP3_SPEAKER_COLOR_ROL
	var MP3_SPEAKER_COLOR_OUT
	
	///////background
	var MP3_BACKGROUND_COLOR
	
	/////progress
	var MP3_BACKGROUND_PROGRESS
	var MP3_CURRENT_PROGRESS
	
	////time view
	var MP3_TIME_COLOR
	
	///////////preloader
	var MP3_PRELOADER_COLOR
	
	////buffer
	var MP3_BUFFER_COLOR
	
	////align title
	var MP3_ALIGN_TITLE="L"
	
	//////position X
	var MP3_POSITION_X
	
	//////position Y
	var MP3_POSITION_Y
	
	/////color glow
	var MP3_GLOW_COLOR
	
	////color glow scroll
	var MP3_VOLUME_GLOW_COLOR_SCROLL
	
	////color PROGRESS SCROLL
	var MP3_PROGRESS_GLOW_COLOR_SCROLL
	
	/////color VOLUME circle scroll
	var MP3_VOLUME_COLOR_CIRCLE
	
	/////color PROGRESS circle scroll
	var MP3_PROGRESS_COLOR_CIRCLE
	
	////////////////visible circle
	var MP3_CIRCLE_VISIBLE
	
	
	
	
	////////////////////////////////////////////////////////////////////////////////
	
	function Mp3Model(){
	
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	function muteFlv(value_:Boolean) {
		
		if(__userDisabledSound==false){
				if (value_ == true&&muteSound==false) {
					muteSound=true
				}else if(value_ == false&&muteSound==true) {
					muteSound=false
				}
		}
				
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	
	
	////////////////////////////////////////////////////////////////////////////////
	
	function set width(width_:Number){
		__width=int(width_)
		this.dispatchEvent({target:this,type:"onSetSize"})		
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	function get width(){
		return __width		
	}
	
	
	////////////////////////////////////////////////////////////////////////////////
	
	private function create_sound(){
		delete this.__sound
		var mc:MovieClip=_root.createEmptyMovieClip("32xyzqwastriweruifdsfkdsfe",457457686658658544)
		this.__sound = new Sound(mc)
		_soundbuftime=10
		///trace(_soundbuftime)

		var __this:Mp3Model=this
		this.__sound.onLoad=function(){
			//clearInterval(__this.__interPreloader)
			
		}
		
		
		this.__sound.onSoundComplete=Delegate2.create(this,dispatchSoundComplete)
		
		clearInterval(this.__interPreloader)
		progressPreloader()
		this.__interPreloader=setInterval(this,'progressPreloader',1)
	}
	
	//////////////////////////////progress load mp3 file//////////////////////////////////////////////////
	
	function progressPreloader(){
		var l=this.__sound.getBytesLoaded()
		var t=this.__sound.getBytesTotal()
		
		this.dispatchEvent({target:this,type:"onProgressLoad",l:l,t:t})		
		
		
		if(l>=t&&t>0&&l>0){
			clearInterval(this.__interPreloader)	
			this.dispatchEvent({target:this,type:"onProgressLoadEnd"})	
		}
		
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	
      public function getTotalTime():Number{
		  
		 var tt:Number = __sound.duration * __sound.getBytesTotal() / __sound.getBytesLoaded();
        return  tt 
      } 
	
	////////////////////////////////////////////////////////////////////////////////
	
	function set muteSound(value_:Boolean){
		this.__muteSound=value_
		if(this.muteSound==true){
			this.volume=(this.__oldVolume==undefined) ? __volumeFirst : this.__oldVolume
			this.dispatchMuteOn()
		}else if(this.muteSound==false){
			this.__oldVolume=this.volume
				this.volume=0
			this.dispatchMuteOff()
		}
	}
	
	/////////////////////////////////////////////
	
	function get muteSound(){
		return this.__muteSound
	}
	
	//////////////////////////////////////////////////////
	
	public function next(){
		
		if(current==undefined){
			this.current=0
			return;
		}
		
		
		if(this.current==(this.getLength()-1)){
		    this.current=0
		}else{
			this.current++
		}
	}
	
	//////////////////////////////////////////////////////////
	
	public function prev(){
		if(current==undefined){
			this.current=(this.getLength()-1)
			return;
		}
		
		
		if(this.current==0){
		this.current=(this.getLength()-1)
		}else{
		this.current--
		}
	}
	
	/////////////////////////////////////////////////////////
	
	function getLength(){
		return this.__array.length
	}
	
	//////////////////////////////////////////////////////
	
	function setMp3(array_){
		this.__array=array_
		dispatchInit()
		if(this.autoPlay==true){
			this.current=0			
		}
		
		
	}
	
	////////////////////////////////////////////////////////////////////
	
	function getAttributes():PropertyItem{
	 return this.__array[this.__current]	
	}
	
	////////////////////////////////////////////////////////////////////
	
	function set current(nr_:Number){
		this.__current=nr_	
			///this.Stop()
		 this.Start(this.__array[current].path)
	
		  dispatchCurrent()
		  
		  //dispatchEvent({target:this,type:"onLoadSound"})	
	}
	
	////////////////////////////////////////////////////////////////////
	
	function get current(){
		return this.__current
	}
	
	////////////////////////////////////////////////////////////////////////////////START STOP and PAUSE
	
	function Start(mp3_,pos_){
		if(mp3_!=undefined){
			this.Stop()
			create_sound()
			this.__sound.loadSound(mp3_,true)
			this.__sound.start(0,1)
			this.state="play"
			if(this.volume==undefined){
			this.volume=this.__volumeFirst
			}
			else{
			this.volume=this.volume 
			}
			
			if(this.muteSound==undefined){
				this.muteSound=__muteFirst
			}
		    return;
		    }
		////////////////////////////
		if(this.state=="stop"){
		this.__sound.start(0,1)		
		state="play"
		}else if(this.state=="pause"){
		if(pos_==undefined){
		var poz=Math.round(this.__sound.position/1000)
		}else{
		var poz=pos_
		}
		this.__sound.start(poz,1)		
		state="play"
		}
	}

	////////////////////////////////////////////////////////////////////////////////
	
	function Stop(){
		if(this.state=="play"||this.state=="pause"){
		this.__sound.stop()
		this.state="stop"
		}
		
	}

	////////////////////////////////////////////////////////////////////////////////
	
	function Pause(){
		if(this.state=="play"){
			this.__sound.stop()
			this.state="pause"
		}
		
	}
		
	////////////////////////////////////////////////////////////
	
	function set volume(volume_){
		this.__volume=volume_
		this.__sound.setVolume(this.volume)
		dispatchVolume()
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	function get volume(){
		return this.__volume		
	}

	////////////////////////////////////////////////////////
	
	function set state(stan_){
		this.__state=stan_
		if(state=="play"){
			dispatchPlay()
		}else if(state=="pause"){
			dispatchPause()
		}else if(state=="stop"){
			dispatchStop()
		}
	}
	
	///////////////////////////////
	
	function get state(){
		return this.__state
		
	}
	
	///////////////////////////////////
	
	function dispatchPlay(){
		clearInterval(this.__interProgressPlay)
		this.__interProgressPlay=setInterval(this,'progressPlay',70)
		
		dispatchEvent({target:this,type:"onPlay"})		
	}
	
	////////////////////////////////////////////////////////////////////////////////
	
	function progressPlay(){
		dispatchEvent({target:this,type:"onProgressPlay"})
	}
	
	//////////////////////////////////////////////////////////////////////////////////
	
	function dispatchStop(){
		clearInterval(this.__interProgressPlay)
		dispatchEvent({target:this,type:"onStop"})		
	}
	
	///////////////
	
	function dispatchPause(){
		clearInterval(this.__interProgressPlay)
		dispatchEvent({target:this,type:"onPause"})		
	}
	
	/////////////////////////////////////////////////////////////
	
	function dispatchVolume(){
		dispatchEvent({target:this,type:"onChangedVolume"})		
	}
	
	////////////////////////
	
	function dispatchCurrent(){
		dispatchEvent({target:this,type:"onChangedCurrent"})	
	}
	
	/////////////////////////
	
	function dispatchMuteOn(){
		dispatchEvent({target:this,type:"onMuteOn"})
	}
	
	////////////////////////////
	
	function dispatchMuteOff(){
		dispatchEvent({target:this,type:"onMuteOff"})
	}
	
	///////////////////////////////////////////////
	
	function dispatchSoundComplete(){
		this.next()
		dispatchEvent({target:this,type:"onSoundComplete"})
	}
	
	////////////////////////////////////////////////
	
	function dispatchInit(){
		dispatchEvent({target:this,type:"onInit"})		
	}
	
	////////////////////////////////////////////////
  
}