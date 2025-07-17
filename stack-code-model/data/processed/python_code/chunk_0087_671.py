import menu_tree.components.Scroll;
import menu_tree.mvc.AbstractController;
import menu_tree.mvctemplate.*;
import menu_tree.I.*
import menu_tree.util.Observable
import flash.display.BitmapData
import mx.data.components.XMLConnector;
import mx.events.EventDispatcher
import mx.utils.Delegate

import mx.transitions.Tween
import mx.transitions.easing.*

 import LuminicBox.Log.*;

class menu_tree.mvctemplate.TreeModel extends Observable{
var __tree:Tree
var __container:MovieClip	
var __containerBig:MovieClip
var __xml
var __array:Array
var __zagniezdzone
var __scroll:Scroll
var current:AbstractItem
var __height:Number=300
var __width:Number=0
var __oldMovieClip:AbstractItem
var counterEndTweenY:Number
var allTweenY:Number
var mcMask:MovieClip
var mcArea:MovieClip
var tweenKorekteY:Tween
var currentLocal:Array  ////current in item, subite, etc
var xMax:Number


////////////////CONST
var COLOR_TEXT:Array /////COLOR TEXT
var COLOR_SCROLL
var COLOR_BACKGROUND_SCROLL
var WIDTH_SCROLL:Number=1
var PADDING_LEFT:Number
var PADDING_RIGHT:Number
var PADDING_UP:Number
var PADDING_DOWN:Number 
var COLOR_TITLE_MENU:String
var TITLE_MENU:String
var COLOR_BACKGROUND_MENU:String


		
///////////////////////////////////////////////////////////////////////////////////////

function TreeModel(tree_:Tree){
	COLOR_TEXT=[]
	currentLocal=[]
	 __array=[]
	this.__tree=tree_
	
	
  
}

///////////////////////////////////////////////////////////////////////////////////////

function getWidth(){
	return this.mcMask.getBounds(this.mcMask).xMax
}

/////////////////////////////////////////////////////////////////////////////////////

function hasVisibleTrue(node_:XMLNode) {
	 var array:Array = getHasChildNodes(node_,0,undefined,1)
	 
	 for (var i in array) {
		 var value = array[i].child.attributes
		 var visible = value.visible
		 
		 if (visible == undefined) {
			 return true;
		 }else {
			 return false;
		 }
		 
		
	 
	 }
	 

	
}

/////////////////////////////////////////////////////////////////////////////////////

function init(xml_:XML) {
	  this.__containerBig=this.__tree.__target.createEmptyMovieClip("mcContainerBig",1)
	this.__containerBig._x=PADDING_LEFT
	this.__containerBig._y=PADDING_UP
	this.__container=this.__containerBig.createEmptyMovieClip("mcContainer",1)
	
	
	 this.__xml=xml_
    __array=getHasChildNodes(this.__xml.firstChild,0,undefined,undefined)
	for (var i = 0; i < __array.length; i++) {
		
		
		
	var value=__array[i]
	var item=value.item
	var node:XMLNode = value.child
	
	///if(node.attributes.visible!="false"){
	
	var color_rol=node.attributes.color_rol
	var color_out=node.attributes.color_out
	var row:AbstractItem=AbstractItem(this.__container.attachMovie("_"+item+"TreeView","_itemTreeView_"+i,i,{item:item,model_abstract:this}))
	row.setColorOut(color_out)
	row.setColorRol(color_rol)
	row.item=item
	row.setModel(this)
	row.node=value.child
	row.t.text=value.child.attributes.label.toUpperCase()
	row.t.autoSize=true
	value.child.attributes.ref=row
	//__array[i].ref=row
	
	
	
	/////unVisible arrow 
	if(row.node.hasChildNodes()==false||hasVisibleTrue(row.node)==false){
			row.arrow._visible=false
 	}
		

	
	if(item==0){
		row._x=0
		row.setVisibility(true)
	}else if(item==1){
		row._x=25	
		row.setVisibility(false)
	}else if(item==2){
		row._x=50
		row.setVisibility(false)
	}
	
	var xMaxCounter=(row.getBounds(row).xMax)
	if(xMax==undefined||xMaxCounter>xMax){
		xMax=xMaxCounter
	}
	
	//}
	
	}
		
	createMask()
	updatePosition()
 }
 
//////////////////////////////////////////////////////////////////////////////////////////////////////

function setSize(width_,height_){
	height=height_
    width=width_
}

////////////////////////////////////////////////////////////////////////////////////////////////////////
 
function set width(value_:Number){
	if(value_){
	__width=value_
	}
	if(value_=="auto"){
		__width=xMax+PADDING_LEFT+PADDING_RIGHT
	}
	
	
	this.createMask()
    this.addRemoveScroll()
    this.korekteY()
	this.dispatchEvent({target:this,type:"onChangedSize"})
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

function get width(){
	return __width
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

function set height(value_:Number){
	if(value_){
	__height=value_
	}
	this.createMask()
    this.addRemoveScroll()
    this.korekteY()
	this.dispatchEvent({target:this,type:"onChangedSize"})
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

function get height(){
	return __height
}

///////////////////////////////////////////////////////////////////////////////////////////////////////

private function createMask(){
	var space:Number=5
	mcMask=this.__tree.__target.createEmptyMovieClip("mcMask",432)
	mcMask._x=PADDING_LEFT-space
	mcMask._y=PADDING_UP
	Drawing.rectangle(mcMask,0,0,this.width-(PADDING_LEFT+PADDING_RIGHT)+2*space,this.__height-(PADDING_UP+PADDING_DOWN),["0xFF0000",20])
	this.mcArea=this.mcMask.duplicateMovieClip("mcArea__",999)
	this.mcArea._visible=false
	this.__container.setMask(mcMask)
}

//////////////////////////add or remove scrolll/////////////////////////////////////////////////////////////////////////

function addRemoveScroll(){
	if(getContainerHeight()>(this.height-(PADDING_UP+PADDING_DOWN))){
	this.addScroll()
	}else{
	 this.__scroll.removeMovieClip()
	 this.__container.stop()
	 this.__container.stopTween()
	 this.tweenKorekteY.stop()
	//this.__container._y=0
   	////var a=new Tween(this.__container,"_y",Strong.easeOut,this.__container._y,0,1, true);
	this.__container.tween('_y',0,0.5,'linear',0)
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////////

function addScroll(){
	var containerScroll:MovieClip=this.__tree.__target.createEmptyMovieClip("mcContainerScroll",43265)
	this.__scroll=Scroll(containerScroll.attachMovie("_scrollMenuTree", "_scrollMenuTree_", 2343,{COLOR_SCROLL:COLOR_SCROLL,COLOR_BACKGROUND_SCROLL:COLOR_BACKGROUND_SCROLL}))
	this.__scroll.__tree=this
	var stosunek=((this.__height-(PADDING_DOWN+PADDING_UP))/getContainerHeight())
		this.__scroll.height = this.__height - (PADDING_DOWN + PADDING_UP)
		///__scroll.width=200
		this.__scroll.y = PADDING_UP
		this.__scroll.x =5 //(this.width-20)-this.WIDTH_SCROLL
		this.__scroll.zakres = [0,-getContainerHeight()+(this.__height-PADDING_UP-PADDING_DOWN),stosunek];
		this.__scroll.onChange = Delegate.create(this,this.onChange)
		this.__scroll.setScrollPosition(this.__container._y,false)
		this.__scroll.onPressSuwak=Delegate2.create(this,this.onPressScroll)
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

function onPressScroll(){
	delete this.__container.onEnterFrame
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

function onChange(w){
	this.__container._y=w
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

function updatePosition(){
var old:AbstractItem

this.counterEndTweenY=0
allTweenY=0
	
for(var i=0;i<this.__array.length;i++){
	var value=this.__array[i]
	var ref:AbstractItem=AbstractItem(value.child.attributes.ref)
		
if(ref.getVisibility()==true){	
	if(old==undefined){
		ref.y=0
	}else{
		ref.y=old.y+old.getHeight()
	}
	allTweenY++
	ref.stopTween("_y")
	///ref.tween('_y',ref.y,0.5,'easeOutCubic',0,{scope:this,func:this.onEndTweenY})
	ref._tween.stop()
	
	var time=0.7
	
	ref._tween=new Tween(ref,"_y",Strong.easeInOut,ref._y,ref.y,time, true);
	////ref._tween.onMotionChanged=Delegate2.create(this,this.onChangedTweenY,ref)
	ref._tween.onMotionFinished=Delegate.create(this,this.onEndTweenY)
	old=ref
}
}
__oldMovieClip=old
this.korekteY()
}

//////////////////////////////////////container tree//////////////////////////////////////////////////////////////////////

function getContainerHeight(){
	return this.__oldMovieClip._y+this.__oldMovieClip.getHeight()	
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////

function getContainerWidth(){
	return this.__width	
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function onChangedTweenY(ref){
	//this.addRemoveScroll()
	///this.korekteY()
}

///////////////////////////////////////////////////////////////////////////////////////////

function onEndTweenY(){
	this.counterEndTweenY++
	if(this.counterEndTweenY>=allTweenY){
	this.addRemoveScroll()
	korekteY()
	this.dispatchEvent({target:this,type:"onEndTween"})
	}
}

////////////////////////position container and scroll////////////////////////////////////////////////////////////////////////

function korekteY(){
	var h=this.height-(PADDING_UP+PADDING_DOWN)
	var currentY=this.current.getBounds(this.__container._parent).yMin
	var spaceTween=(h/2)-currentY
	var newYContainer=Math.min(Math.max((this.__container._y+spaceTween),(-getContainerHeight()+h)),0 )
	

	///////////////////////////////////////////////////variant 1
	var _this:TreeModel=TreeModel(this)
	this.__container.onEnterFrame=function(){
     if(1){
	this._y+=(newYContainer-this._y)/2
	_this.__scroll.setScrollPosition(this._y)
	if( Math.abs(newYContainer-this._y)<1){
		delete this.onEnterFrame
	 }else{
		
	 }
	 }
	}
	
	//////////////////////////////////////////////////end variant 1
	/*
	 // variant 2
	//this.__container.stopTween()
	this.tweenKorekteY.stop()
	this.tweenKorekteY = new Tween(this.__container,"_y",Strong.easeInOut,this.__container._y,newYContainer,.6, true);
	this.tweenKorekteY.onMotionFinished = Delegate2.create(this,this.onKorekteEnd)
	this.tweenKorekteY.onMotionChanged = Delegate2.create(this,this.onKorekteEnd)
    /*/
 }

////////////////////////////////////////////////////////////////////////////////////////////////

function onKorekteEnd(){
	 this.__scroll.setScrollPosition(this.__container._y,false)
	addRemoveScroll()
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

private function private_getHasChildNodes(child:XMLNode,item_:Number,id_:Number,visible_){ 
	var len = child.childNodes.length;
	var old:MovieClip;
	for (var i = 0; i<len; i++) {
		
		
	var no_id = (id_ == undefined || id_ != child.childNodes[i].attributes.id)//////////no id
	
	if(visible_==1){
	   var no_visible = true
	}else {
		var no_visible = child.childNodes[i].attributes.visible != "false" 
	}
		
	
	
	
	if (no_visible ) {
	this.__zagniezdzone.push( { child:child.childNodes[i], item:item_ } )
		
	}

	if (child.childNodes[i].hasChildNodes()&&no_id) {
			if (item_ == 0) {
				private_getHasChildNodes(child.childNodes[i],1,id_);
			} else if(item_ == 1) {
				private_getHasChildNodes(child.childNodes[i],2,id_);
			} else if(item_ == 2){
				private_getHasChildNodes(child.childNodes[i],3,id_);
				
			}
		}
}
	return this.__zagniezdzone
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////

public function getHasChildNodes(child:XMLNode,item_:Number,id_:Number,visible_){  
	this.__zagniezdzone=[]
	return this.private_getHasChildNodes(child,item_,id_,visible_)
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function reset(){
	for(var i=0;i<this.__array.length;i++){
		var value=__array[i]
		var item=value.item
	    var ref=value.child.attributes.ref
		if(item==0){
			ref.hideRow()		
			this.currentLocal[ref.item]=undefined
		}
	}
	this.updatePosition()
}

////////////////setSelectedId(id_menu_in_xml_file//////////////////////////////////////////////////////////////////////

public function setSelectedId(id_:Number,dispatch_:Boolean):Void{
	dispatch_=(dispatch_==undefined) ? true : dispatch_
	var currentNode:XMLNode = this.getNode(id_)
	
	
	var nod:XMLNode = __xml.idMap[String(id_)]
	var visible:String = nod.attributes.visible
	
	var counter:Number=0
	if (visible == "false") {
		do {
		counter++
		nod=nod.parentNode
		currentNode = this.getNode(nod.attributes.id)
		if (counter > 4) { break;}
		}while(nod.attributes.visible=="false")
	}
	

	

	
///var log:Logger = new Logger("Tester");
//log.addPublisher( new ConsolePublisher() );
////log.info("set selected id = " + currentNode)



	
	if (currentNode == undefined) {
		///currentNode=getNode()
		//reset()
	}
	
	////////////search parent node/////////////////////////////
	var parentNode:XMLNode=currentNode
	var arrayParent:Array=[]
	do{
	parentNode=parentNode.parentNode
	arrayParent.push(parentNode.attributes.ref)
	}while(parentNode.parentNode!=null)
	///////////////onPress parent node///////////////////////////////////
	for(var i in arrayParent){
	  var ref:AbstractItem=AbstractItem(arrayParent.pop())
	  if(ref.active==true){
	  ref.onPress(false)
	  }
	}
	//////////////onPress Current Node////////////////////////////////
	currentNode.attributes.ref.onPress(dispatch_)
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

public function getNode(id_:Number):XMLNode{
		for(var i in __array){
		var value:Object=__array[i]
		var id:Number=(value.child.attributes.id)
		if(id==id_){
			return value.child
		}
	}
}
	
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

public function setSelected(array_:Array,boolean_:Boolean){
	var currentXml:XMLNode=__xml.firstChild
	for(var i=0;i<array_.length;i++){
		var value:Number=Number(array_[i]-1)
		currentXml=currentXml.childNodes[value]
	}
	var id=currentXml.attributes.id
	setSelectedId(id,boolean_)
}

//////////////////////////get Pathway////////////////////////////////////////////////////////////////////////////////////////

public function getPathway():Array{
	var arrayNode=[]
	var _currentNode:XMLNode=this.current.node
	var _parentNode:XMLNode=_currentNode
	arrayNode.push(_currentNode)
	do{
		_parentNode=_parentNode.parentNode
		arrayNode.unshift(_parentNode)
		
	}while(_parentNode.parentNode.parentNode.parentNode!=null)
    return arrayNode;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////


  
}