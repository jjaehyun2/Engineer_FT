﻿import caurina.transitions.*;
import ascb.util.Proxy;
import agung.utils.UMc;
import agung.utils.UTf;

/**
 * This class handles the tooltip for the mp3 player, bottom cart and full screen button
 */
class agung.tech01.main_l.scrollerDescriptionGlobal extends MovieClip
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
	private var lastStr:String;
		
	private var yDefPos:Number;
	private var yOverPos:Number;
	
	private var myInterval:Number;
	
	private var newBgWidth:Number;
	private var newBgHeight:Number;
	
	private var tsSettings:Object
	
	public function scrollerDescriptionGlobal() {
		textHolder = holder["lst"];
		mask = holder["mask"];
	
		
		lastText = textHolder["a"];
		lastText["txt"].autoSize = true;
		textHolder._x = 6;
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
	
	private function onMouseMove(forced:Number) {
		if (tsSettings.toggleTooltip == 1) {
			this._visible = true;
			var newX:Number = Math.ceil(this._parent._xmouse - newBgWidth - Number(tsSettings.tooltipXCorrect) + 29);
			var newY:Number = Math.ceil(this._parent._ymouse - Number(tsSettings.tooltipYCorrect) - 27 - 4);
		
			if (forced == 1) {
				this._x = newX;
				this._y = newY;
			}
			else {
				Tweener.addTween(this, {_x:newX, _y: newY, time:.2, transition:"easeOutQuad" } );
			}
			
		}
		else {
			this._visible = false;
		}
		
		
	}
	
	/**
	 * a new text will be set
	 * @param	str
	 */
	public function setNewText(str:String) {
		if ((tsSettings.toggleTooltip == 1)&&(str!=lastStr)) {
			Tweener.addTween(this, { _alpha:100, time:.2, transition:"easeOutQuad" } );

			Tweener.addTween(lastText, { _y:-mask._height -20, time:.3, transition:"easeOutQuad", onComplete:Proxy.create(this, removeLastText, lastText) } );
			
			textIdx++;
		
			lastText = textHolder["a"].duplicateMovieClip("textHolder" + textIdx, textIdx);
				
			lastText._y = mask._height + 10;
				
			
			
			lastText["txt"].autoSize = true;
			lastText["txt"].wordWrap = false;
			lastText["txt"].text = str;
			
			if ((str != "") && (str != " ") && (str != undefined)) {
				newBgWidth = Math.ceil(lastText["txt"].textWidth + 20)
				newBgHeight = Math.ceil(16 + lastText["txt"].textHeight)
			}
			else {
				newBgWidth = 0
				newBgHeight = 0
				this._alpha = 0;
			}
			 
			Tweener.addTween(bg, { _width:newBgWidth, _height:newBgHeight, time:.4, transition:"easeOutQuad" } );
		
			Tweener.addTween(mask, { _width:newBgWidth, _height:lastText["txt"].textHeight, time:.4, transition:"easeOutQuad",onComplete:Proxy.create(this,onMouseMove)  } );
			
			Tweener.addTween(lastText["txt"], { _width:newBgWidth - 10, _height:lastText["txt"].textHeight, time:.4, transition:"easeOutQuad" } );
				
			Tweener.addTween(lastText, { _y:-1, time:.4, transition:"easeOutQuad", rounded:true } );
			
			if ((str != "") && (str != " ") && (str != undefined)) {
				normalShow();
			}
			else {
				normalHide()
			}
				
			lastStr = str;
		}
		else {
			if (tsSettings.toggleTooltip == 1) {
				normalShow();
			}
		}
		
	}
	
	
	
	
	
	
	public function setNewTextAdjusted(str:String) {
			Tweener.addTween(this, { _alpha:100, time:.2, transition:"easeOutQuad" } );
	
			lastText["txt"].autoSize = true;
			lastText["txt"].wordWrap = false;
			lastText["txt"].text = str;
			
		
			newBgWidth = Math.ceil(lastText["txt"].textWidth + 20)
			newBgHeight = Math.ceil(16 + lastText["txt"].textHeight)
			
			bg._width = newBgWidth;
			bg._height = newBgHeight;
			
			mask._width = newBgWidth;
			mask._height = lastText["txt"].textHeight;
			
			lastText["txt"]._width = newBgWidth - 10;
			lastText["txt"]._height = lastText["txt"].textHeight;

			normalShow();

			lastStr = undefined;
	}

	private function removeLastText(pLast:MovieClip) {
		pLast.removeMovieClip();
	}
	
	private function normalHide() {
		if (this._y != 0) {
			Mouse.removeListener(this);
			Tweener.addTween(this, { _alpha:0, _y:yDefPos, time:.5, transition:"easeOutQuad" } );
		}
	}
	
	private function normalShow() {
		if (this._y != -12) {
			if (this._alpha == 0) {
				onMouseMove(1);
			}
			Mouse.addListener(this);
			Tweener.addTween(this, { _alpha:100, _y:yOverPos, time:.5, transition:"easeOutQuad" } );
		}
	}
}