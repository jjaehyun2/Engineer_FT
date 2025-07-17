import mx.utils.Delegate

/**
 * This class is used for the seek bar of the video player
 */
class SimpleSlider extends MovieClip
{
	public var minValue:Number = 0
	public var maxValue:Number = 100
	public var onChange:Function

	private var currentValue:Number = 0
	private var dragging:Boolean = false
	
	public function get value():Number
	{
		return this.currentValue
	}
	
	public function set value(value:Number):Void
	{
		if(!dragging)
		{
			setValue(value)
		}
	}
	
	public function set enabled(enabled:Boolean):Void
	{
		if(!enabled)
		{
			this["mc_thumb"].stopDrag()
			dragging = false
		}
		
		this["mc_thumb"].enabled = enabled
	}
	
	public function SimpleSlider()
	{
		this["mc_thumb"].onPress = Delegate.create(this, mc_thumb_press)
		this["mc_thumb"].onRelease = Delegate.create(this, mc_thumb_release)
		this["mc_thumb"].onReleaseOutside = Delegate.create(this, mc_thumb_release)
	}
	
	public function mc_thumb_press():Void
	{
		dragging = true
		this["mc_thumb"].startDrag(this, false, 0, this["mc_track"]._width, 0, 0)
	}
	
	public function mc_thumb_release():Void
	{
		this["mc_thumb"].stopDrag()
		setValue(Math.round(this["mc_thumb"]._x / (this["mc_track"]._width / (maxValue - minValue))))
		onChange(this.value)
		dragging = false
	}
	
	private function setValue(value:Number):Void
	{
		this.currentValue = (value <= maxValue) ? value : maxValue
		this["mc_thumb"]._x = Math.round(value * (this["mc_track"]._width / (maxValue - minValue)))
		if(this["mc_thumb"]._x + this["mc_thumb"]._width > this["mc_track"]._width)
		{
			this["mc_thumb"]._x = this["mc_track"]._width - this["mc_thumb"]._width
		}
	}
}