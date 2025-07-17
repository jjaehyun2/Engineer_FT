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

import net.yoshiweb.display.graphics.Pattern;
/**
* MangaPatterns
*
* @description	wwwusic.net（スリーダブリュージック）さんで公開されている『モノクロ印刷風 Photoshop パターン素材 - wwwusic MANGA ScreenTone [ wwwusic.net ] 』を Flashで使えるように再現しました。
* @see        	http://wwwusic.net/design/2007/12/wwwusic_manga_screentone.php
*
* @author     	Takano Yoshihiro
* @since		Flash Player 8 (ActionScript 2.0)
* @version		0.20080115
*/
class net.yoshiweb.display.graphics.MangaPatterns {
	private var CLASS_NAME:String = "[net.yoshiweb.display.graphics.MangaPatterns]";
	//
	//コンストラクタ
	private function MangaPatterns() {
	}
	/////////////////////////////////////////////////////////////////
	// public
	/////////////////////////////////////////////////////////////////
	/**
	* ARARE（あられ）
	* @description	黒い点と若干灰色掛かった点の集合パターンです。
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("arare_mc", this.getNextHighestDepth());
	*	mc._x = 0;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.arare(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function arare(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 1, 0, 0, 0];
		tileArray[1] = [1, 1, 0, 0, 0];
		tileArray[2] = [0, 0, 3, 2, 3];
		tileArray[3] = [0, 0, 2, 1, 2];
		tileArray[4] = [0, 0, 3, 2, 3];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		argbArray[2] = getARGB(rgb, alpha * 0.6);	// ARGB
		argbArray[3] = getARGB(rgb, alpha * 0.2);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* KOISHI（小石）
	* @description	大きい黒い点と小さい黒い点の集合パターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("koishi_mc", this.getNextHighestDepth());
	*	mc._x = 50;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.koishi(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function koishi(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 1, 0, 0, 0];
		tileArray[1] = [1, 1, 0, 0, 0];
		tileArray[2] = [0, 0, 0, 0, 0];
		tileArray[3] = [0, 0, 0, 1, 0];
		tileArray[4] = [0, 0, 0, 0, 0];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* TENUGUI（手拭）
	* @description	生地の織りが細かいようなパターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("tenugui_mc", this.getNextHighestDepth());
	*	mc._x = 100;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.tenugui(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function tenugui(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 2];
		tileArray[1] = [2, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		argbArray[2] = getARGB(rgb, alpha * 0.2);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* FUROSHIKI（風呂敷）
	* @description	均等に織られた柄のパターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("furoshiki_mc", this.getNextHighestDepth());
	*	mc._x = 150;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.furoshiki(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function furoshiki(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [1, 1, 2, 2];
		tileArray[1] = [1, 1, 2, 2];
		tileArray[2] = [2, 2, 1, 1];
		tileArray[3] = [2, 2, 1, 1];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		argbArray[2] = getARGB(rgb, alpha * 0.2);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* KAZARI（錺り）
	* @description	細かい飾り縫いをしたようなパターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("kazari_mc", this.getNextHighestDepth());
	*	mc._x = 200;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.kazari(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function kazari(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [0, 0, 0, 0, 0];
		tileArray[1] = [0, 0, 1, 0, 0];
		tileArray[2] = [0, 1, 1, 1, 0];
		tileArray[3] = [0, 0, 1, 0, 0];
		tileArray[4] = [0, 0, 0, 0, 0];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* SHINBUN（新聞）
	* @description	写真を白黒印刷したときのようなパターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("shinbun_mc", this.getNextHighestDepth());
	*	mc._x = 250;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.shinbun(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function shinbun(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [2, 1, 2, 0, 0, 0];
		tileArray[1] = [1, 1, 1, 0, 0, 0];
		tileArray[2] = [2, 1, 2, 0, 0, 0];
		tileArray[3] = [0, 0, 0, 2, 1, 2];
		tileArray[4] = [0, 0, 0, 1, 1, 1];
		tileArray[5] = [0, 0, 0, 2, 1, 2];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha);			// ARGB
		argbArray[2] = getARGB(rgb, alpha * 0.2);	// ARGB
		//
		Pattern.custom(mc, width, height, tileArray, argbArray);
	}
	/**
	* SEBIRO（背広）
	* @description	微妙な色合いを演出するパターン
	* @usage
	*	<code>
	*	import net.yoshiweb.display.graphics.MangaPatterns;
	*	//
	*	// 適用先、サイズ、色、アルファを決めて
	*	var mc:MovieClip = this.createEmptyMovieClip("sebiro_mc", this.getNextHighestDepth());
	*	mc._x = 300;
	*	var width:Number = 50;
	*	var height:Number = 50;
	*	var rgb:Number = 0x000000;
	*	var alpha:Number = 100;
	*	//
	*	// 実行
	*	MangaPatterns.sebiro(mc, width, height, rgb, alpha);
	*	</code>
	*/
	public static function sebiro(mc:MovieClip, width:Number, height:Number, rgb:Number, alpha:Number) {
		// タイル状のパターン２次元配列を作成
		var tileArray:Array = new Array();
		tileArray[0] = [2, 2, 2, 0, 0, 0];
		tileArray[1] = [2, 1, 2, 0, 0, 0];
		tileArray[2] = [2, 2, 2, 0, 0, 0];
		tileArray[3] = [0, 0, 0, 2, 2, 2];
		tileArray[4] = [0, 0, 0, 2, 1, 2];
		tileArray[5] = [0, 0, 0, 2, 2, 2];
		//
		// 各ピクセルを塗りつぶす色を配列で指定
		var argbArray:Array = new Array();
		argbArray[0] = 0x00;						// 透過
		argbArray[1] = getARGB(rgb, alpha * 0.4);	// ARGB
		argbArray[2] = getARGB(rgb, alpha * 0.2);	// ARGB
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