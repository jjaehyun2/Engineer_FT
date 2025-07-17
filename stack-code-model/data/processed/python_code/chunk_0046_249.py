package com.unhurdle.spectrum
{
  //TODO
  //didn't fix this at all
  COMPILE::JS{
    import org.apache.royale.core.WrappedHTMLElement;
  }
  import org.apache.royale.utils.PointUtils;
  import org.apache.royale.geom.Point;
  import org.apache.royale.events.MouseEvent;
  import org.apache.royale.utils.number.pinValue;
  import org.apache.royale.utils.number.getPercent;
  public class RampSlider extends SliderBase
  {
    public function RampSlider()
    {
      super();
      typeNames = getSelector() + " " + valueToSelector("ramp");
    }

    private var handle:HTMLElement;
    
    COMPILE::JS
    override protected function createElement():WrappedHTMLElement{
        var elem:WrappedHTMLElement = super.createElement();
        controlsContainer = newElement("div",appendSelector("-controls"));
        var ramp:HTMLDivElement = newElement("div") as HTMLDivElement;
        ramp.className = appendSelector("-ramp");
        var svgElement:SVGElement = newIconSVG("");
        var pathElement:SVGPathElement = newSVGElement("path","") as SVGPathElement;
        pathElement.setAttribute("d","M240,4v8c0,2.3-1.9,4.1-4.2,4L1,9C0.4,9,0,8.5,0,8c0-0.5,0.4-1,1-1l234.8-7C238.1-0.1,240,1.7,240,4z");
        svgElement.setAttribute("viewBox","0 0 240 16");
        svgElement.setAttribute("preserveAspectRatio","none");
        svgElement.setAttribute("aria-hidden",true);
        svgElement.appendChild(pathElement);
        ramp.appendChild(svgElement);
        controlsContainer.appendChild(ramp);
        handle = newElement("div",appendSelector("-handle"));
        handle.style.left = "40%"
        input = newElement("input",appendSelector("-input")) as HTMLInputElement;
        input.type = "range";
        input.step = "1";
        max = 50;
        handle.appendChild(input);
        controlsContainer.appendChild(handle);
        elem.appendChild(controlsContainer);
        element.addEventListener('mousedown', onMouseDown);
        return elem;
    }
    
    // override protected function positionElements():void{
		// }

    public function get value():Number
    {
    	return Number(input.value);
    }

    public function set value(value:Number):void
    {      
			input.value = "" + value;
			if(parent){
				// positionElements();
			}
			if(valueNode){
				valueNode.text = "" + value;
			}
    }
    // override protected function getValue():String{
		// 	return input.value;
		// }    
		// override protected function enableDisableInput(value:Boolean):void{
		// 	input.disabled = value;
		// }
    COMPILE::JS
    override protected function onMouseMove(e:MouseEvent):void {
      if(disabled){
        return;
      }
			var sliderOffsetWidth:Number = element.offsetWidth;
      var localX:Number = PointUtils.globalToLocal(new Point(e.clientX,e.clientY),this).x;
			var x:Number = pinValue(localX,0,sliderOffsetWidth);
			var percent:Number = getPercent(x,sliderOffsetWidth);
			var val:Number = (max-min) / (100/percent) + min;
			var stepVal:Number = step;
			var rem:Number = val % stepVal;
			val = val - rem;
			if (rem > (stepVal/2)){
		    val += stepVal;
			}
			value = val;
      handle.style.left = percent + "%";
    }
  }
}