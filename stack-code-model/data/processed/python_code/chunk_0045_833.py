﻿import caurina.transitions.*;
import ascb.util.Proxy;
import agung.utils.UMc;
import agung.utils.UTf;
import agung.utils.UNode;
import agung.utils.UAddr;
import asual.sa.SWFAddress;

class agung.tech01.materi.projectDescription extends MovieClip
{
	private var mainSettings:Object;
	private var settingsObj:Object;
	public var node:XMLNode;
	
	
	private var HitZone:MovieClip;
	private var ScrollArea:MovieClip;
	private var ScrollButton:MovieClip;
	private var ContentMask:MovieClip;
	private var Content:MovieClip;
	private var viewHeight:Number;
	private var totalHeight:Number;
	private var ScrollHeight:Number;
	private var scrollable:Boolean;
	
	public var holder:MovieClip;
		private var lst:MovieClip;
		private var mask:MovieClip;
		public var scroller:MovieClip;
			private var stick:MovieClip;
			private var bar:MovieClip;
			
	
	private var scanImageIdx:Number = 0;
	private var lstHeight:Number = 0;

	private var addedToThumbWidth:Number = 11 + 11;
	private var addedToThumbHeight:Number = 11 + 11;
	
	private var myInterval:Number;
	
	public function projectDescription() {
		this._visible = false;

		lst = holder["lst"];
		mask = holder["mask"];
		scroller = holder["scroller"];
		scroller._alpha = 0
		stick = scroller["stick"];
		bar = scroller["bar"];
		
		UTf.initTextArea(lst["txt"], true);
		lst.setMask(mask);
	}
	
	
	public function setNode(pNode:XMLNode, pMainSettings:Object){
		node = pNode;
		mainSettings = pMainSettings;
	
		node = node.firstChild;
		
		
		settingsObj = UNode.nodeToObj(node);
		

		var scrlWidth:Number = Math.round((settingsObj.thumbWidth + addedToThumbWidth) * settingsObj.horizontalNumberOfItems + settingsObj.horizontalSpace * (settingsObj.horizontalNumberOfItems - 1));
		
		this._x = scrlWidth + 20;
		
		mask._width = Math.ceil(mainSettings.moduleWidth - scrlWidth) - 22 - 12 - 60;
		mask._height = Math.ceil(mainSettings.moduleHeight);
		
		stick._height = mask._height;
		
		scroller._x = Math.round(mask._width + 8);
		
		lst["txt"]._width = Math.ceil(mask._width);
		lst["txt"].text = "";
		
		myInterval = setInterval(this, "startHandle", 1000);
		
		this._visible = true;
	}

	private function startHandle() {
		lst["txt"].htmlText = node.nextSibling.nextSibling.firstChild.nodeValue;
	
		this.onEnterFrame = Proxy.create(this, cc);
		
		this._alpha = 100;
		
		clearInterval(myInterval);
		
		treatAddress();
	}
	
	public function treatAddress() {
		var str:String = UAddr.contract(SWFAddress.getValue());
		var strArray:Array = str.split("/");
		
		if (strArray[4]) {
			disableMouseListener()
		}
		else {
			enableMouseListener()
		}
	}

	private function cc() {
		if (scanImageIdx == 100) {
			delete this.onEnterFrame;
		}
		else {
			if (lstHeight != lst._height) {
				lstHeight = lst._height;
				ScrollBox();
			}
		}
		
		scanImageIdx++;
	}
	
	public function disableMouseListener() {
		Mouse.removeListener(this);
	}
	
