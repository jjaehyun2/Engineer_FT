package away3d.entities
{

	import away3d.animators.IAnimator;
	import away3d.arcane;
	import away3d.bounds.BoundingSphere;
	import away3d.bounds.BoundingVolumeBase;
	import away3d.cameras.Camera3D;
	import away3d.core.base.IRenderable;
	import away3d.core.base.SubGeometry;
	import away3d.core.managers.Stage3DProxy;
	import away3d.core.partition.EntityNode;
	import away3d.core.partition.RenderableNode;
	import away3d.materials.MaterialBase;

	import flash.display3D.IndexBuffer3D;
	import flash.display3D.VertexBuffer3D;
	import flash.geom.Matrix;
	import flash.geom.Matrix3D;
	import flash.geom.Vector3D;

	use namespace arcane;

	/**
	 * Sprite3D is a 3D billboard, a renderable rectangular area that is always aligned with the projection plane.
	 * As a result, no perspective transformation occurs on a Sprite3D object.
	 *
	 * todo: mvp generation or vertex shader code can be optimized
	 */
	public class Sprite3D extends Entity implements IRenderable
	{
		private static var _geometry:SubGeometry;

		private var _material:MaterialBase;
		private var _spriteMatrix:Matrix3D;
		private var _animator : IAnimator;
		
		private var _width:Number;
		private var _height:Number;
		private var _shadowCaster:Boolean = false;

		public function Sprite3D( material:MaterialBase, width:Number, height:Number ) {
			super();
			this.material = material;
			_width = width;
			_height = height;
			_spriteMatrix = new Matrix3D();
			if( !_geometry ) {
				_geometry = new SubGeometry();
				_geometry.updateVertexData( Vector.<Number>( [-.5, .5, .0, .5, .5, .0, .5, -.5, .0, -.5, -.5, .0] ) );
				_geometry.updateUVData( Vector.<Number>( [.0, .0, 1.0, .0, 1.0, 1.0, .0, 1.0] ) );
				_geometry.updateIndexData( Vector.<uint>( [0, 1, 2, 0, 2, 3] ) );
				_geometry.updateVertexTangentData( Vector.<Number>( [1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0] ) );
				_geometry.updateVertexNormalData( Vector.<Number>( [.0, .0, -1.0, .0, .0, -1.0, .0, .0, -1.0, .0, .0, -1.0] ) );
			}
		}

		public function get width():Number {
			return _width;
		}

		public function set width( value:Number ):void {
			if( _width == value ) return;
			_width = value;
			invalidateTransform();
		}

		public function get height():Number {
			return _height;
		}

		public function set height( value:Number ):void {
			if( _height == value ) return;
			_height = value;
			invalidateTransform();
		}

		public function getVertexBuffer( stage3DProxy:Stage3DProxy ):VertexBuffer3D {
			return _geometry.getVertexBuffer( stage3DProxy );
		}

		public function getUVBuffer( stage3DProxy:Stage3DProxy ):VertexBuffer3D {
			return _geometry.getUVBuffer( stage3DProxy );
		}

		public function getVertexNormalBuffer( stage3DProxy:Stage3DProxy ):VertexBuffer3D {
			return _geometry.getVertexNormalBuffer( stage3DProxy );
		}

		public function getVertexTangentBuffer( stage3DProxy:Stage3DProxy ):VertexBuffer3D {
			return _geometry.getVertexTangentBuffer( stage3DProxy );
		}

		public function getIndexBuffer( stage3DProxy:Stage3DProxy ):IndexBuffer3D {
			return _geometry.getIndexBuffer( stage3DProxy );
		}

		override public function pushModelViewProjection( camera:Camera3D ):void {
			var comps:Vector.<Vector3D>;
			var rot:Vector3D;
			if( ++_mvpIndex == _stackLen ) {
				_mvpTransformStack[_mvpIndex] = new Matrix3D();
				++_stackLen;
			}

			// todo: find better way
			var mvp:Matrix3D = _mvpTransformStack[_mvpIndex];
			mvp.copyFrom( sceneTransform );
			mvp.append( camera.inverseSceneTransform );
			comps = mvp.decompose();
			rot = comps[1];
			rot.x = rot.y = rot.z = 0;
			mvp.recompose( comps );
			mvp.append( camera.lens.matrix );
			mvp.copyColumnTo( 3, _pos );
			_zIndices[_mvpIndex] = -_pos.z;
		}

		public function get numTriangles():uint {
			return 2;
		}

		public function get sourceEntity():Entity {
			return this;
		}

		public function get material():MaterialBase {
			return _material;
		}

		public function set material( value:MaterialBase ):void {
			if( value == _material ) return;
			if( _material ) _material.removeOwner( this );
			_material = value;
			if( _material ) _material.addOwner( this );
		}

		
		/**
		 * Defines the animator of the mesh. Act on the mesh's geometry. Defaults to null
		 */
		public function get animator() : IAnimator
		{
			return _animator;
		}

		public function get castsShadows():Boolean {
			return _shadowCaster;
		}

		override protected function getDefaultBoundingVolume():BoundingVolumeBase {
			return new BoundingSphere();
		}

		override protected function updateBounds():void {
			_bounds.fromExtremes(-.5 * _scaleX, -.5 * _scaleY, 0, .5 * _scaleX, .5 * _scaleY, 0);
			_boundsInvalid = false;
		}


		override protected function createEntityPartitionNode():EntityNode {
			return new RenderableNode( this );
		}

		override protected function updateTransform():void {
			super.updateTransform();
			_transform.prependScale( _width, _height, 1 );
		}

		public function get uvTransform():Matrix {
			return null;
		}

		public function getSecondaryUVBuffer( stage3DProxy:Stage3DProxy ):VertexBuffer3D {
			return _geometry.getSecondaryUVBuffer(stage3DProxy);
		}

		public function getCustomBuffer(stage3DProxy : Stage3DProxy) : VertexBuffer3D
		{
			return _geometry.getCustomBuffer(stage3DProxy);
		}

		public function get vertexBufferOffset() : int
		{
			return _geometry.vertexBufferOffset;
		}

		public function get normalBufferOffset() : int
		{
			return _geometry.normalBufferOffset;
		}

		public function get tangentBufferOffset() : int
		{
			return _geometry.tangentBufferOffset;
		}

		public function get UVBufferOffset() : int
		{
			return _geometry.UVBufferOffset;
		}

		public function get secondaryUVBufferOffset() : int
		{
			return _geometry.secondaryUVBufferOffset;
		}

		public function get vertexData():Vector.<Number> {
			return _geometry.vertexData;
		}

		public function get indexData():Vector.<uint> {
			return _geometry.indexData;
		}

		public function get UVData():Vector.<Number> {
			return _geometry.UVData;
		}
	}
}