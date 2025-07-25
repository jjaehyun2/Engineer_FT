﻿class Control extends MovieClip
{
	public var play_mc:MovieClip;
	public var pause_mc:MovieClip;
	public var background_mc:MovieClip;
	
	public var initialState:String;
	public var realWidth:Number;
	
	public var state:String;

	public var addListener:Function;
	public var removeListener:Function;
	private var broadcastMessage:Function;

	/**
	 * Constructor
	 */
	function Control()
	{
		AsBroadcaster.initialize(this);
		
		if(this.state == "play") this.pause_mc._visible = false;
		else this.play_mc._visible = false;
		
		this.realWidth = this.background_mc._width;
		
		background_mc.hover_mc._visible = play_mc.hover_mc._visible = pause_mc.hover_mc._visible = false;
	}
	
	function onRollOver()
	{
		_switch(true);
	}

	function onRollOut()
	{
		_switch(false);
	}
	
	function onReleaseOutside()
	{
		_switch(false);
	}

	function onRelease()
	{
		this.toggle(true);
	}
	
	private function _switch(toggle:Boolean):Void
	{
		if(this.state == "play") this.play_mc.hover_mc._visible = toggle;
		if(this.state == "pause") this.pause_mc.hover_mc._visible = toggle;
		this.background_mc.hover_mc._visible = toggle;
	}
	
	public function toggle(broadcast:Boolean):Void
	{
		if(broadcast == undefined) broadcast = false;
		if(this.state == "play")
		{
			if(broadcast) broadcastMessage("onPlay");
			this.play_mc._visible = false;
			this.play_mc.hover_mc._visible = false;
			this.pause_mc._visible = true;
			this.state = "pause";
		} else
		{
			if(broadcast) broadcastMessage("onPause");
			this.pause_mc._visible = false;
			this.pause_mc.hover_mc._visible = false;
			this.play_mc._visible = true;
			this.state = "play";
		}
	}
	
	public function flip():Void
	{
		this.background_mc._rotation = 180;
		this.background_mc._y += this.background_mc._height;
		this.background_mc._x += this.background_mc._width;
		this.play_mc._x = 14;
		this.pause_mc._x = 13;
	}
}