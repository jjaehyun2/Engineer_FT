package Components
{
	
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	import mx.controls.Menu;
	import mx.core.FlexGlobals;
	import mx.core.UIComponent;
	import mx.events.MenuEvent;
	import mx.managers.PopUpManager;
	import mx.rpc.events.ResultEvent;
	
	import skins.Item_images_skin;
	
	import view.S_DestinationLinkListTitleWindow;
	import view.S_PortListTitleWindow;
	import view.S_SimpleTitleWindowExample;
	import view.S_SourceLinkListTitleWindow;
	import view.Vnet_switchPropertiesWindow;
	
	import vo.Vnet_switch;
	
	public class Switch extends Item_image
	{
		[Bindable]
		public var Switch_id:String;
		
		[Bindable]
		public var Switch_name:String;
		
		[Bindable]
		public var port:int;
		
		[Bindable]
		public var type:String;
		
		public var Crl_id:String;
		public var Dp_id:String;
		private var N_table:int;
		private var Dp_desc:String;
		private var Sw_desc:String;
		private var Hw_desc:String;
		private var Serial_num:String;
		private var Mfr_desc:String;
		private var point:Point = new Point();
		
		/*****************mouse click and show menu*****************************/
		/*************************menu data********************************/	
		private var menuData:Array=
			[{label:'Properties'}, {label:'Delete'}];
		private var myMenu:Menu;
		
		
		/**********************click menu event ***************************************/	  
		private function menuHandler(event:MenuEvent):void {
			
			if(event.item.label=="Port List")
			{ 			
				showPortDialogue();
			} 	
			
			if(event.item.label=="Flow Table")
			{ 			
				showFlowDialogue();
			} 	
			
			if(event.item.label=="Link_src Switch List")
			{ 			
				showSourceLinkDialogue();
			} 	
			
			if(event.item.label=="Link_src_dst Switch List")
			{ 			
				showDestinationLinkDialogue();
			} 
			
			if(event.item.label=="Add and Delete Flow Entry") 
			{ 			
				AddFlowEntryDialogue();
			} 	
			// trace(event.item["label"]);
			if(event.item.label=="Delete") 
			{ 			
				this.Delete();
				Vnet_switch.vnet_delete(this.getSwitch_id());
			}	
			if(event.item.label=="Properties") 
			{ 			
				showDialogue();
			}
			if (event.item.label=="Add ACL Rule")
			{
				showAddFirewallRulerDialogue();
			}
			if(event.item.label=="Query ACL Rule")
			{
				showQueryFirewallRulerDialogue();
			}
			if(event.item.label=="Delete ACL Rule")
			{
				showDeleteFirewallRulerDialogue();
			}
			if(event.item.label=="Port Statistics")
			{
				mouseOverHandler();
			}
		}
/*****************pop up menu, when select menu item *****************************/	
		public function showMenu(event:MouseEvent):void{
			myMenu= Menu.createMenu(this,menuData, false); 			
			//click event
			myMenu.addEventListener("itemClick", menuHandler); 
			//pop up menu 
			point.x=event.stageX; 
			point.y=event.stageY;  
			myMenu.show(point.x , point.y); 
		}
		public function AddFlowEntryDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;			
		}
	
		public function showDialogue():void{
			/*  pop up myPanel, judge if can interact with parent component. when true, 
			blurring the background, and can not interact with parent component */				  
			FlexGlobals.topLevelApplication.activeItem = this;
			
			//  this.parent = this.host_IP;
			var myPanel:Vnet_switchPropertiesWindow = 
				Vnet_switchPropertiesWindow(PopUpManager.createPopUp(this, Vnet_switchPropertiesWindow, true)); 
			
			myPanel.x = 420;
			
			myPanel.y = 170;			
		}
		
		public function showPortDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;
			var myPanel:S_PortListTitleWindow = 
				S_PortListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, S_PortListTitleWindow, false)); 
			
			myPanel.x = 100;
			
			myPanel.y = 150;			
		}
		
		public function showFlowDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;		
		}
		
		public function showSourceLinkDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;
			var myPanel:S_SourceLinkListTitleWindow = 
				S_SourceLinkListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, S_SourceLinkListTitleWindow, false)); 
			
			myPanel.x = 100;
			
			myPanel.y = 150;				
		}
		
		public function showDestinationLinkDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;
			var myPanel:S_DestinationLinkListTitleWindow = 
				S_DestinationLinkListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, S_DestinationLinkListTitleWindow, false)); 
			
			myPanel.x = 100;
			
			myPanel.y = 150;			
		}
		
		public function showAddFirewallRulerDialogue():void{
			FlexGlobals.topLevelApplication.activeItem=this;	
		}
		
		public function showDeleteFirewallRulerDialogue():void
		{
			FlexGlobals.topLevelApplication.activeItem=this;
		}
		
		public function showQueryFirewallRulerDialogue():void
		{
			FlexGlobals.topLevelApplication.activeItem=this;
		}
		
