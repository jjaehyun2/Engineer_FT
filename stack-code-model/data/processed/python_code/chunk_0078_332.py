package spark.menubar 
{
    import flash.events.Event;
    import flash.events.MouseEvent;
    import mx.events.FlexEvent;
    import mx.core.IVisualElement;
    import spark.components.List;
    import spark.components.IItemRenderer;
    import spark.events.IndexChangeEvent;
    import spark.menubar.events.SparkMenuEvent;
        
    [Event(name="change", type="spark.menubar.events.SparkMenuEvent")]
    
    public class SparkMenuBar extends List
    {
        override public function dispatchEvent(event:Event):Boolean
        {
            if (event.type == IndexChangeEvent.CHANGE && event is IndexChangeEvent && !(event is SparkMenuEvent))
            {
                var ice:IndexChangeEvent = event as IndexChangeEvent;
                
                // check for a menubar entry without a menu
                if (dataProvider.getItemAt(ice.newIndex).children().length() == 0)
                {
                    event = SparkMenuEvent.convert(ice, null, dataProvider.getItemAt(ice.newIndex));
                    super.dispatchEvent(event);
                }
                // don't dispatch change events directly from the MenuBar, only forward SparkMenuEvents from the
                // menus.
                dispatchEvent(new FlexEvent(FlexEvent.VALUE_COMMIT));                
                return true;          
            }
            return super.dispatchEvent(event);
        }
        
        override protected function item_mouseDownHandler(event:MouseEvent):void
        {
            // someone else handled it already since this is cancellable thanks to 
            // some extra code in SystemManager that redispatches a cancellable version 
            // of the same event
            if (event.isDefaultPrevented())
                return;
            
            // Handle the fixup of selection
            var newIndex:int
            if (event.currentTarget is IItemRenderer)
                newIndex = IItemRenderer(event.currentTarget).itemIndex;
            else
                newIndex = dataGroup.getElementIndex(event.currentTarget as IVisualElement);

            // if selectedIndex is not newIndex, base class will dispatch an event.
            // if they match, we have to force the dispatch
            if (newIndex == selectedIndex)
            {
                // but only if it is a menubar item without a menu
                if (dataProvider.getItemAt(newIndex).children().length() == 0)
                {
                    var sme:SparkMenuEvent = new SparkMenuEvent(IndexChangeEvent.CHANGE,
                        false, false, newIndex, newIndex, null, dataProvider.getItemAt(newIndex));
                    dispatchEvent(sme);                    
                }
            }
            
            super.item_mouseDownHandler(event);
        }
    }
    
}