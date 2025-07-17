class ConfigurationSite{
	
	  
 
   static var NEW_STAGE_WIDTH
   static var NEW_STAGE_HEIGHT

    static var URL_CSS
   static var MAIN_MENU
   static var LOGO_PATH 	    ////////pathway logo
   static var LOGO_REDIRECT  	////////REDIRECT logo
   static var LOGO_POSITION   ////////Logo position  
   static var MP3_DATE          ////////path mp3
   static var MENU_PRIMARY      ////////path menu primary
   static var MENU_SECONDARY    ////////path menu secondary
   static var FOOTER             ////////desc footer
   static var FOOTER_COLOR
   static var FOOTER_DESC
   static var HEADER	        ////////DESC HEADER
   static var DEFAULT_BACKGROUND ////////default background
   static var PATHWAY_TEMPLATE  ////////pathway for template
   static var FIRST_ID           //////first template (id)
   static var MENU_VISIBLE
   static var FOOTER_VISIBLE
   static var MP3_VISIBLE
   static var NEW_PAGE_WIDTH
   
   static var PRELOADER_BACKGROUND_COLOR
   static var PRELOADER_COLOR_TEXT
   static var PRELOADER_BAR_COLOR
   
   static var COLOR_BUTTON_SHOV_HIDE_PLAYER
   
   static var LOGO_X
   static var LOGO_Y
   
   static var SMOOTHING_BACKGROUND
   
   static var COMPANY_NAME
   
   static var SWF_ADRESS_ATTRIB
   static var SWF_TITLE_ATTRIB
  
   

   static var GRADIENT_BACKGROUND
   static var GRADIENT_COLOR
   
   
	
		
		

	
		
	
	static var __data:XML
	static var _loaded:Number
///////////////////////////////////////////////////////////////////////////////////////////////
static function load(xml){
		__data=new XML()
		__data.ignoreWhite=true
		__data.onLoad=function(){
			var len=this.firstChild.childNodes.length
			for(var i=0;i<len;i++){
				var nod=this.firstChild.childNodes[i]
				var node_name=nod.nodeName
				var value=nod.firstChild.nodeValue
				
				
				              
            	ConfigurationSite[node_name]=value
				
				
				
				
				
			}
		ConfigurationSite._loaded=1
		}
	__data.load(xml)
	}
///////////////////////////////////////////////////////////////////////////////////////////////	
	static function get loaded(){
		return _loaded
	}
///////////////////////////////////////////////////////////////////////////////////////////////	
	
	
	
	
	
	
	
}