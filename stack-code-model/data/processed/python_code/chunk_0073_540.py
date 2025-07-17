package flash.display3D.textures
{
	import flash.media.Camera;
	import flash.net.NetStream;


	public final class VideoTexture extends TextureBase
	{
		public function VideoTexture() {
			super();
		}

		public function attachNetStream(param1:NetStream):void { }

		public function attachCamera(param1:Camera):void { }

		public function get videoWidth():int { return 0; }

		public function get videoHeight():int { return 0; }
	}
}