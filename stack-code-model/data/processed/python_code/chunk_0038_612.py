package org.openPyro.examples
{
	import org.openPyro.core.UIControl;
	import org.openPyro.painters.CompositePainter;
	import org.openPyro.painters.FillPainter;
	import org.openPyro.painters.GradientFillPainter;
	import org.openPyro.painters.Stroke;
	import org.openPyro.painters.StrokePainter;
	
	public class HaloTrackSkin extends UIControl
	{
		public function HaloTrackSkin(gradientRotation:Number=0)
		{
			var fillPainter:FillPainter = new FillPainter(0xffffff);
			var gradientFill:GradientFillPainter = new GradientFillPainter([0x000000,0xdfdfdf, 0xffffff],[.4,1,1],[1,140,255],gradientRotation)
			var strokePainter:StrokePainter = new StrokePainter(new Stroke(1, 0x777777))
			var compositePainter:CompositePainter = new CompositePainter()
			compositePainter.addPainter(fillPainter);
			compositePainter.addPainter(strokePainter)
			compositePainter.addPainter(gradientFill);
			this.backgroundPainter = compositePainter;
		}

	}
}