import mx.controls.ProgressBar;
import templateMp3.mvc.*
import templateMp3.I.*
import templateMp3.util.Observable
import templateMp3.mvcMp3.*

class templateMp3.mvcMp3.Mp3{
	
///instance
static var __instance:Mp3
	
// model
var __model:Mp3Model
  
////tools
var __tools:ToolsMp3View
   
/////// volume
var __volume:VolumeView

////speaker
var __speaker:SpeakerView

////speaker 2
var __speakerContainer:SpeakerView

/////equalizer
var __equalizer:EqualizerView

////container root
var __containerRoot:ContainerRootView

////time
var __time:TimeView

//////progress
var __progress:ProgressView

////preloader
var __preloader:PreloaderView

/////buffer
var __buffer:BufferView

//////desc
var __desc:DescView

/////////////////////////////////////////////////////////////////////////////////////////////////
  
  public function Mp3(target:MovieClip) {
	 __instance=this
	 __model=new Mp3Model()
	 __model.__target=this
	 	 
	 ////container root
	 this.__containerRoot=ContainerRootView(target.attachMovie("_containerRoot","_containerRoot_",2))
	 this.__containerRoot.setModel(__model)
	 this.__containerRoot._y=0
	 this.__model.addEventListener("onSetSize",this.__containerRoot)
	 
	 /////tools
	 this.__tools=ToolsMp3View(this.__containerRoot.attachMovie("_toolsMp3","_tools_",33253))
	// this.__tools._x=70
	 //this.__tools._y=2
	 this.__tools.setModel(this.__model)
	 this.__model.addEventListener("onPlay",__tools)
	 this.__model.addEventListener("onStop",__tools)
	 this.__model.addEventListener("onPause",__tools)
	 this.__model.addEventListener("onInit",__tools)
	  	 
     ////volume
	 this.__volume=VolumeView(this.__containerRoot.attachMovie("_volume","_volume_",3))
	 this.__volume._x=160
	 this.__volume._y=15
	 this.__volume.setModel(this.__model)
	 this.__model.addEventListener("onPlay",this.__volume)
	 this.__model.addEventListener("onStop",this.__volume)
	 this.__model.addEventListener("onPause",this.__volume)
	 this.__model.addEventListener("onChangedCurrent",this.__volume)
	 this.__model.addEventListener("onChangedVolume",this.__volume)
	 this.__model.addEventListener("onMuteOn",this.__volume)
	 this.__model.addEventListener("onMuteOff",this.__volume)
	 	 
	  ///speaker equalizer
	 this.__speaker=SpeakerView(this.__containerRoot.attachMovie("_speakerEqualizer","_speakerEqualizer_",4))
	 this.__speaker._x=0
	 this.__speaker._y=3
     this.__speaker.setModel(this.__model)
	 this.__model.addEventListener("onPlay",this.__speaker)
	 this.__model.addEventListener("onStop",this.__speaker)
	 this.__model.addEventListener("onPause",this.__speaker)
	 this.__model.addEventListener("onChangedCurrent",this.__speaker)
	 this.__model.addEventListener("onMuteOn",this.__speaker)
	 this.__model.addEventListener("onMuteOff",this.__speaker)
	 
	 /*
	 ///////equalizer
	 this.__equalizer=EqualizerView(this.__containerRoot.attachMovie("_equalizer","_equalizer_",543))
	 this.__equalizer._x=40
	 this.__equalizer._y=17
	 this.__equalizer.setModel(this.__model)
	 this.__model.addEventListener("onPlay",this.__equalizer)
	 this.__model.addEventListener("onStop",this.__equalizer)
	 this.__model.addEventListener("onPause",this.__equalizer)
	 this.__model.addEventListener("onChangedCurrent",this.__equalizer)
	 this.__model.addEventListener("onMuteOn",this.__equalizer)
	 this.__model.addEventListener("onMuteOff",this.__equalizer)
	 this.__model.addEventListener("onSetSize",this.__equalizer)
	 /*/
	 
	 ///////////////////////////////time
	 this.__time=TimeView(this.__containerRoot.attachMovie("_time","_time_",1234512))
	 this.__time.setModel(__model)
	 this.__model.addEventListener("onPlay",this.__time)
	 this.__model.addEventListener("onStop",this.__time)
	 this.__model.addEventListener("onPause",this.__time)
	 this.__model.addEventListener("onProgressPause",this.__time)
	 this.__model.addEventListener("onProgressPlay",this.__time)
	 this.__model.addEventListener("onProgressLoad",this.__time)
	 
	 /////////////////////////////////progress
	 this.__progress=ProgressView(this.__containerRoot.attachMovie("_progress","_progress_",429000))
	 this.__progress.setModel(__model)
	 this.__model.addEventListener("onPlay", this.__progress)
	 this.__model.addEventListener("onStop", this.__progress)
	 this.__model.addEventListener("onPause", this.__progress)
	 this.__model.addEventListener("onSetSize",this.__progress)
	 this.__model.addEventListener("onChangedCurrent",this.__progress)
		 
	 ////////////////////////////////preloader
	 this.__preloader=PreloaderView(this.__progress.__scroll.attachMovie("_preloader","__preloader__",980))
	 this.__preloader._rotation=90
	 this.__model.addEventListener("onChangedCurrent",this.__preloader)
	 this.__model.addEventListener("onProgressLoad",this.__preloader)
	 this.__model.addEventListener("onSetSize",this.__preloader)
	 this.__preloader.setModel(__model)
	 
	 //////////////////////////////////////buffer
	 this.__buffer=BufferView(this.__containerRoot.attachMovie("_bufferMp3","_bufferMp3_",654218765))
	 this.__model.addEventListener("onPlay", this.__buffer)
	 this.__model.addEventListener("onStop", this.__buffer)
	 this.__model.addEventListener("onPause", this.__buffer)
	 this.__model.addEventListener("onProgressPause", this.__buffer)
	 this.__model.addEventListener("onProgressPlay", this.__buffer)
	 this.__model.addEventListener("onProgressLoad", this.__buffer)
	 this.__buffer.setModel(__model)
	 
	 //////////////////////////////////desc
	 this.__desc=DescView(this.__containerRoot.background.attachMovie("_descMp3","_descMp3_",1100))
	 this.__desc.setModel(__model)
	 this.__model.addEventListener("onChangedCurrent",this.__desc)
	 this.__model.addEventListener("onSetSize",this.__desc)
	 
	 
	 //////////////////////////////////end containerRoot	 
}

}