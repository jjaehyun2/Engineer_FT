package com.illuzor.circles.tools {
	
	import com.distriqt.extension.adverts.AdvertPlatform;
	import com.distriqt.extension.adverts.AdvertPosition;
	import com.distriqt.extension.adverts.Adverts;
	import com.distriqt.extension.adverts.events.AdvertEvent;
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class AdsManager {
		
		private static const DEV_ID:String = "";
		private static const ADMOB_ID:String = "";
		
		private static var allCorrect:Boolean;
		private static var adsShowed:Boolean;
		
		public static function init():void {
			try {
				Adverts.init(DEV_ID);
				if (Adverts.isSupported) {
					Adverts.service.addEventListener(AdvertEvent.RECEIVED_AD, onAdvertEvent, false, 0, true );
					Adverts.service.addEventListener(AdvertEvent.ERROR, onAdvertEvent, false, 0, true );
					Adverts.service.addEventListener(AdvertEvent.USER_EVENT_DISMISSED, onAdvertEvent, false, 0, true );
					Adverts.service.addEventListener(AdvertEvent.USER_EVENT_LEAVE, onAdvertEvent, false, 0, true );
					Adverts.service.addEventListener(AdvertEvent.USER_EVENT_SHOW_AD, onAdvertEvent, false, 0, true );
					
					if (Adverts.service.isPlatformSupported(AdvertPlatform.PLATFORM_ADMOB )) {
						Adverts.service.initialisePlatform(AdvertPlatform.PLATFORM_ADMOB, ADMOB_ID);
						allCorrect = true;
					}
					
				} else {
					trace("ads not supported");
				}
			} catch (e:Error) {
				trace("ads error")
			}
		}
		
		public static function showAds():void {
			if (allCorrect) {
				var size:AdvertPosition = new AdvertPosition();
				size.verticalAlign = AdvertPosition.ALIGN_TOP;
				size.horizontalAlign = AdvertPosition.ALIGN_CENTER;
				Adverts.service.showAdvert(size);
				adsShowed = true;
			}
		}
		
		public static function hideAds():void {
			if (adsShowed) {
				Adverts.service.hideAdvert();
				adsShowed = false;
			}
		}
		
		private static function onAdvertEvent(e:AdvertEvent):void {
			switch (e.type) {
				case AdvertEvent.RECEIVED_AD:
					trace("reveive ad");
				break;
				case AdvertEvent.ERROR:
					trace("error ad", JSON.stringify(e.details));
				break;
				case AdvertEvent.USER_EVENT_DISMISSED:
					trace("USER_EVENT_DISMISSED ad");
				break;
				case AdvertEvent.USER_EVENT_LEAVE:
					trace("USER_EVENT_LEAVE ad");
				break;
				case AdvertEvent.USER_EVENT_SHOW_AD:
					trace("USER_EVENT_SHOW_AD ad");
				break;
			}
		}
		
	}
}