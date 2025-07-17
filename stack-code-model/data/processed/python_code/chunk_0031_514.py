package metaswarm.node.components.databox   {
	import flash.display.*;
	import flash.text.*;
	
	public class DataBoxMaker extends Sprite{
		
		private static const CLOSE:String = "closeDataBox";
		private static const POPOUT:String = "popout";
		private static const POPIN:String = "popin";
		
		public var dbx:DataBox;
		
		public function DataBoxMaker(dataBox:DataBox):void{
			this.dbx = dataBox;
			init();
		}
		public function init():void {
			//
		}
		public function make():void {
			makeTextField();
			//makeButtons();
		}
		
		private function makeTextField():void {
			/*h1 = new TextField();
			h2 = new TextField();
			h3 = new TextField();
			l = new TextField();*/
			//var t:TextField = new TextField(); 

			var h1Fmt:TextFormat = new TextFormat("Technic", 18, 0x333333);
			//var h2Fmt:TextFormat = new TextFormat();
			var h3Fmt:TextFormat = new TextFormat("Technic", 14, 0x06c);
			var lFmt:TextFormat = new TextFormat("Technic", 8, 0x333333);
			
			/*h1Fmt.TextFormat(font:String = null, 
					   size:Object = null, 
					   color:Object = null, 
					   bold:Object = null, 
					   italic:Object = null, 
					   underline:Object = null, 
					   url:String = null, 
					   target:String = null, 
					   align:String = null, 
					   leftMargin:Object = null, 
					   rightMargin:Object = null, 
					   indent:Object = null, 
					   leading:Object = null);*/
			
			//alwaysShowSelection : Boolean 
			 
			
			//dbx.t.autoSize = TextFieldAutoSize.LEFT;
			dbx.t.height = 100;
			dbx.t.width = 100;
			//dbx.t.background = true;
			//dbx.t.backgroundColor = 0x231F20; 
			dbx.t.alpha = 50;
			//dbx.t.border = true; 
			//dbx.t.borderColor = 0x000000; 
			//t.height = 
			//t.width = 
			dbx.t.mouseEnabled  = false;
			//t.mouseWheelEnabled = true; 
			//t.multiline = true; 
			dbx.t.wordWrap = true;
			
			//t.numLines [read-only]  
			//t.length [read-only]
			//t.scrollH : int 
			//t.scrollV : int 
			//t.selectable = true; 
			//t.tabEnabled = true;  
			//t.thickness : Number
			/*//t.width = 
			//t.height =
			t.background = true;
			t.backgroundColor = 0xCCCCCC; //light gray
			t.border = true;
			t.borderColor = 0x333333; //dark gray
			t.autoSize = TextFieldAutoSize.LEFT;
			//addChild(this);*/
			dbx.t.text = "";
			
			var c0:uint = 0;
			var c1:uint = c0 + dbx.dat[0].length + dbx.dat[1].length +1;
			var c2:uint = c1 + dbx.dat[2].length + 1;
			var c3:uint = c2 + 10;
			
			dbx.t.appendText(dbx.dat[0] + dbx.dat[1] + '\n');
			dbx.t.appendText(dbx.dat[2] + '\n');
			dbx.t.appendText("__________" + '\n');
			//t.text += dat[0] + dat[1] + '\n';
			//t.text += dat[2] + '\n';
			//t.text += "__________" + '\n';

			for(var i:uint=3; i<dbx.dat.length; i++){
				dbx.t.appendText(dbx.dat[i] + ", ");
				//t.text += dat[i] + ", ";
			}
			
			dbx.t.setTextFormat(h1Fmt, c0, c1);
			dbx.t.setTextFormat(h3Fmt, c1, c2);
			dbx.t.setTextFormat(h3Fmt, c2, c3);
			dbx.t.setTextFormat(lFmt, c3, dbx.t.text.length);
			
			dbx.t.selectable = false;
			dbx.t.mouseEnabled = false;
			//this.id = 0;
			dbx.addChild(dbx.t);
			//initTag();
		}
		
		private function makeButtons():void {
			
			dbx.closeButton = new CustomSimpleButton(CLOSE);
			dbx.popoutButton = new CustomSimpleButton(POPOUT);
			dbx.popinButton = new CustomSimpleButton(POPIN);
			//dbx.loadExtButton:CustomSimpleButton = new CustomSimpleButton("e");
		
			//var myButton:Button = new Button();
			//dbx.close.label = "x";
			//dbx.close.emphasized = true;
			//dbx.close.width = 15;
			//close.move(20, 20);
			
			/*dbx.closeButton.make();
			dbx.popoutButton.make();
			dbx.popinButton.make();
			dbx.loadExtButton.make();*/
			
			dbx.closeButton.x = dbx.t.width-dbx.closeButton.width;
			//dbx.closeButton.y = dbx.t.height;
			
			dbx.popoutButton.x = dbx.t.width-dbx.popoutButton.width;
			dbx.popoutButton.y = dbx.t.height-15;
			
			dbx.popinButton.x = dbx.t.width-(15 * 2);
			dbx.popinButton.y = dbx.t.height-15;
			
			//dbx.loadExtButton.x = dbx.t.width-(15 * 3);
			//dbx.loadExtButton.y = dbx.t.height-15;
			
			
			dbx.addChild(dbx.closeButton);
			dbx.addChild(dbx.popoutButton);
			dbx.addChild(dbx.popinButton);
			//dbx.addChild(dbx.loadExtButton);
			
		}
	}
}