package net.psykosoft.psykopaint2.home.views.gallery
{

	import away3d.materials.lightpickers.LightPickerBase;

	import com.greensock.TweenLite;
	import com.greensock.easing.Quad;

	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.display3D.Context3DCompareMode;
	import flash.display3D.Context3DStencilAction;
	import flash.events.Event;
	import flash.geom.Rectangle;
	import flash.geom.Vector3D;
	import flash.utils.getTimer;

	import away3d.containers.ObjectContainer3D;
	import away3d.containers.View3D;
	import away3d.core.base.Geometry;
	import away3d.core.managers.Stage3DProxy;
	import away3d.entities.Mesh;
	import away3d.events.Object3DEvent;
	import away3d.hacks.BitmapRectTexture;
	import away3d.hacks.MaskingMethod;
	import away3d.hacks.PaintingMaterial;
	import away3d.hacks.RectTextureBase;
	import away3d.hacks.StencilMethod;
	import away3d.hacks.TrackedBitmapRectTexture;
	import away3d.lights.LightBase;
	import away3d.materials.ColorMaterial;
	import away3d.materials.TextureMaterial;
	import away3d.materials.lightpickers.StaticLightPicker;
	import away3d.primitives.PlaneGeometry;
	import away3d.textures.BitmapTexture;
	import away3d.textures.Texture2DBase;

	import net.psykosoft.psykopaint2.base.utils.gpu.TextureUtil;
	import net.psykosoft.psykopaint2.base.utils.images.BitmapDataUtils;
	import net.psykosoft.psykopaint2.base.utils.misc.TrackedBitmapData;
	import net.psykosoft.psykopaint2.core.configuration.CoreSettings;
	import net.psykosoft.psykopaint2.core.managers.gestures.GrabThrowController;
	import net.psykosoft.psykopaint2.core.managers.gestures.GrabThrowEvent;
	import net.psykosoft.psykopaint2.core.models.GalleryImageCollection;
	import net.psykosoft.psykopaint2.core.models.GalleryImageProxy;
	import net.psykosoft.psykopaint2.core.models.GalleryType;
	import net.psykosoft.psykopaint2.core.models.PaintMode;
	import net.psykosoft.psykopaint2.core.models.PaintingGalleryVO;
	import net.psykosoft.psykopaint2.home.model.GalleryImageCache;
	import net.psykosoft.psykopaint2.home.views.book.HomeMaterialsCache;

	import org.osflash.signals.Signal;

	public class GalleryView extends Sprite
	{
		public static const CAMERA_FAR_POSITION:Vector3D = new Vector3D(-814, -40.14, 450);
		public static var CAMERA_NEAR_POSITION:Vector3D = null;

		private static const PAINTING_OFFSET:Number = 831;
		private static const PAINTING_SPACING:Number = 250;
		private static const PAINTING_WIDTH:Number = 210;
		private static const PAINTING_Y:Number = 5;
		private static const PAINTING_Z:Number = -160;
		private static const SWIPE_SCENE_RECT:Rectangle = new Rectangle(PAINTING_OFFSET + 10 - 250, -100, 500, 300);

		public var requestReconnectSignal:Signal = new Signal();
		public var requestImageCollection:Signal = new Signal(int, int, int); // source, start index, amount of images
		public var requestActiveImageSignal:Signal = new Signal(int, int); // source, index

		private var _imageCache:GalleryImageCache;
		private var _view:View3D;
		private var _stage3DProxy:Stage3DProxy;
		private var _container:ObjectContainer3D;

		private var _paintings:Vector.<GalleryPaintingView> = new Vector.<GalleryPaintingView>();
		private var _lowQualityMaterials:Vector.<TextureMaterial> = new Vector.<TextureMaterial>();

		private var _paintingGeometry:Geometry;
		private var _loadingTexture:BitmapTexture;
		private var _numPaintings:int;
		private var _activeImageProxy:GalleryImageProxy;

		private var _swipeController:GrabThrowController;
		private var _cameraZoomController:GalleryCameraZoomController;

		private var _minSwipe:Number;
		private var _maxSwipe:Number;

		// for throwing/dragging:
		private var _dragCountsAsTap:Boolean;
		private var _tween:TweenLite;
		private var _hasEnterFrame:Boolean;
		private var _friction:Number;
		private var _tweenTime:Number = .5;
		private var _startTime:Number;
		private var _startPos:Number;
		private var _velocity:Number;
		private var _targetPos:Number;
		private var _visibleStartIndex:int;
		private var _visibleEndIndex:int;

		private var _paintingOccluder:Mesh;

		// static hack to prevent render reordering
		private static var _occluderMaterial:ColorMaterial;
		private static var _highQualityMaterial:PaintingMaterial;

		private var _highQualityNormalSpecularTexture:BitmapRectTexture;
		private var _stillLoadingNormalSpecularTexture:BitmapRectTexture;
		private var _highQualityColorTexture:BitmapRectTexture;
		private var _fullsizeCompositedTexture:BitmapRectTexture;

		private var _showHighQuality:Boolean;
		private var _loadingHQ:Boolean;
		private var _dragStartX:Number;
		private var _dragStartY:Number;
		private var _highQualityIndex:int = -1;
		private var _ribbon:Mesh;
		private var _lightPicker:LightPickerBase;

		public function GalleryView(view:View3D, light:LightBase, stage3dProxy:Stage3DProxy)
		{
			_view = view;
			_stage3DProxy = stage3dProxy;
			_lightPicker = new StaticLightPicker([light]);
			_imageCache = new GalleryImageCache(_stage3DProxy);
			_imageCache.thumbnailLoaded.add(onThumbnailLoaded);
			_imageCache.thumbnailDisposed.add(onThumbnailDisposed);
			//_paintingModes = new Vector.<int>();
			createRibbon();
			_imageCache.loadingComplete.add(onAllThumbnailsLoaded);
			_container = new ObjectContainer3D();
			_container.x = -PAINTING_OFFSET;
			_container.y = PAINTING_Y;
			_container.z = PAINTING_Z;
			_container.rotationY = 180;
			_container.mouseEnabled = false;
			_container.mouseChildren = false;
			_view.scene.addChild(_container);
			_view.camera.addEventListener(Object3DEvent.SCENETRANSFORM_CHANGED, onCameraMoved);
			initGeometry();
			initLoadingTexture();
			initOccluder();
			initHighQualityMaterial();
			updateSwipeInteractionRect();
//			showInteractionRect();
		}

		private function createRibbon():void {

			var ribbonMaterial:TextureMaterial = HomeMaterialsCache.getTextureMaterialById(HomeMaterialsCache.ICON_PAINTINGMODE);

			var stencilMethod:StencilMethod = new StencilMethod();
			stencilMethod.referenceValue = 40;
			stencilMethod.compareMode = Context3DCompareMode.NOT_EQUAL;
			ribbonMaterial.addMethod(stencilMethod);

			_ribbon = new Mesh(new PlaneGeometry(25, 25, 1, 1, false, true), ribbonMaterial);
			_ribbon.x = -92;
			_ribbon.y = 66;
			_ribbon.z = -1;
			//_ribbon.scaleX = _ribbon.scaleY = 0.5; 
		}

		private function calculateCameraNearPosition():Vector3D
		{
			var matrix:Vector.<Number> = _view.camera.lens.matrix.rawData;
			var pos:Vector3D = new Vector3D();
			pos.x = -PAINTING_OFFSET;
			pos.y = PAINTING_Y;
			// solve projection equation for camera.z with screen width in NDC (= 2)
			pos.z = PAINTING_WIDTH * matrix[0] / 2 + PAINTING_Z;
			return pos;
		}

		// for debug purposes:
		private function showInteractionRect():void
		{
			var geometry:PlaneGeometry = new PlaneGeometry(SWIPE_SCENE_RECT.width, SWIPE_SCENE_RECT.height, 1, 1, false);
			var material:ColorMaterial = new ColorMaterial(0xff0000, .5);
			var mesh:Mesh = new Mesh(geometry, material);
			mesh.x = -(SWIPE_SCENE_RECT.x + SWIPE_SCENE_RECT.width * .5);
			mesh.y = SWIPE_SCENE_RECT.y + SWIPE_SCENE_RECT.height * .5;
			mesh.z = PAINTING_Z;
			mesh.rotationY = 180;
			material.depthCompareMode = Context3DCompareMode.ALWAYS;
			_view.scene.addChild(mesh);
		}

		public function get showHighQuality():Boolean
		{
			return _showHighQuality;
		}

		public function set showHighQuality(value:Boolean):void
		{
			if (_showHighQuality == value) return;
			_showHighQuality = value;

			if (_showHighQuality) {
				showHighQualityMaterial();
			}
			else {
				removeHighQualityMaterial();
				disposeHighQualityMaterial();
			}
		}

		private function showHighQualityMaterial():void
		{
			if (!_highQualityColorTexture)
				initHighQualityMaterial();

			if (_activeImageProxy) {
				_loadingHQ = true;
				//MATHIEU: WE LOAD THE COMPOSITE IMAGE INSTEAD OF THE COLOR/NORMAL DATA FIRST
				_activeImageProxy.loadFullSizedComposite(onFullsizedCompositeComplete, onSurfaceDataError);
			}
		}



		private function initHighQualityMaterial():void
		{
			var emptyNormalMap : BitmapData = new TrackedBitmapData(1, 1, false, 0x00808000);

			//BookMaterialsProxy.getBitmapDataById(BookMaterialsProxy.THUMBNAIL_LOADING)
			_fullsizeCompositedTexture = new TrackedBitmapRectTexture(null);
			_highQualityColorTexture = new TrackedBitmapRectTexture(null);
			_highQualityNormalSpecularTexture = new TrackedBitmapRectTexture(null);
			_stillLoadingNormalSpecularTexture = new BitmapRectTexture(emptyNormalMap);
			_stillLoadingNormalSpecularTexture.getTextureForStage3D(_stage3DProxy);
			emptyNormalMap.dispose();

			if (!_highQualityMaterial)
				_highQualityMaterial = new PaintingMaterial();

			_highQualityMaterial.lightPicker = _lightPicker;
			_highQualityMaterial.albedoTexture = _fullsizeCompositedTexture;
			_highQualityMaterial.normalSpecularTexture = _stillLoadingNormalSpecularTexture;
			_highQualityMaterial.ambientColor = 0xffffff;
			_highQualityMaterial.specular = 1.5;
			_highQualityMaterial.gloss = 150;

			_highQualityMaterial.enableStencil = true;
			_highQualityMaterial.stencilReferenceValue = 40;
			_highQualityMaterial.stencilCompareMode = Context3DCompareMode.NOT_EQUAL;
		}

		// this creates a geometry that prevents paintings from being rendered outside the gallery area
		private function initOccluder():void
		{
			var occluderGeometry:PlaneGeometry = new PlaneGeometry(500, 200, 1, 1, false);

			if (!_occluderMaterial) {
				_occluderMaterial = new ColorMaterial(0xff00ff);
				var maskingMethod:MaskingMethod = new MaskingMethod();
				maskingMethod.disableAll();
				var stencilMethod:StencilMethod = new StencilMethod();
				stencilMethod.referenceValue = 40;
				stencilMethod.actionDepthAndStencilPass = Context3DStencilAction.SET;
				stencilMethod.actionDepthFail = Context3DStencilAction.SET;
				stencilMethod.actionDepthPassStencilFail = Context3DStencilAction.SET;
				_occluderMaterial.addMethod(maskingMethod);
				_occluderMaterial.addMethod(stencilMethod);
			}
			_paintingOccluder = new Mesh(occluderGeometry, _occluderMaterial);
			_paintingOccluder.x = -300;
			_paintingOccluder.y = PAINTING_Y;
			_paintingOccluder.z = PAINTING_Z + 100;
			_paintingOccluder.rotationY = 180;
			_view.scene.addChild(_paintingOccluder);
		}

		public function initInteraction():void
		{
			_swipeController ||= new GrabThrowController(stage);

			if (CAMERA_NEAR_POSITION == null) {
				CAMERA_NEAR_POSITION = calculateCameraNearPosition();
			}

			_cameraZoomController ||= new GalleryCameraZoomController(stage, _view.camera, PAINTING_WIDTH, PAINTING_Z, CAMERA_FAR_POSITION, CAMERA_NEAR_POSITION);

			_swipeController.addEventListener(GrabThrowEvent.DRAG_STARTED, onDragStarted, false, 0, true);
			_swipeController.start(10000, true);

			updateSwipeInteractionRect();
			_cameraZoomController.start();
		}

		private function updateSwipeInteractionRect():void
		{
			if (!_swipeController) return;
			var topLeft:Vector3D = new Vector3D(-SWIPE_SCENE_RECT.x, SWIPE_SCENE_RECT.y + SWIPE_SCENE_RECT.height, PAINTING_Z);
			var bottomRight:Vector3D = new Vector3D(-(SWIPE_SCENE_RECT.x + SWIPE_SCENE_RECT.width), SWIPE_SCENE_RECT.y, PAINTING_Z);
			topLeft = _view.project(topLeft);
			bottomRight = _view.project(bottomRight);
			_swipeController.interactionRect = new Rectangle(topLeft.x, topLeft.y, bottomRight.x - topLeft.x, bottomRight.y - topLeft.y);
		}

		public function stopInteraction():void
		{
			if (_swipeController) {
				_swipeController.stop();
				_swipeController.removeEventListener(GrabThrowEvent.DRAG_STARTED, onDragStarted);
				_swipeController.removeEventListener(GrabThrowEvent.DRAG_UPDATE, onDragUpdate);
				_swipeController.removeEventListener(GrabThrowEvent.RELEASE, onDragRelease);
			}

			if (_cameraZoomController) {
				_cameraZoomController.stop();
			}
		}

		public function get onZoomUpdateSignal():Signal
		{
			return _cameraZoomController ? _cameraZoomController.onZoomUpdateSignal : null;
		}

		private function onDragStarted(event:GrabThrowEvent):void
		{
			killTween();
			_dragStartX = stage.mouseX;
			_dragStartY = stage.mouseY;
			_dragCountsAsTap = true;
			_swipeController.addEventListener(GrabThrowEvent.DRAG_UPDATE, onDragUpdate, false, 0, true);
			_swipeController.addEventListener(GrabThrowEvent.RELEASE, onDragRelease, false, 0, true);
		}

		private function onEnterFrame(event:Event):void
		{
			var t:Number = (getTimer() - _startTime) / 1000;

			updateVisibility();

			if (t > _tweenTime) {
				_container.x = _targetPos;
				killTween();
			}
			else {
				_container.x = _startPos + (_velocity + .5 * _friction * t) * t;
			}
		}

		private function onDragUpdate(event:GrabThrowEvent):void
		{
			// when straying too far from start position, it can't possibly be a tap
			if (Math.abs(stage.mouseX - _dragStartX) > 2 * CoreSettings.GLOBAL_SCALING ||
					Math.abs(stage.mouseY - _dragStartY) > 2 * CoreSettings.GLOBAL_SCALING
					)
				_dragCountsAsTap = false;
			constrainSwipe(_container.x - unprojectVelocity(event.velocityX));
			updateVisibility();
		}

		private function unprojectVelocity(screenSpaceVelocity:Number):Number
		{
			var matrix:Vector.<Number> = _view.camera.lens.matrix.rawData;
			var z:Number = _view.camera.z - PAINTING_Z;
			return screenSpaceVelocity / CoreSettings.STAGE_WIDTH * 2 * z / matrix[0];
		}

		private function killTween():void
		{
			if (_tween) {
				_tween.kill();
				_tween = null;
			}

			if (_hasEnterFrame) {
				removeEventListener(Event.ENTER_FRAME, onEnterFrame);
				_hasEnterFrame = false;
			}
		}

		private function constrainSwipe(position:Number):void
		{
			if (position > _maxSwipe) position = _maxSwipe;
			else if (position < _minSwipe) position = _minSwipe;

			_container.x = position;
		}

		private function onDragRelease(event:GrabThrowEvent):void
		{
			_swipeController.removeEventListener(GrabThrowEvent.DRAG_UPDATE, onDragUpdate);
			_swipeController.removeEventListener(GrabThrowEvent.RELEASE, onDragRelease);

			var velocity:Number = unprojectVelocity(event.velocityX);
			if (Math.abs(event.velocityX) < 3 * CoreSettings.GLOBAL_SCALING) {
				moveToNearest();

				if (_dragCountsAsTap && !event.interrupted && mousePosInFocusedPainting()) {
					if (_activeImageProxy && _activeImageProxy.collectionType != GalleryType.NONE)
						zoomFully();
					else
						requestReconnectSignal.dispatch();
				}
			}
			else {
				throwToPainting(velocity);
			}
		}

		private function zoomFully():void
		{
			TweenLite.to(_cameraZoomController, .5, {zoomFactor: 1, ease: Quad.easeOut});
		}

		private function mousePosInFocusedPainting():Boolean
		{
			// _activeImageProxy can be null for error message 'paintings'
			var index : int = _activeImageProxy? _activeImageProxy.index : 0;
			var painting:GalleryPaintingView = _paintings[index];
			var paintingPosition:Vector3D = _view.camera.project(painting.scenePosition);
			var matrix:Vector.<Number> = _view.camera.lens.matrix.rawData;
			var z:Number = _view.camera.z - PAINTING_Z;
			var halfProjSize:Number = PAINTING_WIDTH * matrix[0] / z * .5;

			// TODO: This can be done entirely in NDC
			var mouseX:Number = stage.mouseX / CoreSettings.STAGE_WIDTH * 2.0 - 1.0 - paintingPosition.x;
			var mouseY:Number = stage.mouseY / CoreSettings.STAGE_HEIGHT * 2.0 - 1.0 - paintingPosition.y;
			return mouseX > -halfProjSize && mouseX < halfProjSize && mouseY > -halfProjSize && mouseY < halfProjSize;
		}

		private function throwToPainting(velocity:Number):void
		{
			if (velocity > 0 && velocity < 20) velocity = 20;
			if (velocity < 0 && velocity > -20) velocity = -20;
			// convert per frame to per second, and reduce speed (doesn't feel good otherwise)
			_velocity = -velocity * 60 / 2;
			_startPos = _container.x;
			var targetTime:Number = .25;
			var targetFriction:Number = .8;
			var targetIndex:int;
			if (_velocity > 0) targetFriction = -targetFriction;

			// where would the target end up with the current speed after aimed time with aimed friction?
			_targetPos = _startPos + _velocity * targetTime + targetFriction * targetTime * targetTime;

			if (_targetPos > _maxSwipe) {
				targetIndex = _numPaintings - 1;
				_targetPos = _maxSwipe;
			}
			else if (_targetPos < _minSwipe) {
				targetIndex = 0;
				_targetPos = _minSwipe;
			}
			else {
				targetIndex = getNearestPaintingIndex(_targetPos);
				_targetPos = targetIndex * PAINTING_SPACING - PAINTING_OFFSET;
			}

			requestActiveImage(targetIndex);

			// solving:
			// p(t) = p(0) + v(0)*t + a*t^2 / 2 = target
			// v(t) = v(0) + a*t = 0
			// for 'a' (acceleration, ie negative friction) and 't'

			_tweenTime = 2 * (_targetPos - _startPos) / _velocity;
			_friction = -_velocity / _tweenTime;

			_startTime = getTimer();
			_hasEnterFrame = true;
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}

		private function moveToNearest():void
		{
			var index:int = getNearestPaintingIndex(_container.x);
			requestActiveImage(index);
			_tween = TweenLite.to(_container, .5,
					{    x: index * PAINTING_SPACING - PAINTING_OFFSET,
						ease: Quad.easeInOut,
						onUpdate: updateVisibility
					});
		}

		private function getNearestPaintingIndex(position:Number):Number
		{
			return Math.round((position + PAINTING_OFFSET) / PAINTING_SPACING);
		}

		private function initGeometry():void
		{
			var aspectRatio:Number = CoreSettings.STAGE_HEIGHT / CoreSettings.STAGE_WIDTH;
			_paintingGeometry = new PlaneGeometry(PAINTING_WIDTH, PAINTING_WIDTH * aspectRatio, 1, 1, false);
		}

		private function initLoadingTexture():void
		{
			//var bitmapData:BitmapData = new TrackedBitmapData(16, 16, true, 0xFFAAAAAA);

			_loadingTexture = new BitmapTexture(TextureUtil.autoResizePowerOf2(HomeMaterialsCache.getBitmapDataById(HomeMaterialsCache.THUMBNAIL_LOADING)));
			_loadingTexture.getTextureForStage3D(_stage3DProxy);
			//bitmapData.dispose();

		}


		public function setImmediateActiveImage(galleryImageProxy:GalleryImageProxy):void
		{
			setActiveImage(galleryImageProxy);

			if (galleryImageProxy)
				_container.x = -(PAINTING_OFFSET - galleryImageProxy.index * PAINTING_SPACING);
			else
				_container.x = -PAINTING_OFFSET;
		}

		public function setActiveImage(galleryImageProxy:GalleryImageProxy):void
		{
			if (!_activeImageProxy || !galleryImageProxy || _activeImageProxy.collectionType != galleryImageProxy.collectionType)
				resetPaintings();

			if (_activeImageProxy && (!galleryImageProxy || _activeImageProxy.id != galleryImageProxy.id))
				removeHighQualityMaterial();

			// make sure to clone so we can load while the book is loading
			_activeImageProxy = galleryImageProxy? galleryImageProxy.clone() : null;

			if (!_activeImageProxy) {
				_numPaintings = 0;
				return;
			}

			const amountOnEachSide:int = 2;
			var min:int = galleryImageProxy.index - amountOnEachSide;
			var amount:int = amountOnEachSide * 2 + 1;

			if (min < 0) {
				amount += min;	// fix amount to still have correct amount of the right
				min = 0;
			}

			requestImageCollection.dispatch(galleryImageProxy.collectionType, min, amount);
		}

		private function removeHighQualityMaterial():void
		{
			_highQualityIndex = -1;
			if (_activeImageProxy)
				_activeImageProxy.cancelLoading();
			// also test if painting hasn't been destroyed yet due to panning
			if (_paintings && _activeImageProxy && _paintings[_activeImageProxy.index]) {
				var index:uint = _activeImageProxy.index;
				_paintings[index].material = _lowQualityMaterials[index];
			}
		}

		private function requestActiveImage(index:int):void
		{
			if (_activeImageProxy && _activeImageProxy.index != index) {
				removeHighQualityMaterial();
				requestActiveImageSignal.dispatch(_activeImageProxy.collectionType, index);
			}
		}

		private function resetPaintings():void
		{
			_imageCache.thumbnailLoaded.remove(onThumbnailLoaded);
			_imageCache.thumbnailDisposed.remove(onThumbnailDisposed);
			disposePaintings();
			_visibleEndIndex = -1;
			_visibleStartIndex = 0;
			_imageCache.clear();
			_imageCache.thumbnailLoaded.add(onThumbnailLoaded);
			_imageCache.thumbnailDisposed.add(onThumbnailDisposed);
			//_paintingModes = new Vector.<int>();
		}

		//private var _paintingModes:Vector.<int>;

		public function setImageCollection(collection:GalleryImageCollection):void
		{
			_numPaintings = collection.numTotalPaintings;
			_paintings.length = _numPaintings;
			_lowQualityMaterials.length = _numPaintings;
			updateVisibility();
			_imageCache.replaceCollection(collection);

			if (collection.type == GalleryType.NONE)
				_activeImageProxy = null;

			_minSwipe = -PAINTING_OFFSET;
			_maxSwipe = -(PAINTING_OFFSET - (_numPaintings - 1) * PAINTING_SPACING);
		}

		private function updateVisibility():void
		{
			if (_numPaintings == 0) return;
			var index:int = getNearestPaintingIndex(_container.x);
			var visibleStart:int = index - 1;
			var visibleEnd:int = index + 2;
			var i:int;

			if (visibleStart < 0) visibleStart = 0;
			if (visibleStart >= _numPaintings) visibleStart = _numPaintings;
			if (visibleEnd >= _numPaintings) visibleEnd = _numPaintings;

			//REMOVE INVISIBLE ONES ON THE LEFT
			for (i = _visibleStartIndex; i < visibleStart; ++i) {
				if (_paintings[i]) {
					destroyPainting(i);
				}
			}
			//SHOW NEEDED ONES
			for (i = visibleStart; i < visibleEnd; ++i) {
				if (!_paintings[i])
					createPainting(i);
			}
			//REMOVE INVISIBLE ONES ON THE RIGHT
			for (i = Math.min(_visibleEndIndex,_paintings.length-1) ; i >=visibleEnd ; --i) {
				//if (_paintings.length>0&&_paintings[i])
				if(_paintings.length>i-1 && _paintings[i]){
					destroyPainting(i);
				}
			}

			_visibleStartIndex = visibleStart;
			_visibleEndIndex = visibleEnd;
		}

		private function createPainting(index:int):void
		{
			var texture:Texture2DBase = _imageCache.getThumbnail(index);
			texture ||= _loadingTexture;

			var material:TextureMaterial = new TextureMaterial(texture);
			material.lightPicker = _lightPicker;
			material.mipmap = false;
			//material.alphaBlending=true;
			var stencilMethod:StencilMethod = new StencilMethod();
			stencilMethod.referenceValue = 40;
			stencilMethod.compareMode = Context3DCompareMode.NOT_EQUAL;
			material.addMethod(stencilMethod);

			_lowQualityMaterials[index] = material;


			_paintings[index] = new GalleryPaintingView(_paintingGeometry, material);
			_paintings[index].x = index * PAINTING_SPACING;


			if (GalleryImageProxy(_imageCache.proxies[index]))
				_paintings[index].showRibbon(GalleryImageProxy(_imageCache.proxies[index]).paintingMode == PaintMode.COLOR_MODE, _ribbon);

			// in case the active painting was moved out of sight and disposed, reset the HQ material
			// UNLESS it hasn't finished loading!
			if (!_loadingHQ && _showHighQuality && _highQualityIndex == index) {
				_paintings[index].material = _highQualityMaterial;
			}

			_container.addChild(_paintings[index]);

			//TweenLite.killTweensOf(_paintings[index]);
			//TweenLite.from(_paintings[index],0.5,{y:300,ease:Expo.easeOut});


		}

		public function dispose():void
		{
			_view.camera.removeEventListener(Object3DEvent.SCENETRANSFORM_CHANGED, onCameraMoved);
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			if ( _view.scene.contains(_container) ) _view.scene.removeChild(_container);
			disposePaintings();
			_container.dispose();
			_imageCache.thumbnailDisposed.removeAll();
			_imageCache.thumbnailLoaded.removeAll();
			_imageCache.loadingComplete.remove(onAllThumbnailsLoaded);
			_imageCache.clear();
			//_paintingModes = null;
			_paintingGeometry.dispose();
			_loadingTexture.dispose();
			if ( _paintingOccluder.geometry )_paintingOccluder.geometry.dispose();
			_paintingOccluder.dispose();
			//TO FIX. MAKES PROBLEM WHEN STARTING A PAINTING
			//if(_ribbon.material)_ribbon.material.dispose();
			_ribbon.geometry.dispose();
			disposeHighQualityMaterial();
			stopInteraction();
		}

		private function onCameraMoved(event:Object3DEvent):void
		{
			updateSwipeInteractionRect();
		}

		private function disposeHighQualityMaterial():void
		{
			removeHighQualityMaterial();
			if (_highQualityColorTexture) {
				_fullsizeCompositedTexture.dispose();
				_highQualityColorTexture.dispose();
				_highQualityNormalSpecularTexture.dispose();
				_fullsizeCompositedTexture.dispose();
				_highQualityColorTexture = null;
				_highQualityNormalSpecularTexture = null;
				_fullsizeCompositedTexture = null;
			}
		}

		private function disposePaintings():void
		{
			for (var i:int = 0; i < _numPaintings; ++i) {
				if (_paintings[i])
					destroyPainting(i);
			}
		}

		private function destroyPainting(i:int):void
		{
			var painting:GalleryPaintingView = _paintings[i];
			if (_container.contains(painting))
				_container.removeChild(painting);
			painting.dispose();
			_lowQualityMaterials[i].dispose();
			_paintings[i] = null;
			_lowQualityMaterials[i] = null;
		}

		private function onThumbnailLoaded(imageProxy:GalleryImageProxy, thumbnail:RectTextureBase):void
		{
			if (_paintings[imageProxy.index]) {
				_lowQualityMaterials[imageProxy.index].texture = thumbnail;
				_paintings[imageProxy.index].showRibbon(imageProxy.paintingMode == PaintMode.COLOR_MODE, _ribbon);
			}
		}

		private function onThumbnailDisposed(imageProxy:GalleryImageProxy):void
		{
			// this probably also means the painting shouldn't be visible anymore
			var painting:GalleryPaintingView = _paintings[imageProxy.index];
			if (painting) {
				_lowQualityMaterials[imageProxy.index].texture = _loadingTexture;

				if (painting.parent)
					_container.removeChild(painting);
			}
		}

		private function onAllThumbnailsLoaded():void
		{
			// we can load the high resolution now for
			if (_showHighQuality){
				showHighQualityMaterial();
			}
		}

		private function onFullsizedCompositeComplete(compositedFullSize:BitmapData):void
		{
			//HAD TO ADD THIS CONDITION TO FOOLPROOF. MIGHT WANT TO CHECK IT OUT LATER
			if(_fullsizeCompositedTexture){
				_fullsizeCompositedTexture.bitmapData =compositedFullSize;
				_fullsizeCompositedTexture.getTextureForStage3D(_stage3DProxy);
				_highQualityMaterial.albedoTexture = _fullsizeCompositedTexture;
				_highQualityMaterial.normalSpecularTexture = _stillLoadingNormalSpecularTexture;

				compositedFullSize.dispose();
	
				// it may have been disposed before load finished?
				if (_activeImageProxy && _paintings[_activeImageProxy.index])
					_paintings[_activeImageProxy.index].material = _highQualityMaterial;
	
				_activeImageProxy.loadSurfaceData(onSurfaceDataComplete, onSurfaceDataError, onSurfaceColorDataComplete);
			}
		}

		private function onSurfaceColorDataComplete(galleryVO:PaintingGalleryVO):void
		{

			// it may have been disposed before load finished?
			if (_activeImageProxy && _paintings[_activeImageProxy.index])
				_paintings[_activeImageProxy.index].material = _highQualityMaterial;
		}

		private function onSurfaceDataComplete(galleryVO:PaintingGalleryVO):void
		{


			//MATHIEU: NOW WE ONLY DISPLAY WHEN BOTH THE COLOR AND BUMP HAVE BEEN LOADED
			// if view disposed, sometimes loading doesn't close in time?
			if (_highQualityNormalSpecularTexture) {

				//COLOR MAP
				_highQualityColorTexture.bitmapData = galleryVO.colorData;
				_highQualityColorTexture.getTextureForStage3D(_stage3DProxy);
				_highQualityMaterial.albedoTexture = _highQualityColorTexture;
				//_highQualityMaterial.normalSpecularTexture = _stillLoadingNormalSpecularTexture;

				//NORMAL MAP
				_highQualityNormalSpecularTexture.bitmapData = galleryVO.normalSpecularData;
				_highQualityNormalSpecularTexture.getTextureForStage3D(_stage3DProxy);
				_highQualityMaterial.normalSpecularTexture = _highQualityNormalSpecularTexture;
			}

			_highQualityIndex = _activeImageProxy.index;


			_loadingHQ = false;
			galleryVO.dispose();
		}

		private function onSurfaceDataError():void
		{
			// TODO: Show error
		}

		private function onAddedToStage(event:Event):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
		}
	}
}