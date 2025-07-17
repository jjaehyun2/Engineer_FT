package ro.ciacob.desktop.io {
	import flash.utils.ByteArray;

	public class RawDiskWritter extends AbstractDiskWritter {
		public function RawDiskWritter() {
			super(this);
		}

		override protected function serializeSource(source:Object):ByteArray {
			if (!(source is ByteArray)) {
				throw(new Error('The RawDiskWritter.serializeSource() method expects a ByteArray as its argument.'));
			}
			return source as ByteArray;
		}
	}
}