package 
{
	import flash.display.DisplayObject;
	import flash.display.MovieClip;
	import flash.display.Bitmap;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.events.Event;
	import flash.events.MouseEvent;
	import flash.display.Graphics;
	import components.*;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import mx.controls.Alert;
	
	
	public class Main extends Sprite
	{
		
		[Embed(source="../assets/11949863251401131855candy_31.svg.med.png")]
		private var layer0Class:Class;
		var layer0:Bitmap = new layer0Class() as Bitmap;
		var item0 = new GoBagItem("Candy","Candy is a yummy treat, but it is not good for nutrition or sustained energy in a crisis.",false,layer0);
		
	
		[Embed(source="../assets/11971038831932190305kelan_whistle.svg.med.png")]
		private var layer1Class:Class;
		var layer1:Bitmap = new layer1Class() as Bitmap;
		var item1 = new GoBagItem("Whistle","Whistles produce a loud noise so that people can find you, even if you are trapped under rubble.",true,layer1);

		[Embed(source="../assets/basketball.png")]
		private var layer2Class:Class;
		var layer2:Bitmap = new layer2Class() as Bitmap;
		var item2 = new GoBagItem("Basketball","Basketballs are a source of outdoors entertainment.",false,layer2);

		[Embed(source="../assets/bike.png")]
		private var layer3Class:Class;
		var layer3:Bitmap = new layer3Class() as Bitmap;
		var item3 = new GoBagItem("Bike","A bike is a means of transportation. However, it can only be used by one person and it may not be practical after a tornado.",false,layer3);
		
		
		[Embed(source="../assets/canned-goods-md.png")]
		private var layer4Class:Class;
		var layer4:Bitmap = new layer4Class() as Bitmap;
		var item4 = new GoBagItem("Canned Food","Canned food lasts for a long time and can be opened with a multitool.",true,layer4);
		
		[Embed(source="../assets/boots.png")]
		private var layer5Class:Class;
		var layer5:Bitmap = new layer5Class() as Bitmap;
		var item5 = new GoBagItem("Boots","Boots are sturdy footwear that protect your feet from sharp objects on the ground.",true,layer5);
		
		[Embed(source="../assets/fireworks.png")]
		private var layer6Class:Class;
		var layer6:Bitmap = new layer6Class() as Bitmap;
		var item6 = new GoBagItem("Fireworks","Fireworks are explosive and may start dangerous fires.",false,layer6);
		
		[Embed(source="../assets/flashlight.png")]
		private var layer7Class:Class;
		var layer7:Bitmap = new layer7Class() as Bitmap;
		var item7 = new GoBagItem("Flashlight","Flashlights illuminate dark areas, helping you find people and things.",true,layer7);
		
		[Embed(source="../assets/cash.png")]
		private var layer8Class:Class;
		var layer8:Bitmap = new layer8Class() as Bitmap;
		var item8 = new GoBagItem("Cash","Cash can be used to buy supplies or necessary items.",true,layer8);
		
		[Embed(source="../assets/radio.png")]
		private var layer9Class:Class;
		var layer9:Bitmap = new layer9Class() as Bitmap;
		var item9 = new GoBagItem("Radio","A battery-powered radio lets you listen to emergency broadcasts and weather reports even when the power is out.",true,layer9);
		
		[Embed(source="../assets/doll.png")]
		private var layer10Class:Class;
		var layer10:Bitmap = new layer10Class() as Bitmap;
		var item10 = new GoBagItem("Doll","A small toy figurine.",false,layer10);
		
		[Embed(source="../assets/waterbottle.png")]
		private var layer11Class:Class;
		var layer11:Bitmap = new layer11Class() as Bitmap;
		var item11 = new GoBagItem("Waterbottle","Waterbottles are a source of clean, drinkable water to help you stay hydrated.",true,layer11);
		
		[Embed(source="../assets/wrench.png")]
		private var layer12Class:Class;
		var layer12:Bitmap = new layer12Class() as Bitmap;
		var item12 = new GoBagItem("Wrench","A wrench can be used to turn off the utilities of a house during a tornado.",true,layer12);

		[Embed(source="../assets/firstaidkit.png")]
		private var layer13Class:Class;
		var layer13:Bitmap = new layer13Class() as Bitmap;
		var item13 = new GoBagItem("First Aid Kit","First Aid Kits contain supplies to help handle injuries, like cuts.",true,layer13);
		
		[Embed(source="../assets/gamesystem.png")]
		private var layer14Class:Class;
		var layer14:Bitmap = new layer14Class() as Bitmap;
		var item14 = new GoBagItem("Game System","Game systems are a source of entertainment, but require batteries that might be used for radios and flashlights.",false,layer14);
		
		[Embed(source="../assets/hardhat.png")]
		private var layer15Class:Class;
		var layer15:Bitmap = new layer15Class() as Bitmap;
		var item15 = new GoBagItem("Hard Hat","A hard hat protects your head from debris.",true,layer15);
		
		[Embed(source="../assets/map.png")]
		private var layer16Class:Class;
		var layer16:Bitmap = new layer16Class() as Bitmap;
		var item16 = new GoBagItem("Map","Maps of the local area help you find your way to safety.",true,layer16);
			
		[Embed(source="../assets/mp3.png")]
		private var layer17Class:Class;
		var layer17:Bitmap = new layer17Class() as Bitmap;
		var item17 = new GoBagItem("MP3 Player","MP3 players allow you to listen to music.",false,layer17);
		
		[Embed(source="../assets/multitool.png")]
		private var layer18Class:Class;
		var layer18:Bitmap = new layer18Class() as Bitmap;
		var item18 = new GoBagItem("Multitool","A multitool can be used as a knife, a can opener, scissors, and more.",true,layer18);
		
		[Embed(source="../assets/teddybear.png")]
		private var layer19Class:Class;
		var layer19:Bitmap = new layer19Class() as Bitmap;
		var item19 = new GoBagItem("Teddy Bear", "A soft toy bear.", false, layer19);
		
		[Embed(source = "../assets/tabletop.png")]
		private var layer21Class:Class;
		var layer21:Bitmap = new layer21Class() as Bitmap;
		var background:DisplayObject = layer21;
		
		var textBox:TextField = new TextField();
		var itemsAdded:int = 0;
		
		[Embed(source="../assets/gobag.png")]
		private var layer20Class:Class;
		var layer20:Bitmap = new layer20Class() as Bitmap;
		var bag = new GoBag(layer20, true);
		
		[Embed(source = "../assets/button.png")]
		private var buttonLayer:Class;
		var button:Bitmap = new buttonLayer() as Bitmap;
		
		private var box = new Sprite();
		
		private var items:Array = new Array(
			item0,
			item1,
			item2,
			item3,
			item4,
			item5,
			item6,
			item7,
			item8,
			item9,
			item10,
			item11,
			item12,
			item13,
			item14,
			item15,
			item16,
			item17,
			item18,
			item19
		);
		
		
		
		private var startPositionsX:Array = new Array(50, 150, 250, 350);
		private var startPositionsY:Array = new Array(50, 150, 250, 350, 450);
		
		private var goodItems:Array = new Array();
		private var badItems:Array = new Array();
		
		var xPos:int; 
		var yPos:int; 
		
		public function Main():void 
		{
			if (stage) init();
			else addEventListener(Event.ADDED_TO_STAGE, init);
		}
		
		private function init(e:Event = null):void 
		{
			removeEventListener(Event.ADDED_TO_STAGE, init);
			
			setUp(stage);
			
			
		}
		
		private function setUp(stage:Stage):void
		{
			
			
			for (var i:int = 1; i < items.length; i++ )
			{
				if (items[i].isAccepted == true)
					goodItems.push(items[i]);
				else
					badItems.push(items[i]);
					
					
				stage.addChild(items[i]);
				items[i].x = startPositionsX[i%4];
				items[i].y = startPositionsY[i % 5];
				items[i].visible = true;
				items[i].height = 75;
				if(i == 7)
				{
			
					items[i].width = 50
				}
				items[i].scaleX = items[i].scaleY;
				items[i].addEventListener(MouseEvent.MOUSE_DOWN, dragObject);
				items[i].addEventListener(MouseEvent.MOUSE_UP, stopDragObject);
				items[i].addEventListener(MouseEvent.MOUSE_OVER, itemHover);
			}
			
			trace("good "+goodItems.length);
			trace("bad " +badItems.length);
			
			stage.addChild(bag);
			bag.x = stage.width - 300;
			bag.y = stage.height + 100;
			bag.height = 100;
			bag.scaleX = bag.scaleY;

			
			textBox.text = "Welcome to the Go Bag Buidler game! A go bag is a useful tool for emergency preparedness that holds a few handy, necessary items. Whenever there is a tornado, grab your go bag and take it with you. \n\n You can see a bag and a group of items. Drag the items you think are most useful and appropriate and drag them into the bag at the bottom of the screen.";
			textBox.border = true;
			textBox.wordWrap = true;
			textBox.width = (220+stage.width)/4;
			textBox.height = stage.height+100;
			textBox.x = 600;
			textBox.y = 0;
			textBox.background = true;
			textBox.textColor = 0xFFFFFF;
			textBox.backgroundColor = 0xaba9a9;
			
			
			var scale:Number = stage.stageWidth / background.width;
			if (background.height * scale > stage.stageHeight)
			{
				scale - stage.stageHeight / background.height;
			}
			
			background.scaleX = scale;
			background.scaleY = 2;
			stage.addChildAt(background, 0);
			stage.addChild(textBox);
		}
		private function dragObject(e:MouseEvent):void
		{
			trace(e.currentTarget);
			e.currentTarget.parent.addChild(e.currentTarget);
			e.currentTarget.startDrag();
		}
		
		private function stopDragObject(e:MouseEvent):void
		{
			var stage:Stage = (e.currentTarget).parent;
			e.currentTarget.stopDrag();
			trace(e.currentTarget.dropTarget.parent.name);
			if (e.currentTarget.dropTarget)
			{
				trace("dropped");//verify instance names
				
				if (e.currentTarget.dropTarget.parent.name == "instance65")//check for the instance name of the go-bag, what i think it is
					{
						
						//here the item has been dropped on something and it is the bag
						itemsAdded = itemsAdded + 1;
						//add it to the bag and remove from the stage
						bag.addToBag(e.currentTarget);
						e.currentTarget.visible = false;
						e.currentTarget.x = stage.width;
						e.currentTarget.y = stage.height;
						checkForEnd(stage);
						
					}
					
					//dropped the iterm on something but not the bag do nothing
			}
			
			//here it was dropped on nothing, continue to do nothing
		}
		
		private function getPosition(target:Object):void
		{
			xPos = target.x;
			yPos = target.y;
		}
		
		private function itemHover(e:MouseEvent): void
		{
			
				textBox.text = "Name: "+e.currentTarget.itemName + "\n\n" + "Desciption: " + e.currentTarget.description;
			
		}
		
		private function checkForEnd(stage:Stage): void
		{
			if(itemsAdded == goodItems.length)
			{
				//this should go somwewhere else but is backbone of score calculation
				trace(bag.getScore());
				
				
				var myClickHandler:Function = function (evt_obj:Object) {
					if (evt_obj.detail == Alert.OK) {
						trace(Alert.okLabel);
					} else if (evt_obj.detail == Alert.CANCEL){
						trace(Alert.cancelLabel);
					}
				};
			clearChildren(stage);
			endGame(stage);
			}
		}
		
		public function clearChildren(parent:Stage):void
		{
			if ((parent as DisplayObject) == null)
			{
				return;
			}
			while (parent.numChildren > 0)
			{
				parent.removeChildAt(0);
			}
			
			
			
		}
		
		public function endGame(stage:Stage):void
		{
			var finalTxt = new TextField();
			finalTxt.background = true;
			finalTxt.backgroundColor = 0x0191C8;
			finalTxt.width = 800;
			finalTxt.height = 800;
			finalTxt.textColor = 000000;
			finalTxt.defaultTextFormat = new TextFormat("Arial", 30);
			finalTxt.text = "Congratulations you put  " + bag.getScore() + " out of "+ goodItems.length + " correct items in the bag!";
			stage.addChild(finalTxt);
			
			
			box.addChild(button);
			
			stage.addChild(box);
			box.addEventListener(MouseEvent.CLICK, setUpMenu2);
			box.x = 300;
			box.y = 300;
		}
		
		public function setUpMenu2(e:MouseEvent):void
		{
			var stage:Stage = ((e.currentTarget).parent);
			clearChildren(stage);
			setUp(stage);
			bag.y = 600;
		}
		
		
				
	}
}