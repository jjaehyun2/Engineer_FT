import template_form.mvctemplate.*;
import template_form.I.*
import template_form.util.Observable
import template_form.mvc.*
import flash.display.BitmapData
import mx.events.EventDispatcher
import mx.utils.Delegate
import template_form.Configuration

class template_form.mvctemplate.FormModel extends Observable{


var __maxHeight:Number=150
var __sendTrue:String="__sendTrue_EMPTY"
var __sendFalse:String="__sendFalse__EMPTY"
var __sendProgress:String="__sendProgress__EMPTY"
var __buttonSend:String = "__buttonSend_EMPTY"
var __buttonReset:String="__buttonRESET_EMPTY"


/////////////////////////////////////////////////color
var __titleColor:Number
var __borderColor:Number
var __backgrondColor:Number
var __errorBorderColor:Number
var __inputColor:Number
var __alertColor:Number
var __buttonTextColor:Number
var __buttonBackgroundColor:Number
/////////////////////////////////////////////////end color

var __spaceY:Number


var __headline
var __sendTo ///e-mail
var __urlSend:String	
var __vars:LoadVars
var __view:Array	////view
var __form:Form
var __alignButton:String="R"
var __xml:XML
		
///////////////////////////////////KONSTRUKTOR//////////////////////////////

function FormModel(form_:Form){ 
this.__form=form_	
__view=[]

}

///////////////////////////////////////////////////////////////////////////////////////////////

function dataProvider(xml_){

	this.__xml=xml_.firstChild
	
	var old
	for(var i=0;i<__xml.firstChild.childNodes.length;i++){
		var node:XMLNode=__xml.firstChild.childNodes[i]
		var mc:AbstractView=AbstractView(this.addItem(node.attributes))
		var attrib:Object=node.attributes
		var x:Number=Number(attrib.x)
		var y:Number=Number(attrib.y)
		
		if(!isNaN(y)&&!isNaN(x)){  ///it is number in xml file
		mc._y=y	
		mc._x=x
		}else{    /////empty number x and y in xml file
		mc._y=(i==0) ? 0 : old._y+old.getHeight()+__spaceY
		}
		old=AbstractView(mc)
	}
	
	
	this.__form.__container.__oldRows=mc
	
	this.setPositionButton()
	
	

}

////////////////////////////////////////////////////////////////////////////////////////////////

function addItem(obj:Object){
	var container=this.__form.__container
    var instance:AbstractView=AbstractView(container.addItem(obj))
	__view.push(instance)
	return instance
}

//////////////////////////////////////////////////////////////////////////////////

function setPositionButton(){
	var container=this.__form.__container
	var buttonSend = this.__form.__buttonSend
	var buttonReset=this.__form.__buttonReset
	var status=this.__form.__status
	
	
	////////////////////buttonSend
		
	var button_send_x:Number=Number(this.__xml.firstChild.attributes.button_send_x)
	var button_send_y:Number=Number(this.__xml.firstChild.attributes.button_send_y)
	
	if(!isNaN(button_send_x)&&!isNaN(button_send_y)){
	
	buttonSend._x=button_send_x
	buttonSend._y = button_send_y
	
	
	

		
	}else{
	buttonSend._x=(this.__alignButton=="L") ? 0 : container.getWidth()-buttonSend._width
	buttonSend._y = 220//container.getHeight()+35
	
	}
	
	buttonReset._x=(__alignButton=="L") ? buttonSend._x+buttonSend._width+5 :buttonSend._x-buttonReset._width-5
	buttonReset._y = buttonSend._y
	
	
	
	////////////////////////////status (alert)
		
	var alert_x:Number=Number(this.__xml.firstChild.attributes.alert_x)
	var alert_y:Number=Number(this.__xml.firstChild.attributes.alert_y)
	
	if(!isNaN(alert_x)&&!isNaN(alert_y)){
	
	status._x=alert_x
	status._y=alert_y
		
	}else{
	status._y=this.__form.__buttonSend._y+this.__form.__buttonSend._height+5
	}
	
	
	this.__form.__target._y=Configuration.POSITION_Y//-this.__form.__container.getHeight()/2
	
}

////////////////////////////////////////////////////////////////////////////////////////////////

function check(){
	for(var i=0;i<this.__view.length;i++){
		var mc:AbstractView=AbstractView(this.__view[i])
		var value=mc.check()
		if(value==false){
			mc.shovError()
		return false
		}else{
			mc.hideError()
		}
		
	}
	
	send()
	return true
}


////////////////////////////////////////////////////////////////////////////////////////////////

function reset() {
	clear()
	
}

////////////////////////////////////////////////////////////////////////////////////////////////

function getKeySubject(){
	
	for(var i=0;i<this.__xml.firstChild.childNodes.length;i++){
	var node:XMLNode=this.__xml.firstChild.childNodes[i]
	if(node.attributes.subject=="true"){
	return 	node.attributes.key
	}
	}
	
}

////////////////////////////////////////////////////////////////////////////////////////////////

function getKeyReturnableEmail(){
	
	for(var i=0;i<this.__xml.firstChild.childNodes.length;i++){
	var node:XMLNode=this.__xml.firstChild.childNodes[i]
	if(node.attributes.returnable_email=="true"){
	return 	node.attributes.key
	}
	}
	
}


/////////////////////////////////////////////////////////////////////////////////////////////////

function send(){
	this.dispatchEvent({target:this,type:"onSend"})
	this.__vars=new LoadVars()
	delete this.__vars.onLoad
	
	for(var i=0;i<this.__view.length;i++){
	var mc:AbstractView=AbstractView(this.__view[i])
	var value=mc.getValue()
	var key=mc.getKey()
	this.__vars[key]=mc.getTitle()+":"+value
	}
	this.__vars.onLoad=Delegate.create(this,onLoadVars)
	
	this.__vars.SENDTO=this.__sendTo  ////email
	this.__vars.HEADLINE=this.__headline
	this.__vars.KEY_SUBJECT=getKeySubject()//KEY_SUBJECT
	this.__vars.KEY_RETURNABLE_EMAIL=getKeyReturnableEmail()///KEY_RETURNABLE_EMAIL
	this.__vars.sendAndLoad(__urlSend,this.__vars,"POST")
	
	for(var i in this.__vars){
		///trace("key = "+i+"  value "+this.__vars[i])
	}
	
}

/////////////////////////////////////////////////////////////////////////////////////////////////

function onLoadVars(succes){
	if(succes&&this.__vars.senden=="ok"){
		this.dispatchEvent({target:this,type:"onSendTrue"})
	}else{
		this.dispatchEvent({target:this,type:"onSendFalse"})		
	}
}


/////////////////////////////////////////////////////////////////////////////////////////////////

	public function clear(){
		for(var i=0;i<this.__view.length;i++){
		var mc:AbstractView=AbstractView(this.__view[i])
        mc.clear()
		
	}
	}
	
/////////////////////////////////////////////////////////////////////////////////////////////////

function addButtonSend(){
	
	
	
}

///////////////////////////////////////////////////////////////////////////////////////////////////


  
}