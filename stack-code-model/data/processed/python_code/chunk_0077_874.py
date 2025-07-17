package com.unhurdle.spectrum
{

  [Event(name="itemClicked", type="org.apache.royale.events.ValueEvent")]
  public class Breadcrumbs extends List
  {
    /**
     * <inject_html>
     * <link rel="stylesheet" href="assets/css/components/breadcrumb/dist.css">
     * </inject_html>
     * 
     */

    public function Breadcrumbs()
    {
      super();
    }
    override protected function getSelector():String{
      return "spectrum-Breadcrumbs";
    }
    override protected function getTag():String{
      return "div";
    }
    private var _isTitle:Boolean;

    public function get isTitle():Boolean
    {
    	return _isTitle;
    }

    public function set isTitle(value:Boolean):void
    {
      if(value != !!_isTitle){
          toggle(valueToSelector("title"),value);
      }
      _isTitle = value;
    }
    private var _multiline:Boolean;

    public function get multiline():Boolean
    {
    	return _multiline;
    }

    public function set multiline(value:Boolean):void
    {
      if(value != !!_multiline){
        toggle(valueToSelector("multiline"),value);
      }
      _multiline = value;
    }
    private var _compact:Boolean;

    public function get compact():Boolean
    {
    	return _compact;
    }

    public function set compact(value:Boolean):void
    {
      if(value != !!_compact){
        toggle(valueToSelector("compact"),value);
      }
      _compact = value;
    }
  }
}