package com.unhurdle.spectrum
{
   COMPILE::JS
  {
    import org.apache.royale.html.util.addElementToWrapper;
    import org.apache.royale.core.WrappedHTMLElement;
  }
  public class TabIndicator extends SpectrumBase
  {
    public function TabIndicator()
    {
      super();
      typeNames = getSelector();
    }

    override protected function getSelector():String{
      return getTabsSelector() + "-selectionIndicator";
    }
    
  COMPILE::JS
    override protected function createElement():WrappedHTMLElement
    {
      var elem:WrappedHTMLElement = addElementToWrapper(this,'div');
      return elem;
    }    
  }
}