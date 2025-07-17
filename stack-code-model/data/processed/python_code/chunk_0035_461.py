import templateSlider.mvc.*
import templateSlider.I.*
import templateSlider.mvcgallery.*
import templateSlider.util.Observable
import templateSlider.mvcloader.*


class templateSlider.mvcgallery.Gallery{

  
  ////instance Gallery	
  static var __instance:Gallery

  ////target
  var __target:MovieClip

  // model
  var __model:GalleryModel
    
  ////button slide
  var __buttonSlide:BSlideView
  
  ////network
  var __network:NetworkView
   
  ////image
  var __image:ImageView
     
  ////preloader
  var __preloader:PreloaderView
  
    ////desc
  var __desc:DescView
  
  ///time slide
  var __time:TimeView
  
  /////portion image
  var __portionImage:PortionImageView
   
  /////portion thumb
  var __portionThumb:PortionThumbView
  
  /////arrow next
  var __arrowNext:ArrowNextView
  
  ////arrow prev
  var __arrowPrev:ArrowPrevView
  
  ////button close image
  var __buttonCloseImage:BCloseImageView
  
  ////button info
  var __buttonInfo:InfoView
  
  var inter
   
///////////////////////////////////////////////////////////////////////////////////////////////////////////
  
  static function getInstance(){
	  return __instance
  }
  
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////
  
