////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////

package spark.globalization.supportClasses
{
import flash.errors.IllegalOperationError;
import flash.events.EventDispatcher;
import flash.globalization.DateTimeStyle;
import flash.events.Event;

import mx.core.mx_internal;

import spark.formatters.DateTimeFormatter;

use namespace mx_internal;

[ResourceBundle("core")]

[ExcludeClass]

/**
 *  CalendarDate class provides a set of utility functions
 *  to deal with date manipulations about calendars.
 *
 *  <p>For the Mega release, this class supports only Gregorian
 *  calendar support and provideds the minimum functions.</p>
 *
 *  <p>For the Ultra relase, the intention is to virtualize calendars
 *  (Greogorian, Arabic, Hebrew, Japapane etc.) and to provide the
 *  uniformed operations for calendars, such as ways to increment/decrement
 *  month and year and so on.</p>
 *
 *  @see spark.formatters.DateTimeFormatter
 *  @see flash.globalization.DateTimeFormatter
 *
 *  @langversion 3.0
 *  @playerversion Flash 11
 *  @playerversion AIR 3
 *  @productversion Flex 4.6
 */
public class CalendarDate
{
    //--------------------------------------------------------------------------
    //
    //  Class Constants
    //
    //--------------------------------------------------------------------------
    
    private static const MILLISECONDS_PER_DAY:int = 1000 * 60 * 60 * 24;
    
    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------
    
    /**
     *  Constructs a new <code>CalendarDate</code> object.
     *
     *  <p>If the <code>date</code> argument is a <code>null</code>,
     *  today's date will be used.</p>
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    public function CalendarDate(date:Date = null)
    {
        if (!date)
            date = new Date();
        
        this.date = date;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------
    
    //----------------------------------
    //  date
    //----------------------------------
    
    /**
     *  @private
     *
     *  The internal storage for the <code>date</code> property.
     */
    private var _date:Date;
    
    /**
     *  The date object that represents a date in Gregorian calendar.
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    public function get date():Date
    {
        return _date;
    }
    
    public function set date(value:Date):void
    {
        _date = value;
    }
    
    //----------------------------------
    //  numDaysInMonth
    //----------------------------------
    
    /**
     *  Number of days in the current month.
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    public function get numDaysInMonth():int
    {
        return getEndOfMonth(date).date - getBeginingOfMonth(date).date + 1;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Private Methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  Calculate the begining of the current month.
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    private static function getBeginingOfMonth(date:Date):Date
    {
        const d:Date = new Date(date);
        
        d.date = 1;
        
        return d;
    }
    
    /**
     *  Calculate the begining of the next month.
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    private static function getBeginingOfNextMonth(date:Date):Date
    {
        const d:Date = new Date(date);
        
        d.date = 28;
        while (d.month == date.month)
            d.time += MILLISECONDS_PER_DAY;
        
        return d;
    }
    
    /**
     *  Calculate the end of the current month.
     *
     *  @langversion 3.0
     *  @playerversion Flash 11
     *  @playerversion AIR 3
     *  @productversion Flex 4.6
     */
    private static function getEndOfMonth(date:Date):Date
    {
        const d:Date = getBeginingOfNextMonth(date);
        
        d.time -= MILLISECONDS_PER_DAY;
        
        return d;
    }
}
}