package Components
{
	import flash.events.MouseEvent;
	import flash.filters.BitmapFilterQuality;
	import flash.geom.Point;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.controls.Image;
	import mx.controls.Menu;
	import mx.core.FlexGlobals;
	import mx.events.MenuEvent;
	
	import skins.Item_images_skin;
	
	import spark.components.supportClasses.SkinnableComponent;
	import spark.filters.GlowFilter;
	
	
	
	
	public class Item_image extends SkinnableComponent  implements Component
	{
		/*
		*parentLink:itemImage Out degree
		*childrenLinks:itemImage In degree
		*adjLinks:itemImage Out degree and In degree(undirected)
		*/
		private var parentLink:ArrayCollection = new ArrayCollection();
		private var childrenLinks:ArrayCollection = new ArrayCollection();	
		private var adjLinks:ArrayCollection = new ArrayCollection();	
		private var time:String = "";
		private var counter:int = 0;
		
		[Bindable]
		public var source:String;
		
		[Bindable]
		public var title:String;
		
		
		/***********partial switch related set***************/
		public function setSwitch_id(_id:String):void{}		
		public function setSwitch_name(_name:String):void{}
		public function setCrl_id(c_id:String):void{}
		public function setDp_id(d_id:String):void{}
		public function setN_table(_n:int):void{}
		public function setDp_desc(d_d:String):void{}
		public function setSw_desc(s_d:String):void{}
		public function setHw_desc(h_d:String):void{}
		public function setMfr_desc(m_d:String):void{}
		public function setSerial_num(s_n:String):void{}
		/*****************End*****************************/
		
		/******************partial host related set***************/
		public function setHost_ID(_id:String):void{}
		public function setHost_Name(_name:String):void{}
		public function setHost_Config(_config:int):void{}
		public function setHost_IP(_ip:String):void{}
		public function setSwitch_ID(s_id:String):void{}		
		public function setMac_Add(_add:String):void{}
		public function setimage(_add:int):void{}
		public function setflavor(_add:int):void{}
		public function getHost_IP():String{return "";}
		public function getHost_Config():int{return 0;}
		public function getimage():int{return -1;}
		public function getflavor():int{return -1;}
		public function setHost_Subnet(_add:String):void{}
		public function getHost_Subnet():String{return "";}
		/*****************End*****************************/
		
		/******************partial controller related set***************/
		public function setCon_id(_id:String):void{}
		public function setCon_type(_type:String):void{}
		public function setRest_url(_url:String):void{}
		public function setCon_name(_name:String):void{}
		public function getCon_type():String{return "";}
		public function getCon_id():String{return "";}
		//setflavor
		//getflavor
		/*****************End*****************************/
	
		public function getadjLinks():ArrayCollection {
			return this.adjLinks;
		}
		
		public function setadjLinks(adjLinks:ArrayCollection):void {
			this.adjLinks = adjLinks;
		}
		
		public function getChildrenLinks():ArrayCollection {
			return this.childrenLinks;
		}
		
		public function setChildrenLinks(childrenLinks:ArrayCollection):void {
			this.childrenLinks = childrenLinks;
		}
		
		public function getTime():String {
			return this.time;
		}
		
		public function setTime(_time:String):void {
			this.time = _time;
		}
		
		public function getCounter():int {
			return this.counter;
		}
		
		public function setCounter(_counter:int):void {
			this.counter = _counter;
		}
		
		public function getParentLink():ArrayCollection {
			return this.parentLink;
		}
		
		public function setParentLink(parentLink:ArrayCollection):void {
			this.parentLink = parentLink;
		}		
		
		public function Item_image()
		{
			super();			
			this.addEventListener(MouseEvent.CLICK,clickEvent);
		}
		
		public function settitle(str:String):void{
			this.title = str;
		}
		
		public function gettitle():String {
			return this.title;
		}
		
		public function setXY(xvalue:int,yvalue:int):void{
			this.x = xvalue;
			this.y = yvalue;
		}	
		
		public function Delete():void {	
			
			var parentLinks:ArrayCollection = this.getParentLink();
			var childrenLinks:ArrayCollection = this.getChildrenLinks();
			//delete Childrenlink's opposite adjacent edges
			for(var j1:int=0; j1< childrenLinks.length; j1++){
				var other_parentLinks:ArrayCollection = Item_image(childrenLinks[j1].toObj).getParentLink();
				var other_adjLinks_2:ArrayCollection = Item_image(childrenLinks[j1].toObj).getadjLinks();
				for(var j2:int=0; j2< other_parentLinks.length; j2++ ){
					if(other_parentLinks[j2].fromObj == this){
						other_parentLinks.removeItemAt(j2);
						break;
					}
				}
				for(var j3:int=0; j3< other_adjLinks_2.length;j3++){
					if((other_adjLinks_2[j3].toObj == this)||(other_adjLinks_2[j3].fromObj == this)){
						other_adjLinks_2.removeItemAt(j3);
						break;
					}
				}
			}
			
			//delete Parentlink opposite adjacent edges
			for(var i1:int=0; i1< parentLinks.length; i1++){
				var other_childrenLinks:ArrayCollection = parentLinks[i1].fromObj.getChildrenLinks();
				var other_adjLinks:ArrayCollection = parentLinks[i1].fromObj.getadjLinks();
				for(var i2:int=0; i2< other_childrenLinks.length; i2++ ){
					if(other_childrenLinks[i2].toObj == this){
						other_childrenLinks.removeItemAt(i2);
						break;
					}
				}
				for(var i3:int=0; i3< other_adjLinks.length;i3++){
					if((other_adjLinks[i3].toObj == this)||(other_adjLinks[i3].fromObj == this)){
						other_adjLinks.removeItemAt(i3);
						break;
					}
				}
			}
			
			this.source = null;
			this.title = null;
			this.setStyle("skinClass",skins.Item_images_skin);
			
			//delete object's adjacent edges
			for(var i:int=0; i < parentLinks.length; i++) {
				var parentLink:Link = parentLinks.getItemAt(i) as Link;
				parentLink.Deleteadj();
			}
			for(var j:int=0; j < childrenLinks.length; j++) {
				var childLink:Link = childrenLinks.getItemAt(j) as Link;
				childLink.Deleteadj();
			}
			
			delete this;
		}
		
		
		public function clickEvent(event:MouseEvent):void{
			var color:Number =0x000000;//shadow color  
			var alpha:Number =0.5; //shadow transparency, less value, more transparent  
			var blurX:Number = 35;  //width of the left and right shadows  
			var blurY:Number = 35;  //the shadow width of the upper and lower borders  
			var strength:Number = 2;  
			var inner:Boolean = true;  
			var knockout:Boolean = false;  
			var quality:Number = BitmapFilterQuality.HIGH;  
			
			
			if(FlexGlobals.topLevelApplication.selectedObj){
				FlexGlobals.topLevelApplication.selectedObj.filters=[];
				FlexGlobals.topLevelApplication.selectedObj.recover();
			}
			
			FlexGlobals.topLevelApplication.selectedObj = this;
			filters = [new GlowFilter(color,alpha,blurX, blurY,strength, quality,inner,knockout)];			
		}
		
		public function recover():void{}
	}
}