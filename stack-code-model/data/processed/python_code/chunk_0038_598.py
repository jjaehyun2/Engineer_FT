package com.unhurdle.spectrum
{
  //TODO this doesn't work!
  COMPILE::JS{
    import org.apache.royale.core.WrappedHTMLElement;
  }

  public class ShowOnOverTooltip extends SpectrumBase
  {
    public function ShowOnOverTooltip()
    {
      super();
      typeNames = "u-tooltip-showOnHover";
    }
    
    private var textNode:TextNode;
    private var toolTip:Tooltip;

    override protected function getTag():String{
      return "span";
    }
    COMPILE::JS
    override protected function createElement():WrappedHTMLElement{
      super.createElement();
      textNode = new TextNode("");
      toolTip = new Tooltip();
      style = "margin: 15px 50px; cursor: default;";
      addElement(toolTip);
      textNode.element = element;
      return element;
    }

    public function get visibleText():String
    {
      return textNode.text;
    }

    public function set visibleText(value:String):void
    {
      textNode.text = value;
    }
    public function get text():String
    {
      return toolTip.text;
    }

    public function set text(value:String):void
    {
      toolTip.text = value;
    }
    public function get flavor():String
    {
      return toolTip.flavor;
    }

    public function set flavor(value:String):void
    {
      toolTip.flavor = value;
    }
    public function get icon():String
    {
      return toolTip.icon;
    }

    public function set icon(value:String):void
    {
      toolTip.icon = value;
    }
    public function get direction():String
    {
      return toolTip.direction;
    }

    public function set direction(value:String):void
    {
      toolTip.direction = value;
    }
    public function get isOpen():Boolean
    {
      return toolTip.isOpen;
    }

    public function set isOpen(value:Boolean):void
    {
      toolTip.isOpen = value;
    }    
  }
}