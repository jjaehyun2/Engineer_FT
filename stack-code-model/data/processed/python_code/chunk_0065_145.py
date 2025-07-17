package Components
{
	import flash.events.MouseEvent;
	import flash.filters.BitmapFilterQuality;
	import flash.geom.Point;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Image;
	import mx.controls.Menu;
	import mx.core.FlexGlobals;
	import mx.events.MenuEvent;
	
	import skins.Item_images_skin;
	
	import spark.components.supportClasses.SkinnableComponent;
	import spark.filters.GlowFilter;
	
	
	
	
	public class Item_image extends SkinnableComponent  implements Component
	{
		private var parentLink:ArrayCollection = new ArrayCollection();
		private var childrenLinks:ArrayCollection = new ArrayCollection();	
		
		[Bindable]
		public var source:String;
		
		[Bindable]
		public var title:String;
		
		
		/***********partial switch configure function***************/
		public function setSwitch_id(_id:int):void{}		
		public function setSwitch_name(_name:String):void{}
		public function setCrl_id(c_id:int):void{}
		public function setDp_id(d_id:String):void{}
		public function setN_table(_n:int):void{}
		public function setDp_desc(d_d:String):void{}
		public function setSw_desc(s_d:String):void{}
		public function setHw_desc(h_d:String):void{}
		public function setMfr_desc(m_d:String):void{}
		public function setSerial_num(s_n:String):void{}
		/*****************End*****************************/
		
		/**********partial host configure function***************/
		public function setHost_ID(_id:int):void{}
		public function setHost_Name(_name:String):void{}
		public function setHost_IP(_ip:String):void{}
		public function setSwitch_ID(s_id:int):void{}		
		public function setMac_Add(_add:String):void{}
		/*****************End*****************************/
		
		/**********partial controller configure function************/
		public function setCon_id(_id:int):void{}
		public function setCon_type(_type:String):void{}
		public function setRest_url(_url:String):void{}
		public function setCon_name(_name:String):void{}
		/*****************End*****************************/
	
		
		public function getChildrenLinks():ArrayCollection {
			return this.childrenLinks;
		}
		
		public function setChildrenLinks(childrenLinks:ArrayCollection):void {
			this.childrenLinks = childrenLinks;
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
		
		public function setXY(xvalue:int,yvalue:int):void{
			this.x = xvalue;
			this.y = yvalue;
		}	
		
		public function Delete():void {	
			this.source = null;
			this.title = null;
			this.setStyle("skinClass",skins.Item_images_skin);
			var parentLinks:ArrayCollection = this.getParentLink()
			for(var i:int=0; i < parentLinks.length; i++) {
				var parentLink:Link = parentLinks.getItemAt(i) as Link;
				parentLink.Delete();
			}
			var childrenLinks:ArrayCollection = this.getChildrenLinks();
			for(var j:int=0; j < childrenLinks.length; j++) {
				var childLink:Link = childrenLinks.getItemAt(j) as Link;
				childLink.Delete();
			}
			delete this;
		}
		
		
		public function clickEvent(event:MouseEvent):void{
			var color:Number =0x000000;//shadow color
			var alpha:Number =0.5; //adjust the opacity of the shadow. Smaller value. More hyaline.
			var blurX:Number = 35;  //width of shadow(left and right).
			var blurY:Number = 35;  //width of shadow(bottom and up).
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