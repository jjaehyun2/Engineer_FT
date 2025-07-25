/**
 * ...
 * Author: SiuzukZan <minoscc@gmail.com>
 * Date: 14/12/10 15:05
 */
package cc.minos.codec.mp4.boxs {

	import cc.minos.codec.mp4.Mp4;

	/**
	 * sync sample table (key frames)
	 */
	public class StssBox extends Box {

		private var _count:uint;
		private var _keyframes:Array = [];

		public function StssBox()
		{
			super(Mp4.BOX_TYPE_STSS);
		}

		override protected function init():void
		{
			data.position = 12;
			_count = data.readUnsignedInt();
			for (var i:int = 0; i < _count; i++)
			{
				_keyframes.push(data.readUnsignedInt());
			}
		}

		public function get keyframes():Array
		{
			return _keyframes;
		}

		public function get count():uint
		{
			return _count;
		}
	}
}