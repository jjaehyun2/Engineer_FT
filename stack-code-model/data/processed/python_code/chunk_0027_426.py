////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2005-2010 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.collections
{

import flash.events.Event;
import flash.events.EventDispatcher;
import mx.collections.errors.SortError;
import mx.managers.ISystemManager;
import mx.managers.SystemManager;
import mx.resources.IResourceManager;
import mx.resources.ResourceManager;
import mx.utils.ObjectUtil;

[ResourceBundle("collections")]
[Alternative(replacement="spark.collections.SortField", since="4.5")]

/**
 *  Provides the sorting information required to establish a sort on a field
 *  or property in a collection view.
 *
 *  The SortField class is meant to be used with the Sort class.
 *
 *  Typically the sort is defined for collections of complex items, that is
 *  items in which the sort is performed on properties of those objects.
 *  As in the following example:
 *
 *  <pre><code>
 *     var col:ICollectionView = new ArrayCollection();
 *     col.addItem({first:"Anders", last:"Dickerson"});
 *     var sort:Sort = new Sort();
 *     sort.fields = [new SortField("first", true)];
 *     col.sort = sort;
 *  </code></pre>
 *
 *  There are situations in which the collection contains simple items, like
 *  <code>String</code>, <code>Date</code>, <code>Boolean</code>, etc.
 *  In this case, sorting should be applied to the simple type directly.
 *  When constructing a sort for this situation only a single sort field is
 *  required and should not have a <code>name</code> specified.
 *  For example:
 *
 *  <pre><code>
 *     var col:ICollectionView = new ArrayCollection();
 *     col.addItem("California");
 *     col.addItem("Arizona");
 *     var sort:Sort = new Sort();
 *     sort.fields = [new SortField(null, true)];
 *     col.sort = sort;
 *  </code></pre>
 *
 *  <p>By default the comparison provided by the SortField class does
 *  not provide correct language specific
 *  sorting for strings.  For this type of sorting please see the 
 *  <code>spark.collections.Sort</code> and 
 *  <code>spark.collections.SortField</code> classes.</p>
 * 
 *  @mxml
 *
 *  <p>The <code>&lt;mx:SortField&gt;</code> tag has the following attributes:</p>
 *
 *  <pre>
 *  &lt;mx:SortField
 *  <b>Properties</b>
 *  caseInsensitive="false"
 *  compareFunction="<em>Internal compare function</em>"
 *  descending="false"
 *  name="null"
 *  numeric="null"
 *  /&gt;
 *  </pre>
 *
 *  @see mx.collections.ICollectionView
 *  @see mx.collections.Sort
 *  @see spark.collections.Sort
 *  @see spark.collections.SortField

 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class SortField extends EventDispatcher implements ISortField
{
    include "../core/Version.as";

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     *
     *  @param name The name of the property that this field uses for
     *              comparison.
     *              If the object is a simple type, pass <code>null</code>.
     *  @param caseInsensitive When sorting strings, tells the comparator
     *              whether to ignore the case of the values.
     *  @param descending Tells the comparator whether to arrange items in
     *              descending order.
     *  @param numeric Tells the comparator whether to compare sort items as
     *              numbers, instead of alphabetically.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function SortField(name:String = null,
                              caseInsensitive:Boolean = false,
                              descending:Boolean = false,
                              numeric:Object = null)
    {
        super();

        _name = name;
        _caseInsensitive = caseInsensitive;
        _descending = descending;
        _numeric = numeric;
        _compareFunction = stringCompare;
    }

    //--------------------------------------------------------------------------
    //
    //  Variables
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     *  Used for accessing localized Error messages.
     */
    private var resourceManager:IResourceManager =
                                    ResourceManager.getInstance();

    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------

    //---------------------------------
    //  arraySortOnOptions
    //---------------------------------

    /**
    *  @inheritDoc
    *
    *  @langversion 3.0
    *  @playerversion Flash 9
    *  @playerversion AIR 1.1
    *  @productversion Flex 3
    */
    public function get arraySortOnOptions():int
    {
        if (usingCustomCompareFunction
            || name == null
            || _compareFunction == xmlCompare
            || _compareFunction == dateCompare)
        {
            return -1;
        }
        var options:int = 0;
        if (caseInsensitive) options |= Array.CASEINSENSITIVE;
        if (descending) options |= Array.DESCENDING;
        if (numeric == true || _compareFunction == numericCompare) options |= Array.NUMERIC;
        return options;
    }

    //---------------------------------
    //  caseInsensitive
    //---------------------------------

    /**
     *  @private
     *  Storage for the caseInsensitive property.
     */
    private var _caseInsensitive:Boolean;

    [Inspectable(category="General")]
    [Bindable("caseInsensitiveChanged")]

    /**
     *  Specifies whether the sort for this field should be case insensitive.
     *
     *  @default false
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get caseInsensitive():Boolean
    {
        return _caseInsensitive;
    }

    /**
     *  @private
     */
    public function set caseInsensitive(value:Boolean):void
    {
        if (value != _caseInsensitive)
        {
            _caseInsensitive = value;
            dispatchEvent(new Event("caseInsensitiveChanged"));
        }
    }

    //---------------------------------
    //  compareFunction
    //---------------------------------

    /**
     *  @private
     *  Storage for the compareFunction property.
     */
    private var _compareFunction:Function;

    [Inspectable(category="General")]

    /**
     *  The function that compares two items during a sort of items for the
     *  associated collection. If you specify a <code>compareFunction</code>
     *  property in an ISort object, Flex ignores any 
     *  <code>compareFunction</code> properties of the ISort's SortField
     *  objects.
     *  <p>The compare function must have the following signature:</p>
     *
     *  <p><code>function myCompare(a:Object, b:Object):int</code></p>
     *
     *  <p>This function must return the following values:</p>
     *
     *   <ul>
     *        <li>-1, if <code>a</code> should appear before <code>b</code> in
     *        the sorted sequence</li>
     *        <li>0, if <code>a</code> equals <code>b</code></li>
     *        <li>1, if <code>a</code> should appear after <code>b</code> in the
     *        sorted sequence</li>
     *  </ul>
     * 
     *  <p>The default value is an internal compare function that can perform
     *  a string, numeric, or date comparison in ascending or descending order,
     *  with case-sensitive or case-insensitive string comparisons.
     *  Specify your own function only if you need a need a custom comparison
     *  algorithm. This is normally only the case if a calculated field is
     *  used in a display.</p>
     *  
     *  Note if you need, language specific sorting then consider using the
     *  <code>spark.collections.SortField</code> class.
     * 
     *  @see spark.collections.SortField
     * 
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get compareFunction():Function
    {
        return _compareFunction;
    }

    /**
     *  @private
     */
    public function set compareFunction(c:Function):void
    {
        _compareFunction = c;
        _usingCustomCompareFunction = (c != null);
    }

    //---------------------------------
    //  descending
    //---------------------------------

    /**
     *  @private
     *  Storage for the descending property.
     */
    private var _descending:Boolean;

    [Inspectable(category="General")]
    [Bindable("descendingChanged")]

    /**
     *  @inheritDoc
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get descending():Boolean
    {
        return _descending;
    }

    /**
     *  @private
     */
    public function set descending(value:Boolean):void
    {
        if (_descending != value)
        {
            _descending = value;
            dispatchEvent(new Event("descendingChanged"));
        }
    }

    //---------------------------------
    //  name
    //---------------------------------

    /**
     *  @private
     *  Storage for the name property.
     */
    private var _name:String;

    [Inspectable(category="General")]
    [Bindable("nameChanged")]

    /**
     *  @inheritDoc
     *
     *  @default null
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get name():String
    {
        return _name;
    }

    /**
     *  @private
     */
    public function set name(n:String):void
    {
        _name = n;
        dispatchEvent(new Event("nameChanged"));
    }

    //---------------------------------
    //  numeric
    //---------------------------------

    /**
     *  @private
     *  Storage for the numeric property.
     */
    private var _numeric:Object;

    [Inspectable(category="General")]
    [Bindable("numericChanged")]

    /**
     *  @inheritDoc
     *
     *  @default null
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get numeric():Object
    {
        return _numeric;
    }

    /**
     *  @private
     */
    public function set numeric(value:Object):void
    {
        if (_numeric != value)
        {
            _numeric = value;
            dispatchEvent(new Event("numericChanged"));
        }
    }

    //---------------------------------
    //  usingCustomCompareFunction
    //---------------------------------

    private var _usingCustomCompareFunction:Boolean;

    /**
     *  @inheritDoc
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function get usingCustomCompareFunction():Boolean
    {
        return _usingCustomCompareFunction;
    }

    //--------------------------------------------------------------------------
    //
    //  Overridden Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @private
     *  A pretty printer for Sort that lists the sort fields and their
     *  options.
     */
    override public function toString():String
    {
        return ObjectUtil.toString(this);
    }

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  @inheritDoc
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function initializeDefaultCompareFunction(obj:Object):void
    {
        // if the compare function is not already set then we can set it
        if (!usingCustomCompareFunction)
        {
            if (numeric == true)
                _compareFunction = numericCompare;
            else if (caseInsensitive || numeric == false)
                _compareFunction = stringCompare;
            else
            {
                // we need to introspect the data a little bit
                var value:Object;
                if (_name)
                {
                    try
                    {
                        value = obj[_name];
                    }
                    catch(error:Error)
                    {
                    }
                }
                //this needs to be an == null check because !value will return true
                //where value == 0 or value == false
                if (value == null)
                {
                    value = obj;
                }

                var typ:String = typeof(value);
                switch (typ)
                {
                    case "string":
                        _compareFunction = stringCompare;
                    break;
                    case "object":
                        if (value is Date)
                        {
                            _compareFunction = dateCompare;
                        }
                        else
                        {
                            _compareFunction = stringCompare;
                            var test:String;
                            try
                            {
                                test = value.toString();
                            }
                            catch(error2:Error)
                            {
                            }
                            if (!test || test == "[object Object]")
                            {
                                _compareFunction = nullCompare;
                            }
                        }
                    break;
                    case "xml":
                        _compareFunction = xmlCompare;
                    break;
                    case "boolean":
                    case "number":
                        _compareFunction = numericCompare;
                    break;
                }
            }  // else
        } // if
    }

    /**
     *  @inheritDoc
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    public function reverse():void
    {
        descending = !descending;
    }

    //--------------------------------------------------------------------------
    //
    //  Private Methods
    //
    //--------------------------------------------------------------------------

    private function nullCompare(a:Object, b:Object):int
    {
        var value:Object;
        var left:Object;
        var right:Object;

        var found:Boolean = false;

        // return 0 (ie equal) if both are null
        if (a == null && b == null)
        {
            return 0;
        }

        // we need to introspect the data a little bit
        if (_name)
        {
            try
            {
                left = a[_name];
            }
            catch(error:Error)
            {
            }

            try
            {
                right = b[_name];
            }
            catch(error:Error)
            {
            }
        }

        // return 0 (ie equal) if both are null
        if (left == null && right == null)
            return 0;

        if (left == null && !_name)
            left = a;

        if (right == null && !_name)
            right = b;


        var typeLeft:String = typeof(left);
        var typeRight:String = typeof(right);


        if (typeLeft == "string" || typeRight == "string")
        {
                found = true;
                _compareFunction = stringCompare;
        }
        else if (typeLeft == "object" || typeRight == "object")
        {
            if (left is Date || right is Date)
            {
                found = true;
                _compareFunction = dateCompare
            }
        }
        else if (typeLeft == "xml" || typeRight == "xml")
        {
                found = true;
                _compareFunction = xmlCompare;
        }
        else if (typeLeft == "number" || typeRight == "number"
                 || typeLeft == "boolean" || typeRight == "boolean")
        {
                found = true;
                _compareFunction = numericCompare;
        }

        if (found)
        {
            return _compareFunction(left, right);
        }
        else
        {
            var message:String = resourceManager.getString(
                "collections", "noComparatorSortField", [ name ]);
            throw new SortError(message);
        }
    }

    /**
     *  Pull the numbers from the objects and call the implementation.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    private function numericCompare(a:Object, b:Object):int
    {
        var fa:Number;
        try
        {
            fa = _name == null ? Number(a) : Number(a[_name]);
        }
        catch(error:Error)
        {
        }

        var fb:Number;
        try
        {
            fb = _name == null ? Number(b) : Number(b[_name]);
        }
        catch(error:Error)
        {
        }

        return ObjectUtil.numericCompare(fa, fb);
    }

    /**
     *  Pull the date objects from the values and compare them.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    private function dateCompare(a:Object, b:Object):int
    {
        var fa:Date;
        try
        {
            fa = _name == null ? a as Date : a[_name] as Date;
        }
        catch(error:Error)
        {
        }

        var fb:Date;
        try
        {
            fb = _name == null ? b as Date : b[_name] as Date;
        }
        catch(error:Error)
        {
        }

        return ObjectUtil.dateCompare(fa, fb);
    }

    /**
     *  Pull the strings from the objects and call the implementation.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    private function stringCompare(a:Object, b:Object):int
    {
        var fa:String;
        try
        {
            fa = _name == null ? String(a) : String(a[_name]);
        }
        catch(error:Error)
        {
        }

        var fb:String;
        try
        {
            fb = _name == null ? String(b) : String(b[_name]);
        }
        catch(error:Error)
        {
        }

        return ObjectUtil.stringCompare(fa, fb, _caseInsensitive);
    }

    /**
     *  Pull the values out fo the XML object, then compare
     *  using the string or numeric comparator depending
     *  on the numeric flag.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion Flex 3
     */
    private function xmlCompare(a:Object, b:Object):int
    {
        var sa:String;
        try
        {
            sa = _name == null ? a.toString() : a[_name].toString();
        }
        catch(error:Error)
        {
        }

        var sb:String;
        try
        {
            sb = _name == null ? b.toString() : b[_name].toString();
        }
        catch(error:Error)
        {
        }

        if (numeric == true)
        {
            return ObjectUtil.numericCompare(parseFloat(sa), parseFloat(sb));
        }
        else
        {
            return ObjectUtil.stringCompare(sa, sb, _caseInsensitive);
        }
    }
}
}