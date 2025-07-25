////////////////////////////////////////////////////////////////////////////////
//
// Copyright (c) 2010 ESRI
//
// All rights reserved under the copyright laws of the United States.
// You may freely redistribute and use this software, with or
// without modification, provided you include the original copyright
// and use restrictions.  See use restrictions in the file:
// <install location>/License.txt
//
////////////////////////////////////////////////////////////////////////////////
package widgets.eSearch
{

    import mx.core.ClassFactory;
    
    import spark.components.DataGroup;
    
    // these events bubble up from the SearchResultItemRenderer
    [Event(name="relateClick", type="flash.events.Event")]
    
    public class RelateResultDataGroup extends DataGroup
    {
        public function RelateResultDataGroup()
        {
            super();
            this.itemRenderer = new ClassFactory(RelateResultItemRenderer);
        }
    }
}