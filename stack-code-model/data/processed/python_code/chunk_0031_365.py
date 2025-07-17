package com.unhurdle.spectrum
{
  COMPILE::JS{
    import org.apache.royale.html.util.addElementToWrapper;
    import org.apache.royale.core.WrappedHTMLElement;
    import com.unhurdle.spectrum.const.IconType;
  }
  public class ExplicitPagination extends SpectrumBase
  {
    public function ExplicitPagination()
    {
      super();
      toggle(valueToSelector("explicit"),true);
      pagesNum = 1;
      pageIsSelected = 1;
      href = "";
    }
    override protected function getSelector():String{
				return "spectrum-Pagination";
		}

    private var input:HTMLInputElement;
    private var span:TextNode;
    private var prev:HTMLLinkElement;
    private var next:HTMLLinkElement;

    COMPILE::JS
    override protected function createElement():WrappedHTMLElement{
      var elem:WrappedHTMLElement = addElementToWrapper(this,"nav");
      var buttonBase:String = "spectrum-ActionButton spectrum-ActionButton--quiet ";
      prev = newElement("a",buttonBase + appendSelector("-prevButton")) as HTMLLinkElement
      var prevType:String = IconType.CHEVRON_LEFT_MEDIUM;
      var prevCheckIcon:Icon = new Icon(Icon.getCSSTypeSelector(prevType));
      prevCheckIcon.type = prevType;
      prev.appendChild(prevCheckIcon.element);
      prev.addEventListener("click",prevPage);
      elem.appendChild(prev);
      input = newElement("input","spectrum-Textfield " + appendSelector("-input")) as HTMLInputElement;
      input.type = "text";
      input.name = "field";
      input.value = "" + pageIsSelected;
      input.addEventListener("change",changeValue);
      elem.appendChild(input);
      span = new TextNode("");
      span.element = newElement("span","spectrum-Body--secondary" + appendSelector("-counter"));
      span.element.style.marginLeft = '6px';
      elem.appendChild(span.element);
      next = newElement("a",buttonBase + appendSelector("-nextButton")) as HTMLLinkElement
      var nextType:String = IconType.CHEVRON_RIGHT_MEDIUM;
      var nextCheckIcon:Icon = new Icon(Icon.getCSSTypeSelector(nextType));
      nextCheckIcon.type = nextType;
      next.appendChild(nextCheckIcon.element);
      next.addEventListener("click",nextPage);
      elem.appendChild(next);
      return elem;
    }
    private var _href:String;

    public function get href():String
    {
    	return _href;
    }

    public function set href(value:String):void
    {
      if(value){
      	_href = value;
      } else {
        _href = "#";
        }
        COMPILE::JS
        {
          prev.href = _href;
          next.href = _href;
        }
    }

    private function prevPage():void{
      pageIsSelected > 1? pageIsSelected--: pageIsSelected = 1;
    }
    private function nextPage():void{
      pageIsSelected < pagesNum? pageIsSelected++: pageIsSelected = pagesNum;
    }
    private function enableOrDisable():void{
        pageIsSelected == 1? prev.classList.add("is-disabled"): prev.classList.remove("is-disabled");
        pageIsSelected == pagesNum? next.classList.add("is-disabled"): next.classList.remove("is-disabled");
    }
    
    private var _pageIsSelected:Number;

    public function get pageIsSelected():Number
    {
    	return _pageIsSelected;
    }

    public function set pageIsSelected(val:Number):void
    {
      if(val && val <= pagesNum){
      	_pageIsSelected = val;
      }
      enableOrDisable();
      input.value = "" + _pageIsSelected;
    }
    private var _pagesNum:int;

    public function get pagesNum():int{
    	return _pagesNum;
    }

    public function set pagesNum(val:int):void
    {
        if(val != !!_pagesNum){
        	_pagesNum = val;
        }
      enableOrDisable();
      span.text = "  of  " + _pagesNum + "  pages";
    }

    private function changeValue():void{
      COMPILE::JS{
        if(Number(input.value) > pagesNum){
          input.value = "" + pagesNum;
        }
        if(Number(input.value) < 0){
          input.value = "1";
        }
        pageIsSelected = Number(input.value);
      }
    }
  }
}