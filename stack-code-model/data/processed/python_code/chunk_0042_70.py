/**
 * Created by Administrator on 2015/8/12.
 */
package gui3D.shapes
{
	import away3d.entities.Mesh;
	import away3d.events.MouseEvent3D;
	import away3d.materials.ColorMaterial;
	import away3d.materials.lightpickers.StaticLightPicker;
	import away3d.primitives.CubeGeometry;

	import constants.ShapeType;

	import gui3D.Geometry3D;

	import universal.pattern.event.GameDispatcher;
	import universal.pattern.event.GameEventConst;

	public class ACube extends AShapeBase
	{
		private var _cubeMesh:Mesh;
		private var _cubeGeometry:CubeGeometry;
		private var _colorMaterial:ColorMaterial;

		//Geometry3D的引用
		private var _geometry3d:Geometry3D;

		public function ACube(geometry3d:Geometry3D)
		{
			type = ShapeType.CUBE_TYPE;
			_geometry3d = geometry3d;
			_cubeGeometry = new CubeGeometry(_width, _height, _depth);
			_colorMaterial = new ColorMaterial(_color, _alpha);
			_colorMaterial.lightPicker = new StaticLightPicker([_geometry3d.light]);
			_cubeMesh = new Mesh(_cubeGeometry, _colorMaterial);
			addChild(_cubeMesh);
			_geometry3d.mainView.scene.addChild(this);
			_cubeMesh.mouseEnabled = true;
			addEventListener(MouseEvent3D.MOUSE_DOWN, downEvt);
		}

		private function downEvt(event:MouseEvent3D):void
		{
			GameDispatcher.dispatchEvent(GameEventConst.DOWN_ITEM, {item: this});
		}

		override public function set width(value:Number):void
		{
			super.width = value;
			if (_cubeGeometry)
			{
				_cubeGeometry.width = _width;
			}
		}

		override public function set height(value:Number):void
		{
			super.height = value;
			if (_cubeGeometry)
			{
				_cubeGeometry.height = _height;
			}
		}

		override public function set depth(value:Number):void
		{
			super.depth = value;
			if (_cubeGeometry)
			{
				_cubeGeometry.depth = _depth;
			}

		}

		override public function set alpha(value:Number):void
		{
			super.alpha = value;
			if (_colorMaterial)
			{
				_colorMaterial.alpha = _alpha;
			}
		}

		override public function set color(value:uint):void
		{
			super.color = value;
			if (_colorMaterial)
			{
				_colorMaterial.color = _color;
			}
		}

		override public function destroy():void
		{
			super.destroy();
			if (_colorMaterial)
			{
				_colorMaterial.dispose();
				_colorMaterial = null;
			}
			if (_cubeGeometry)
			{
				_cubeGeometry.dispose();
				_cubeGeometry = null;
			}
			if (_cubeMesh && _cubeMesh.parent)
			{
				_cubeMesh.removeEventListener(MouseEvent3D.MOUSE_DOWN, downEvt);
				_cubeMesh.parent.removeChild(_cubeMesh);
				_cubeMesh.dispose();
				_cubeMesh = null;
			}
			if (_geometry3d && _geometry3d.mainView && _geometry3d.mainView.scene)
			{
				if (_geometry3d.mainView.scene.contains(this))
				{
					_geometry3d.mainView.scene.removeChild(this);
				}
			}
			_geometry3d && (_geometry3d = null);
		}
	}
}