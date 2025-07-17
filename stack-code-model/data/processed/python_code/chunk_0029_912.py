package devoron.components.filechooser.workerclassinfo
{
	import devoron.data.singleloaders.BYTESloader;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.KeyboardEvent;
	import flash.system.MessageChannel;
	import flash.system.Worker;
	import flash.text.TextField;
	import flash.ui.Keyboard;
	import flash.utils.ByteArray;
	import org.as3commons.asblocks.api.IField;
	import org.as3commons.asblocks.api.IMethod;
	import org.as3commons.asblocks.impl.ASParserImpl;
	import org.as3commons.asblocks.impl.ASProject;
	import org.as3commons.asblocks.impl.ClassTypeNode;
	import org.as3commons.asblocks.impl.CompilationUnitNode;
	import org.as3commons.asblocks.parser.api.ISourceCode;
	import org.as3commons.asbook.impl.ASBook;
	import org.as3commons.asbuilder.impl.ASBuilderFactory;
	
	/**
	 * WorkerClassInfo.
	 * Генерирует изображение 
	 * размером 197х100(что за странные цифры?)
	 * содержащее
	 *
	 * name qName
	 * imports n
	 * methods n
	 * fields n
	 * 
	 * @author Devoron
	 */
	public class ClassInfoRenderer extends Sprite
	{
		
		/** @private Канал связи "из фоновового воркера в основной" */
		private var backToMain:MessageChannel;
		/** @private Канал связи "из основного воркера в фоновый" */
		private var mainToBack:MessageChannel;
		private var bytes:ByteArray;
		
		//private var objectsAndPaths:
		
		public function ClassInfoRenderer()
		{
			super();
			
			// создаём каналы связи по тем же самым ключам, что и классе Main
			backToMain = Worker.current.getSharedProperty("backToMainChannel");
			mainToBack = Worker.current.getSharedProperty("mainToBackChannel");
			
			//добавить слушатель на получение данных из основного воркера
			//mainToBack.addEventListener(Event.CHANNEL_MESSAGE, mainWorkerAudioDataHandler);
			stage.addEventListener(KeyboardEvent.KEY_DOWN, onKey);
			
			stage.addChild(this);
			
			BYTESloader.loadBytes("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\src\\MAINS\\other\\editors\\ScriptTestApplication2.as", createImage, this.onError);
		}
		
		private var path:String;
		
		/**
		 * Обработчик получения команды на вычисление спектра.
		 * @param	e
		 */
		private function mainWorkerAudioDataHandler(e:Event):void
		{
			var result:* = mainToBack.receive();
			path = String(result);
			
			// получить байты файла исходного кода
			bytes = Worker.current.getSharedProperty("bytes");
			
			if (bytes)
			{
				//sound = new Sound();
				//sound.addEventListener(Event.COMPLETE, onSoundComplete);
				//sound.loadCompressedDataFromByteArray(bytes, bytes.length);
				//createImage(bytes);
				createImage(bytes);
			
			}
		}
		
		private function onSoundComplete(e:Event):void
		{
			
			//backToMain.send("в рот мне ноги");
			createImage(bytes);
		}
		
		private function createImage(bytes:ByteArray):void
		{
			var imageSprite:Sprite = new Sprite();
			var nameTF:TextField = new TextField();
			var importsTF:TextField = new TextField();
			var methodsTF:TextField = new TextField();
			var fieldsTF:TextField = new TextField();
			var interfacesTF:TextField = new TextField();
			var codeLinesTF:TextField = new TextField();
			var isDynamicTF:TextField = new TextField();
			var isFinalTF:TextField = new TextField();
			var isSubTypeTF:TextField = new TextField();
			var classNameTF:TextField = new TextField();
			classNameTF.width = 197;
			var packageNameTF:TextField = new TextField();
			packageNameTF.width = 180;
			
			
			var bd:BitmapData = new BitmapData(197, 100);
			bd.lock();
			var length:Number = bytes.length;
			
			
				bytes.position = 0;
				var sourceCode:String = bytes.readMultiByte(bytes.bytesAvailable, "utf-8");
				
				var codeLines:Array = sourceCode.split("\n");
				
				var factory:ASBuilderFactory = new ASBuilderFactory();
				var sCode:ISourceCode = factory.newSourceCode(sourceCode, "MAINS.other.editors.ScriptTestApplication2");
				
				var project:ASProject = new ASProject(factory);
				var book:ASBook = new ASBook(project);
				book.process();
				
				var parser:ASParserImpl;
				if (!parser)
					parser = factory.newParser() as ASParserImpl;
				var unit:CompilationUnitNode = parser.parseString(sourceCode, true) as CompilationUnitNode;
				
				
				gtrace(unit);
				//gtrace(book.access.packages);
			
				var classNode:ClassTypeNode = unit.typeNode as ClassTypeNode;
				var methods:Vector.<IMethod> = classNode.methods;
				var fields:Vector.<IField> = classNode.fields;
				var interfaces:Vector.<String> = classNode.implementedInterfaces;
				//var packageName:String = classNode.packageName;
				var className:String = classNode.name;
				
				//var packageNode:PackageNode  = classNode.node.parent as PackageNode;
				//var packageNode:PackageNode = element as PackageNode;
				//var imports:Vector.<String> = packageNode.findImports();
				
				classNameTF.text = className;
				packageNameTF.text = classNode.qualifiedName;
				//nameTF.text = "
				fieldsTF.text = "f\t\t" + String(fields.length);
				methodsTF.text = "m\t\t" +  String(methods.length);
				interfacesTF.text ="i\t\t" +   String(interfaces.length);
				codeLinesTF.text = "code lines\t\t" +   String(codeLines.length);
				//importsTF.text = "imports\t\t" +   String(imports.length);
				
				isDynamicTF.text	 = classNode.isDynamic ?  "d" : " ";
				isFinalTF.text = classNode.isFinal ?  "f " : " ";
				isSubTypeTF.text = classNode.isSubType ?  "ext" : " ";
				
				
			/*	classNode.isDynamic
				classNode.isFinal
				classNode.isSubType*/
				
				classNameTF.x = 5;
				classNameTF.x = 0;
				
				packageNameTF.x =5;
				packageNameTF.y =25;
				
				fieldsTF.x = 5;
				fieldsTF.y = 75;
				
				methodsTF.x = 35;
				methodsTF.y = 75;
				
				interfacesTF.x = 5;
				interfacesTF.y = 75;
				
				isDynamicTF.x = 105;
				isDynamicTF.y = 25;
				
				isFinalTF.x = 135;
				isFinalTF.y = 25;
				
				codeLinesTF.x = 105;
				codeLinesTF.y = 75;
				
				importsTF.x = 105;
				importsTF.y = 50;
				
				//packageNameTF.x =105;
				//packageNameTF.y = 25;
			
				imageSprite.addChild(classNameTF);
				imageSprite.addChild(fieldsTF);
				imageSprite.addChild(methodsTF);
				imageSprite.addChild(interfacesTF);
				imageSprite.addChild(codeLinesTF);
				imageSprite.addChild(isDynamicTF);
				imageSprite.addChild(isFinalTF);
				imageSprite.addChild(importsTF);
				//imageSprite.addChild(isSubTypeTF);
				imageSprite.addChild(packageNameTF);
				
				//stage.addChild(imageSprite);
				
				
				bd.draw(imageSprite);
				
				var bi:Bitmap = new Bitmap(bd);
				
				if (super.numChildren > 0){
					removeChildAt(0);
				}
				
				addChild(bi);
			//var ba:ByteArray = new ByteArray();
			//bd.copyPixelsToByteArray(bd.rect, ba);
			
			//backToMain.send(path);
			//backToMain.send(ba);
			//onDecode(bd);
		}
		
		protected function onKey(e:KeyboardEvent):void 
		{
			if (e.keyCode == Keyboard.R){
				//TXTloader.loadTXT("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\src\\MAINS\\other\\editors\\ScriptTestApplication2.as", liveServer.setCode, this.onError);
				BYTESloader.loadBytes("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\src\\MAINS\\other\\editors\\ScriptTestApplication2.as", createImage, this.onError);
			}
		}
		
		protected function onError(any:*):void 
		{
			gtrace(any);
		}
	
	}

}