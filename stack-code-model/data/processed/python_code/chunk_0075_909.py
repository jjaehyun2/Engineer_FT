class templateMp3.Configuration {
	 
	
	///url mp3
	static var URL_MP3_LIST
	
	
	
	
	////color list 
	static var MP3_NUMBER_COLOR_ROL
	static var MP3_NUMBER_COLOR_OUT
	
	////color tools
	static var MP3_TOOLS_COLOR_ROL
	static var MP3_TOOLS_COLOR_OUT
	
	
	////equalizer
	static var MP3_EQUALIZER_COLOR_OLD
    static var MP3_EQUALIZER_COLOR_NORMAL
	
	/////Volume
	static var MP3_VOLUME_COLOR_BACKGROUND
	static var MP3_VOLUME_COLOR_CURRENT
	
	/////Speaker
	static var MP3_SPEAKER_COLOR_ROL
	static var MP3_SPEAKER_COLOR_OUT
	
	///////background
	static var MP3_BACKGROUND_COLOR
	
	/////progress
	static var MP3_BACKGROUND_PROGRESS
	static var MP3_CURRENT_PROGRESS
	
	////time view
	static var MP3_TIME_COLOR
	
	///////preloader
	static var MP3_PRELOADER_COLOR
	
	///////buffer
	static var MP3_BUFFER_COLOR
	
	//////align
	static var MP3_ALIGN_TITLE
	
	/////position X
	static var MP3_POSITION_X
	
	/////position Y
	static var MP3_POSITION_Y
	
	////width player
	static var MP3_WIDTH
	
	/////////////autoPlay
	static var MP3_AUTO_PLAY
	
	
	/////////volume first
	static var MP3_VOLUME_FIRST
	
	
	////color glow background
	static var MP3_GLOW_COLOR
	
	///color VOLUME glow scroll
	static var MP3_VOLUME_GLOW_COLOR_SCROLL
	
	///color PROGRESS glow scroll
	static var MP3_PROGRESS_GLOW_COLOR_SCROLL
	
	/////color circle
	static var MP3_VOLUME_COLOR_CIRCLE
	
	/////color circle
	static var MP3_PROGRESS_COLOR_CIRCLE
	
	
	/////circle visible
	static var MP3_CIRCLE_VISIBLE
	
	

	

	 
	
	
	
	
	
	
	
	
	
	
	
	
	
	static var __data:XML
	static var _loaded:Number
	
///////////////////////////////////////////////////////////////////////////////////////////////

static function load(xml){
		__data=new XML()
		__data.ignoreWhite=true
		__data.onLoad=function(){
	
			//Configuration.setXml(this)
			
		Configuration._loaded=1
		}
	__data.load(xml)
	}
	
///////////////////////////////////////////////////////////////////////////////////////////////	

	static function get loaded(){
		return _loaded
	}
	
///////////////////////////////////////////////////////////////////////////////////////////////	

static function setXml(xml_:XML){
	
			var len=xml_.firstChild.childNodes.length
			for(var i=0;i<len;i++){
				var nod=xml_.firstChild.childNodes[i]
				var node_name=nod.nodeName
				
				Configuration[node_name]=nod.firstChild.nodeValue
			}
	
}

//////////////////////////////////////////////////////////////////////////////////////////////
	
	
}