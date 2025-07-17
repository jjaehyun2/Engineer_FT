/**
 * ...
 * @author Landaes
 */
import com.greensock.*;
import com.greensock.easing.*;
class landaes.Scroll extends MovieClip
{
	private var distancia:Number;
	private var tiempo:Number;
	public function Scroll() {
		
	}
	
	public function setMoviesAA(scr:Scroll, c:MovieClip, m:MovieClip, bArr:MovieClip, bAba:MovieClip,colorOver:Number, dist:Number, t:Number) {
		if (isNaN(colorOver)) {
			colorOver = 0xFFFFFF;
		}
		if (isNaN(dist)) {
			dist = 50;
		}
		if (isNaN(t)) {
			t = 0.4;
		}
		bArr.onRollOver = function () {
			scr.overGlow(bArr,colorOver);
		}
		bArr.onRollOut = function () {
			scr.outGlow(bArr,colorOver);
		}
		
		bArr.onRelease = function () {
			scr.upScroll(scr,c, m, bArr, bAba, dist, t);
		}
		bAba.onRollOver = function () {
			scr.overGlow(bAba,colorOver);
		}
		bAba.onRollOut = function () {
			scr.outGlow(bAba,colorOver);
		}
		
		bAba.onRelease = function () {
			scr.downScroll(scr,c, m, bArr, bAba, dist, t);
		}
	}
	public function setMoviesLR(scr:Scroll, c:MovieClip, m:MovieClip, bl:MovieClip, br:MovieClip, colorOver:Number, dist:Number, t:Number) {
		if (isNaN(colorOver)) {
			colorOver = 0xFFFFFF;
		}
		if (isNaN(dist)) {
			dist = 50;
		}
		if (isNaN(t)) {
			t = 0.4;
		}
		bl.onRollOver = function () {
			scr.overGlow(bl,colorOver);
		}
		bl.onRollOut = function () {
			scr.outGlow(bl,colorOver);
		}
		
		bl.onRelease = function () {
			scr.lScroll(scr,c, m, bl, br, dist, t);
		}
		br.onRollOver = function () {
			scr.overGlow(br,colorOver);
		}
		br.onRollOut = function () {
			scr.outGlow(br,colorOver);
		}
		
		br.onRelease = function () {
			scr.rScroll(scr,c, m, bl, br,  dist, t);
		}
	}
	public function upScroll(scr:Scroll, c:MovieClip, m:MovieClip, bArr:MovieClip, bAba:MovieClip, dist:Number, t:Number) {
		disable(bArr);
		disable(bAba);
		outGlow(bArr);
		outGlow(bAba);
		new TweenMax(c,t,{_y:c._y - dist, onComplete:checkScrollUP, onCompleteParams:[scr,c,m,bArr,bAba]});
	}

	private function checkScrollUP(scr:Scroll,c:MovieClip,m:MovieClip,bArr:MovieClip,bAba:MovieClip) {
		//trace(c._y);
		//trace(m._y);
		if (c._y + c._height <= m._y + m._height) {
			new TweenMax(c,0.2,{_y:m._y + m._height-c._height});
			scr.disable(bArr);
			scr.enable(bAba);
		} else {
			scr.enable(bArr);
			scr.enable(bAba);
		}

	}

	public function downScroll(scr:Scroll,c:MovieClip,m:MovieClip,bArr:MovieClip,bAba:MovieClip,dist:Number,t:Number) {
		disable(bArr);
		disable(bAba);
		outGlow(bArr);
		outGlow(bAba);
		new TweenMax(c,t,{_y:c._y + dist, onComplete:checkScrollDOWN, onCompleteParams:[scr,c,m,bArr,bAba]});
	}

	private function checkScrollDOWN(scr:Scroll,c:MovieClip,m:MovieClip,bArr:MovieClip,bAba:MovieClip) {
		//trace(c._y + c._height);
		//trace(m._y + m._height);
		if (c._y >= m._y) {
			new TweenMax(c,0.2,{_y:m._y});
			scr.enable(bArr);
			scr.disable(bAba);
		} else {
			scr.enable(bArr);
			scr.enable(bAba);
		}
	}

	public function lScroll(scr:Scroll,c:MovieClip,m:MovieClip,bL:MovieClip,bR:MovieClip,dist:Number,t:Number) {
		
		disable(bL);
		disable(bR);
		outGlow(bL);
		outGlow(bR);
		new TweenMax(c,t,{_x:c._x - dist, onComplete:checkScrollL, onCompleteParams:[scr,c,m,bL,bR]});
	}

	private function checkScrollL(scr:Scroll,c:MovieClip,m:MovieClip,bL:MovieClip,bR:MovieClip) {
		//trace(c._x);
		//trace(m._x);
		if (c._x + c._width <= m._x + m._width) {
			new TweenMax(c,0.2,{_x:m._x + m._width-c._width});
			scr.disable(bL);
			scr.enable(bR);
		} else {
			scr.enable(bL);
			scr.enable(bR);
		}

	}

	public function rScroll(scr:Scroll,c:MovieClip,m:MovieClip,bL:MovieClip,bR:MovieClip,dist:Number,t:Number) {
		
		disable(bL);
		disable(bR);
		outGlow(bL);
		outGlow(bR);
		new TweenMax(c,t,{_x:c._x + dist, onComplete:checkScrollR, onCompleteParams:[scr,c,m,bL,bR]});
	}

	private function checkScrollR(scr:Scroll,c:MovieClip,m:MovieClip,bL:MovieClip,bR:MovieClip) {
		//trace(c._x + c._width);
		//trace(m._x + m._width);
		if (c._x >= m._x) {
			new TweenMax(c,0.2,{_x:m._x});
			scr.enable(bL);
			scr.disable(bR);
		} else {
			scr.enable(bL);
			scr.enable(bR);
		}
	}
	
	public function overGlow(mc:MovieClip,colorOver:Number) {
		new TweenMax(mc,0.2,{glowFilter:{color:colorOver, alpha:0.7, blurX:10, blurY:10, strength:2}});
	}
	public function outGlow(mc:MovieClip,colorOver:Number) {
		new TweenMax(mc,0.2,{glowFilter:{color:colorOver, alpha:0, blurX:0, blurY:0}});
	}
	
	public function disable(mc:MovieClip) {
		mc._alpha = 50;
		mc.enabled = false;
	}
	public function enable(mc:MovieClip) {
		mc._alpha = 100;
		mc.enabled = true;
	}
	
}