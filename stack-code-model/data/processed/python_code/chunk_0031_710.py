package Components
{
	
	
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import flash.events.TimerEvent;
	import flash.geom.Point;
	import flash.media.Video;
	import flash.net.URLRequest;
	import flash.utils.Timer;
	import flash.utils.setInterval;
	import flash.utils.setTimeout;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Image;
	import mx.controls.Label;
	import mx.controls.Menu;
	import mx.core.FlexGlobals;
	import mx.events.MenuEvent;
	import mx.managers.CursorManager;
	import mx.managers.PopUpManager;
	import mx.messaging.AbstractConsumer;
	
	import org.bytearray.gif.events.GIFPlayerEvent;
	import org.bytearray.gif.player.GIFPlayer;
	
	import spark.effects.Animate;
	import spark.effects.Move;
	
	import view.L_SimpleTitleWindowExample;
	

	public class Link extends Sprite implements Component
	{
		public  var fromObj:Item_image;		
		public  var toObj:Item_image;
		private var link_id:int;
		private var myMenu:Menu;
		public var f_port:int;
		public var t_port:int;		
		private var point:Point = new Point();	
		/*private var move1:Move = new Move();
		private var move2:Move =  new Move();
		private var target1:DataPackage = new DataPackage();
		private var target2:DataPackage =  new DataPackage();
		private var timer:Timer = new Timer(5000);
		private var counter:int = 0;*/
		
	/*	public function timerMethod():void{
			setInterval(reset,5000);
		}
		
		public function timerFunction(timerevent:TimerEvent):void{
			reset();
		}
		
		public function reset():void{
			move1.end();
			move2.end();
			target1.visible = false;
			target2.visible = false;
			moveFunction();
		}	*/
		
		/****************impl: mouse click and menu pop up****************/
		/*************************menu set********************************/	
				
	    private var menuData:Array=
		[{label:'properties'},{label:'remove'}];
		/*****************impl menu pop up, define function to handle entry select event*********************/			
      public function showMenu(event:MouseEvent):void{
		  	
			myMenu= Menu.createMenu(this,menuData, false); 			
			//menuHandler is responsible to handle mouse click event
			myMenu.addEventListener("itemClick", menuHandler); 
			//get mouse location and pop up dialogue
			point.x=event.stageX; 
			point.y=event.stageY;  
			myMenu.show(point.x , point.y); 
			
		}
	  /**********************define function to handle menu click event***************************************/	 
	  private function menuHandler(event:MenuEvent):void {		 
		  //click remove entry
		  // trace(event.item["label"]);
		  if(event.item.label=="properties")
		  {
			  showDialogue();
		  }
		  if(event.item.label=="remove") 
		  { 			
			  Delete(); 
		  } 
		  
	  }
	  /**************************dialogue pop up**************************************/
	  public function showDialogue():void{
		  /*  the third parameter 'true' represents: if have access to parent elements afer myPanel window popping up
		  in the case of 'true', background blur effect appears, can not have access to parent elements */	  
		  FlexGlobals.topLevelApplication.activeLink = this;
		  
		  //  this.parent = this.host_IP;
		  var myPanel:L_SimpleTitleWindowExample = 
			  L_SimpleTitleWindowExample(PopUpManager.createPopUp(this, L_SimpleTitleWindowExample, true)); 
		  
		  myPanel.x = 420;
		  
		  myPanel.y = 170;			
	  }
 /*****************Impl line stronger*****************************/
	  public function bold(event:MouseEvent):void{
		  if(FlexGlobals.topLevelApplication.selectedObj){
			  FlexGlobals.topLevelApplication.selectedObj.filters=[];
			  FlexGlobals.topLevelApplication.selectedObj.recover();
		  }		
		  FlexGlobals.topLevelApplication.selectedObj = this;		 
		  this.graphics.clear();
		  this.graphics.moveTo(fromObj.x + 27, fromObj.y + 16);
		  this.graphics.lineStyle(7, 0xFF0000 , 1);
		  this.graphics.lineTo(toObj.x + 27, toObj.y + 16);		 
	  }
	  
 /*****************Impl line recover*****************************/
	  public function recover():void{
		  this.graphics.clear();
		  this.graphics.moveTo(fromObj.x + 27, fromObj.y + 16);
		  this.graphics.lineStyle(3, 0x0000FF , 1);
		  this.graphics.lineTo(toObj.x + 27, toObj.y + 16);
	  }
	  
	  
	  
	  
/**************************dialogue END***********************************************/
	
	  
/**************************constructed function**********************************************/
	  
		public function Link(fromObj:Item_image, toObj:Item_image)
		{
			super();
			this.buttonMode=true;
			this.useHandCursor=true;
			this.doubleClickEnabled=true;
			this.addEventListener(MouseEvent.CLICK,bold);
			this.addEventListener(MouseEvent.DOUBLE_CLICK,showMenu);
			this.fromObj = fromObj;
			this.toObj = toObj;			
			setSrcDstPort();
			this.link_id = FlexGlobals.topLevelApplication.getlink_num();			
			drawLine();	
			//setTimeout(timerMethod,5000);
		}
		
		public function setSrcDstPort():void{
			if(fromObj.className=="Switch" && toObj.className=="Switch"){
				var ttemp:Switch = this.toObj as Switch;
				var ftemp:Switch = this.fromObj as Switch;
				var ltemp:ArrayCollection = FlexGlobals.topLevelApplication.ac_link;
				var ptemp:ArrayCollection = FlexGlobals.topLevelApplication.ac_port;
				for(var i:int=0;i<ltemp.length;i++){
					if(ltemp[i].src_switch_id==ftemp.getSwitch_id() &&
					   ltemp[i]. dst_switch_id==ttemp.getSwitch_id()){
						for(var j:int=0;j<ptemp.length;j++){
							if(ptemp[j].id==ltemp[i].src_port_id){
								f_port = ptemp[j].port_no;
							}
							if(ptemp[j].id==ltemp[i].dst_port_id){
								t_port = ptemp[j].port_no;
							}
						}
					}
				}
			}
			if(fromObj.className=="Controller" && toObj.className=="Switch"){
				t_port=65534;
				f_port=0;
			}
		}
		
		public function getlink_id():int{
			return this.link_id;
		}
		
		public function drawLine():void {
			this.graphics.moveTo(fromObj.x + 27, fromObj.y + 16);
        	this.graphics.lineStyle(3, 0x0000FF, 1);
        	this.graphics.lineTo(toObj.x + 27, toObj.y + 16);	
			
		}
		
		public function redraw():void {			
			if(fromObj != null && toObj != null) {
				this.graphics.clear();
				drawLine();
			}			
		}	 	
		
		public function Delete():void{
			if(fromObj != null && toObj != null) {
				this.graphics.clear();
				fromObj=null;
				toObj=null;
				FlexGlobals.topLevelApplication.selectedObj=null;
				delete this;
		   }
		}
	}
}