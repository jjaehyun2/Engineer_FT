/**
 * Created by Administrator on 2015/8/17.
 */
package gui3D.shapes
{
	import away3d.containers.ObjectContainer3D;
	import away3d.entities.Mesh;
	import away3d.events.MouseEvent3D;
	import away3d.materials.ColorMaterial;
	import away3d.primitives.PlaneGeometry;

	import com.greensock.TweenMax;

	import flash.geom.Vector3D;

	import gui3D.Geometry3D;

	public class CubeUnfold extends ObjectContainer3D
	{
		private var _geometry3d:Geometry3D;
		private var _colorMaterial:ColorMaterial;

		private var _leftGeometry:PlaneGeometry;
		private var _leftMesh:Mesh;

		private var _rightGeometry:PlaneGeometry;
		private var _rightMesh:Mesh;

		private var _frontGeometry:PlaneGeometry;
		private var _frontMesh:Mesh;

		private var _backGeometry:PlaneGeometry;
		private var _backMesh:Mesh;

		private var _topGeometry:PlaneGeometry;
		private var _topMesh:Mesh;

		private var _bottomGeometry:PlaneGeometry;
		private var _bottomMesh:Mesh;

		private var _width:Number = 200;
		private var _height:Number = 200;

		public function CubeUnfold(geometry3d:Geometry3D)
		{
			super();
			this._geometry3d = geometry3d;
			_colorMaterial = new ColorMaterial(0xff0000);

			_bottomGeometry = new PlaneGeometry(_width, _height);
			_bottomGeometry.doubleSided = true;
			_bottomMesh = new Mesh(_bottomGeometry, _colorMaterial);
			addChild(_bottomMesh);
			_bottomMesh.mouseEnabled = true;


			_leftGeometry = new PlaneGeometry(_width, _height);
			_leftGeometry.doubleSided = true;
			_colorMaterial = new ColorMaterial(0x00ff00);
			_leftMesh = new Mesh(_leftGeometry, _colorMaterial);
			_leftMesh.mouseEnabled = true;
			addChild(_leftMesh);
			_leftMesh.position = new Vector3D(0, 100, -100);
			_leftMesh.rotationX = 90;


			_rightGeometry = new PlaneGeometry(_width, _height);
			_rightGeometry.doubleSided = true;
			_colorMaterial = new ColorMaterial(0x0000ff);
			_rightMesh = new Mesh(_rightGeometry, _colorMaterial);
			_rightMesh.mouseEnabled = true;
			addChild(_rightMesh);
			_rightMesh.position = new Vector3D(0, 100, 100);
			_rightMesh.rotationX = -90;


			_frontGeometry = new PlaneGeometry(_width, _height);
			_frontGeometry.doubleSided = true;
			_colorMaterial = new ColorMaterial(0xffff00);
			_frontMesh = new Mesh(_frontGeometry, _colorMaterial);
			addChild(_frontMesh);
			_frontMesh.mouseEnabled = true;
			_frontMesh.position = new Vector3D(100, 100, 0);
			_frontMesh.rotationZ = 90;


			_backGeometry = new PlaneGeometry(_width, _height);
			_backGeometry.doubleSided = true;
			_colorMaterial = new ColorMaterial(0x00ffff);
			_backMesh = new Mesh(_backGeometry, _colorMaterial);
			_backMesh.mouseEnabled = true;
			addChild(_backMesh);
			_backMesh.position = new Vector3D(-100, 100, 0);
			_backMesh.rotationZ = -90;

			_topGeometry = new PlaneGeometry(_width, _height);
			_topGeometry.doubleSided = true;
			_colorMaterial = new ColorMaterial(0xff3300);
			_topMesh = new Mesh(_topGeometry, _colorMaterial);
			_topMesh.mouseEnabled = true;
			addChild(_topMesh);
			_topMesh.position = new Vector3D(0, 200, 0);
			_topMesh.rotationZ = 0;

			_geometry3d.mainView.scene.addChild(this);
			addEventListener(MouseEvent3D.MOUSE_DOWN, onMouseDown, false, 0, true);
			addEventListener(MouseEvent3D.MOUSE_UP, onMouseUp, false, 0, true);
		}

		private function onMouseUp(event:MouseEvent3D):void
		{
			TweenMax.to(_leftMesh, 1, {rotationX: 90, x: 0, y: 100, z: -100});
			TweenMax.to(_rightMesh, 1, {rotationX: -90, x: 0, y: 100, z: 100});
			TweenMax.to(_frontMesh, 1, {rotationZ: 90, x: 100, y: 100, z: 0});
			TweenMax.to(_topMesh, 1, {rotationZ: 0, x: 0, y: 200, z: 0});
			TweenMax.to(_backMesh, 1, {rotationZ: -90, x: -100, y: 100, z: 0});
		}

		private function onMouseDown(event:MouseEvent3D):void
		{
			TweenMax.to(_leftMesh, 1, {rotationX: 0, x: 0, y: 0, z: -200});
			TweenMax.to(_rightMesh, 1, {rotationX: 0, x: 0, y: 0, z: 200});
			TweenMax.to(_frontMesh, 1, {rotationZ: 0, x: 200, y: 0, z: 0});
			TweenMax.to(_topMesh, 1, {rotationZ: -180, x: 400, y: 0, z: 0});
			TweenMax.to(_backMesh, 1, {rotationZ: 0, x: -200, y: 0, z: 0});
		}
	}
}