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
* CharCodeクラス
*
* @description	文字列を扱うためのメソッドを持つクラスです。
* @usage		
*	<code>
*	</code>
* @author		Takano Yoshihiro
* @since		Flash Player 6 (ActionScript 2.0)
* @version		0.20060402
* @history
* 	20060402 - バグ修正
*	20060331 - 作成
*/
class net.yoshiweb.utils.string.CharCode {
	private var CLASS_NAME:String = "[CharCode]";
	/**
	* コンストラクタ
	*/
	private function CharCode() {
	}
	//------------------------------------------------------------
	/**
	* コードチェック
	* @param	str		文字列
	* @param	min		範囲小
	* @param	max		範囲大
	* @return			指定した範囲に文字が含まれていたら true、それ以外は false
	*/
	public static function isCode(str:String, min:Number, max:Number):Boolean {
		var len:Number = str.length;
		while (len--) {
			var num:Number = str.substr(len, 1).charCodeAt(0);
			if (num<min || num>max) {
				return false;
				break;
			}
		}
		return true;
	}
	/**
	* 文字が半角数字かどうかを調べる
	* @param	str		文字列
	* @return			全部半角数字だったら true、それ以外は false
	*/
	public static function isDigit(str:String):Boolean {
		return (isCode(str, 0x30, 0x39));
	}
	/**
	* 文字が半角アルファベットの大文字かどうかを調べる
	* @param	str		文字列
	* @return			全部半角アルファベットの大文字だったら true、それ以外は false
	*/
	public static function isUpperCase(str:String):Boolean {
		return (isCode(str, 0x41, 0x5a));
	}
	/**
	* 文字が半角アルファベットの小文字かどうかを調べる
	* @param	str		文字列
	* @return			全部半角アルファベットの小文字だったら true、それ以外は false
	*/
	public static function isLowerCase(str:String):Boolean {
		return (isCode(str, 0x61, 0x7a));
	}
	/**
	* 文字が半角アルファベットかどうかを調べる
	* @param	str		文字列
	* @return			全部半角アルファベットだったら true、それ以外は false
	*/
	public static function isLetter(str:String):Boolean {
		return (isUpperCase(str) || isLowerCase(str));
	}
	/**
	* 文字が半角アルファベットまたは半角数字かどうかを調べる
	* @param	str		文字列
	* @return			全部半角アルファベットまたは半角数字だったら true、それ以外は false
	*/
	public static function isLetterOrDigit(str:String):Boolean {
		return (isLetter(str) || isDigit(str));
	}
	/**
	* 文字列が全て半角文字かを判定
	* @param	str		文字列
	* @return			全部半角だったら true、それ以外は false
	*/
	public static function isHalf(str:String):Boolean {
		return (isCode(str, 0x00, 0x7f) || isCode(str, 0xFF61, 0xFF9F));
	}
	/**
	* 文字列のバイト数を求める(?)
	* @param	str		文字列
	* @return			文字列のバイト数
	*/
	public static function getBytesTotal(str:String):Number {
		var cnt:Number = 0;
		var len:Number = str.length;
		while (len--) {
			cnt += (isHalf(str.substr(len, 1))) ? 1 : 2;
		}
		return cnt;
	}
	//------------------------------------------------------------
	private function toString():String {
		return CLASS_NAME;
	}
	//------------------------------------------------------------
}