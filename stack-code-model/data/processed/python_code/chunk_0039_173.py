package {

	import flash.display.MovieClip;
	import flash.net.*;
	import flash.display.Loader;
	
	
	public class smallskill {
		private var pl2:MovieClip = new MovieClip();
		var pl2loader = new Loader();
		var pl3url = new URLRequest("../skills/luffy/skill1.png");
		public function smallskill() {
			//pl2loader.load(pl3url);
			//pl2.addChild(pl2loader);
			//pl2.scaleX = 0.3;
			//pl2.scaleY = 0.3;
			//addChild(pl2);
			trace("WTF?");
		}
		public function getMc2(){
			return pl2;
		}
		public function getMc(i){
			var pl2url = new URLRequest("../skills/luffy/skill"+i+".png");
			trace(i);
			trace("../skills/luffy/skill"+i+".png");
			pl2loader.load(pl2url);
			pl2.addChild(pl2loader);
			pl2.scaleX = 0.3;
			pl2.scaleY = 0.3;
		}
	}
}
/*
var nav1Items:Array = new Array("about", "work", "contact");

var nav1:MovieClip = new MovieClip();
nav1.x=2;
nav1.y=2;

addChild(nav1);

for (var i:Number = 0; i< nav1Items.length; i++) {
    //Create text field
    var myFont:Font =new Font();//"Calibri"
    var myFormat:TextFormat = new TextFormat();
    var label_txt:TextField = new TextField();
    //Set text style
    myFormat.font = myFont.fontName;
    myFormat.size = 16;
    label_txt.defaultTextFormat = myFormat;
    var n1:MovieClip= new MovieClip();
    n1.addChild(label_txt);
    n1.mouseChildren=false;
    n1.buttonMode=true;
    n1.y=i*20;
    label_txt.text = nav1Items[i];
    label_txt.autoSize = TextFieldAutoSize.LEFT;
    nav1.addChild(n1);
}*/