	public function enableMouseListener() {
		Mouse.addListener(this);
	}
	
	
	private function ScrollBox() {
		ScrollArea = stick;
		ScrollButton = bar;
		Content = lst;
		ContentMask = mask;
		
		HitZone = ContentMask.duplicateMovieClip("_hitzone_", this.getNextHighestDepth());
		HitZone._alpha = 0;
		HitZone._width = ContentMask._width;
		HitZone._height = ContentMask._height;
		
		Content.setMask(ContentMask);
		ScrollArea.onPress = Proxy.create(this, startScroll);
		ScrollArea.onRelease = ScrollArea.onReleaseOutside = Proxy.create(this, stopScroll);
		
		totalHeight = Content._height + 4;
		scrollable = false;
		
		updateScrollbar();
		
		
		
		ScrollButton.onRollOver = Proxy.create(this, barOnRollOver);
		ScrollButton.onRollOut = Proxy.create(this, barOnRollOut);
		ScrollButton.onPress = Proxy.create(this, startScroll);
		ScrollButton.onRelease = ScrollButton.onReleaseOutside = Proxy.create(this, stopScroll);
		
		barOnRollOut();
	}
	
	private function updateScrollbar() {
		viewHeight = ContentMask._height;
		
		var prop:Number = viewHeight/(totalHeight-4);
		
		if (prop >= 1) {
			scrollable = false;
			scroller._alpha = 0
			ScrollArea.enabled = false;
			ScrollButton._y = 0;
			Content._y = 0;
			scroller._visible = false;
		} else {
			ScrollButton._height = ScrollArea._height * prop;
			scrollable = true;
			ScrollButton._visible = true;
			ScrollArea.enabled = true;
			ScrollButton._y = 0;
			scroller._alpha = 100
			ScrollHeight = ScrollArea._height - ScrollButton._height;
			
			if(ScrollButton._height>(ScrollArea._height)){
				scrollable = false;
				scroller._alpha = 0
				ScrollArea.enabled = false;
				ScrollButton._y = 0;
				Content._y = 0;
			}
			
			scroller._alpha = 100;
			scroller._visible = true;
		}
	}
	
	private function startScroll() {
		var center:Boolean = !ScrollButton.hitTest(_level0._xmouse, _level0._ymouse, true);
		var sbx:Number = ScrollButton._x;
		if (center) {
			var sby:Number = ScrollButton._parent._ymouse-ScrollButton._height/2;
			sby<0 ? sby=0 : (sby>ScrollHeight ? sby=ScrollHeight : null);
			ScrollButton._y = sby;
		}

			
		ScrollButton.startDrag(false, sbx, 0, sbx, ScrollHeight);
		ScrollButton.onMouseMove = Proxy.create(this, updateContentPosition);
		updateContentPosition();
	}
	
	private function stopScroll() {
		ScrollButton.stopDrag();
		delete ScrollButton.onMouseMove;
		barOnRollOut();

	}
	
	private function updateContentPosition() {
		if (scrollable == true) {
			var contentPos:Number = (viewHeight-totalHeight)*(ScrollButton._y/ScrollHeight);
		this.onEnterFrame = function() {
			if (Math.abs(Content._y-contentPos)<1) {
				Content._y = contentPos;
				delete this.onEnterFrame;
				return;
			}
			Content._y += (contentPos - Content._y) / 10;
		};
		}
		else{
			Content._y = 0;
			delete Content.onEnterFRame;
		}
		
	}
	
	private function scrollDown() {
		var sby:Number = ScrollButton._y+ScrollButton._height/4;
		if (sby>ScrollHeight) {
			sby = ScrollHeight;
		}
		ScrollButton._y = sby;
		updateContentPosition();
	}
	
	private function scrollUp() {
		var sby:Number = ScrollButton._y-ScrollButton._height/4;
		if (sby<0) {
			sby = 0;
		}
		ScrollButton._y = sby;
		updateContentPosition();
	}
	
	private function onMouseWheel(delt:Number) {
		if (!HitZone.hitTest(_level0._xmouse, _level0._ymouse, true)) {
			return;
		}
		var dir:Number = delt/Math.abs(delt);
		if (dir<0) {
			scrollDown();
		} else {
			scrollUp();
		}
	}
	
	private function barOnRollOver() {
		Tweener.addTween(bar["over"], { _alpha:100, time:0.15, transition:"linear" } );
	}
	
	private function barOnRollOut() {
		Tweener.addTween(bar["over"], { _alpha:0, time:0.15, transition:"linear" } );
	}
}