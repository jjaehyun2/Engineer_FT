package net.psykosoft.psykopaint2.home.views.home
{

	import flash.display.BitmapData;
	import flash.events.LocationChangeEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.geom.Matrix3D;
	import flash.geom.Rectangle;
	import flash.media.StageWebView;
	import flash.net.SharedObject;
	import flash.net.URLVariables;
	
	import away3d.core.managers.Stage3DProxy;
	
	import net.psykosoft.psykopaint2.core.configuration.CoreSettings;
	import net.psykosoft.psykopaint2.core.managers.gestures.GestureManager;
	import net.psykosoft.psykopaint2.core.managers.rendering.ApplicationRenderer;
	import net.psykosoft.psykopaint2.core.managers.rendering.GpuRenderManager;
	import net.psykosoft.psykopaint2.core.managers.rendering.GpuRenderingStepType;
	import net.psykosoft.psykopaint2.core.models.LoggedInUserProxy;
	import net.psykosoft.psykopaint2.core.models.NavigationStateModel;
	import net.psykosoft.psykopaint2.core.models.NavigationStateType;
	import net.psykosoft.psykopaint2.core.models.PaintingModel;
	import net.psykosoft.psykopaint2.core.signals.NotifyGyroscopeUpdateSignal;
	import net.psykosoft.psykopaint2.core.signals.NotifyHomeDistanceToSectionChangedSignal;
	import net.psykosoft.psykopaint2.core.signals.NotifyProfilePictureUpdatedSignal;
	import net.psykosoft.psykopaint2.core.signals.RequestHidePopUpSignal;
	import net.psykosoft.psykopaint2.core.signals.RequestShowPopUpSignal;
	import net.psykosoft.psykopaint2.core.signals.ToggleDepthOfFieldSignal;
	import net.psykosoft.psykopaint2.core.views.base.MediatorBase;
	import net.psykosoft.psykopaint2.core.views.popups.tutorial.TutorialPopup;
	import net.psykosoft.psykopaint2.home.signals.NotifyHomeViewIntroZoomCompleteSignal;
	import net.psykosoft.psykopaint2.home.signals.NotifyHomeViewSceneReadySignal;
	import net.psykosoft.psykopaint2.home.signals.RequestHomeIntroSignal;
	import net.psykosoft.psykopaint2.core.signals.RequestRemoveBookSignal;

	public class HomeViewMediator extends MediatorBase
	{
		[Inject]
		public var view : HomeView;

		[Inject]
		public var stateModel : NavigationStateModel;

		[Inject]
		public var stage3dProxy : Stage3DProxy;

		[Inject]
		public var paintingModel : PaintingModel;

		[Inject]
		public var applicationRenderer : ApplicationRenderer;

		[Inject]
		public var notifyHomeViewIntroZoomComplete : NotifyHomeViewIntroZoomCompleteSignal;

		[Inject]
		public var requestHomeIntroSignal : RequestHomeIntroSignal;
		
		[Inject]
		public var requestRemoveBookSignal : RequestRemoveBookSignal;

		[Inject]
		public var notifyHomeViewSceneReadySignal : NotifyHomeViewSceneReadySignal;

		[Inject]
		public var notifyGyroscopeUpdateSignal : NotifyGyroscopeUpdateSignal;

		[Inject]
		public var userProxy : LoggedInUserProxy;

		// TODO: Make pop-ups truly modal using blockers instead of enforcing this on mediators!
		// probably should do the same for book, so "scrollEnabled" is not necessary at all
		[Inject]
		public var requestShowPopUpSignal : RequestShowPopUpSignal;

		[Inject]
		public var requestHidePopUpSignal : RequestHidePopUpSignal;

		[Inject]
		public var notifyProfilePictureUpdatedSignal : NotifyProfilePictureUpdatedSignal;

		[Inject]
		public var notifyHomeDistanceToSectionChangedSignal : NotifyHomeDistanceToSectionChangedSignal;

		[Inject]
		public var toggleDepthOfFieldSignal : ToggleDepthOfFieldSignal;

		private var _currentNavigationState : String;
		
		
		private var _localCache:SharedObject;
		private var _connectionCount:int=0;

		
		override public function initialize() : void
		{
			// Init.
			registerView(view);
			super.initialize();

			// Fully active states.
			manageStateChanges = false;

			requestShowPopUpSignal.add(onShowPopUp);
			requestHidePopUpSignal.add(onHidePopUp);
			requestHomeIntroSignal.add(onIntroRequested);
			requestRemoveBookSignal.add(onRequestRemoveBook)
			notifyGyroscopeUpdateSignal.add(onGyroscopeUpdate);
			notifyProfilePictureUpdatedSignal.add(onProfilePictureUpdate);
			toggleDepthOfFieldSignal.add(view.setDepthOfFieldEnabled);

			// From view.
			view.disabledSignal.add(onDisabled);

			view.activeSectionChanged.add(onActiveSectionChanged);
			view.distanceToSectionChanged.add(onDistanceToSectionChanged);
			view.sceneReadySignal.add(onSceneReady);

			view.stage3dProxy = stage3dProxy;
			view.enable();

			userProxy.loadUserImage();
			
			
			_localCache = SharedObject.getLocal("com.psykopaint.localData");
			if (_localCache.data["connectionCount"] )
			{
				_localCache.data["connectionCount"] = _localCache.data["connectionCount"]+1;
				_connectionCount = _localCache.data["connectionCount"];
				
			} else {
				//FIRST TIME WE CONNECT
				_connectionCount = 1;
				_localCache.data["connectionCount"] = _connectionCount;
				_localCache.flush();
			}
			
		}
		
		private function onRequestRemoveBook():void
		{
			//REMOVING BOOK FROM DISPLAY LIST WILL ALSO DISPOSE IT AUTOMATICALLY
			if(view.bookView&&view.bookView.parent) view.bookView.parent.removeChild(view.bookView);
			
		}
		
		override public function destroy() : void
		{
			view.disable();

			requestShowPopUpSignal.remove(onShowPopUp);
			requestHidePopUpSignal.remove(onHidePopUp);
			requestHomeIntroSignal.remove(onIntroRequested);
			view.activeSectionChanged.remove(onActiveSectionChanged);
			view.distanceToSectionChanged.remove(onDistanceToSectionChanged);

			view.disabledSignal.remove(onDisabled);
			view.sceneReadySignal.remove(onSceneReady);
			notifyGyroscopeUpdateSignal.remove(onGyroscopeUpdate);
			notifyProfilePictureUpdatedSignal.remove(onProfilePictureUpdate);

			toggleDepthOfFieldSignal.remove(view.setDepthOfFieldEnabled);

			view.dispose();

			super.destroy();
		}

		private function onActiveSectionChanged(sectionID : int) : void
		{
//			trace("HVM - onActiveSectionChanged: " + sectionID);
			switch (sectionID) {
				case HomeView.GALLERY:
					// bit of a hack to make the book show up with the painting details menu
					requestNavigationStateChange(NavigationStateType.GALLERY_BROWSE_MOST_RECENT);
					requestNavigationStateChange(NavigationStateType.GALLERY_PAINTING);
					break;
				case HomeView.EASEL:
					requestNavigationStateChange(NavigationStateType.HOME_ON_EASEL);
					break;
				case HomeView.HOME:
					requestNavigationStateChange(NavigationStateType.HOME);
					break;
				case HomeView.SETTINGS:
					requestNavigationStateChange(NavigationStateType.SETTINGS);
					break;
			}
		}

		private function onDistanceToSectionChanged(dis:Number):void {
			notifyHomeDistanceToSectionChangedSignal.dispatch(dis);
		}

		private function onShowPopUp(popUpType:String) : void
		{
			view.scrollingEnabled = false;
		}

		private function onHidePopUp() : void
		{
			updateScrollingForState();
		}

		private function onGyroscopeUpdate(orientationMatrix : Matrix3D) : void
		{
			view.setOrientationMatrix(orientationMatrix);
		}

		private function onProfilePictureUpdate(bitmapData : BitmapData):void
		{
			view.updateProfilePicture(bitmapData);
		}

		private function onDisabled() : void
		{
			GpuRenderManager.removeRenderingStep(view.renderScene, GpuRenderingStepType.NORMAL);
			_currentNavigationState = null;
		}

		// -----------------------
		// From app.
		// -----------------------

		private function onIntroRequested() : void
		{
			//TESTING ONLY
			//_connectionCount = 1;
			
			if(_connectionCount==1){
				///THE FIRST TIME WE USE THE APP THE TRANSITION IS SLOW
				view.playIntroAnimation(onIntroComplete,3);
				//THEN IT'S A BIT FASTER
			}else if(_connectionCount<=4){
				view.playIntroAnimation(onIntroComplete,1.5);
			}else {
				//IF WE COME BACK OFTEN IT'S MUCH FASTER
				view.playIntroAnimation(onIntroComplete,0.5);
			}
		}

		private function onIntroComplete() : void
		{
			//SHOW TUTORIAL POPUP ON FIRST LOAD
			if(_connectionCount==1)
			{
				view.scrollingEnabled=false;

				var tutorialPopup:TutorialPopup = new TutorialPopup();
				tutorialPopup.scaleX = tutorialPopup.scaleY = CoreSettings.GLOBAL_SCALING;
				view.stage.addChild(tutorialPopup);
				tutorialPopup.onTutorialPopupCloseSignal.add(onTutorialClose);
				
				
				//SEND NOTIFICATION ZOOM COMPLETE ON TUTORIAL CLOSE ONLY IF TUTORIAL VISIBLE
				notifyHomeViewIntroZoomComplete.dispatch();
				view.activateCameraControl();
				
			}else {
				notifyHomeViewIntroZoomComplete.dispatch();
				view.activateCameraControl();
			}
		}
		
		private function onTutorialClose():void{
			view.scrollingEnabled=true;
			
			
		}

		override protected function onStateChange(newState : String) : void
		{
			super.onStateChange(newState);
			
			// rendering should not happen until we're in an actual state
			if (!_currentNavigationState)
				GpuRenderManager.addRenderingStep(view.renderScene, GpuRenderingStepType.NORMAL, 0);

			_currentNavigationState = newState;

			// this is not ideal, but hey!

			switch (newState) {
				case NavigationStateType.HOME:
					view.activeSection = HomeView.HOME;
					break;
				case NavigationStateType.GALLERY_BROWSE_FOLLOWING:
				case NavigationStateType.GALLERY_BROWSE_MOST_LOVED:
				case NavigationStateType.GALLERY_BROWSE_MOST_RECENT:
				case NavigationStateType.GALLERY_BROWSE_YOURS:
				case NavigationStateType.GALLERY_BROWSE_USER:
				case NavigationStateType.GALLERY_PAINTING:
					view.activeSection = HomeView.GALLERY;
					break;
				case NavigationStateType.PICK_IMAGE:
					view.activeSection = HomeView.EASEL;
					break;
				case NavigationStateType.HOME_ON_EASEL:
					view.activeSection = HomeView.EASEL;
					//this is necessary to reactivate the camera panning when coming back from painting
					view.activateCameraControl();
					break;
				case NavigationStateType.SETTINGS:
					view.activeSection = HomeView.SETTINGS;
					break;
				case NavigationStateType.CROP:
					view.activeSection = HomeView.CROP;
					break;
			}

			updateScrollingForState();
		}

		private function updateScrollingForState() : void
		{
			if (_currentNavigationState == NavigationStateType.GALLERY_SHARE ||
				_currentNavigationState == NavigationStateType.CAPTURE_IMAGE ||
				_currentNavigationState == NavigationStateType.PICK_SAMPLE_IMAGE ||
				_currentNavigationState == NavigationStateType.PICK_USER_IMAGE_IOS ||
				_currentNavigationState == NavigationStateType.PICK_USER_IMAGE_DESKTOP ||
				_currentNavigationState == NavigationStateType.CROP
			)
				view.scrollingEnabled = false;
			else
				view.scrollingEnabled = true;
		}

		// From view.
		// -----------------------

		private function onSceneReady() : void
		{
			notifyHomeViewSceneReadySignal.dispatch();
		}
	}
}