package net.psykosoft.psykopaint2.core.signals
{

	import net.psykosoft.psykopaint2.base.robotlegs.signals.TracingSignal;

	public class RequestLoadSurfaceSignal extends TracingSignal
	{
		public function RequestLoadSurfaceSignal() {
			super(int);	// PaintMode.PHOTO_MODE or PaintMode.COLOR_MODE
		}
	}
}