import templateNewsy.mvcgallery.*;
import templateNewsy.I.*
import templateNewsy.util.Observable
import flash.display.BitmapData
import mx.events.EventDispatcher


class templateNewsy.mvcgallery.ThumbModel{
 	
var __array:Array //// array all thumbs
var __portionLength:Number  ///size portion
var __current=1 ////first portion
	
		
////////////////////////////////////////////////////////////////////////////////

function ThumbModel(array_){
	this.__array=array_.slice()
	
}

////////////////////////////////////////////////////////////////////////////////////////////////

function getPortion(nr:Number){
	 nr--
	nr*=__portionLength
	return __array.slice(nr,nr+__portionLength)
}

////////////////////////////////////////////////////////////////////////////////////////////////

function getLength(){
	return Math.ceil((__array.length-1)/__portionLength)
	
}

////////////////////////////////////////////////////////////////////////////////

function setCurrent(current_){
	this.__current=current_
}

///////////////////////////////////////////////////

function getCurrent(){
	return this.__current
}

/////////////////////////return number portion

function getNumer(nr_:Number){
	var nr=Math.ceil(nr_/this.__portionLength)
	return nr
}

/////////////////////////////////

	
  
}