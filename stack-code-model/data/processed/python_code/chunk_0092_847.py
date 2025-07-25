// Copyright � 2007. Adobe Systems Incorporated. All Rights Reserved.
package hansune.motion.easing
{

/**
 *  The Quadratic class defines three easing functions to implement 
 *  accelerated motion with ActionScript animations. The acceleration of motion 
 *  for a Quadratic easing equation is the same as for a timeline tween at 100% easing
 *  and is less dramatic than for the Cubic easing equation.
 * 
 * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
 * @see ../../../motionXSD.html Motion XML Elements 
 * @see fl.motion.FunctionEase  
 */  
public class Quadratic
{


	//--------------------------------------------------------------------------
	//
	//  Class methods
	//
	//--------------------------------------------------------------------------

    /**
     *  The <code>easeIn()</code> method starts motion from a zero velocity 
     *  and then accelerates motion as it executes. 
     *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase         
     */  
	public static function easeIn(t:Number, b:Number,
								  c:Number, d:Number):Number
	{
		return c * (t /= d) * t + b;
	}

    /**
     *  The <code>easeOut()</code> method starts motion fast 
     *  and then decelerates motion to a zero velocity as it executes. 
     *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase         
     */  
	public static function easeOut(t:Number, b:Number,
								   c:Number, d:Number):Number
	{
		return -c * (t /= d) * (t - 2) + b;
	}

    /**
     *  The <code>easeInOut()</code> method combines the motion
     *  of the <code>easeIn()</code> and <code>easeOut()</code> methods
	 *  to start the motion from a zero velocity, 
     *  accelerate motion, then decelerate to a zero velocity. 
     *
     *  @param t Specifies the current time, between 0 and duration inclusive.
	 *
     *  @param b Specifies the initial value of the animation property.
	 *
     *  @param c Specifies the total change in the animation property.
	 *
     *  @param d Specifies the duration of the motion.
     *
     *  @return The value of the interpolated property at the specified time.
     * @playerversion Flash 9.0.28.0
     * @playerversion AIR 1.0
     * @productversion Flash CS3
     * @langversion 3.0
     * @keyword Ease, Copy Motion as ActionScript    
     * @see fl.motion.FunctionEase         
     */  
	public static function easeInOut(t:Number, b:Number,
									 c:Number, d:Number):Number
	{
		if ((t /= d / 2) < 1)
			return c / 2 * t * t + b;

		return -c / 2 * ((--t) * (t - 2) - 1) + b;
	}
}

}