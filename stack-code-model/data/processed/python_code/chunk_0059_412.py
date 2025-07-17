﻿import caurina.transitions.*;
import ascb.util.Proxy;
import agung.utils.UMc;
import agung.utils.UTf;

/**
 * This class handles the scroller description
 */
class agung.tech01.tentang_orang.scrollerDescription extends MovieClip
{
	private var settingsObj:Object;
	public var node:XMLNode;
	
	private var theWidth:Number;
	
	private var holder:MovieClip;
		private var textHolder:MovieClip;
		private var mask:MovieClip;
	
	private var bg:MovieClip;
	
			
	private var textIdx:Number = 0;
	private var lastText:MovieClip;
	
	private var status:Number = 0;
	private var lastStr:XMLNode;
		
	private var yDefPos:Number;
	private var yOverPos:Number;
	
	private var myInterval:Number;
	
	private var newBgWidth:Number;
	private var newBgHeight:Number;
	
	private var tsSettings:Object
	
	public function scrollerDescription() {
		textHolder = holder["lst"];
		mask = holder["mask"];
	
		
		lastText = textHolder["a"];
		lastText["txt"].autoSize = true;
		textHolder._x = 12;
		holder._y = 4;
		this._alpha = 0;
		textHolder.setMask(mask);
	}
	
	

	public function hide() {
		Tweener.addTween(this, { _alpha:0, time:.2, transition:"easeOutQuad"} );
	}
	
	public function setSettings(pSettings:Object, ptsSettings:Object ) {
		settingsObj = pSettings;
		tsSettings = ptsSettings;
		
	}
	
	private function onMouseMove() {
		if (tsSettings.toggleTooltip == 1) {
			
			if (tsSettings.enableTooltipAutoCorrectX == 0) {
				var newX:Number = Math.ceil(this._parent._xmouse - newBgWidth + tsSettings.tooltipXCorrect);
			}
			else {
				var newX:Number = Math.ceil(this._parent._xmouse - newBgWidth/2 + tsSettings.tooltipXCorrect);
			}
			var newY:Number = Math.ceil(this._parent._ymouse - newBgHeight - tsSettings.tooltipYCorrect);
			Tweener.addTween(this, { _x:newX, _y:newY, time:.2, transition:"easeOutQuad" } );
		}
		
		
	}
	
	/**
	 * a new text will be set each time this function is calles externally
	 * @param	str
	 */
	public function setNewText(pNode:XMLNode) {
		if (tsSettings.toggleTooltip == 1) {
			pNode = pNode.firstChild.firstChild;
		
			Tweener.addTween(this, { _alpha:100, time:.2, transition:"easeOutQuad" } );

			Tweener.addTween(lastText, { _y:-mask._height -20, time:.3, transition:"easeOutQuad", onComplete:Proxy.create(this, removeLastText, lastText) } );
			
			textIdx++;
		
			lastText = textHolder["a"].duplicateMovieClip("textHolder" + textIdx, textIdx);
				
			lastText._y = mask._height + 10;
				
			UTf.initTextArea(lastText["txt"], true);
			
			lastText["txt"].htmlText = pNode.nodeValue;
			
			 newBgWidth = Math.ceil(lastText["txt"].textWidth + 30 + 12)
			 newBgHeight =  Math.ceil(16 + lastText["txt"].textHeight)
			 
			Tweener.addTween(bg, { _width:newBgWidth, _height:newBgHeight, time:.4, transition:"easeOutQuad" } );
		
			Tweener.addTween(mask, { _width:newBgWidth, _height:lastText["txt"].textHeight, time:.4, transition:"easeOutQuad" } );
			
			Tweener.addTween(lastText["txt"], { _width:newBgWidth - 30, _height:lastText["txt"].textHeight, time:.4, transition:"easeOutQuad" } );
				
			Tweener.addTween(lastText, { _y:-1, time:.4, transition:"easeOutQuad", rounded:true } );
			
			normalShow();
			
			lastStr = pNode;
		}
		
	}

	private function removeLastText(pLast:MovieClip) {
		pLast.removeMovieClip();
	}
	
	private function normalHide() {
		if (this._y != 0) {
			Tweener.addTween(this, { _alpha:0, _y:yDefPos, time:.5, transition:"easeOutQuart" } );
		}
	}
	
	private function normalShow() {
		if (this._y != -12) {
			Tweener.addTween(this, { _alpha:100, _y:yOverPos, time:.5, transition:"easeOutQuart" } );
		}
	}
}