//****************************************************************************
//Copyright (C) 2007 flashextension.net. All Rights Reserved.
//The following is Sample Code and is subject to all restrictions on
//such code as contained in the End User License Agreement accompanying
//this product.
//****************************************************************************

import mx.transitions.Tween;
import mx.transitions.OnEnterFrameBeacon;
import flash.geom.ColorTransform;

class com.color.TweenColorTransform extends Tween {

	public var finishCT:ColorTransform;	
	public var beginCT:ColorTransform;
	public var changeCT:ColorTransform;
	
	public var changeProp:String = "redOffset";
	public var rgba:Array = ["redOffset","greenOffset","blueOffset","alphaOffset","redMultiplier","greenMultiplier","blueMultiplier","alphaMultiplier"];
	
	function set position (p:ColorTransform):Void {
		this.setPosition (p);		
	}
	
	function setPosition (ct:ColorTransform):Void {
		
		// discern between mc and object
		if (typeof this.obj == "movieclip")
		{
			this.obj.transform.colorTransform = ct;			
		}
		else
		{
			// copy all props
			for (var i = 0; i < this.rgba.length; i++)
			{
				var p = this.rgba[i];
				this.obj[p] = ct[p];
			}
		}
		this.broadcastMessage ("onMotionChanged", this, ct);	
		// added updateAfterEvent for setInterval-driven motion
		updateAfterEvent();
	}

	
	
	function get position ():ColorTransform {
		return this.getPosition();
	};
	function getPosition (t:Number):ColorTransform {
		if (t == undefined) t = this._time;
		var cc = this.changeCT[this.changeProp];
		var new_pos = this.func (t, this.beginCT[this.changeProp], cc, this._duration);
		
		// now update the others
		var tk = (cc != 0) ? ((new_pos - this.beginCT[this.changeProp]) / cc) : 0;

		
		var ct = new ColorTransform();
		for (var i = 0; i < this.rgba.length; i++)
		{
			var p = this.rgba[i];
			ct[p] = this.beginCT[p] + this.changeCT[p] * tk;
		}
		
		return ct;
	};
	
	function set begin(b:ColorTransform):Void {
		
		this.beginCT = new ColorTransform();

		// copy all props
		for (var i = 0; i < this.rgba.length; i++)
		{
			var p = this.rgba[i];
			this.beginCT[p] = b[p];
		}
		
	}
	
	function get begin():ColorTransform {
		return this.beginCT;
	}
	
	function set finish (f:ColorTransform):Void {
		this.finishCT = f;
		
		// compute change for r,g,b,a		
		this.changeCT = new ColorTransform();
		
		// use greatest delta r,g,b to pull numbers out of 'func'
		var max = 0;
		for (var i = 0; i < this.rgba.length; i++)
		{
			var p = this.rgba[i];
			this.changeCT[p] = f[p] - this.beginCT[p];
			if (Math.abs(this.changeCT[p]) > max) this.changeProp = p;
		}
		
	};
	
	function get finish ():ColorTransform {
		return this.finishCT;
	};
	
/////////////////////////////////////////////////////////////////////////

/*  constructor for TweenColorTransform class

	obj: reference - the object which the Tween targets
	prop: string - name of the property (in obj) that will be affected
	begin: ColorTransform - the starting value of prop SHOULD BE A ColorTransform!
	finish: ColorTransform - the finishing value of prop SHOULD BE A ColorTransform!
	duration: number - the length of time of the motion; set to infinity if negative or omitted
	useSeconds: boolean - a flag specifying whether to use seconds instead of frames
*/
	function TweenColorTransform (obj, prop, func, begin, finish, duration, useSeconds) {
		
		OnEnterFrameBeacon.init();
		if (!arguments.length) return;
		this.obj = obj;
		this.prop = prop;
		
		// begin & finish should be color transform objects
		this.begin = begin;
		
		if (func) this.func = func;
		this.finish = finish;
		
		this.position = begin;
		this.duration = duration;
		this.useSeconds = useSeconds;
		this._listeners = [];
		this.addListener (this);
		this.start();
	}
							
	
	function continueTo (finish:ColorTransform, duration:Number):Void {
		this.begin = this.position;
		this.finish = finish;
		if (duration != undefined)
			this.duration = duration;
		this.start();
	};
	
	function toString ():String {
		return "[TweenColorTransform]";
	}

	///////// PRIVATE METHODS


}