import template_form.mvc.*
import template_form.I.*
import template_form.mvctemplate.*
import template_form.util.Observable
import template_form. mvclogowanie.*


class template_form.mvctemplate.Form{

  
 var __model:FormModel
 var __target:MovieClip
 var __container:ContainerView
 var __buttonSend:SendView 
 var __buttonReset:ResetView
 var __status:StatusView
 
 static var __instance:Form
    
/////////////////////////////////////////////////////////////////////////////

  static function getInstance(){
	  if(Form.__instance==undefined){
		  trace("WARNING !!! - NIE STWORZYLES INSTANCJI FROM !")		  
	  }
	  return __instance
  }
  
 ////////////////////////////////////////////////////////////////////////////// 
  
  public function Form(target:MovieClip) {
	   this.__target=target
	 __instance=this
	 __model=new FormModel(this)
		   
	 
//////////////////////////////////////////////////////////////////////////////container form

   this.__container=ContainerView(this.__target.attachMovie("_containerView","_containerView_",5))
   this.__container.setModel(this.__model)
   
   
	
///////////////////////////////////////////////////////////////////////////////button Send

  this.__buttonSend=SendView(this.__target.attachMovie("_buttonView","_buttonView_",10))
  this.__buttonSend.setModel(this.__model)
  
  ///////////////////////////////////////////////////////////////////////////////button Reset

  __buttonReset=ResetView(this.__target.attachMovie("_butReset","_butReset_",11))
  __buttonReset.setModel(this.__model)
  
  //////////////////////////////////////////////////////////////////////////////status view

  this.__status=StatusView(this.__target.attachMovie("_statusView","_statusView_",15))
  this.__status.setModel(this.__model)
  this.__model.addEventListener("onSendTrue",this.__status)
  this.__model.addEventListener("onSendFalse",this.__status)
  this.__model.addEventListener("onSend",this.__status)
	

	



  }

 

}