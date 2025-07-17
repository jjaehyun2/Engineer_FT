import templateList.mvcgallery.*
import templateList.mvc.AbstractView
import mx.events.EventDispatcher

class templateList.mvcgallery.PortionComponentsView extends AbstractView {
	var __page_length:Number;	////length portion
	var __viev_length:Number = 5;	////length
	var __linkage:String = "_number";	////linkage library
	var arrow_right:MovieClip;	/////arrow rights
	var arrow_left:MovieClip;	////arrow left
	var __spaceArrow:Number=12  ///space arrow
	var __space_x:Number = 0;	///space
	var content:MovieClip;
	var __current:Number ///current number
	var __array:Array;
	////color text
	var __color_normal = "0xFFFFFF";
	var __color_rol = "0xFF0000";
	/////color background ////
	var __colorBackgroundNormal = "0x000000";
	var __colorBackgroundRol = "0xFFFFFF";
	//color separator
	var __colorSep="0x2F2F2F";

	function PortionComponentsView() {
	EventDispatcher.initialize(this)
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////

	function addEventListener(){}
	function removeListener(){}
	function dispatchEvent(){}
	
////////////////////////////////////////////////////////////////////////////////////////////////
	
	function shov(){
		this.content._visible=true
		arrow_right._visible=true
		this.arrow_left._visible=true
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////

	function hide(){
		this.content._visible=false
		arrow_right._visible=false
		this.arrow_left._visible=false
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////
	
	function set setPageLength(f){
	__page_length=f
	if(this.__page_length==1){
		hide()
	}else{
		this.shov()
	}
	if(__page_length<__viev_length){
		__viev_length=__page_length
	}
	}

//////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function selectedIndex(current,pres){
		if(this.__page_length>1){
		create_cyfry(current,pres)
		}
	}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function create_cyfry(current, pres:Boolean) {
		__current = current;
		this.createEmptyMovieClip("content", 1);
		var ost;
		var i;
		var count = 0;
		///////////////////////////////////////////////////////////position first und old number
		i = __current-(Math.floor(__viev_length/2));
		var odds=this.__page_length-this.__viev_length
		if(i<1){
			i=1
		}else if(i>odds){
			i=odds+1
		}

///////////////////////////////////////////////////////////////////////////////////////////////////////

		__array=[]
		while (count<__viev_length) {
			var p = content.getNextHighestDepth();
			var c = content.attachMovie(this.__linkage, this.__linkage+p, p);
			__array.push(c)
			////color background
			c.t.stopTween();
			c.background.stopTween();
			var k = new Color(c.background);
			k.setRGB((i == __current) ? __colorBackgroundRol : __colorBackgroundNormal);
			/////
			c.blokada = (i == __current) ? 1 : 0;
			c.__this = this;
			c.i = i;
			c.t.autoSize = true;
			
			if (i<=0) {
				////number<1
				c.t.text = 0;
				c.t._visible = false;
				c.background.colorTo(__colorBackgroundNormal, .3);
				c.enabled = false;
			} else if (i>__page_length) {
				c.t.text = __page_length;
				c.t._visible = false;
				c.background.colorTo(__colorBackgroundNormal, .3);
				c.enabled = false;
			} else {
				c.t.text = i;
				
			}
			c.background._width = c.t._width+c.t._x*2;
			c.background._height = c.t._height;
			c._x = (!ost) ? 0 : ost.getBounds(ost._parent).xMax+__space_x;

			///separator
			if(count<__viev_length-1&&i>0&&i<__page_length){
			c.lineStyle(2,__colorSep,100)
			c.moveTo(c._width,4)
			c.lineTo(c._width,14)
			}
			////
			c.t.textColor = (i == __current) ? __color_rol : __color_normal;
			///
			c.onPress = function() {
				this.__this.selectedIndex(this.i,true);
			};
			c.onRollOver = function() {
				if (!this.blokada) {
					this.t.colorTo(this.__this.__color_rol, .3);
					this.background.colorTo(this.__this.__colorBackgroundRol, .3);
				}
			};
			c.onRollOut = function() {
				if (!this.blokada) {
					this.t.colorTo(this.__this.__color_normal, .3);
					this.background.colorTo(this.__this.__colorBackgroundNormal, .3);
				}
			};

			ost = c;
			i++;
			count++;
		}
		
		///////
		if(this.__page_length>this.__viev_length){
		var mc=__array[Math.floor(__viev_length/2)]
		content._x = -mc.getBounds(this).xMax+mc._width/2
		}else{
		content._x=-content._width/2				
		}
		/////
		arrowR();
		arrowL();
		//////////
		if(pres==true){
		dispatchEvent({target:this,type:"onChanged"})
        }
	}

	
////////////////////////////////////////////////////////////////////////////////////////////////////////////	
	
	function arrowR() {
		this.attachMovie("button_next", "arrow_right", 54);
		arrow_right._x = int(content.getBounds(this).xMax+__spaceArrow)
	    var __this = this;
		arrow_right.onPress = function() {
			__this.selectedIndex(__this.__current+1,true);
		};
		arrow_right.enabled = (__current == __page_length) ? false : true;
	}
	
///////////////////////////////////////////////////////////////////////////////////////////////////


	function arrowL() {
		this.attachMovie("button_prev", "arrow_left", 50);
		arrow_left._x=int(content._x-arrow_left._width-__spaceArrow)
		var __this = this;
		arrow_left.onPress = function() {
			__this.selectedIndex(__this.__current-1,true);
		};
	
		arrow_left.enabled = (__current == 1) ? false : true;
	}
	
	
	
/////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	
	
	
}