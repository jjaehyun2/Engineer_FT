package application.assetLibs{

	import flash.events.ProgressEvent;
	import flash.events.Event;
	import flash.text.Font;
	
	public class FontLoader extends LoaderCore {
		
		public function FontLoader(url:String) {
			_callLoadAssets(url);
		}
		
		override public function _onComplete(event:Event):void {
		
			try {
				
				var $adObj:Object = event.target.applicationDomain;
				var $etcObj:Object = event.target.content;				
				
				/*var Syl:Class = $adObj.getDefinition("SylfaenDF3") as Class;
				var BPG_Nino:Class = $adObj.getDefinition("BPG_Nino_MkhedruliDF3") as Class;
				var MyriadPro:Class = $adObj.getDefinition("MyriadProDF3") as Class;
				var ALKSanet:Class = $adObj.getDefinition("ALKSanetDF3") as Class;
				var BPG_Glaho_Arial:Class = $adObj.getDefinition("BPG_Glaho_ArialDF3") as Class;
				var BPGIngiriArialDF3:Class = $adObj.getDefinition("BPGIngiriArialDF3") as Class;
				
				Font.registerFont(ALKSanet);
				Font.registerFont(MyriadPro);
				Font.registerFont(BPG_Nino);
				Font.registerFont(Syl);
				Font.registerFont(BPG_Glaho_Arial);
				Font.registerFont(BPGIngiriArialDF3);*/
				
				var bpgArial:Class = $adObj.getDefinition("FontsLib__bpgArialRegular") as Class;
				var hKolh:Class = $adObj.getDefinition("FontsLib__hKolkhetyMtavBold") as Class;
				var bpgMrglovani:Class = $adObj.getDefinition("FontsLib__bpgMrglovaniCapsRegular") as Class;
				var lariSym:Class = $adObj.getDefinition("FontsLib__lariSymbol") as Class;
				Font.registerFont(bpgArial);
				Font.registerFont(bpgMrglovani);
				Font.registerFont(hKolh); 
				Font.registerFont(lariSym); 
				
				//_configureRemoveListeners();
				
				
				
				_loaded = true;
				
				dispatchEvent(new AppEvent(AppEvent.RESOURCE_LOADED, null ,true));
			} catch (e:TypeError) {
				
			}
		}
		
        override public function _onProgressHandler(event:ProgressEvent):void {
		  // MainSettings.instance.container.preloader._updateProgress(event.bytesTotal, event.bytesLoaded , null,'Loading Fonts...');
		   
			
        }
	}
}