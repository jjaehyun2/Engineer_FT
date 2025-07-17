/*
 * Licensed under the MIT License
 *
 * Copyright(c) yoshiweb.NET
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

package net.yoshiweb.utils.system
{
	import flash.system.Capabilities;
	/**
	 * PlayerCheck クラス
	 * 
	 * @description	Flash Player のバージョンチェックなどをするクラス
	 * @usage		
	 * 	<code>
	 * 	</code>
	 * @author		Takano Yoshihiro
	 * @version		0.20081127
	 */

	public class PlayerCheck
	{
		// コンストラクタ
		public function PlayerCheck()
		{
		}
		////////////////////////////////////////////////////////////////////
		// public
		////////////////////////////////////////////////////////////////////
		/**
		 * プレーヤーのバージョンチェック
		 * @param	majors		メジャーバージョン	※ 必須
		 * @param	minor		マイナーバージョン	※ デフォルト値：0
		 * @param	bugfix		バグフィックス		※ デフォルト値：0
		 * @param	buildnumber	ビルド番号			※ デフォルト値：0
 		 * @return	指定したバージョンよりも新しかったら true それ以外は false
		 * @usage	
		 *	<code>
		 *	// プレーヤーがバージョン 9,0,115,0 以上か調べる
		 *	import net.yoshiweb.utils.system.PlayerCheck;
		 *	PlayerCheck.isVersion(9, 0, 115, 0);
		 *	</code>
		 * @see		http://weblogs.macromedia.com/akamijo/archives/2008/10/flash_player_10_10.html
		 */
		public static function isVersion(majors:int, minor:int = 0, bugfix:int = 0, buildnumber:int = 0):Boolean
		{
			// Flash Playerのバージョンを取得
			var str:String = Capabilities.version;
			var tbl:Array = str.split(" ")[1].split(",");

			//　調べたいベージョンを配列に格納
			var args:Array = new Array();
			args.push(majors);
			args.push(minor);
			args.push(bugfix);
			args.push(buildnumber);
			
			var len:Number = args.length;
			for (var i:Number = 0; i<len; i++) {
				var ver:Number = Number(tbl[i]);
				var num:Number = Number(args[i]);
				if (ver > num) {
					return true;
				} else if (ver < num) {
					return false;
				}
			}
			return true;
		}
		/**
		 * ムービープレビュー用プレーヤーか判別
		 * @return	ムービープレビュー用プレーヤーの場合は true それ以外は false
		 */
		public static function isMoviePreview():Boolean
		{
			return (Capabilities.playerType == "External") && Capabilities.isDebugger;
		}
	}
}