  public function Gallery(target:MovieClip) {
	  this.__target=target
	 __instance=this
	 __model=new GalleryModel()
	 __model.__target=this
	 

	 // inter=setInterval(this,'addView',50)
	  addView()
  }
	  
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////
 
 
 function addView(){
  

	   clearInterval(inter)
	   

	 
	  	  
///////////////////////////////////////////////////////////////////buttton close image

/*
      this.__buttonCloseImage=BCloseImageView(__target.attachMovie("_ButtonCloseImage","_ButtonCloseImage_",1008))
	  this.__buttonCloseImage.hide()
	  this.__buttonCloseImage._x=Stage.width/2	
	  this.__buttonCloseImage._y=Stage.height/2
	  this.__buttonCloseImage.setModel(this.__model)
	  __model.addEventListener("onImageResize", this.__buttonCloseImage)
	  __model.addEventListener("onPressClose",this.__buttonCloseImage)
	  __model.addEventListener("onIntroStart",this.__buttonCloseImage)
	  __model.addEventListener("onIntroEnd",this.__buttonCloseImage)
	  __model.addEventListener("onExitStart",this.__buttonCloseImage)
	  __model.addEventListener("onExitEnd",this.__buttonCloseImage)
	  __model.addEventListener("onStopSlide",this.__buttonCloseImage)
	  __model.addEventListener("onStartSlide",this.__buttonCloseImage)
	   __model.addEventListener("onResize", this.__buttonCloseImage)
	   
/*/
	   
	   
////////////////////////////////////////////////button info

       __buttonInfo=InfoView(__target.attachMovie("_info","_infoe_",7005))
	   __buttonInfo.hide()
	   __buttonInfo.setModel(this.__model)
	  __model.addEventListener("onImageResize",  __buttonInfo)
	  __model.addEventListener("onPressClose", __buttonInfo)
	  __model.addEventListener("onIntroStart", __buttonInfo)
	  __model.addEventListener("onIntroEnd", __buttonInfo)
	  __model.addEventListener("onExitStart", __buttonInfo)
	  __model.addEventListener("onExitEnd", __buttonInfo)
	  __model.addEventListener("onStopSlide", __buttonInfo)
	  __model.addEventListener("onStartSlide", __buttonInfo)
	   __model.addEventListener("onResize",  __buttonInfo)
	    __model.addEventListener("onChangedIndex", __buttonInfo)


  
	  
///////////////////////////////////////////////////////////////////////////desc 
	
	  __desc=DescView(__target.attachMovie("_desc_gallery","_desc_gallery_",23232997))
	  __desc.setModel(__model)
	  __model.addEventListener("onChangedIndex",__desc)
	  __model.addEventListener("onLoadThumb",__desc)
	  __model.addEventListener("onLoadImageInit",__desc)
	  __model.addEventListener("onIntroStart",__desc)
	  __model.addEventListener("onIntroEnd",__desc)
	  __model.addEventListener("onExitStart",__desc)
	  __model.addEventListener("onExitEnd",__desc)
	  __model.addEventListener("onPressClose",__desc)
	  __model.addEventListener("onImageResize", __desc)
	  __model.addEventListener("onResize", __desc)
	  __model.addEventListener("onShovInfo", __desc)
	  
	 
		
///////////////////////////////////BSlideView (button enabled/disabled slide)

	  __buttonSlide=BSlideView(__target.attachMovie("_slide_button","_slide_button",3000000))
	  __buttonSlide.hide()
	  __buttonSlide.setModel(__model)
	  __model.addEventListener("onIntroStart",__buttonSlide)
	  __model.addEventListener("onIntroEnd",__buttonSlide)
	  __model.addEventListener("onExitStart",__buttonSlide)
	  __model.addEventListener("onExitEnd",__buttonSlide)
	  __model.addEventListener("onImageResize",__buttonSlide)
	  __model.addEventListener("onProgressTime",__buttonSlide)
	  __model.addEventListener("onStopSlide",__buttonSlide)
	  __model.addEventListener("onStartSlide",__buttonSlide)
	  __model.addEventListener("onChangedIndex",__buttonSlide)
	  __model.addEventListener("onLoadThumb",__buttonSlide)
	  __model.addEventListener("onNext",__buttonSlide)
	  __model.addEventListener("onPrev",__buttonSlide)
	  __model.addEventListener("onPressClose",__buttonSlide)
	  __model.addEventListener("onLoadImage",__buttonSlide)
	  __model.addEventListener("onResize",__buttonSlide)
	  
	
/////////////////////////////////////////////////////////////////////////////////////time slide

	  __time=TimeView(__buttonSlide.mc_slide.attachMovie("_time_gallery","_time_gallery_",40))
	  __time.hide()
	  __time.setModel(__model)
	  __model.addEventListener("onIntroStart",__time)
	  __model.addEventListener("onIntroEnd",__time)
	  __model.addEventListener("onExitStart",__time)
	  __model.addEventListener("onExitEnd",__time)
	  __model.addEventListener("onImageResize",__time) 
	  __model.addEventListener("onProgressTime",__time)
	  __model.addEventListener("onStopSlide",__time)
	  __model.addEventListener("onStartSlide",__time)
	  __model.addEventListener("onChangedIndex",__time)
	  __model.addEventListener("onLoadThumb",__time)
	  __model.addEventListener("onNext",__time)
	  __model.addEventListener("onPrev",__time)
	   __model.addEventListener("onPressClose",__time)
	   __model.addEventListener("onResize",__time)
	  
	  		  
//////////////////////////////////////////////////////////////portion thumb

      __portionThumb=PortionThumbView(__target.attachMovie("_portionThumb","_portionThumb_",50))
	  __portionThumb._x=732
      __portionThumb._y=202
      __portionThumb.setModel(__model)
      __model.addEventListener("onLoadThumb",__portionThumb)
      __model.addEventListener("onChangedIndex",__portionThumb)
      __model.addEventListener("onChangedPortion",__portionThumb)
	  __model.addEventListener("onResize",__portionThumb)
     


////////////////////portion Image//////////////////////////////////////////////////////////////////////////////////

	__portionImage=PortionImageView(__target.attachMovie("_portionImage","_portionImage_",60000))
	__portionImage.setModel(__model)
	__model.addEventListener("onLoadThumb",__portionImage)
	__model.addEventListener("onImageResize",__portionImage)
	__model.addEventListener("onChangedIndex",__portionImage)
	__model.addEventListener("onIntroStart",__portionImage)
	__model.addEventListener("onIntroEnd",__portionImage)
	

	   
////////////////////preloader///////////////////////////////////////////////////////////////////////////////////////

	__preloader=PreloaderView(__target.attachMovie("_preloader","preloader",1057,{_x:0,_y:250}))
	__preloader.hide()
	__preloader.setModel(__model)
	__model.addEventListener("onLoadImageStart",__preloader)
	__model.addEventListener("onLoadImageInit",__preloader)
	__model.addEventListener("onLoadImageProgress",__preloader)
	__model.addEventListener("onResize",__preloader)
	  
	 
//////////////////////network///////////////////////////////////////////////////////////////////////////////
/*
	 __network=NetworkView(__target.attachMovie("_network_gallery","_network_gallery_",80))
	 __network._x=300
	 __network._y=100
	 __network.setModel(__model)
	 __model.addEventListener("onChangedIndex",__network)
	 __model.addEventListener("onLoadThumb",__network)
	 __model.addEventListener("onChangedPortion",__network)
	 __model.addEventListener("onLoadImage",__network)
	 __model.addEventListener("onPressClose",__network)
	 __model.addEventListener("onResize",__network)
	  /*/
	  
////////////////////////////////////Arrow Next Image
 /*
    this.__arrowNext=ArrowNextView(__target.attachMovie("_arrowNext_gallery","_arrowNext_gallery_",90))
	this.__arrowNext.setModel(__model)
	__model.addEventListener("onChangedIndex",this.__arrowNext)
	__model.addEventListener("onLoadThumb",this.__arrowNext)
	__model.addEventListener("onImageResize",this.__arrowNext)
	__model.addEventListener("onPressClose",this.__arrowNext)
	__model.addEventListener("onLoadImage",this.__arrowNext)
	__model.addEventListener("onIntroStart",this.__arrowNext)
	__model.addEventListener("onIntroEnd",this.__arrowNext)
	__model.addEventListener("onExitStart",this.__arrowNext)
	__model.addEventListener("onExitEnd",this.__arrowNext)
	__model.addEventListener("onResize",this.__arrowNext)
	/*/
///////////////////////////////////Arrow Prev Image
   /*
    this.__arrowPrev=ArrowPrevView(__target.attachMovie("_arrowPrev_gallery","_arrowPrev_gallery_",100))
	this.__arrowPrev.setModel(__model)
	__model.addEventListener("onChangedIndex",this.__arrowPrev)
	__model.addEventListener("onLoadThumb",this.__arrowPrev)
	__model.addEventListener("onImageResize",this.__arrowPrev)
	__model.addEventListener("onPressClose",this.__arrowPrev)
	__model.addEventListener("onLoadImage",this.__arrowPrev)
	__model.addEventListener("onIntroStart",this.__arrowPrev)
	__model.addEventListener("onIntroEnd",this.__arrowPrev)
	__model.addEventListener("onExitStart",this.__arrowPrev)
	__model.addEventListener("onExitEnd",this.__arrowPrev)
	__model.addEventListener("onResize",this.__arrowPrev)
 /*/
/////////////////////////////////////////////////////////////////image

	  __image=ImageView(__target.attachMovie("_image_gallery","_image_gallery_",1011))
	  __image.setModel(__model)
	  __model.addEventListener("onResize",this.__image)
	  __model.addEventListener("onChangedIndex",this.__image)
	  __model.addEventListener("onLoadThumb",this.__image)
	  __model.addEventListener("onLoadImageInit",this.__image)
	  __model.addEventListener("onIntroStart",this.__image)
	  __model.addEventListener("onIntroEnd",this.__image)
	  __model.addEventListener("onExitStart",this.__image)
	  __model.addEventListener("onExitEnd",this.__image)
	  __model.addEventListener("onLoadImage",this.__image)
	  __model.addEventListener("onPressClose",this.__image)
	
	 	
 }
	  
	


 

}