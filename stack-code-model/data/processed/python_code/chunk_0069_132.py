package com.unhurdle.spectrum
{
  import org.apache.royale.binding.ContainerDataBinding;

  public class FlexContainer extends Group
  {
    public function FlexContainer()
    {
      super();
      setStyle("display","flex");
			addBead(new ContainerDataBinding());
    }

    public function get alignContent():String{
      COMPILE::SWF{return "";}
      COMPILE::JS{return element.style.alignContent;}
    }
    /**
     * Takes any of the values accepted by flexbox align-content
     */
    public function set alignContent(value:String):void{
      setStyle("alignContent",value);
    }
    public function get alignItems():String{
      COMPILE::SWF{return "";}
      COMPILE::JS{return element.style.alignItems;}
    }
    /**
     * Takes any of the values accepted by flexbox align-items
     */
    public function set alignItems(value:String):void{
      setStyle("alignItems",value);
    }

    public function get justifyContent():String{
      COMPILE::SWF{return "";}
      COMPILE::JS{return element.style.justifyContent;}
    }
    /**
     * Takes any of the values accepted by flexbox justify-content
     */
    public function set justifyContent(value:String):void{
      setStyle("justifyContent",value);
    }

    private var _vertical:Boolean = false;

    public function get vertical():Boolean
    {
    	return _vertical;
    }

    public function set vertical(value:Boolean):void
    {
    	_vertical = value;
      computeDirection();
    }

    private var _reverse:Boolean;

    public function get reverse():Boolean
    {
    	return _reverse;
    }

    public function set reverse(value:Boolean):void
    {
    	_reverse = value;
      computeDirection();
    }
    private function computeDirection():void{
      var direction:String = vertical ? "column" : "row";
      if(reverse){
        direction += "-reverse";
      }
      setStyle("flexDirection",direction);
    }

    private var _wrap:Boolean;

    public function get wrap():Boolean
    {
    	return _wrap;
    }

    public function set wrap(value:Boolean):void
    {
    	_wrap = value;
      if(value){
        _reverseWrap = false;
      }
      setWrap();
    }

    private var _reverseWrap:Boolean;

    public function get reverseWrap():Boolean
    {
    	return _reverseWrap;
    }

    public function set reverseWrap(value:Boolean):void
    {
    	_reverseWrap = value;
      if(value){
        _wrap = false;
      }
      setWrap();
    }

    private function setWrap():void{
      var wrapVal:String;
      if(_wrap){
        wrapVal = "wrap";
      } else if(_reverseWrap){
        wrapVal = "wrap-reverse";
      } else {
        wrapVal = "nowrap";
      }
      setStyle("flexWrap",wrapVal);
    }


  }
}