package devoron.sdk.server
{
	import devoron.as3code.ClassProxy;
	import devoron.as3code.ClassProxyDomain;
	import devoron.as3code.ScriptContext;
	import devoron.file.FileInfo;
	import devoron.studio.codeeditor.history.CodeHistory;
	import devoron.studio.codeeditor.livecode.codehandlers.LiveMethodNodeHandler;
	import devoron.studio.codeeditor.livecode.LiveCodeStrategy;
	import devoron.studio.codeeditor.livecode.CodeElementsTableModel;
	import devoron.studio.codeeditor.livecode.LivePackageNodeHandler;
	import devoron.studio.compiler.AS3CodeCompiler;
	import devoron.studio.compiler.RemoteScope;
	import devoron.studio.compiler.ScopeProxy;
	import devoron.studio.compiler.ScriptBytecode;
	import devoron.studio.runtime.preloader.StudioRuntimeGUI;
	import devoron.studio.runtime.server.events.LiveServerEvent;
	import devoron.studio.runtime.server.ILiveClientController;
	import devoron.studio.runtime.server.LiveClientMediator;
	import devoron.studio.runtime.server.LiveGenerator;
	import devoron.studio.runtime.SWCLibraryDomain;
	import flash.events.EventDispatcher;
	import flash.events.GlobalEventDispatcher;
	import flash.system.ApplicationDomain;
	import flash.utils.ByteArray;
	import flash.utils.Dictionary;
	import org.as3commons.asblocks.api.IClassType;
	import org.as3commons.asblocks.impl.ASParserImpl;
	import org.as3commons.asblocks.impl.ASProject;
	import org.as3commons.asblocks.impl.ASQName;
	import org.as3commons.asblocks.impl.CompilationUnitNode;
	import org.as3commons.asblocks.impl.FieldNode;
	import org.as3commons.asblocks.parser.api.ISourceCode;
	import org.as3commons.asblocks.visitor.ASBlocksWalker;
	import org.as3commons.asbook.impl.ASBook;
	import org.as3commons.asbuilder.impl.ASBuilderFactory;
	import org.as3commons.bytecode.abc.AbcFile;
	import org.as3commons.bytecode.emit.IAbcBuilder;
	import org.as3commons.bytecode.emit.impl.AbcBuilder;
	import org.as3commons.bytecode.emit.impl.ClassBuilder;
	import org.as3commons.bytecode.emit.impl.event.ExtendedClassesNotFoundError;
	import org.as3commons.bytecode.emit.IPackageBuilder;
	import org.aswing.util.HashMap;
	
	/**
	 * StudioServer
	 * @author Devoron
	 */
	public class StudioServer extends EventDispatcher
	{
		public var as3code:String;
		protected var compiler:AS3CodeCompiler;
		protected var compiledScript:ScriptBytecode;
		protected var remoteProxy:RemoteScope;
		protected var gui:StudioRuntimeGUI;
		protected var sourceCode:String;
		protected var localScope:ScopeProxy;
		public static var unit:CompilationUnitNode;
		public static var factory:ASBuilderFactory;
		public var scriptDomain:ClassProxyDomain;
		
		private var bodies:HashMap;
		private var body:String;
		public static var targetClasses:Dictionary;
		public static var targetMethods:Dictionary;
		public static var instance:StudioServer;
		protected var parser:ASParserImpl;
		protected var clientController:ILiveClientController;
		
		public var classBuilder:ClassBuilder;
		
		public function StudioServer(clientController:ILiveClientController = null)
		{
			
			if (StudioServer.instance)
			{
				throw new Error("LiveServer already initialized!");
				return;
			}
			instance = this;
			
			if (!clientController)
			{
				clientController = new LiveClientMediator();
			}
			
			this.setClientController(clientController);
		
		}
		
		/**
		 * Установить пользовательский интерфейс.
		 * @param	gui
		 * @param	theme
		 */
		public function setGUI(gui:StudioRuntimeGUI /*, theme:BasicLookAndFeel = null*/):void
		{
			this.gui = gui;
			
			/*if (theme)
			   UIManager.setLookAndFeel(theme);*/
			
			gui.revalidate();
			gui.updateUI();
		}
		
		/**
		 * Установка исходного кода из .as файла.
		 * @param	data FileInfo or String
		 */
		public function setCode(data:*):void
		{
			
			// новые данные для модели
			var model:CodeElementsTableModel = StudioRuntimeGUI.model;
			model.setData([]);
			
			//var searchByteArray:ByteArray = new ByteArray();
			//AbcSpec.writeStringInfo(originalString, searchByteArray);
			
			//if(!methodsRepair)
			//this.methodsRepair = new LiveStation();
			
			this.sourceCode;
			if (data is FileInfo)
			{
				var ba:ByteArray = (data as FileInfo).data;
				ba.position = 0;
				sourceCode = ba.readMultiByte(ba.bytesAvailable, "utf-8");
			}
			else if (data is String)
			{
				sourceCode = data as String;
			}
			
			// создание abc-файла для этого кода
			// AbcFile содержит в себе массивы всех элементов кода
			var file:AbcFile = new AbcFile();
			var abcBuilder:IAbcBuilder = new AbcBuilder(file);
			var packageBuilder:IPackageBuilder = abcBuilder.definePackage("com.classes.generated");
			classBuilder = packageBuilder.defineClass("RuntimeClass") as ClassBuilder;
			classBuilder.addEventListener(ExtendedClassesNotFoundError.EXTENDED_CLASSES_NOT_FOUND, classNotFoundErrorHandler);
			
			// билдер фабрики
			factory = new ASBuilderFactory();
			// исходный код
			var sCode:ISourceCode = factory.newSourceCode(sourceCode, "MAINS.other.editors.ScriptTestApplication2");
			
			var project:ASProject = new ASProject(factory);
			var book:ASBook = new ASBook(project);
			book.process();
			
			if (!parser)
				parser = factory.newParser() as ASParserImpl;
			unit = parser.parseString(sourceCode, true) as CompilationUnitNode;
			
			//var remoteProxy:RemoteScope = new RemoteScope(_this, _this);
			
			var liveClass:devoron.as3code.ClassProxy = new devoron.as3code.ClassProxy(this._this, this._this);
			var liveCS:LiveCodeStrategy = new LiveCodeStrategy();
			liveCS.targetScope = liveClass;
			
			var history:CodeHistory = new CodeHistory(classBuilder);
			var ast:LiveClassAST = new LiveClassAST();
			
			liveCS.registerNodeHandler("org.as3commons.asblocks.impl.PackageNode", new devoron.studio.codeeditor.livecode.LivePackageNodeHandler());
			liveCS.registerNodeHandler("org.as3commons.asblocks.impl.MethodNode", new devoron.studio.codeeditor.livecode.codehandlers.LiveMethodNodeHandler(history, liveClass, ast));
			
			//var strat:LiveCodeStrategy = new LiveCodeStrategy();
			//strat.targetScope = remoteProxy;
			
			var vis:ASBlocksWalker = new ASBlocksWalker(liveCS);
			vis.visitPackage(unit.packageNode);
			vis.visitClassType(unit.typeNode as IClassType);
		
			//GlobalEventDispatcher.instance.dispatchEvent(new CodeEvent(CodeEvent.ADD_METHOD, "", methodQName, ba2));
			//clientController.prepareScope(null, 
		}
		
		protected function createLiveCodeStrategy():LiveCodeStrategy
		{
			return null;
		}
		
		private var liveGenerator:LiveGenerator = new LiveGenerator();
		
		public function generateScriptForMethod(methodName:String, stats:Vector.<String>):void
		{
			//var methodName:String = "MAINS.other.editors.ScriptTestApplication2#function:someFunc"
			//scopeProxy
			//MAINS.other.editors.ScriptTestApplication2#function:omggg30
			//MAINS.other.editors.ScriptTestApplication2#function:omggg3 = Vector.<String> @9b7c791
			
			//var stats:Vector.<String> = MethodNodeHandler.methodsStatememtsHash.get(methodName);
			if (stats)
			{
				//compiledScript = generateScriptFromFunctionBody(stats.join("\n"), new ScriptDomain(ApplicationDomain.currentDomain), compiler);
				var domain:ClassProxyDomain = new ClassProxyDomain(ApplicationDomain.currentDomain);
				var remoteScope:RemoteScope = new RemoteScope(null, null);
				compiledScript = liveGenerator.generateScriptFromFunctionBody(remoteScope, stats.join("\n"), domain);
				
				// отсюда, из сервера, скрипт должен быть отправлен клиенту
				GlobalEventDispatcher.instance.dispatchEvent(new LiveServerEvent(LiveServerEvent.GENERATE_SCRIPT, compiledScript.name, methodName, compiledScript.bytes));
			}
		}
		
		/**
		 * Сгенерировать скрипт для поля.
		 * @param	fieldName
		 */
		public function generateScriptForField(fieldName:String, field:FieldNode):void
		{
			var methodName:String = "MAINS.other.editors.ScriptTestApplication2#function:someFunc"
			//scopeProxy
			//MAINS.other.editors.ScriptTestApplication2#function:omggg30
			//MAINS.other.editors.ScriptTestApplication2#function:omggg3 = Vector.<String> @9b7c791
		
			//var stats:Vector.<String> = FieldNodeHandler.fieldsHash.get(fieldName) as FieldNode;
			//var field:FieldNode = FieldNodeHandler.fieldsHash.get(fieldName) as FieldNode;
			//field.name
			// один необязательный параметр, возвращаемое значение по типу переменной - геттер и сеттер в одной функции
		
			//var fieldInitializerScript:String = ASTUtil.initText(field.initializer.node);
			//compiledScript = generateScriptFromFunctionBody(fieldInitializerScript, new ScriptDomain(ApplicationDomain.currentDomain), compiler);
			//compiledScript = liveGenerator.generateScriptFromFunctionBody(null, stats.join("\n"), domain);
		
			//GlobalEventDispatcher.instance.dispatchEvent(new CodeEvent(CodeEvent.GENERATE_SCRIPT, compiledScript.name, methodName, compiledScript.bytes));
		}
		
		public function initServer():void
		{
			/*var server:AIRServer = new AIRServer();
			
			server.addEndPoint(new SocketEndPoint(1234, new AMFSocketClientHandlerFactory()));
			
			server.addEventListener(AIRServerEvent.CLIENT_ADDED, clientAddedHandler);
			server.addEventListener(AIRServerEvent.CLIENT_REMOVED, clientRemovedHandler);
			server.addEventListener(MessageReceivedEvent.MESSAGE_RECEIVED, messageReceivedHandler);*/
		}
		
		/*	protected function clientAddedHandler(event:AIRServerEvent):void
		   {
		   trace("Client added: " + event.client.id + "\n");
		   }*/
		
		/*protected function clientRemovedHandler(event:AIRServerEvent):void
		   {
		   trace("Client removed: " + event.client.id + "\n");
		   }*/
		
		/*protected function messageReceivedHandler(event:MessageReceivedEvent):void
		   {
		   trace("<client" + event.message.senderId + "> " + event.message.data + "\n");
		   }*/
		
		/**
		 * Каждый хелпер должен выполняться в отдельном потоке
		 * в собственном домене.
		 * @param	helper возможно IThread-класс, который конвертируется в поток
		 * или массив байтов хелпера
		 */
		public function registerSWC(liverHelper:*):void
		{
		/*	liverHelper.liveApplicationDomain = new LiveServerDomain();
		
		   var libsDirectoryPath:String = "F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\lib\\";
		
		   var swcPaths:String = gui.libsTF.getText();
		   //trace(ta.getText());
		
		   var swcArray:Array = swcPaths.split("\r");*/
		
			   // все названия забрать из gui.li
			   //swcArray.push("linalg.swc");
			   //swcArray.push("linalg.swc");
			   //swcArray.push("opprimendi-away3d4-1.6.66(1).swc");
			   //swcArray.push("fzip.swc");
			   //swcArray.push("fzip.swc");
			   //swcLD.setLibrariesDirectoryPath(libsDirectoryPath);
		
		}
		
		private function onError(e:Error):void
		{
			gtrace(e);
		}
		
		private function onComplete(as3code:*):void
		{
			//processAS3Code(as3code);
		}
		
		//public function init(repairToolWorkerClass:Class, scriptDomain:ScriptDomain):void
		//{
		//repairToolWorker = WorkerDomain.current.createWorker(new repairToolWorkerClass());
		
		// каналы связи
		/*	toRepairStation = repairToolWorker.createMessageChannel(Worker.current);
		   fromRepairStation = Worker.current.createMessageChannel(repairToolWorker);
		
		   // задать фоновому воркеру каналы со связанными с ними строковыми ключами
		   repairToolWorker.setSharedProperty("toRepairStation", toRepairStation);
		   repairToolWorker.setSharedProperty("fromRepairStation", fromRepairStation);
		
		   //добавить слушатель на получение данных из фонового воркера
		   fromRepairStation.addEventListener(Event.CHANNEL_MESSAGE, repairToolWorkerResultHandler);*/
		//}
		
		/**
		 * Генерация скрипта из тела функции.
		 * Тут всё просто - даём тело
		 * из него генерируется скрипт.
		 *
		 * Если это дебаг, то в scope добавляется gtrace,
		 * а так он
		 *
		 * А ещё этот код до сего момента можно было пропатчить
		 * как угодно) И можно будет.
		 *
		 * @param	body
		 */
		public function generateScriptFromFunctionBody3(body:String, domain:ClassProxyDomain = null, compiler:AS3CodeCompiler = null):ScriptBytecode
		{
			//if (compiler.initialized)
			//{
			// домен скрипта может наследоваться от домена этого класса
			//if (!domain)
			//domain = new ScriptDomain(new ApplicationDomain(ApplicationDomain.currentDomain));
			//domain = new ScriptDomain(ApplicationDomain.currentDomain);
			
			//domain.addDefinition("org.aswing.graphics.Pen", "Pen");
			
			// сюда циклом записюываются определения
			//domain.addDefinition("
			var useObjectProxies:Boolean = true;
			
			//scope = {stage:};
			
			//scope.gtrace = CodeWindow.outputTA.appendText;
			//scope.gtrace = out;
			
			// здесь должна быть обманка - с ScriptDomain - все 
			//scopeProxy.trace = trace;
			//scopeProxy.gtrace = gtrace;
			//remoteProxy = new ScopeProxy(null, null);
			
			var context:ScriptContext = new ScriptContext(remoteProxy, useObjectProxies, domain);
			//body = "trace(1111111111111111111111111);";
			gtrace("*************************");
			gtrace(body);
			gtrace("*************************");
			
			//var script:BytecodeScript = compiler.compile(as3code, context) as BytecodeScript;
			
			//this.compiledScript = generateScriptFromFunctionBody(sourceCode, scriptDomain, compiler);
			//script.scope = prepareScope
			//compiledScript.scope
			
			var script:ScriptBytecode = compiler.compiler.compile(body, context) as ScriptBytecode;
			
			// ЗДЕСЬ НЕОБХОДИМО СОЗДАТЬ СКРИПТ И ОТПРАВИТЬ ЕГО В ОСНОВНОЙ ПОТОК - REPAIR STATION
			// ЗАГРУЖАТЬ ЕГО НУЖНО ТАМ. REPAIR STATION ВСТРАИВАЕТСЯ В РАБОЧЕЕ ПРИЛОЖЕНИЕ И УПРАВЛЯЕТСЯ
			// ЧЕРЕЗ ПУБЛИЧНЫЕ МЕТОДЫ
			//if (script)
			//{
			////script.addEventListener(ScriptErrorEvent.SCRIPT_ERROR, onScriptError);
			//script.addEventListener(ScriptEvent.LOAD, onScriptLoad);
			//script.load();
			//}
			
			//}
			return script;
		}
		
		static public function addDefinition(qname:ASQName):void
		{
			//var def:* = getDefinitionByName(qname.qualifiedName);
			//domain.addDefinition("org.aswing.graphics.Pen", "Pen");
			//domain.addDefinition(, "Pen");
		}
		
		//private var compiler:
		
		public function _this(name:String):*
		{
			var any:*;
			try
			{
				any = this[name];
			}
			catch (e:Error)
			{
				if (e.errorID == 1069)
					return null;
			}
			return any;
		}
		
		public function getQualifiedDefinitionNames(targetDomain:String):void
		{
			//ApplicationDomain.currentDomain.getQualifiedDefinitionNames
		}
		
		public function addSWCLibrary(swcName:String):void
		{
			//var libsDirectory:String = "F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\lib\\";
			var swcLD:SWCLibraryDomain = SWCLibraryDomain.instance;
			if (!swcLD)
			{
				swcLD = new SWCLibraryDomain();
				swcLD.setLibrariesDirectoryPath("F:\\Projects\\projects\\flash\\studio\\DevoronStudio\\lib\\");
				swcLD.addEventListener(SWCLibraryDomainEvent.DOMAIN_COMPLETE, onSWCLibraryDomainComplete);
			}
			
			swcLD.loadLibrary(swcName);
		
		/*for each (var swcName:String in names)
		   {
		   swcLD.loadLibrary(swcName);
		   }*/
		}
		
		protected function onSWCLibraryDomainComplete(e:SWCLibraryDomainEvent):void
		{
			gtrace("8:[SWC_LIBRARY_DOMAIN COMPLETE]");
			//lib
			//gtrace((e.currentTarget as SWCLibraryDomain).findClass);
			//SWCLibraryDomain.instance.
		}
		
		protected function setClientController(clientController:ILiveClientController):void
		{
			this.clientController = clientController;
		}
		
		protected function onScriptError(e:ScriptErrorEvent):void
		{
			gtrace(e);
		}
		
		protected function errorHandler(e:IOErrorEvent):void
		{
			gtrace(e);
		}
		
		protected function loadedHandler(e:Event):void
		{
		
		}
		
		protected function onNewClassReady(cls:Class):void
		{
			gtrace(cls);
		}
		
		protected function classNotFoundErrorHandler(e:ExtendedClassesNotFoundError):void
		{
			gtrace("2:" + e.className + "[" + e.applicationDomain.getQualifiedDefinitionNames() + "]" + e.toString());
		}
	
	}

}