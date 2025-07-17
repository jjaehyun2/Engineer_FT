package devoron.components.filechooser
{
	import org.aswing.EmptyIcon;
	import org.aswing.Icon;
	import devoron.data.singleloaders.BYTESloader;
	import devoron.file.FileInfo;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Graphics;
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
	import org.as3commons.asblocks.api.IPackage;
	import org.as3commons.asblocks.impl.ASParserImpl;
	import org.as3commons.asblocks.impl.ASProject;
	import org.as3commons.asblocks.impl.ClassTypeNode;
	import org.as3commons.asblocks.impl.CompilationUnitNode;
	import org.as3commons.asblocks.impl.PackageNode;
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
	public class AS3FCH implements IFileChooserHelper
	{
		
		/** @private Канал связи "из фоновового воркера в основной" */
		private var backToMain:MessageChannel;
		/** @private Канал связи "из основного воркера в фоновый" */
		private var mainToBack:MessageChannel;
		private var bytes:ByteArray;
		
		//private var objectsAndPaths:
		
		public function AS3FCH()
		{
			super();
			
			// создаём каналы связи по тем же самым ключам, что и классе Main
			backToMain = Worker.current.getSharedProperty("backToMainChannel");
			mainToBack = Worker.current.getSharedProperty("mainToBackChannel");
			
			//добавить слушатель на получение данных из основного воркера
			//mainToBack.addEventListener(Event.CHANNEL_MESSAGE, mainWorkerAudioDataHandler);
			//stage.addEventListener(KeyboardEvent.KEY_DOWN, onKey);
			
			//stage.addChild(this);
			
			//BYTESloader.loadBytes("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\src\\MAINS\\other\\editors\\ScriptTestApplication2.as", createImage, this.onError);
		}
		
		/* INTERFACE devoron.components.filechooser.IFileChooserHelper */
		
		public function getSupportedExtensions():Array 
		{
			return ["as"];	
		}
		
		public function getPreviewObject(fi:FileInfo, previewObjectCompleteListener:Function):void 
		{
			this.previewObjectCompleteListener = previewObjectCompleteListener;
			BYTESloader.loadBytes(fi.nativePath, createImage, this.onError);
		}
		
		public function getType():String 
		{
			return "code";
		}
		
		public function getIcon():Icon 
		{
			return new EmptyIcon(20, 20);
		}
		
		public function isEnabled():Boolean 
		{
			return enabled;
		}
		
		public function setEnabled(b:Boolean):void 
		{
			enabled = b;
		}
		
		private var path:String;
		private var previewObjectCompleteListener:Function;
		private var enabled:Boolean = true;
		
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
			var sizeTF:TextField = new TextField();
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
			
			sizeTF.text = String(Math.round((length / 1024) * 100) / 100) + " KB";
			
			bytes.position = 0;
			var sourceCode:String = bytes.readMultiByte(bytes.bytesAvailable, "utf-8");
			
			var codeLines:Array = sourceCode.split("\n");
			
			var factory:ASBuilderFactory = new ASBuilderFactory();
			var sCode:ISourceCode = factory.newSourceCode(sourceCode, "MAINS.ScriptTestApplication2");
			
			var project:ASProject = new ASProject(factory);
			var book:ASBook = new ASBook(project);
			book.process();
			
			var parser:ASParserImpl;
			if (!parser)
				parser = factory.newParser() as ASParserImpl;
			var unit:CompilationUnitNode = parser.parseString(sourceCode, true) as CompilationUnitNode;
			
			var packageNode:IPackage = unit.packageNode;
			var imports:Vector.<String> = packageNode.findImports();
			var importClassName:String;
			
			// получить все имена определений классов для ApplicationDomain.currentDomain в удалённом клиенте
			//LiveServer.instance.getQualifiedDefinitionNames("");
			//for each (importClassName in imports)
			//{
				//var clsName:String = importClassName.substring(importClassName.lastIndexOf(".") + 1, importClassName.length);
			
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
			
			classNameTF.text = className + " " + classNode.visibility.toString().toUpperCase();
			if(classNode.packageName)
			packageNameTF.text = classNode.packageName;
			
			
			//nameTF.text = "
			fieldsTF.text = "fields " + String(fields.length);
			methodsTF.text = "methods " + String(methods.length);
			interfacesTF.text = "interfaces " + String(interfaces.length);
			codeLinesTF.text = "lines " + String(codeLines.length);
			importsTF.text = "imports " +   String(imports.length);
			
			isDynamicTF.text = classNode.isDynamic ? "dynamic" : " ";
			isFinalTF.text = classNode.isFinal ? "final " : " ";
			isSubTypeTF.text = classNode.isSubType ? "ext" : " ";
			
			/*	classNode.isDynamic
			   classNode.isFinal
			   classNode.isSubType*/
			
			classNameTF.x = 5;
			
			packageNameTF.x = 5;
			packageNameTF.y = 20;
			
			fieldsTF.x = 5;
			fieldsTF.y = 40;
			
			methodsTF.x = 105;
			methodsTF.y = 40;
			
			interfacesTF.x = 5;
			interfacesTF.y = 60;
			
			isDynamicTF.x = 105;
			isDynamicTF.y = 20;
			
			isFinalTF.x = 135;
			isFinalTF.y = 20;
			
			importsTF.x = 105;
			importsTF.y = 60;
			
			codeLinesTF.x = 5;
			codeLinesTF.y = 80;
			
			sizeTF.x = 105;
			sizeTF.y = 80;
			
			//packageNameTF.x =105;
			//packageNameTF.y = 25;
			
			imageSprite.addChild(classNameTF);
			imageSprite.addChild(fieldsTF);
			imageSprite.addChild(methodsTF);
			imageSprite.addChild(interfacesTF);
			imageSprite.addChild(codeLinesTF);
			imageSprite.addChild(sizeTF);
			imageSprite.addChild(isDynamicTF);
			imageSprite.addChild(isFinalTF);
			imageSprite.addChild(importsTF);
			//imageSprite.addChild(isSubTypeTF);
			imageSprite.addChild(packageNameTF);
			
			//stage.addChild(imageSprite);
			
			bd.draw(imageSprite);
			
			//var bi:Bitmap = new Bitmap(bd);
			
			////if (super.numChildren > 0)
			//{
				//removeChildAt(0);
			//}
			
			//addChild(bi);
			
			var ba:ByteArray = new ByteArray();
			bd.copyPixelsToByteArray(bd.rect, ba);
			
			
			createImage.call(null, ba);
			
			
		
			//backToMain.send(path);
			//backToMain.send(ba);
			//onDecode(bd);
		}
		
		protected function onKey(e:KeyboardEvent):void
		{
			if (e.keyCode == Keyboard.R)
			{
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