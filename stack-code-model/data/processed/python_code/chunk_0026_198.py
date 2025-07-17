package Components
{
	import Main.Vnet_Workbench;
	
	import flash.events.MouseEvent;
	import flash.geom.Point;
	
	import mx.controls.Alert;
	import mx.controls.Menu;
	import mx.core.FlexGlobals;
	import mx.events.MenuEvent;
	import mx.managers.PopUpManager;
	
	import skins.Item_images_skin;
	
	import view.C_SimpleTitleWindowExample;
	import view.C_SwitchListTitleWindow;
	import view.Vnet_controllerPropertiesWindow;
	import view.Vnet_hostConsoleWindow;
	
	import vo.Vnet_controller;
	
	public class Controller extends Item_image
	{
		private var Con_id:String;
		private var Con_type:String;
		private var Rest_url:String;
		private var Con_name:String;
		private var point:Point = new Point();
		public var flavor:int = -1;
		public var image:int = -1;
		
		[Bindable]
		public var console_url:String;
		
		[Bindable]
		public var controller_ip:String;
				
		/*****************mouse click and show menu *****************************/
		/*************************menu data********************************/	
		private var menuData:Array=
			[{label:'Switch List'},{label:'Console'},{label:'Properties'},{label:'Delete'}];
		private var myMenu:Menu;
	
	
		/**************************pop up dialogue************************************************/
		public function showDialogue():void{
			/*  pop up myPanel, judge if can interact with parent component. when true, 
			blurring the background, and can not interact with parent component */				  
			FlexGlobals.topLevelApplication.activeItem = this;
			
			//  this.parent = this.host_IP;
			var myPanel:Vnet_controllerPropertiesWindow = 
				Vnet_controllerPropertiesWindow(PopUpManager.createPopUp(this, Vnet_controllerPropertiesWindow, true)); 
			
			myPanel.x = 420;
			
			myPanel.y = 170;			
		}
		
		public function showSwitchDialogue():void{
			FlexGlobals.topLevelApplication.activeItem = this;
			var myPanel:C_SwitchListTitleWindow = 
				C_SwitchListTitleWindow(PopUpManager.createPopUp(FlexGlobals.topLevelApplication.parentDisplayObject, C_SwitchListTitleWindow, false)); 
			
			myPanel.x = 100;
			
			myPanel.y = 150;				
		}
		
		/**********************click menu event ***************************************/	  
		private function menuHandler(event:MenuEvent):void {
			
			if(event.item.label=="Switch List")
			{ 			
				showSwitchDialogue();
			} 	
			
			if(event.item.label=="Console") 
			{ 			
				FlexGlobals.topLevelApplication.activeItem = this;
				FlexGlobals.topLevelApplication.showConsole();
			}
			
			if(event.item.label=="Properties") 
			{ 			
				showDialogue();
			} 	
	
			// trace(event.item["label"]);
			if(event.item.label=="Delete") 
			{ 			
				 this.Delete();
				 Vnet_controller.vnet_delete(this.getCon_id());
			} 		
		}
		/*****************pop up menu, when select menu item*****************************/	
		public function showMenu(event:MouseEvent):void{
			myMenu= Menu.createMenu(this,menuData, false); 			
			//click event
			myMenu.addEventListener("itemClick", menuHandler); 
			//pop up menu 
			point.x=event.stageX; 
			point.y=event.stageY;  
			myMenu.show(point.x , point.y); 
		}
		
/**************************structure*****************************************/
		public function Controller()
		{		
			super();
			//enable double click(default as unable)	
			this.source="images/controller_mini.jpg";
			setStyle("skinClass", skins.Item_images_skin);
			this.doubleClickEnabled = true;
			this.addEventListener(MouseEvent.DOUBLE_CLICK,showMenu);
		}
/**************************get and set Con_id*********************************/		
		public override function getCon_id():String{
			return this.Con_id;
		}
		public override function setCon_id(_id:String):void{
			this.Con_id=_id;
		}
/**************************get and set Con_name*********************************/		
		public function getName():String{
			return this.Con_name;
		}
		public override function setCon_name(_name:String):void{
			this.Con_name = _name;
		}
/**************************get and set Con_type*******************************/
		public override function getCon_type():String{
			return this.Con_type;
		}
		public override function setCon_type(_type:String):void{
			this.Con_type=_type;
		}
/*************************get and set Rest_url********************************/
		public function getRset_url():String{
			return this.Rest_url;
		}
		public override function setRest_url(_url:String):void{
			this.Rest_url=_url;
		}
/***********************get and set flavor*********************************/
		public override function getflavor():int{
			return this.flavor;
		}
		public override function setflavor(_add:int):void{
			this.flavor=_add;
		}
/***********************get and set image*********************************/
		public override function getimage():int{
			return this.image;
		}
		public override function setimage(_add:int):void{
			this.image=_add;
		}
/**************************end*********************************************/
	}
}