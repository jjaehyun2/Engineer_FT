package net.psykosoft.psykopaint2.core.drawing.brushes.shapes
{
	import flash.display3D.Context3D;

	
	public class NoisyBrushShape2 extends EmbeddedBrushShape
	{
		public static const NAME:String = "noisy";

		
		[Embed(source="assets/png/NoiseShape.png", mimeType="image/png")]
		protected var SourceMap:Class;
		
		//[Embed(source="assets/notentirelycircularheight9_8x8.png", mimeType="image/png")]
		[Embed(source="assets/png/NoiseShape4.png", mimeType="image/png")]
		protected var SourceNormalSpecularMap:Class;

		public function NoisyBrushShape2(context3D : Context3D)
		{
			super(context3D, NAME, SourceMap,SourceNormalSpecularMap,512,2,2);
			rotationRange = Math.PI*2;
		}
	}
}