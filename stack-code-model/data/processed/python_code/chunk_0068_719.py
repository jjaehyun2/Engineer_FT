/*
 Copyright aswing.org, see the LICENCE.txt.
*/

package org.aswing.models{
	
import flash.events.EventDispatcher;
import flash.events.IEventDispatcher;
import org.aswing.event.InteractiveEvent;

/**
 * The default implementation of BoundedRangeModel.
 * @author iiley
 */
public class NumberBoundedRangeModel extends EventDispatcher {
	
	private var value:Number;
	private var extent:Number;
	private var min:Number;
	private var max:Number;
	private var isAdjusting:Boolean;
	
	/**
	 * Create a DefaultBoundedRangeModel
	 * @throws RangeError when invalid range properties
	 */
	public function NumberBoundedRangeModel(value:Number=0, extent:Number=0, min:Number=0, max:Number=100){
		isAdjusting = false;
		
		if (max >= min && value >= min && value + extent >= value && value + extent <= max){
			this.value = value;
			this.extent = extent;
			this.min = min;
			this.max = max;
		}else{
			throw new RangeError("invalid range properties");
		}
	}
	
	public function getValue():Number{
		return value;
	}
	
	public function getExtent():Number{
		return extent;
	}
	
	public function getMinimum():Number{
		return min;
	}
	
	public function getMaximum():Number{
		return max;
	}
	
	public function setValue(n:Number, programmatic:Boolean = true):void {
		n = Math.min(n, max - extent);
		var newValue:Number = Math.max(n, min);
		setRangeProperties(newValue, extent, min, max, isAdjusting, programmatic);
		
	}
	
	public function setExtent(n:int):void{
		var newExtent:Number = Math.max(0, n);
		if (value + newExtent > max){
			newExtent = max - value;
		}
		setRangeProperties(value, newExtent, min, max, isAdjusting);
	}
	
	public function setMinimum(n:int):void{
		var newMax:Number = Math.max(n, max);
		var newValue:Number = Math.max(n, value);
		var newExtent:Number = Math.min(newMax - newValue, extent);
		setRangeProperties(newValue, newExtent, n, newMax, isAdjusting);
	}
	
	public function setMaximum(n:int):void{
		var newMin:Number = Math.min(n, min);
		var newExtent:Number = Math.min(n - newMin, extent);
		var newValue:Number = Math.min(n - newExtent, value);
		setRangeProperties(newValue, newExtent, newMin, n, isAdjusting);
	}
	
	public function setValueIsAdjusting(b:Boolean):void{
		setRangeProperties(value, extent, min, max, b, false);
	}
	
	public function getValueIsAdjusting():Boolean{
		return isAdjusting;
	}
	
	public function setRangeProperties(newValue:Number, newExtent:Number, newMin:Number, newMax:Number, adjusting:Boolean, programmatic:Boolean=true):void{
		if (newMin > newMax){
			newMin = newMax;
		}
		if (newValue > newMax){
			newMax = newValue;
		}
		if (newValue < newMin){
			newMin = newValue;
		}
		if (newExtent + newValue > newMax){
			newExtent = newMax - newValue;
		}
		if (newExtent < 0){
			newExtent = 0;
		}
		var isChange:Boolean = newValue != value || newExtent != extent || newMin != min || newMax != max || adjusting != isAdjusting;
		if (isChange){
			value = newValue;
			extent = newExtent;
			min = newMin;
			max = newMax;
			isAdjusting = adjusting;
			fireStateChanged(programmatic);
		}
	}
	
	public function addStateListener(listener:Function, priority:int=0, useWeakReference:Boolean=false):void{
		addEventListener(InteractiveEvent.STATE_CHANGED, listener, false, priority);
	}
	
	public function removeStateListener(listener:Function):void{
		removeEventListener(InteractiveEvent.STATE_CHANGED, listener);
	}
		
	protected function fireStateChanged(programmatic:Boolean):void{
		dispatchEvent(new InteractiveEvent(InteractiveEvent.STATE_CHANGED, programmatic));
	}
	
	override public function toString():String{
		var modelString:String = "value=" + getValue() + ", " + "extent=" + getExtent() + ", " + "min=" + getMinimum() + ", " + "max=" + getMaximum() + ", " + "adj=" + getValueIsAdjusting();
		return "DefaultBoundedRangeModel" + "[" + modelString + "]";
	}
	
}
}