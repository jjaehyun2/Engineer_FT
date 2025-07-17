/*
* Copyright(c) 2008 wwwusic.net
* Copyright(c) 2008 yoshiweb.NET
* 
* Permission is hereby granted, free of charge, to any person obtaining a copy
* of this software and associated documentation files (the "Software"), to deal
* in the Software without restriction, including without limitation the rights
* to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
* copies of the Software, and to permit persons to whom the Software is
* furnished to do so, subject to the following conditions:
* 
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
* 
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
* OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
* THE SOFTWARE.
* 
* The MIT License
* http://www.opensource.org/licenses/mit-license.php
*/

import net.yoshiweb.display.graphics.Pattern
/**
* SimplePatterns
*
* @description	wwwusic.net（スリーダブリュージック）さんで公開されている『シンプルで使える！Photoshop パターン素材 - wwwusic Simple Patterns [ wwwusic.net ] 』を Flashで使えるように再現しました。
* @see          http://wwwusic.net/design/2007/12/wwwusic_simple_patterns.php
*
* @author       Takano Yoshihiro
* @since		Flash Player 8 (ActionScript 2.0)
* @version		0.20080115
*/
class net.yoshiweb.display.graphics.SimplePatterns {
	private var CLASS_NAME:String = "[net.yoshiweb.display.graphics.SimplePatterns]";
	//
	//コンストラクタ
	private function SimplePatterns() {
	}
	/////////////////////////////////////////////////////////////////
	// public
	/////////////////////////////////////////////////////////////////
	/**
	* Slanted Line(A)
	* @description	右上から左下への斜線
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("slanted_line_a_mc", this.getNextHighestDepth());
	*	mc._x = 0;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.slantedLineA(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function slantedLineA(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 1, 0];
		tileArray[1] = [1, 0, 0];
		tileArray[2] = [0, 0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Slanted Line(B)
	* @description	左上から右下への斜線
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("slanted_line_b_mc", this.getNextHighestDepth());
	*	mc._x = 50;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.slantedLineB(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function slantedLineB(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 0, 0];
		tileArray[1] = [0, 1, 0];
		tileArray[2] = [0, 0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Solid Bar
	* @description	縦線
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("solid_bar_mc", this.getNextHighestDepth());
	*	mc._x = 100;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.solidBar(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function solidBar(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Solid Horizonal
	* @description	横線
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("solid_horizonal_mc", this.getNextHighestDepth());
	*	mc._x = 150;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.solidHorizonal(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function solidHorizonal(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0];
		tileArray[1] = [1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Solid Bold
	* @description	右上から左下への斜線（太）
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("solid_bold_mc", this.getNextHighestDepth());
	*	mc._x = 200;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.solidBold(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function solidBold(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 0, 0, 0, 1, 1, 1, 1, 1, 0];
		tileArray[1] = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0];
		tileArray[2] = [0, 0, 1, 1, 1, 1, 1, 0, 0, 0];
		tileArray[3] = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0];
		tileArray[4] = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0];
		tileArray[5] = [1, 1, 1, 1, 0, 0, 0, 0, 0, 1];
		tileArray[6] = [1, 1, 1, 0, 0, 0, 0, 0, 1, 1];
		tileArray[7] = [1, 1, 0, 0, 0, 0, 0, 1, 1, 1];
		tileArray[8] = [1, 0, 0, 0, 0, 0, 1, 1, 1, 1];
		tileArray[9] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Spot
	* @description	斑点柄
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("spot_mc", this.getNextHighestDepth());
	*	mc._x = 250;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.spot(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function spot(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 0, 0, 0];
		tileArray[1] = [0, 1, 0, 0];
		tileArray[2] = [0, 0, 0, 0];
		tileArray[3] = [0, 0, 0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Lattice
	* @description	格子柄（狭）
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("lattice_mc", this.getNextHighestDepth());
	*	mc._x = 300;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.lattice(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function lattice(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 1];
		tileArray[1] = [1, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;		// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Lattice Wide
	* @description	格子柄（広）
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("lattice_wide_mc", this.getNextHighestDepth());
	*	mc._x = 350;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.latticeWide(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function latticeWide(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 0, 0, 0, 1];
		tileArray[1] = [0, 0, 0, 0, 1];
		tileArray[2] = [0, 0, 0, 0, 1];
		tileArray[3] = [0, 0, 0, 0, 1];
		tileArray[4] = [1, 1, 1, 1, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* Lozenge
	* @description	菱形柄
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("lozenge_mc", this.getNextHighestDepth());
	*	mc._x = 400;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.lozenge(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function lozenge(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 0, 1, 0];
		tileArray[1] = [0, 1, 0, 1];
		tileArray[2] = [1, 0, 0, 0];
		tileArray[3] = [0, 1, 0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* X
	* @description	X柄
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.SimplePatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("x_mc", this.getNextHighestDepth());
	*	mc._x = 450;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	SimplePatterns.x(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function x(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1];
		tileArray[1] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0];
		tileArray[2] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0];
		tileArray[3] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0];
		tileArray[4] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0];
		tileArray[5] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0];
		tileArray[6] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0];
		tileArray[7] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0];
		tileArray[8] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0];
		tileArray[9] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;				// 透過
		argbArray[1] = getARGB(rgb, alpha);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/////////////////////////////////////////////////////////////////
	// private
	/////////////////////////////////////////////////////////////////
	/**
	* ARGB値を求める
	* @usage
	*	<code>
	* 	// 例：0xff0000 の アルファ 50%の ARGB値を求める
	*	var argb:Number = getARGB(0xff0000, 50);
	*	</code>
	*/
	private static function getARGB (rgb:Number, alpha:Number) {
		var a:Number = Math.floor(255*alpha/100);
		var str:String = a.toString(16);
		var num:Number = parseInt(str, 16);
		return (num * 256 * 256 * 256) + rgb;
	}
	/////////////////////////////////////////////////////////////////
	private function toString():String {
		return CLASS_NAME;
	}
}