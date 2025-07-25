package net.psykosoft.psykopaint2.paint.views.base
{

	import flash.display.Sprite;
	
	import net.psykosoft.psykopaint2.core.models.NavigationStateType;
	import net.psykosoft.psykopaint2.core.views.navigation.EmptySubNavView;
	import net.psykosoft.psykopaint2.core.views.navigation.StateToSubNavLinker;
	import net.psykosoft.psykopaint2.paint.views.brush.SelectBrushSubNavView;
	import net.psykosoft.psykopaint2.paint.views.brush.UpgradeSubNavView;
	import net.psykosoft.psykopaint2.paint.views.canvas.CanvasSubNavView;
	import net.psykosoft.psykopaint2.paint.views.canvas.CanvasView;
	import net.psykosoft.psykopaint2.paint.views.canvas.PipetteView;
	import net.psykosoft.psykopaint2.paint.views.color.ColorPickerSubNavView;

	public class PaintRootView extends Sprite
	{
		private var _canvasView:CanvasView;
		private var _pipetteView:PipetteView;

		public function PaintRootView() {
			super();

			// Add main views.
			addChild( _canvasView = new CanvasView() );

			// Link sub-navigation views that are created dynamically by CrNavigationView
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.PAINT, CanvasSubNavView );
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.PAINT_SELECT_BRUSH, SelectBrushSubNavView );
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.LOADING_PAINT_MODE, EmptySubNavView );
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.TRANSITION_TO_PAINT_MODE, EmptySubNavView );
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.PAINT_ADJUST_COLOR, ColorPickerSubNavView );
			StateToSubNavLinker.linkSubNavToState( NavigationStateType.PAINT_BUY_UPGRADE, UpgradeSubNavView );
			//StateToSubNavLinker.linkSubNavToState( NavigationStateType.PAINT_ADJUST_ALPHA, AlphaSubNavView );
			
			addChild( _pipetteView = new PipetteView() );
			
			mouseEnabled = false;
			name = "PaintRootView";
		}

		public function dispose():void {

			removeChild( _canvasView );
			removeChild( _pipetteView );
			// Note: removing the views from display will cause the destruction of the mediators which will
			// in turn destroy the views themselves.
		}
	}
}