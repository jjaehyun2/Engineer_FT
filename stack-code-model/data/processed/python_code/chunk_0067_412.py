package application.assetLibs{

	import application.MainSettings;
	import flash.events.ProgressEvent;
	import flash.events.Event;
	import flash.media.Sound;
	import flash.media.SoundChannel;
	import flash.media.SoundTransform;
	import dynamicSound.Bell1;

	
	public class SoundLoader extends LoaderCore {
		
		
		public function SoundLoader(url:String) {	
			
			_callLoadAssets(url);
			
		}
		
		override public function _onComplete(event:Event):void {
			
			try {
				var $o:Object = event.target.applicationDomain;
				
				
				/*var definitions:*;
				if ($o.hasOwnProperty("getQualifiedDefinitionNames")) {
				  definitions = $o["getQualifiedDefinitionNames"]();
				  for (var i:int = 0; i < definitions.length; i++) {
					  trace(definitions[i] + "\n")
				  }
				}*/
				
				/*var $sc:SoundChannel = new SoundChannel();
				var $s:Sound = new Bell1;
				$s.play();*/
				
				
				SoundLibrary.getSound.Bell1                         = $o.getDefinition("dynamicSound.Bell1") as Class;

				SoundLibrary.getSound.Bell2                         = $o.getDefinition("dynamicSound.Bell2") as Class;
				
				SoundLibrary.getSound.CardAction1                   = $o.getDefinition("dynamicSound.CardAction1") as Class;
				SoundLibrary.getSound.CardAction2                   = $o.getDefinition("dynamicSound.CardAction2") as Class;
				SoundLibrary.getSound.CardAction3                   = $o.getDefinition("dynamicSound.CardAction3") as Class;
				
				SoundLibrary.getSound.CardMove1                     = $o.getDefinition("dynamicSound.CardMove1") as Class;
				SoundLibrary.getSound.CardMove2                     = $o.getDefinition("dynamicSound.CardMove2") as Class;
				SoundLibrary.getSound.CardMove3                     = $o.getDefinition("dynamicSound.CardMove3") as Class;
			
				SoundLibrary.getSound.CardSlide1                    = $o.getDefinition("dynamicSound.CardSlide1") as Class;
				SoundLibrary.getSound.CardSlide2                    = $o.getDefinition("dynamicSound.CardSlide2") as Class;
				SoundLibrary.getSound.CardSlide3                    = $o.getDefinition("dynamicSound.CardSlide3") as Class;
				
				SoundLibrary.getSound.CardDeal                      = $o.getDefinition("dynamicSound.CardDeal") as Class;
				
				SoundLibrary.getSound.CardTurn1                     = $o.getDefinition("dynamicSound.CardTurn1") as Class;
				SoundLibrary.getSound.CardTurn2                     = $o.getDefinition("dynamicSound.CardTurn2") as Class;
				SoundLibrary.getSound.CardTurn3                     = $o.getDefinition("dynamicSound.CardTurn3") as Class;
				
				SoundLibrary.getSound.Notifi                        = $o.getDefinition("dynamicSound.Notifi") as Class;
				
				SoundLibrary.getSound.Turn                          = $o.getDefinition("dynamicSound.Turn") as Class;
				SoundLibrary.getSound.ChooseTrumpCard               = $o.getDefinition("dynamicSound.ChooseTrumpCard") as Class;
				SoundLibrary.getSound.NewGame                       = $o.getDefinition("dynamicSound.NewGame") as Class;
				SoundLibrary.getSound.GameOver                      = $o.getDefinition("dynamicSound.GameOver") as Class;
				SoundLibrary.getSound.SoundTimer                    = $o.getDefinition("dynamicSound.SoundTimer") as Class;
				
				SoundLibrary.getSound.GameLoose                     = $o.getDefinition("dynamicSound.GameLoose") as Class;
				SoundLibrary.getSound.GameWin                       = $o.getDefinition("dynamicSound.GameWin") as Class;
				SoundLibrary.getSound.GameScore                     = $o.getDefinition("dynamicSound.GameScore") as Class;
			
				
				_configureRemoveListeners();
				
				_loaded = true;
				
				dispatchEvent(new AppEvent(AppEvent.LIB_LOADED, null ,true));
			} catch (e:TypeError) {
				
			}
		}	
		
        override public function _onProgressHandler(event:ProgressEvent):void {
		   
		    MainSettings.instance.container.preloader._updateProgress(event.bytesTotal, event.bytesLoaded , null,'Loading Sounds Assets...');
			
        }
	}
}