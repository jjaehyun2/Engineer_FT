import templateBook.mvc.*
import templateBook.I.*
import templateBook.mvctemplate.*
import templateBook.util.Observable
import templateBook.Configuration


class templateBook.mvctemplate.Book{
  
 var __model:BookModel
 var __target:MovieClip
 var __background:BackgroundView
 var __bookView:BookView
 var __preloader:PreloaderMultipleView
 var __next:NextButtonView
 var __prev:PrevButtonView
 var __numberPageView:NumberPageView

//////////////////////////////////////////////////////////////////////////////////////////////
  
  public function Book(target:MovieClip) {
	this.__target=target
	__model=new BookModel(this)
		
  
 ///////////////////////background
 this.__background=BackgroundView(this.__target.attachMovie("_background_book","_background_book_",1))
 this.__background.setModel(this.__model)
 this.__model.addEventListener("onRemoveAll",this.__background)
 this.__model.addEventListener("onTweenPageEnd",this.__background)
 this.__model.addEventListener("onChangeBackground",this.__background)
 this.__model.addEventListener("onResize",this.__background)
 	
	
 ///////////////////////preloader	
 this.__preloader=PreloaderMultipleView(this.__target.attachMovie("_preloaderBook","_preloader_",120))
 this.__preloader.setModel(this.__model)
 this.__model.addEventListener("onRemoveAll",this.__preloader)
  this.__model.addEventListener("onResize", this.__preloader)

 		 
 ///////////////////////view book	 
 this.__bookView=BookView(this.__target.attachMovie("_book","_book_",100))
 this.__bookView=this.__target._book_
 this.__bookView.setModel(this.__model)
 this.__model.addEventListener("onSetPage",this.__bookView)
 this.__model.addEventListener("onResize",this.__bookView)
 this.__model.addEventListener("onLoadBackground",this.__bookView)
 
 
 //////////////////////next button
 this.__next=NextButtonView(this.__target.attachMovie("_nextbutton_book","_nextbutton_book_",5))
 this.__next.setModel(this.__model)
 this.__model.addEventListener("onResize", this.__next)
 this.__model.addEventListener("onSetPage",this.__next)
 this.__model.addEventListener("onNextPage",this.__next)
 this.__model.addEventListener("onPrevPage",this.__next)
 this.__model.addEventListener("onTweenPageEnd",this.__next)
 this.__model.addEventListener("onGotoPage",this.__next)
 
 
 ///////////////////////prev button
 this.__prev=PrevButtonView(this.__target.attachMovie("_prevbutton_book","_prevbutton_book_",8))
 this.__prev.setModel(this.__model)
 this.__model.addEventListener("onResize",this.__prev)
 this.__model.addEventListener("onSetPage",this.__prev)
 this.__model.addEventListener("onNextPage",this.__prev)
 this.__model.addEventListener("onPrevPage",this.__prev)
 this.__model.addEventListener("onTweenPageEnd",this.__prev)
 this.__model.addEventListener("onGotoPage",this.__prev)
 
 
 
 ///////////////////////number page menedzer
 if(Configuration.VISIBLE_MANAGER_PAGE=="true"){
 this.__numberPageView=NumberPageView(this.__target.attachMovie("_NumberPageView","_NumberPageView_",90))
 this.__numberPageView.setModel(this.__model)
 this.__model.addEventListener("onResize",this.__numberPageView)
 this.__model.addEventListener("onSetPage",this.__numberPageView)
 this.__model.addEventListener("onNextPage",this.__numberPageView)
 this.__model.addEventListener("onPrevPage",this.__numberPageView)
 this.__model.addEventListener("onTweenPageEnd",this.__numberPageView)
 this.__model.addEventListener("onGotoPage",this.__numberPageView)
 }
	
 }

}