/*****************End   *****************************/
		
/*****************  mouse move over *****************************/
		private function mouseOverHandler():void{
		}
		
/*****************  End   *****************************/
		
		
		public function Switch()
		{
			super();
			this.source = "images/switch_mini.jpg";
			setStyle("skinClass", skins.Item_images_skin);
			//enable double click(default as unable)		
			this.doubleClickEnabled = true;
			mouseChildren = false;
			this.addEventListener(MouseEvent.DOUBLE_CLICK,showMenu);
			//this.addEventListener(MouseEvent.MOUSE_OVER,mouseOverHandler);
			//this.addEventListener(MouseEvent.MOUSE_OUT,mouseOutHnadler);
			setPort();
		}
		
		public function setPort():void{
			this.port = 6634 +FlexGlobals.topLevelApplication.S_obj.length;
		}
/***************************get and set SwitchID**************************/	
		public function getSwitch_id():String{
			return this.Switch_id;
		}
		public override function setSwitch_id(_id:String):void{
			this.Switch_id=_id;
		}
/***************************get and set SwitchName**************************/	
		public function getName():String{
			return this.Switch_name;
		}
		public override function setSwitch_name(_name:String):void{
			this.Switch_name=_name;
		}
/****************************get and set Crl_id***************************/			
		public function getCrl_id():String{
			return this.Crl_id;
		}
		public override function setCrl_id(c_id:String):void{
			this.Crl_id=c_id;
		}
/**************************get and set Dp_id*****************************/		
		public function getDp_id():String{
			return this.Dp_id;
		}
		public override function setDp_id(d_id:String):void{
			this.Dp_id=d_id;
		}
/************************get and set N_table*****************************/
		public function getN_table():int{
			return this.N_table;
		}
		public override function setN_table(_n:int):void{
			this.N_table=_n;
		}
 /************************get and set Dp_desc*****************************/
		public function getDp_desc():String{
			return this.Dp_desc;
		}
		public override function setDp_desc(d_d:String):void{
			this.Dp_desc=d_d;
		}
 /************************get and set Sw_desc*****************************/
		public function getSw_desc():String{
			return this.Sw_desc;
		}
		public override function setSw_desc(s_d:String):void{
			this.Sw_desc=s_d;
		}
/************************get and set Hw_desc*****************************/
		public function getHw_desc():String{
			return this.Hw_desc;
		}
		public override function setHw_desc(h_d:String):void{
			this.Hw_desc=h_d;
		}
/************************get and set Mfr_desc*****************************/
		public function getMfr_desc():String{
			return this.Mfr_desc;
		}
		public override function setMfr_desc(m_d:String):void{
			this.Mfr_desc=m_d;
		}
/************************get and set Serial_num*****************************/
		public function getSerial_num():String{
			return this.Serial_num;
		}
		public override function setSerial_num(s_n:String):void{
			this.Serial_num=s_n;
		}
/*************************end***********************************************/
	}
}