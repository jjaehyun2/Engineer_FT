/*
* Copyright(c) 2007 yoshiweb.NET
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

/**
* Player クラス
*
* @description	プラグインのバージョンチェックなど、再生しているPlayerを調べるクラス。
*
* @author		Takano Yoshihiro
* @version		0.20070216
*
* @history
* 20070216 - isPreview() → isMoviePreview() へ改名
* 20061114 - isPreview() 追加
* 20060406 - SystemUtils クラスから独立。
* 20060402 - isVersion() マイナーバージョンにも対応
* 20060329 - isVersion() 作成
*/
class net.yoshiweb.utils.system.Player {
	private var CLASS_NAME:String = "[Player]";
	//
	//コンストラクタ
	private function Player() {
	}
	/**
	* プレーヤーのバージョンチェック
	* @param	調べたいプレーヤーのバージョン
	* @return	指定したバージョンよりも新しかったら true それ以外は false
	* @usage	
	*	<code>
	*	// プレーヤーがバージョン8.5以上か調べる
	*	import net.yoshiweb.utils.system.Player;
	*	Player.isVersion(8, 5);
	*	</code>
	* @since	Flash Player 6 (ActionScript 2.0)
	*/
	public static function isVersion():Boolean {
		var tbl:Array = getVersion().split(" ")[1].split(",");
		var len:Number = arguments.length;
		for (var i:Number = 0; i<len; i++) {
			var ver = Number(tbl[i]);
			var arg = arguments[i];
			if (ver>arg) {
				return true;
			} else if (ver<arg) {
				return false;
			}
		}
		return true;
	}
	/**
	* ムービープレビュー用プレーヤーか判別
	* @return	ムービープレビュー用プレーヤーの場合は true それ以外は false
	* @since	Flash Player 7 (ActionScript 2.0)
	*/
	public static function isMoviePreview():Boolean {
		return (System.capabilities.playerType == "External") && System.capabilities.isDebugger;
	}
	//--------------------------------------------------------
	private function toString():String {
		return CLASS_NAME;
	}
	//--------------------------------------------------------
}