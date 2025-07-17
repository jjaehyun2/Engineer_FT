class templateGallery.mvc.AbstractConfiguration{
	
	static var date:XML
	static var _loaded:Number


static function load(xml){
	
		date=new XML()
		date.ignoreWhite=true
		date.onLoad=function(){
			
			var len=this.firstChild.childNodes.length
			for(var i=0;i<len;i++){
				var nod=this.firstChild.childNodes[i]
				var node_name=nod.nodeName
				
				Configuration[node_name]=nod.firstChild.nodeValue
			}
			
			Configuration._loaded=1
		}
		
		date.load(xml)
	}
	
	static function get loaded(){
		return _loaded
	}
	
	
}