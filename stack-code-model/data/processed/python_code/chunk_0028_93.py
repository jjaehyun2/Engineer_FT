class templateNewsy.Configuration{
	
	
	
	
/////////////////////////////////////////////////Configuration GALLERY	

	static var THUMB_WIDTH:Number=134
	static var THUMB_HEIGHT:Number=104
	static var TIMESLIDE:Number
	static var URL_CONFIG_FLV:String
	static var TIME_INTRO:Number
	static var TIME_EXIT:Number
	
	static var BACKGROUND_COLOR_NEWSY
	
	///css
	static var URL_CSS
	static var CSS_STYLE
	
	
	static var URL_PLAYER_FLV:String
	
	
	static var BACKGROUND_SCROLL_COLOR
	static var SCROLL_COLOR
	static var COLOR_SEP

	
	
	
	
	
	
		
	
	
		
		
	
	static var __data:XML
	static var _loaded:Number
	
///////////////////////////////////////////////////////////////////////////////////////////////

static function load(xml){
		__data=new XML()
		__data.ignoreWhite=true
		__data.onLoad=function(){
			Configuration.setXml(this)
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
				var value=nod.firstChild.nodeValue
				

      		if(!isNaN(value)){
				Configuration[node_name]=Number(value)
				}
				else if(value=="true"){
				Configuration[node_name]=true
				}
				else if(value=="false"){
				Configuration[node_name]=false
				}
				else{
				Configuration[node_name]=String(value)
				}
                
                if(Configuration[node_name]=="undefined"){
					Configuration[node_name]=undefined
				}
				
			}
	
}


//////////////////////////////////////////////////////////////////////////////////////////////
	
}