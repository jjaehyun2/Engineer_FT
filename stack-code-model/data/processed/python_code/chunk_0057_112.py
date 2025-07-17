import templateText.TextArea

class templateText.Scroll extends MovieClip {
  	var __scrollHeightNull:Boolean=false  
	var __drag:Number   
	var __last:Number      
	var __first:Number 
	var mc_scroll:MovieClip  
	var arrow_up:MovieClip 
	var arrow_down:MovieClip 
	var __v:Number=10
	var __onChange:Function
	var __height:Number=200 
	var background:MovieClip  
	var __proportion:Number  
	var __textArea:TextArea
	var spaceArrowY:Number=5
	//////////////////////////////////////color

	

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function Scroll(){
		
				
		this.mc_scroll.onPress=Delegate2.create(this,onPressScroll)
		this.mc_scroll.onRelease=this.mc_scroll.onReleaseOutside=Delegate2.create(this,onReleaseScroll)
		this.mc_scroll.onRollOver=Delegate2.create(this,this.onRollOverScroll)
		this.mc_scroll.onRollOut=Delegate2.create(this,this.onRollOutScroll)
		
		////////
		this.arrow_down.onPress=Delegate2.create(this,onPressScroll,"d")
		this.arrow_down.onRelease=this.arrow_down.onReleaseOutside=Delegate2.create(this,onReleaseScroll)
		///
		this.arrow_up.onPress=Delegate2.create(this,onPressScroll,"g")
		this.arrow_up.onRelease=this.arrow_up.onReleaseOutside=Delegate2.create(this,onReleaseScroll)
	
		
	}
	
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	function setColor(mc_,color_){
		var k:Color = new Color(mc_)
		
		//trace("set color scroll = "+color_)
		
		if(color_.length&&mc_){
		k.setRGB(color_)
		}
	}
	
	////////////////////////////////////////////////////
	
	function setColorScroll(color_:String) {
		if(color_.length){
		this.setColor(this.mc_scroll, color_)
		}
		
	}
	
	/////////////////////////////////////////////

	function setColorScrollBackground(color_) {
		if(color_.length){
		this.setColor(this.background, color_)
		}
		
	}
	
	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	function onReleaseScroll(){
		refresh()
		this.mc_scroll.stopDrag()
		delete this.onEnterFrame
      }
	
	////////////////////////////////////
	
	function onRollOverScroll(){
		
	}
	
	//////////////////////////////////////////////
	
	function onRollOutScroll(){
		
		
	}
	
	//////////////////////////////////////////////
	  
	function set limit(t:Array){
		__first=Number(t[0])
		__last=Number(t[1])
		proportion=Number(t[2])
	}

//////////////////////////////////////////////////////////////////////////

      function set proportion(f){
		__proportion=(f>1) ? 1 : f
		scrollHeight=Math.ceil(__drag*__proportion)
		size()
	}

//////////////////////////////////////////////////////////////////////////

      function set height(war:Number){
		__height=war
		size()
	}

//////////////////////////////////////////////////////////////////////////

      function set y(war:Number){
		this._y=war+arrow_up._height
		size()
	}

//////////////////////////////////////////////////////////////////////////

	 function set x(war:Number){
		this._x=war
		 size()
	}

//////////////////////////////////////////////////////////////////////////

	function set onChange(f:Function){
		__onChange=f
	}

//////////////////////////////////////////////////////////////////////////

	function get scrollHeight(){  ////zwraca wysokosc suwaka
		return (__scrollHeightNull==true) ? 0 : mc_scroll._height
	}
	
//////////////////////////////////////////////////////////////////////////


	function set scrollHeight(value){
		mc_scroll._height=value
	}

//////////////////////////////////////////////////////////////////////////

	function size(){
	    __drag=__height-(arrow_down._height+arrow_up._height+spaceArrowY*2)
		this.mc_scroll._y=0
		arrow_down._y=__drag+spaceArrowY
		arrow_up._y=-arrow_up._height-spaceArrowY
		__first=(__first==undefined) ? 0 : __first
		//background._width=mc_scroll._width
		background._height=__drag
		background.onPress=function(){}
		background.useHandCursor=false
	}
	

////////////////////////////////////////////////////////////////////////////////////

	function setScroll(war:Number){
		if(war>1){war=1}
		this.mc_scroll._y=war*(__drag-scrollHeight)
		
		refresh()
		

	}

////////////////////////////////////////////////////////////////////////////////////

	function setScrollPosition(value_,boolean_){
		var p=Math.min(__first,__last)
		var k=Math.max(__first,__last)
        value_=Math.max(p,Math.min(k,value_))
	    mc_scroll._y=( (value_-__first) * (__drag-scrollHeight) ) / (__last-__first)
		
		if(boolean_!=false){
	    refresh()
		}
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////////

	function getScrollPosition(){
	return Math.round(__first+( this.mc_scroll._y / (__drag-scrollHeight) )*(__last-__first))
	}
		
////////////////////////////////////////////////////////////////////////////////////

	function refresh(button:String):Void{    
		      var value_=getScrollPosition()
			__onChange(value_)
				if(button=="d"){ 
				var kon=this.mc_scroll._y+this.scrollHeight  //
				if(kon+__v>__drag) {this.mc_scroll._y=(__drag-this.scrollHeight)}
				else{this.mc_scroll._y+=__v}
				}
			else if(button=="g"){ 
				if(mc_scroll._y-__v<=0){mc_scroll._y=0}
				else{mc_scroll._y-=__v}
			}

	}

////////////////////////////////////////////////////////////////////////////////////

	function onPressScroll(button:String):Void{   //////
			if(button==undefined){this.mc_scroll.startDrag(false,0,0,0,(__drag-scrollHeight))}
		      this.onEnterFrame=Delegate2.create(this,refresh,button)
	}
	
////////////////////////////////////////////////////////////////////////////////////////////////////



}