////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2005-2007 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.skins.halo
{

import flash.display.Graphics;
import mx.skins.ProgrammaticSkin;

/**
 *  The skin for the sort arrow in a column header in a DataGrid.
 *  
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion Flex 3
 */
public class DataGridSortArrow extends ProgrammaticSkin
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
    public function DataGridSortArrow()
    {
    	super();
    }
    
    //--------------------------------------------------------------------------
    //
    //  Overridden properties
    //
    //--------------------------------------------------------------------------
    
    //----------------------------------
    //  measuredWidth
    //----------------------------------
    
    /**
     *  @private
     */
    override public function get measuredWidth():Number
    {
        return 6;
    }
    
    //----------------------------------
    //  measuredHeight
    //----------------------------------
    
    /**
     *  @private
     */
    override public function get measuredHeight():Number
    {
        return 6;
    }
    
    //--------------------------------------------------------------------------
    //
    //  Overridden methods
    //
    //--------------------------------------------------------------------------
    
    /**
     *  @private
     */
    override protected function updateDisplayList(w:Number, h:Number):void
    {
        super.updateDisplayList(w, h);
        
        var g:Graphics = graphics;
        
        g.clear();
        g.beginFill(name == "sortArrowDisabled" ? getStyle("disabledIconColor") : getStyle("iconColor"));
        g.moveTo(0,0);
        g.lineTo(w, 0);
        g.lineTo(w / 2, h);
        g.lineTo(0,0);
        g.endFill();
    }
}

}