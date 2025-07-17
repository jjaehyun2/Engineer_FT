package
{
	import flash.display.Sprite;
	import flash.events.MouseEvent;
	import flash.filesystem.File;
	import flash.filesystem.FileMode;
	import flash.filesystem.FileStream;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.utils.ByteArray;
	
	[SWF(width="960",height="640",frameRate="30",backgroundColor = "#ffffff")]
	public class SceneCreator extends Sprite
	{
		private const ENTER:String = "\n";
		private const TAB:String = "\t";

		private var output:TextField;
		public function SceneCreator()
		{
			super();
			
//			var file:File = File.desktopDirectory.resolvePath("scene.xml");
//			var file:File = new File("E:\\Workplace\\RTSMobile\\src\\xml\\scene.xml");
			
			createBtn(100,100,"导出scene",onClick);
			createBtn(100,150,"导出plane",onClick2);
			
			output = new TextField();
			output.text = "waiting";
			output.x = 100;
			output.y = 300;
			output.selectable = false;
			addChild(output);
		}
		
		protected function createBtn(x:Number,y:Number,txt:String,func:Function):void{
			var text:TextField = new TextField();
			text.autoSize = TextFieldAutoSize.LEFT;
			text.border = true;
			text.text = txt;
			text.x = x;
			text.y = y;
			text.selectable = false;
			text.addEventListener(MouseEvent.CLICK,func);
			addChild(text);
		}
		
		protected function onClick(event:MouseEvent):void
		{
			output.text = "writting file....";
			
			var file:File = new File("E:\\workplace\\RTSMobile\\src\\xml\\scene.xml");
			var fs:FileStream = new FileStream();
			fs.open(file,FileMode.WRITE);
			
			var byte:ByteArray = new ByteArray;
			byte.writeUTFBytes("<data>" + ENTER);
			for(var i:int=0;i<6;i++){
				var scene:SceneData = new SceneData();
				scene.id = i;
				scene.def = i%2;
				scene.width = 1000;
				scene.height = 800;
				scene.basex = 900;
				scene.basey = 500;
				scene.baseHp = 2000;
				
				var batteryCount:int=5;
				for(var j:int=0;j<batteryCount;j++){
					var node:BatNode = new BatNode;
					scene.vec.push(node);
					
					var batData:BatData = new BatData();
					batData.x = 700 + j%2*100;
					batData.y = 200 + j*70;
					batData.attack = 5 + i*5;
					batData.range = 500;
					batData.rate = 1000;
					batData.hpMax = 400;
					batData.drop = 40;
					batData.buddle = 0;
					node.vec.push(batData);
				}
				
				writeScene(byte,scene);
			}
			byte.writeUTFBytes("</data>" + ENTER);
			fs.writeBytes(byte);
			fs.close();
			
			output.text = "scene finish";
		}
		
		protected function onClick2(event:MouseEvent):void
		{
			output.text = "writting file....";
			
			var file:File = new File("E:\\workplace\\RTSMobile\\src\\xml\\plane.xml");
			var fs:FileStream = new FileStream();
			fs.open(file,FileMode.WRITE);
			
			var byte:ByteArray = new ByteArray;
			byte.writeUTFBytes("<data>" + ENTER);
			
			var plane:PlaneData;
			var j:int;
			var cpd:Vector.<Number> = Vector.<Number>([0.5,  2.0,  0.7,  0.9,  1.1,  0.3]);
			var cph:Vector.<Number> = Vector.<Number>([1.0,  0.5,  2.5,  1.5,  1.8,  0.9]);
			var pricesBase:Vector.<int> = Vector.<int>([100,150,180,200,250,280]);
			var pricesRaise:Vector.<int> = Vector.<int>([100,150,180,200,250,280]);
			for(var i:int=0;i<Factory.VEC.length;i++){
				for(j=0;j<5;j++){
					plane = new PlaneData();
					var price:int = pricesBase[i] + pricesRaise[i]*j;
					var attack:int = price * cpd[i];
					var hp:int = price * cph[i];
					plane.setData(hp,attack,350,2000,0,price);
					plane.type = Factory.VEC[i];
					
					writePlane(byte,plane);
				}
			}
			
			byte.writeUTFBytes("</data>" + ENTER);
			fs.writeBytes(byte);
			fs.close();
			
			output.text = "plane finish";
		}
		
		private function writeScene(byte:ByteArray,scene:SceneData):void{
			var str:String = "<scene>" + ENTER;
			str += nodeStr("id",scene.id.toString());
			str += nodeStr("def",scene.def.toString());
			str += nodeStr("width",scene.width.toString());
			str += nodeStr("height",scene.height.toString());
			str += nodeStr("basex",scene.basex.toString());
			str += nodeStr("basey",scene.basey.toString());
			str += nodeStr("baseHp",scene.baseHp.toString());
			for(var i:int=0;i<scene.vec.length;i++){
				str += TAB + "<battery>" + ENTER;
				for(var j:int=0;j<scene.vec[i].vec.length;j++){
					str += TAB;
					str += nodeStr("data",scene.vec[i].vec[j].toString());
				}
				str+= TAB + "</battery>" + ENTER;
			}
			str+="</scene>" + ENTER;
			byte.writeUTFBytes(str);
		}
		
		private function writePlane(byte:ByteArray,plane:PlaneData):void{
			var str:String = "<" + plane.type + ">" + ENTER;
			str+=nodeStr("hpMax",plane.hpMax.toString());
			str+=nodeStr("attack",plane.attack.toString());
			str+=nodeStr("rate",plane.rate.toString());
			str+=nodeStr("range",plane.range.toString());
			str+=nodeStr("buddle",plane.buddle.toString());
			str+=nodeStr("price",plane.price.toString());
			str+= "</" + plane.type + ">" + ENTER;
			byte.writeUTFBytes(str);
		}
		
		private function nodeStr(node:String,value:String):String{
			return TAB + "<" + node + ">" + value + "</" + node +">" + ENTER;
		}
	}
}

class PlaneData{
	public function setData(hpMax:int,attack:int,range:int,rate:int,buddle:int,price:int):void{
		this.hpMax = hpMax;
		this.attack = attack;
		this.range = range;
		this.rate = rate;
		this.buddle = buddle;
		this.price = price;
	}
	
	public var type:String;
	public var hpMax:int;
	public var range:int;
	public var rate:int;
	public var attack:int;
	public var buddle:int;
	public var price:int;
}

class SceneData{
	public var id:int;
	public var def:int;
	public var width:Number;
	public var height:Number;
	
	public var basex:Number;
	public var basey:Number;
	public var baseHp:int;
	
	public var vec:Vector.<BatNode> = new Vector.<BatNode>;
	
	public function SceneData(){
		
	}
}

class BatNode{
	public var vec:Vector.<BatData> = new Vector.<BatData>;
	public function BatNode(){
		
	}
}

class BatData{
	public var x:Number;
	public var y:Number;
	public var range:int;
	public var rate:int;
	public var attack:int;
	public var hpMax:int;
	public var drop:int;
	public var buddle:int;
	
	public function BatData(){
		
	}
	
	public function toString():String{
		return x + "," + y + "," + range + "," + rate + "," + attack + "," + hpMax + "," + drop + "," + buddle;
	}
}