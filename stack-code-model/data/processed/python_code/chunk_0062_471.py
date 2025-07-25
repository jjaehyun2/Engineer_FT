package net.psykosoft.psykopaint2.paint.views.alpha
{

	import net.psykosoft.psykopaint2.core.views.components.button.ButtonIconType;
	import net.psykosoft.psykopaint2.core.views.components.slider.AlphaSlider;
	import net.psykosoft.psykopaint2.core.views.navigation.NavigationBg;
	import net.psykosoft.psykopaint2.core.views.navigation.SubNavigationViewBase;

	import org.osflash.signals.Signal;

	public class AlphaSubNavView extends SubNavigationViewBase
	{
		public static const ID_BACK:String = "Back";

		private var _alphaSlider:AlphaSlider;

		public var viewWantsToChangeAlphaSignal:Signal;

		public function AlphaSubNavView() {
			super();
			viewWantsToChangeAlphaSignal = new Signal();
			_alphaSlider = new AlphaSlider();
			_alphaSlider.valueChangedSignal.add( onSliderValueChanged );
			_alphaSlider.x = 1024 / 2 - _alphaSlider.width / 2;
			_alphaSlider.y = 630;
			addChild( _alphaSlider );
			setAlpha( 0.5 );
		}

		override protected function onEnabled():void {
			
			setLeftButton( ID_BACK, ID_BACK, ButtonIconType.BACK );
			showRightButton( false );
			setBgType( NavigationBg.BG_TYPE_WOOD );
			setHeader( "" );
		}

		override protected function onDisposed():void {
			_alphaSlider.valueChangedSignal.remove( onSliderValueChanged );
		}

		private function onSliderValueChanged( value:Number ):void {
			viewWantsToChangeAlphaSignal.dispatch( value );
		}

		public function setAlpha( value:Number ):void {
			_alphaSlider.value = value;
		}
	}
}