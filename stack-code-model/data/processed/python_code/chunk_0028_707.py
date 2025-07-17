// MindJolt API Library
// ActionScript 2

class MindJoltAPI {
	
	public static var service:Object = { connect: connect }
	public static var ad:Object = { showPreGameAd: showPreGameAd }
	
	public static function showPreGameAd(options:Object):Void {
		if (MindJoltAPI.clip.mindjolt_api_service == undefined) {
			trace("[MindJoltAPI] You must call MindJoltAPI.service.connect before MindJoltAPI.ad.showPreGameAd.")
		}
		if (options == null) {
			options = {}
		}
		if (service.showPreGameAd != undefined) {
			service.showPreGameAd(options)
		} else {
			MindJoltAPI.options = options
			if (options["ad_started"] == null) {
				(options["clip"] != null ? options["clip"] : _root).stop()
			}
		}
	}

	/*
		--------------
		nuts and bolts
		--------------
	*/
	
	private static var gameKey:String
	private static var clip:MovieClip
	private static var callback:Function
	private static var options:Object
	private static var version:String = "1.0.4"
	
	private static function load_service_complete():Void {
		if (clip.mindjolt_api_service.service != null) {
			service = clip.mindjolt_api_service.service
			trace ("[MindJoltAPI] service successfully loaded")
			service.connect(gameKey, clip, callback)
			if (options != null) {
				service.recordAction("showPreGameAd(" + options + ");");
				service.showPreGameAd(options)
			}
			service.getLogger().info("MindJoltAPI loader version [" + version + "]")
		} else {
			trace("[MindJoltAPI] failed to load.")
		}
	}
	
	private static function connect(gameKey:String, clip:MovieClip, callback:Function):Void {
		MindJoltAPI.gameKey = gameKey
		MindJoltAPI.clip = clip != null ? clip : _root
		MindJoltAPI.callback = callback
		if (service.submitScore == undefined) {
			System.security.allowDomain("static.mindjolt.com")
			var mindjolt_api = MindJoltAPI.clip.createEmptyMovieClip("mindjolt_api_service", 10000)
			var api_path:String = _level0["mjPath"] != undefined ? _level0["mjPath"] : "http://static.mindjolt.com/api/as2/api_local_as2.swf"
			var loader:MovieClipLoader = new MovieClipLoader()
			loader.addListener({ onLoadInit: load_service_complete, onLoadError: load_service_complete })
			loader.loadClip(api_path, mindjolt_api)
		}
	}
}