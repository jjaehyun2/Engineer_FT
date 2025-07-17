package
{
	import flash.data.SQLConnection;
	import flash.data.SQLResult;
	import flash.data.SQLStatement;
	import flash.events.ErrorEvent;
	import flash.events.SQLErrorEvent;
	import flash.events.SQLEvent;
	import flash.net.URLRequest;
	import flash.net.navigateToURL;
	import flash.text.TextFormat;
	
	import feathers.controls.Button;
	import feathers.controls.ButtonGroup;
	import feathers.controls.Header;
	import feathers.controls.List;
	import feathers.controls.Panel;
	import feathers.controls.Screen;
	import feathers.controls.ScrollContainer;
	import feathers.controls.ScrollText;
	import feathers.controls.Scroller;
	import feathers.controls.TextInput;
	import feathers.controls.text.TextFieldTextRenderer;
	import feathers.core.ITextRenderer;
	import feathers.core.PopUpManager;
	import feathers.data.ListCollection;
	import feathers.layout.HorizontalLayout;
	import feathers.layout.VerticalLayout;
	
	import starling.display.BlendMode;
	import starling.display.DisplayObject;
	import starling.display.Image;
	import starling.events.Event;
	import starling.events.Touch;
	import starling.events.TouchEvent;
	import starling.events.TouchPhase;
	import starling.textures.Texture;
	
	
	public class IndexScreen extends Screen
	{
		private var header:Header;
		private var container:ScrollContainer = new ScrollContainer();
		private var containerDrawn:Boolean = false;
		private var backButton:Button;
		private var mainPanel:Panel;
		private var keywordInput:TextInput;
		private var searchButton:Button;
		
		private var itemList:List = new List();
		
		private var popupMode:String = "";
		private var abortScreen:Boolean = false; // used to avoid Draw() call if we bounce over to login
		
		private var screenMode:String = Constants.ABOUT;
		private var currentTab:String;
		private var currentUID:int;
		private var currentKeywords:String;
		private var currentTitle:String;
		
		private var uteamImage:Image;
		private var videoImage:Image;
		private var controllerImage:Image;
		private var achievementsImage:Image;
		private var ballImage:Image;
		private var fieldImage:Image;
		private var diamondImage:Image;
		private var aboutImage:Image;
		
		private var aboutContainer:ScrollContainer;
		private var platformButton:Button;
		
		private var sqlconnection:SQLConnection = new SQLConnection();
		private var sqlstatement:SQLStatement = new SQLStatement();
		private var result:SQLResult;
		
		private var stars5Icon:Texture;
		private var stars4Icon:Texture;
		private var stars3Icon:Texture;
		private var stars2Icon:Texture;
		private var stars1Icon:Texture;
		
		private var goldIcon:Texture;
		private var silverIcon:Texture;
		private var bronzeIcon:Texture;
		
		private var eafcIcon:Texture;
		private var runningIcon:Texture;
		private var celebrationsIcon:Texture;
		private var vpIcon:Texture;
		
		private var fiveIcon:Texture;
		private var tenIcon:Texture;
		private var fifteenIcon:Texture;
		private var twentyIcon:Texture;
		private var twentyfiveIcon:Texture;
		private var thirtyIcon:Texture;
		private var fiftyIcon:Texture;
		private var fiftyfiveIcon:Texture;
		private var hundredIcon:Texture;
		
		[Embed(source="../assets/graphics/uteamIcon4x.png")]
		public static const UTEAM_IMAGE:Class;
		
		[Embed(source="../assets/graphics/videoIcon4x.png")]
		public static const VIDEO_IMAGE:Class;		
		
		[Embed(source="../assets/graphics/achievementsIcon4x.png")]
		public static const ACHIEVEMENTS_IMAGE:Class;
		
		[Embed(source="../assets/graphics/celebrations.png")]
		public static const CONTROLLER_IMAGE:Class;
		
		[Embed(source="../assets/graphics/homeicon.png")]
		public static const DIAMOND_IMAGE:Class;

		[Embed(source="../assets/graphics/magnify1x.png")]
		public static const MAGNIFY_IMAGE:Class;
		
		[Embed(source="../assets/graphics/soccerball4x.png")]
		public static const BALL_IMAGE:Class;

		[Embed(source="../assets/graphics/soccerField4x.png")]
		public static const FIELD_IMAGE:Class;
		
		[Embed(source="../assets/graphics/5stars.png")]
		public static const STARS5_IMAGE:Class;
		
		[Embed(source="../assets/graphics/4stars.png")]
		public static const STARS4_IMAGE:Class;
		
		[Embed(source="../assets/graphics/3stars.png")]
		public static const STARS3_IMAGE:Class;
		
		[Embed(source="../assets/graphics/2stars.png")]
		public static const STARS2_IMAGE:Class;
		
		[Embed(source="../assets/graphics/1star.png")]
		public static const STARS1_IMAGE:Class;
		
		[Embed(source="../assets/graphics/gold.png")]
		public static const GOLD_IMAGE:Class;
		
		[Embed(source="../assets/graphics/silver.png")]
		public static const SILVER_IMAGE:Class;
		
		[Embed(source="../assets/graphics/bronze.png")]
		public static const BRONZE_IMAGE:Class;
		
		[Embed(source="../assets/graphics/eafc.png")]
		public static const EAFC_IMAGE:Class;
		
		[Embed(source="../assets/graphics/running.png")]
		public static const RUNNING_IMAGE:Class;
		
		[Embed(source="../assets/graphics/finishing.png")]
		public static const CELEBRATIONS_IMAGE:Class;
		
		[Embed(source="../assets/graphics/vp.png")]
		public static const VP_IMAGE:Class;
		
		[Embed(source="../assets/graphics/5.png")]
		public static const FIVE_IMAGE:Class;
		
		[Embed(source="../assets/graphics/10.png")]
		public static const TEN_IMAGE:Class;
		
		[Embed(source="../assets/graphics/15.png")]
		public static const FIFTEEN_IMAGE:Class;
		
		[Embed(source="../assets/graphics/20.png")]
		public static const TWENTY_IMAGE:Class;
		
		[Embed(source="../assets/graphics/25.png")]
		public static const TWENTYFIVE_IMAGE:Class;
		
		[Embed(source="../assets/graphics/30.png")]
		public static const THIRTY_IMAGE:Class;
		
		[Embed(source="../assets/graphics/50.png")]
		public static const FIFTY_IMAGE:Class;
		
		[Embed(source="../assets/graphics/55.png")]
		
		public static const FIFTYFIVE_IMAGE:Class;
		[Embed(source="../assets/graphics/100.png")]
		public static const HUNDRED_IMAGE:Class;
		
		
		function IndexScreen()  // constructor
		{
			
		}
		public function reDraw():void
		{
			mainPanel.y = Main._model.getAdHeight();
			mainPanel.height = actualHeight - (Main._model.getAdHeight());
		}
		override protected function draw():void
		{
			if (!abortScreen)
			{			
				
			}
		}
		
		override protected function initialize():void
		{
			Main.killSplash();
			
			stars5Icon = Texture.fromBitmap(new STARS5_IMAGE());
			stars4Icon = Texture.fromBitmap(new STARS4_IMAGE());
			stars3Icon = Texture.fromBitmap(new STARS3_IMAGE());
			stars2Icon = Texture.fromBitmap(new STARS2_IMAGE());
			stars1Icon = Texture.fromBitmap(new STARS1_IMAGE());
			
			goldIcon = Texture.fromBitmap(new GOLD_IMAGE());
			silverIcon = Texture.fromBitmap(new SILVER_IMAGE());
			bronzeIcon = Texture.fromBitmap(new BRONZE_IMAGE());
			
			eafcIcon = Texture.fromBitmap(new EAFC_IMAGE());
			runningIcon = Texture.fromBitmap(new RUNNING_IMAGE());
			celebrationsIcon = Texture.fromBitmap(new CELEBRATIONS_IMAGE());
			vpIcon = Texture.fromBitmap(new VP_IMAGE());
			
			fiveIcon = Texture.fromBitmap(new FIVE_IMAGE());
			tenIcon = Texture.fromBitmap(new TEN_IMAGE());
			fifteenIcon = Texture.fromBitmap(new FIFTEEN_IMAGE());
			twentyIcon = Texture.fromBitmap(new TWENTY_IMAGE());
			twentyfiveIcon = Texture.fromBitmap(new TWENTYFIVE_IMAGE());
			thirtyIcon = Texture.fromBitmap(new THIRTY_IMAGE());
			fiftyIcon = Texture.fromBitmap(new FIFTY_IMAGE());
			fiftyfiveIcon = Texture.fromBitmap(new FIFTYFIVE_IMAGE());
			hundredIcon = Texture.fromBitmap(new HUNDRED_IMAGE());
			
			var magnifyIcon:Texture = Texture.fromBitmap(new MAGNIFY_IMAGE());
			var magnifyImage:Image = new Image(magnifyIcon);

			var aboutTexture:Texture = Texture.fromBitmap(new DIAMOND_IMAGE());
			aboutImage = new Image(aboutTexture);
			aboutImage.scaleX = aboutImage.scaleY = Main._appView.getAppScale() / 2;
			aboutImage.name = Constants.ABOUT;
			aboutImage.addEventListener(starling.events.TouchEvent.TOUCH, onButtonTouched);
			
			var videoTexture:Texture = Texture.fromBitmap(new VIDEO_IMAGE());
			videoImage = new Image(videoTexture);
			videoImage.scaleX = videoImage.scaleY = Main._appView.getAppScale() / 2;
			videoImage.name = Constants.VIDEOS;
			videoImage.addEventListener(starling.events.TouchEvent.TOUCH, onButtonTouched);
			
			var achTexture:Texture = Texture.fromBitmap(new ACHIEVEMENTS_IMAGE());
			achievementsImage = new Image(achTexture);			
			achievementsImage.scaleX = achievementsImage.scaleY = Main._appView.getAppScale() / 2;
			achievementsImage.name = Constants.ACHIEVEMENTS;
			achievementsImage.addEventListener(starling.events.TouchEvent.TOUCH, onButtonTouched);
			
			var controllerTexture:Texture = Texture.fromBitmap(new CONTROLLER_IMAGE());
			controllerImage = new Image(controllerTexture);
			controllerImage.scaleX = controllerImage.scaleY = Main._appView.getAppScale() / 2;
			controllerImage.name = Constants.CELEBRATIONS;
			controllerImage.addEventListener(starling.events.TouchEvent.TOUCH, onButtonTouched);

			var ballTexture:Texture = Texture.fromBitmap(new BALL_IMAGE());
			ballImage = new Image(ballTexture);
			ballImage.scaleX = ballImage.scaleY = Main._appView.getAppScale() / 2;
			ballImage.name = Constants.SKILLS;
			ballImage.addEventListener(starling.events.TouchEvent.TOUCH, onButtonTouched);
			
			searchButton = new Button();
			searchButton.label = "";
			searchButton.defaultIcon = magnifyImage;
			searchButton.defaultIcon.scaleX = searchButton.defaultIcon.scaleY = 0.5 * Main._appView.getAppScale();
			searchButton.addEventListener(starling.events.Event.TRIGGERED, popupSearch);
			
			platformButton = new Button();
			platformButton.label = Main._model.getPlatform();
			platformButton.addEventListener(starling.events.Event.TRIGGERED, popupPlatformPicker);
			
			keywordInput = new TextInput();
			
			mainPanel = new Panel();
			mainPanel.x = 0;
			mainPanel.y = 0;
			mainPanel.width = Main._appView.stageWidth;
			mainPanel.height = Main._appView.stageHeight;			
			
			
			mainPanel.headerFactory = function():Header
			{
				header = new Header();
				header.title = "Title";
				header.rightItems = new <DisplayObject>[searchButton];
				header.leftItems = new <DisplayObject>[platformButton];
				return header;
			}
			
			searchButton.visible = false;
			platformButton.visible = false;
			
			addChild(mainPanel);
			
			
			
			mainPanel.footerFactory = function():ScrollContainer
			{
				var layout:HorizontalLayout = new HorizontalLayout();
				layout.gap = 14 * Main._appView.getAppScale();
				layout.paddingTop = 5 * Main._appView.getAppScale();
				layout.paddingBottom = 5 * Main._appView.getAppScale();
				layout.paddingLeft = 2 * Main._appView.getAppScale();
				layout.paddingRight = 2 * Main._appView.getAppScale();
				layout.verticalAlign = VerticalLayout.VERTICAL_ALIGN_MIDDLE;
				layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_CENTER;
				
				var container:ScrollContainer = new ScrollContainer();
				container.layout = layout;
				container.nameList.add( ScrollContainer.ALTERNATE_NAME_TOOLBAR );
				//container.horizontalScrollPolicy = ScrollContainer.SCROLL_POLICY_ON;
				container.verticalScrollPolicy = ScrollContainer.SCROLL_POLICY_OFF;
				
				container.addChild(aboutImage);
				container.addChild(achievementsImage);
				container.addChild(ballImage);
				container.addChild(controllerImage);
				//container.addChild(videoImage);
				
				return container;
			}
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.hasVariableItemDimensions = true;
			layout.horizontalAlign = "right";
			this.itemList = new List();
			itemList.addEventListener(starling.events.Event.ADDED_TO_STAGE, loadFirstList);
			itemList.addEventListener(starling.events.Event.CHANGE, listChanged); 
			itemList.itemRendererProperties.width = Main._appView.stageWidth;
			itemList.itemRendererProperties.labelFactory = function():ITextRenderer
			{
				//or BitmapFontTextRenderer, if you prefer
				var textRenderer:TextFieldTextRenderer  = new TextFieldTextRenderer ();
				//var textRenderer:BitmapFontTextRenderer  = new BitmapFontTextRenderer ();
				textRenderer.wordWrap = true;
				return textRenderer;
			}
			itemList.layout = layout;
			// kick off screen by loading MyVideos (must be done after header is present)
			function loadFirstList(e:starling.events.Event):void 
			{
					shadeToolbarIcons(screenMode);
					createAboutScreen();
			};
			mainPanel.addChild(itemList);
		}
		protected function openDB(statement:String = null):void
		{			
			Main._model.listdata == null;
			if (Main._model.initDB(Constants.DB_NAME))
			{		
				Main._model.sqlconnection.addEventListener(SQLErrorEvent.ERROR, Main._model.sqlError);
				Main._model.listdata = new ListCollection();
				var sqltext:String;
				if (statement == null)
				{
					if (screenMode == Constants.ACHIEVEMENTS)
					sqltext = "SELECT * FROM Achievements ORDER BY points";
					if (screenMode == Constants.SKILLS)
						sqltext = "SELECT * FROM Skills ORDER BY stars";
					if (screenMode == Constants.CELEBRATIONS)
						sqltext = "SELECT * FROM Celebrations ORDER BY type";
					if (screenMode == Constants.VIDEOS)
						sqltext = "SELECT * FROM Videos ORDER BY name";
				}
				else
					sqltext = statement;
				trace("Database sql: " + sqltext);
				Main._model.sqlstatement.text = sqltext;
				Main._model.sqlstatement.addEventListener(SQLEvent.RESULT, onSelectResults);
				Main._model.sqlstatement.addEventListener(SQLErrorEvent.ERROR, Main._model.sqlError);
				Main._model.sqlstatement.execute();
			}
			else
				trace("No DB connection...");
		}
		private function onSelectResults(event:SQLEvent):void
		{		
			Main._model.sqlstatement.removeEventListener(SQLEvent.RESULT, onSelectResults);
			result = Main._model.sqlstatement.getResult();
			if (result.data==null)
			{
				trace("NO DB RESULTS");
			}
			else
			{
				
				for (var i:int = 0; i < result.data.length; i++)
				{
					var row:Object = result.data[i];
					if(screenMode == Constants.ACHIEVEMENTS)
					{
						if (Main._model.getPlatform() == Constants.XBOX)
							if (Number(row.points) == 5)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",fiveIcon));
							else if (Number(row.points) == 10)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",tenIcon));
							else if (Number(row.points) == 15)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",fifteenIcon));
							else if (Number(row.points) == 20)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",twentyIcon));
							else if (Number(row.points) == 25)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",twentyfiveIcon));
							else if (Number(row.points) == 30)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",thirtyIcon));
							else if (Number(row.points) == 50)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",fiftyIcon));
							else if (Number(row.points) == 55)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",fiftyfiveIcon));
							else if (Number(row.points) == 100)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore",hundredIcon));
							else
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,row.points+" Gamerscore"));
						if (Main._model.getPlatform() == Constants.PLAYSTATION)
						{
							if (Number(row.points) < 30)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info,null,bronzeIcon));
							else if (Number(row.points) >= 30 && Number(row.points) < 90)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info, null,silverIcon));
							else if (Number(row.points) >= 90 && Number(row.points) < 180)
								Main._model.listdata.push(new ListItem(row.name+":\n"+row.info, null,goldIcon));
							
						}
					}
					else if(screenMode == Constants.CELEBRATIONS)
					{
						if (Main._model.getPlatform() == Constants.XBOX)
						{
							Main._model.listdata.push(new ListItem(row.name+":\n"+row.xbox,row.type,returnCelebrationTexture(row.type)));
						}
						if (Main._model.getPlatform() == Constants.PLAYSTATION)
						{
							Main._model.listdata.push(new ListItem(row.name+":\n"+row.playstation,row.type,returnCelebrationTexture(row.type)));
						}
					}
					else if(screenMode == Constants.SKILLS)
					{
						if (Main._model.getPlatform() == Constants.XBOX)
						{
							Main._model.listdata.push(new ListItem(row.name+":\n"+row.xbox,row.stars+" Stars",returnStarsTexture(int(row.stars))));
						}
						if (Main._model.getPlatform() == Constants.PLAYSTATION)
						{
							Main._model.listdata.push(new ListItem(row.name+":\n"+row.playstation,row.stars+" Stars",returnStarsTexture(int(row.stars))));
						}
					}
					else if(screenMode == Constants.VIDEOS)
						Main._model.listdata.push(new ListItem(row.name,row.author));
				}
			}
			createList();
			Main._model.closeDB();
		}
		private function returnStarsTexture(stars:int):Texture
		{
			if (stars == 1)
				return stars1Icon;
			else if (stars == 2)
				return stars2Icon;
			else if (stars == 3)
				return stars3Icon;
			else if (stars == 4)
				return stars4Icon;
			else if (stars == 5)
				return stars5Icon;

			return stars1Icon;
		}
		private function returnCelebrationTexture(type:String):Texture
		{
			if (type == "Running Moves")
				return runningIcon;
			else if(type == "EAS FC Unlockables")
				return eafcIcon;
			else if (type == "Finishing Moves")
				return celebrationsIcon;
			else if (type == "Virtual Pro Unlockables")
				return vpIcon;
			
			return runningIcon;
			
		}
		protected function createList():void
		{
			
			mainPanel.removeChild(container);
			itemList.visible = true;
			itemList.isSelectable = false;
			itemList.dataProvider = Main._model.listdata;
			itemList.itemRendererProperties.accessoryLabelField = "accessoryField";
			itemList.itemRendererProperties.accessorySourceField = "icon";
			itemList.itemRendererProperties.labelField = "titleField";
		}
		
		private function createAboutScreen():void
		{
			
			
			if (containerDrawn == false)
			{
				containerDrawn = true;
				aboutContainer = new ScrollContainer();
								
				var layout:VerticalLayout = new VerticalLayout();
				layout.horizontalAlign = HorizontalLayout.HORIZONTAL_ALIGN_CENTER;
				layout.gap = 10;
				aboutContainer.layout = layout;
				
				var textArea:ScrollText  = new ScrollText();
				textArea.text = "Thank you for downloading FIFA 14 Skills and Celebrations. We promise to keep this app updated with the latest info and we are planning on adding much more in the future. Chemistry styles, tutorials, and ultimate team tips are just a few of the things we are planning to add. To keep up to date with all the latest FIFA info give us a like on Facebook or follow us on Twitter. If this app was useful give it a five star rating in the App Store.";
				aboutContainer.addChild( textArea );
				
				var group:ButtonGroup = new ButtonGroup();
				group.direction = ButtonGroup.DIRECTION_HORIZONTAL;
				group.dataProvider = new ListCollection([{ label: "Facebook", triggered: facebook },{ label: "Twitter", triggered: twitter  }/*, { label: "Play Store", triggered: playstore  }*/]);	
				aboutContainer.addChild(group);
				aboutContainer.verticalScrollPolicy == Scroller.SCROLL_POLICY_OFF;
				mainPanel.addChild( aboutContainer );
			}
			
		}
		private function facebook(e:starling.events.Event):void
		{
			navigateToURL(new URLRequest("https://www.facebook.com/IdealisticTechnologiesInc"));
		}
		private function twitter(e:starling.events.Event):void
		{
			navigateToURL(new URLRequest("https://twitter.com/IdealisticTech"));
		}
		private function playstore(e:starling.events.Event):void
		{
			navigateToURL(new URLRequest("https://play.google.com/store/apps/details?id=air.com.idealistictechnologies.fifa14"));
		}
		private function popupSearch():void
		{
			var	searchpanel:Panel = new Panel();
			searchpanel.x = actualWidth*0.1;
			searchpanel.y = actualHeight * 0.2;
			searchpanel.width = actualWidth * 0.8;
			searchpanel.height = actualHeight * 0.6;
			searchpanel.headerProperties.title = "Keyword Search"; 
			searchpanel.horizontalScrollPolicy = ScrollContainer.SCROLL_POLICY_OFF;
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.gap = 10 * Main._appView.getAppScale();
			layout.paddingTop = 10 * Main._appView.getAppScale();
			layout.paddingBottom = 10 * Main._appView.getAppScale();
			layout.paddingLeft = 10 * Main._appView.getAppScale();
			layout.paddingRight = 10 * Main._appView.getAppScale();
			layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_CENTER;
			//layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			searchpanel.layout = layout;
			
			searchpanel.headerFactory = function():Header
			{
				var header:Header = new Header();
				var backButton:Button = new Button();
				backButton.label = "Back";
				backButton.addEventListener(starling.events.Event.TRIGGERED, onPopUpBack);
				function onPopUpBack():void {PopUpManager.removePopUp(searchpanel); itemList.selectedIndex = -1;}
				header.leftItems = new <DisplayObject>[backButton];
				return header;
			}
			PopUpManager.addPopUp(searchpanel);
			
			var promptFormat:TextFormat = new TextFormat( "_sans", 12 * Main._appView.getAppScale(), 0xffffff );
			
			var keywordsInput:TextInput = new TextInput();
			keywordsInput.promptProperties.textFormat = promptFormat;
			keywordsInput.prompt = "keywords (leave empty for all)";
			keywordsInput.width = Main._appView.stageWidth * 0.75;
			searchpanel.addChild(keywordsInput);
			
			var magnifyIcon:Texture = Texture.fromBitmap(new MAGNIFY_IMAGE());
			var magnifyImage:Image = new Image(magnifyIcon);
			
			var searchButton:Button = new Button();
			searchButton.label = "Search";
			searchButton.addEventListener(starling.events.Event.TRIGGERED, doSearch);
			searchButton.addEventListener(starling.events.Event.ADDED_TO_STAGE, setUpButton);
			searchButton.defaultIcon = magnifyImage;
			function doSearch():void 
			{
				PopUpManager.removePopUp(searchpanel);
				openDB("SELECT * FROM "+screenMode+" WHERE name LIKE '%"+keywordsInput.text+"%'");
			};
			searchButton.defaultIcon.scaleX = searchButton.defaultIcon.scaleY = 0.5 * Main._appView.getAppScale();
			searchpanel.addChild(searchButton);
		}
		
		private function popupPlatformPicker():void
		{
			var	platformpanel:Panel = new Panel();
			platformpanel.x = actualWidth*0.1;
			platformpanel.y = actualHeight * 0.2;
			platformpanel.width = actualWidth * 0.8;
			platformpanel.height = actualHeight * 0.6;
			platformpanel.headerProperties.title = "Choose Platform"; 
			platformpanel.horizontalScrollPolicy = ScrollContainer.SCROLL_POLICY_OFF;
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.gap = 10 * Main._appView.getAppScale();
			layout.paddingTop = 10 * Main._appView.getAppScale();
			layout.paddingBottom = 10 * Main._appView.getAppScale();
			layout.paddingLeft = 10 * Main._appView.getAppScale();
			layout.paddingRight = 10 * Main._appView.getAppScale();
			layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_CENTER;
			//layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			platformpanel.layout = layout;
			PopUpManager.addPopUp(platformpanel);
			
			var xboxButton:Button = new Button();
			xboxButton.label = "Xbox";
			xboxButton.addEventListener(starling.events.Event.TRIGGERED, xbox);
			xboxButton.addEventListener(starling.events.Event.ADDED_TO_STAGE, setUpButton);
			function xbox():void 
			{
				Main._model.setPlatform(Constants.XBOX);
				platformButton.label = Constants.XBOX;
				PopUpManager.removePopUp(platformpanel);
				shadeToolbarIcons(screenMode);
				openDB();
			};
			//xboxButton.defaultIcon.scaleX = xboxButton.defaultIcon.scaleY = 0.5 * Main._appView.getAppScale();
			platformpanel.addChild(xboxButton);
			
			var playstationButton:Button = new Button();
			playstationButton.label = "Playstation";
			playstationButton.addEventListener(starling.events.Event.TRIGGERED, playstation);
			playstationButton.addEventListener(starling.events.Event.ADDED_TO_STAGE, setUpButton);
			function playstation():void 
			{
				Main._model.setPlatform(Constants.PLAYSTATION);
				platformButton.label = Constants.PLAYSTATION;
				PopUpManager.removePopUp(platformpanel);
				shadeToolbarIcons(screenMode);
				openDB();
			};
			//playstationButton.defaultIcon.scaleX = playstationButton.defaultIcon.scaleY = 0.5 * Main._appView.getAppScale();
			platformpanel.addChild(playstationButton);
		}
		
		private function onButtonTouched(e:starling.events.TouchEvent):void
		{
			var ended:Touch = e.getTouch(this,TouchPhase.ENDED);
			var hover:Touch = e.getTouch(this,TouchPhase.HOVER);
			if (ended)
			{
				trace("Tap: " , Image(e.target).name);
				//getDBItems(Image(e.target).name, keywordInput.text);  
				this.screenMode = Image(e.target).name;
				shadeToolbarIcons(screenMode);
				if (this.screenMode == Constants.ABOUT)
				{
					createAboutScreen();
					searchButton.visible = false;
					platformButton.visible = false;
					aboutContainer.verticalScrollPolicy == Scroller.SCROLL_POLICY_OFF;
					aboutContainer.visible = true;
					mainPanel.removeChild(itemList);
					mainPanel.addChild(aboutContainer);
				}
				else  // show list items
				{
					searchButton.visible = true;
					platformButton.visible = true;
					openDB();
					container.verticalScrollPolicy == Scroller.SCROLL_POLICY_ON;
					aboutContainer.visible = false;
					mainPanel.removeChild(aboutContainer);
					mainPanel.addChild(itemList);
				}
			}
		}
		
		private function onListRendererAdd(e:starling.events.Event):void
		{
			DisplayObject(e.data).addEventListener(TouchEvent.TOUCH, onRendererTouch);
		}
		
		private function shadeToolbarIcons(tab:String):void  // make all icons normal, then highlight the current tab icon
		{
			trace("ShadeToolbar: " , tab);
			mainPanel.headerProperties.title = tab;
			this.controllerImage.blendMode = BlendMode.NORMAL;
			this.achievementsImage.blendMode = BlendMode.NORMAL;
			this.videoImage.blendMode = BlendMode.NORMAL;
			this.ballImage.blendMode = BlendMode.NORMAL;
			this.aboutImage.blendMode = BlendMode.NORMAL;
			
			switch (tab)
			{
				case Constants.CELEBRATIONS: this.controllerImage.blendMode = BlendMode.NONE; break;
				case Constants.ACHIEVEMENTS: this.achievementsImage.blendMode = BlendMode.NONE; break;
				case Constants.VIDEOS: this.videoImage.blendMode = BlendMode.NONE; break;
				case Constants.SKILLS: this.ballImage.blendMode = BlendMode.NONE; break;
				case Constants.ABOUT: this.aboutImage.blendMode = BlendMode.NONE; break;
				default:  break;
			}
		}
		
		private function onListRendererRemove(e:starling.events.Event):void
		{
			DisplayObject(e.data).removeEventListener(TouchEvent.TOUCH, onRendererTouch);
		}
		
		private function onRendererTouch(e:starling.events.TouchEvent):void
		{

		}
			
		private function httpRequestError( error:flash.events.ErrorEvent):void
		{ 
			trace( "An error occured: " + error.text );  
		};
		
		private function listChanged(e:starling.events.Event):void
		{
			trace("ListChange: " + e.data);
			/*if (itemList.selectedIndex != -1)
				popupContextMenu();*/
		}
		
		private function popupContextMenu():void
		{
			var panel:Panel = new Panel();
			panel.x = actualWidth*0.1;
			panel.y = actualWidth*0.2;
			panel.width = actualWidth*0.8;
			panel.height = actualHeight*0.6;
			panel.headerProperties.title = "Item Actions";
			
			var layout:VerticalLayout = new VerticalLayout();
			layout.gap = 10 * Main._appView.getAppScale();
			layout.paddingTop = 10 * Main._appView.getAppScale();
			layout.paddingBottom = 10 * Main._appView.getAppScale();
			layout.paddingLeft = 10 * Main._appView.getAppScale();
			layout.paddingRight = 10 * Main._appView.getAppScale();
			layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_CENTER;
			//layout.horizontalAlign = VerticalLayout.HORIZONTAL_ALIGN_JUSTIFY;
			panel.layout = layout;
			
			panel.headerFactory = function():Header
			{
				var header:Header = new Header();
				var backButton:Button = new Button();
				backButton.label = "Back";
				backButton.addEventListener(starling.events.Event.TRIGGERED, onPopUpBack);
				function onPopUpBack():void {PopUpManager.removePopUp(panel); itemList.selectedIndex = -1;}
				header.leftItems = new <DisplayObject>[backButton];
				return header;
			}
			PopUpManager.addPopUp(panel);
			
		}
		
		private function setUpButton(e:starling.events.Event):void
		{
			Button(e.target).height = Main._appView.getStdButtonHeight(); 
			Button(e.target).width = Main._appView.stageWidth * .75; // Main._appView.stageWidth*.5;
			Button(e.target).defaultLabelProperties.textFormat = Main._appView.getTxtFmt(12*Main._appView.getAppScale(), 0x000000, true);
		}
		
		private function sqlError(event:SQLErrorEvent):void
		{
			trace("Error message:", event.error.message);
			trace("Details:", event.error.details);
		}
		
	}
	
}