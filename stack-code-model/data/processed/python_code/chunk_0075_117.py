/**
 * Created by newkrok on 15/11/15.
 */
package src.menu.module.menubackground
{
	import flash.display.Stage;
	import flash.events.AccelerometerEvent;
	import flash.events.MouseEvent;
	import flash.geom.Point;
	import flash.sensors.Accelerometer;

	import net.fpp.common.starling.module.AModule;

	import src.menu.module.menubackground.view.MenuBackgroundView;

	import starling.core.Starling;

	public class MenuBackgroundModule extends AModule
	{
		CONFIG::IS_MOBILE_VERSION
		{
			private var _accelerometer:Accelerometer;
		}

		private var _offsetPercent:Point = new Point();

		public function MenuBackgroundModule()
		{
			this._view = this.createModuleView( MenuBackgroundView ) as MenuBackgroundView;

			CONFIG::IS_MOBILE_VERSION
			{
				_accelerometer = new Accelerometer();
			}
		}

		public function setLevelPackId( id:uint ):void
		{
			( this._view as MenuBackgroundView ).setLevelPackId( id );
		}

		CONFIG::IS_MOBILE_VERSION
		{
			public function enable():void
			{
				this._accelerometer.addEventListener( AccelerometerEvent.UPDATE, onAccelerometerUpdate );
			}

			private function onAccelerometerUpdate( e:AccelerometerEvent ):void
			{
				this._offsetPercent.setTo( -e.accelerationX, e.accelerationY );
				this.updateView();
			}
		}

		CONFIG::IS_FLASH_VERSION
		{
			public function enable():void
			{
				Starling.current.nativeStage.addEventListener( MouseEvent.MOUSE_MOVE, onMouseMove );
			}

			private function onMouseMove( e:MouseEvent ):void
			{
				this.calculateOffsetPercents();
				this.updateView();
			}

			private function calculateOffsetPercents():void
			{
				var nStage:Stage = Starling.current.nativeStage;

				var centerX:Number = nStage.stageWidth / 2;
				var centerY:Number = nStage.stageHeight / 2;

				var xDirection:int = nStage.mouseX > centerX ? -1 : 1;
				var yDirection:int = nStage.mouseY > centerY ? -1 : 1;

				this._offsetPercent.setTo( ( nStage.mouseX - centerX ) / centerX * -1, ( nStage.mouseY - centerY ) / centerY )
			}
		}

		private function updateView():void
		{
			( this._view as MenuBackgroundView ).update( this._offsetPercent );
		}

		CONFIG::IS_MOBILE_VERSION
		{
			public function disable():void
			{
				this._accelerometer.removeEventListener( AccelerometerEvent.UPDATE, onAccelerometerUpdate );
			}
		}

		CONFIG::IS_FLASH_VERSION
		{
			public function disable():void
			{
				Starling.current.nativeStage.removeEventListener( MouseEvent.MOUSE_MOVE, onMouseMove );
			}
		}

		override public function dispose():void
		{
			this.disable();

			CONFIG::IS_MOBILE_VERSION
			{
				this._accelerometer = null;
			}

			this._view.removeFromParent( true );
			this._view = null;
		}
	}
}