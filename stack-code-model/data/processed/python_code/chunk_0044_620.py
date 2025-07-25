////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2009 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.charts.chartClasses
{

/**
 *  An AxisLabelSet represents the label and tick data
 *  generated by an implementation of IAxis.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class AxisLabelSet
{
    include "../../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------
    
    /**
     *  Constructor.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function AxisLabelSet()
    {
        super();
    }

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //----------------------------------
    //  accurate
    //----------------------------------

    [Inspectable(environment="none")]

    /**
     *  When returned from the <code>getLabelEstimate()</code> method,
     *  set to <code>true</code> if the estimate accurately represents
     *  the final labels to be rendered. This property is irrelevant 
     *  in other contexts.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var accurate:Boolean;

    //----------------------------------
    //  labels
    //----------------------------------

    [Inspectable(environment="none")]

    /**
     *  An array of AxisLabel objects
     *  representing the values of the generating axis.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var labels:Array /* of AxisLabel */;
    
    //----------------------------------
    //  minorTicks
    //----------------------------------

    [Inspectable(environment="none")]

    /**
     *  An array of values from 0 to 1
     *  representing where to place minor tick marks along the axis.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var minorTicks:Array /* of Number */;    
    
    //----------------------------------
    //  ticks
    //----------------------------------

    [Inspectable(environment="none")]

    /**
     *  An array of values from 0 to 1
     *  representing where to place tick marks along the axis.
     *  
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public var ticks:Array /* of Number */; 
}

}