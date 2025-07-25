// Copyright � 2007. Adobe Systems Incorporated. All Rights Reserved.
package hansune.motion.easing
{

/**
 *  The Back class defines three easing functions to implement 
 *  motion with ActionScript animations. 
 *
 * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
 * @see ../../../motionXSD.html Motion XML Elements 
 * @see fl.motion.FunctionEase 
 */  
public class Back
{


	//--------------------------------------------------------------------------
	//
	//  Class methods
	//
	//--------------------------------------------------------------------------
	
    /**
     *  The <code>easeIn()</code> method starts 
     *  the motion by backtracking and 
     *  then reversing direction and moving toward the target.
	 *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
	 *  @param s Specifies the amount of overshoot, where the higher the value, 
	 *  the greater the overshoot.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase     
     */  
	public static function easeIn(t:Number, b:Number, c:Number,
								  d:Number, s:Number = 0):Number
	{
		if (!s)
			s = 1.70158;
		
		return c * (t /= d) * t * ((s + 1) * t - s) + b;
	}

    /**
     *  The <code>easeOut()</code> method starts the motion by
     *  moving towards the target, overshooting it slightly, 
     *  and then reversing direction back toward the target.
	 *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
	 *  @param s Specifies the amount of overshoot, where the higher the value, 
	 *  the greater the overshoot.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase 
     */  
	public static function easeOut(t:Number, b:Number, c:Number,
								   d:Number, s:Number = 0):Number
	{
		if (!s)
			s = 1.70158;
		
		return c * ((t = t / d - 1) * t * ((s + 1) * t + s) + 1) + b;
	}

    /**
     *  The <code>easeInOut()</code> method combines the motion
	 *  of the <code>easeIn()</code> and <code>easeOut()</code> methods
	 *  to start the motion by backtracking, then reversing direction and 
	 *  moving toward the target, overshooting the target slightly, reversing 
     * direction again, and then moving back toward the target.
	 *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
	 *  @param s Specifies the amount of overshoot, where the higher the value, 
	 *  the greater the overshoot.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase      
     */  
	public static function easeInOut(t:Number, b:Number, c:Number,
									 d:Number, s:Number = 0):Number
	{
		if (!s)
			s = 1.70158; 
		
		if ((t /= d / 2) < 1)
			return c / 2 * (t * t * (((s *= (1.525)) + 1) * t - s)) + b;
		
		return c / 2 * ((t -= 2) * t * (((s *= (1.525)) + 1) * t + s) + 2) + b;
	}
}

}