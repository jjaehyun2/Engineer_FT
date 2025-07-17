import flash.display.MovieClip;
	import flash.events.Event;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	
	import mx.collections.ArrayCollection;

	
		private var myXML:XML = new XML();        
		private var FatTreeXMLURL:URLRequest = new URLRequest("dataprovider/FatTree.xml");
		private var BCubeXMLURL:URLRequest = new URLRequest("dataprovider/BCube.xml")
		private var myLoader:URLLoader;  //required FatTreeXMLURL or ICubeXMLURL
		public var nodeData:ArrayCollection = new ArrayCollection();
		public var linkData:ArrayCollection = new ArrayCollection();
		private var isXMLLoaded:int = 0;
		private var isFatTreeSel:int = 0;
		private var isBCubeSel:int = 0;
		
		public function detect():void{			
			myLoader.addEventListener("complete", xmlLoaded);	
		}
		private function xmlLoaded(event:Event):void
		{
			myXML = XML(myLoader.data);	
			nodeData.removeAll();
			linkData.removeAll();
			initdata();
			isXMLLoaded=1;
			if(isFatTreeSel==1 || isBCubeSel==1){
				DrawFatTree();				
			}
		}

		private function initdata():void{
			
			// iterate node
			var nodeNum:int = myXML.child("node").length();    
			for( var i:int = 0; i < nodeNum; i++ )                     
			{ 
				var node_item:Object = new Object(); 
				
				// iterate parameter
				var node_attNum:int = myXML.node[i].attributes().length();                    
				for (var j:int=0; j<node_attNum; j++) 
				{ 
					var node_attName:String = myXML.node[i].attributes()[j].name(); 
					var node_attValue:String = myXML.node[i].attribute(node_attName); 
					
					// set Object 
					node_item[node_attName] =node_attValue; 
				}   
				
				// add to ArrayCollection 
				nodeData.addItem(node_item); 
			}
			
			//iterate link
			var linkNum:int = myXML.child("link").length();
			for( var i1:int = 0; i1 < linkNum; i1++ )                     
			{ 
				var link_item:Object = new Object(); 
				
				// iterate parameter 
				var link_attNum:int = myXML.link[i1].attributes().length();                    
				for (var j1:int=0; j1<link_attNum; j1++) 
				{ 
					var link_attName:String = myXML.link[i1].attributes()[j1].name(); 
					var link_attValue:String = myXML.link[i1].attribute(link_attName); 
					
					// set Object 
					link_item[link_attName] = link_attValue; 
				}   
				
				// add to ArrayCollection 
				linkData.addItem(link_item); 
			} 
		}