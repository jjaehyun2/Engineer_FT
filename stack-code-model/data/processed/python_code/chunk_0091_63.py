package devoron.sdk.server
{
	import devoron.as3code.ScriptContext;
	import devoron.as3code.ClassProxyDomain;
	import devoron.studio.compiler.AS3CodeCompiler;
	import devoron.studio.compiler.RemoteScope;
	import devoron.studio.compiler.ScriptBytecode;
	import devoron.studio.compiler.events.CompilerErrorEvent;
	import devoron.studio.compiler.events.CompilerEvent;
	import devoron.utils.gtrace;
	import org.as3commons.bytecode.abc.AbcFile;
	import org.as3commons.bytecode.abc.MethodBody;
	
	/**
	 * ...
	 * @author Devoron
	 */
	public class LiveGenerator
	{
		protected var compiler:AS3CodeCompiler;
		
		public function LiveGenerator()
		{
		
		}
		
		/**
		 * Инициализация компилятора.
		 */
		public function initCompiler():void
		{
			this.compiler = new AS3CodeCompiler(false, true);
			compiler.addEventListener(CompilerEvent.INIT, onCompilerInited);
			compiler.addEventListener(CompilerErrorEvent.COMPILER_ERROR, onCompilerError);
			compiler.init();
		}
		
		public function useAbcBuilder():void
		{
			//var text:String = ASTUtil.initText((unit.typeNode as IScriptNode).node);
			//gtrace("2: " + text);
			
			//abcBuilder.addEventListener(Event.COMPLETE, loadedHandler);
			//abcBuilder.addEventListener(IOErrorEvent.IO_ERROR, errorHandler);
			//abcBuilder.addEventListener(IOErrorEvent.VERIFY_ERROR, errorHandler);
			
			try
			{
				//abcBuilder.addEventListener(Event.COMPLETE, loadedHandler);
				//abcBuilder.addEventListener(IOErrorEvent.IO_ERROR, errorHandler);
				//abcBuilder.addEventListener(IOErrorEvent.VERIFY_ERROR, errorHandler);
				//abcBuilder.addEventListener(IOErrorEvent.VERIFY_ERROR, verifieErrorHandler);
				//abcBuilder.build();
				//abcBuilder.buildAndLoad();
				//abcBuilder.buildAndLoad(new ApplicationDomain(ApplicationDomain.currentDomain));
				//var abcSWF:ByteArray = abcBuilder.buildAndExport(ApplicationDomain.currentDomain);
				//
				//AirMediator.writeToFile("D:\\MyGeneratedClasses.swf", abcSWF, AirMediator.BYTES);
				
				//var file2:FileReference = new FileReference();
				//file2.save(abcSWF, "MyGeneratedClasses.swf");
				
			}
			catch (e:Error)
			{
				gtrace("2:" + e);
			}
			
			return;
			//var abc:AbcFile = abcBuilder.buildAndLoad(ApplicationDomain.currentDomain, ApplicationDomain.currentDomain);
			//var abc:ByteArray = abcBuilder.buildAndExport(ApplicationDomain.currentDomain);
			
			//new FileReference().save(abc, "MyGeneratedClasses.swf");
			
			//gtrace(abc);
			
			// создание кода на лету для этого поля
		/*	var c1:Object = {name: unit.typeName, type: "String"};
			var classProperties:Array = [c1];
			
			var classProp:Object;
			var prpp:Array = [];
			for (var j:int = 0; j < classProperties.length; j++)
			{
				classProp = classProperties[j];
				try
				{
					var ClassReference:Class = getDefinitionByName(classProp.type) as Class;
					//trace("point " + getDefinitionByName(String("flash.display::Point")));
					prpp.push(new ClassProperty(classProp.name, ClassReference, MemberVisibility.fromValue("public")));
				}
				catch (e:Error)
				{
					gtrace("2:" + e);
				}*/
				
			//} //const pointPaarGenericClassProperties:TupleClassProperties = new TupleClassProperties(prpp);
			//TupleClassGenerator.getTupleClass(pointPaarGenericClassProperties, this.onNewClassReady);
			
			//gui.setCodeText(sourceCode);
			//return;
			//return;
			
			//if(
			//var source:String = codeArea.getText() != "" ? codeArea.getText(): sourceCode;
			// отправка кода на парсинг и получени экземпляра компиляции
			//var classUnit:ICompilationUnit = methodsRepair.repair(sourceCode) as ICompilationUnit;
			//var classUnit:ICompilationUnit = null;
			//var classUnit:ICompilationUnit = methodsRepair.processAS3Code(sourceCode) as ICompilationUnit;
			
			//return;
			//AbcFile
			//ASBookAccess
			gtrace("\n**");
			//gtrace((classUnit.project.compilationUnits[0]));
			//gtrace(classUnit.node.stringValue);
			
			//gtrace(classUnit.
			gtrace("\n");
			//if (classUnit == null)
			//return;
			
			//gtrace("qName					" + String(classUnit.qname));
			//gtrace("\nI:qname " +String(classUnit.qname));
			//gtrace("packageName			" + String(classUnit.packageName));
			//gtrace("typeName				" + String(classUnit.typeName));
			//gtrace("\n");
			
			// СОЗДАНИЕ ActionsctiptByteCode из исходного файла
			//classUnit.node
			
			//nfr 
			
			//build the function
			/*	var methodBuilder:IMethodBuilder = classBuilder.defineMethod("myFunction");
			   methodBuilder.returnType = "Boolean";
			   methodBuilder.visibility = MemberVisibility.PUBLIC;
			   methodBuilder.isFinal = true;
			
			   //add the parameters
			   methodBuilder.defineArgument("String");
			   methodBuilder.defineArgument("int");
			
			   //here begins the method body with the opcode
			   methodBuilder.addOpcode(Opcode.getlocal_0);
			   methodBuilder.addOpcode(Opcode.pushscope);
			   //call the member "member"
			   methodBuilder.addOpcode(Opcode.getlex, [new QualifiedName("member", LNamespace.PUBLIC)]);
			   //access to the function args
			   methodBuilder.addOpcode(Opcode.getlocal_1);
			   methodBuilder.addOpcode(Opcode.getlocal_2);
			   //call the function at the above prepared member with the prepared args
			   methodBuilder.addOpcode(Opcode.callproperty, [new QualifiedName("myFunction", LNamespace.PUBLIC), 2]);
			   //return the result
			   methodBuilder.addOpcode(Opcode.returnvalue);*/
			
			//fire at own will
			
			return;
			
			try
			{
				//throw new Error("Тут я специально сделал ошибку");
				// а это уже выглядит так, будто мы распарсили swf
				//var abcFile:AbcFile = abcBuilder.build();
				//abcFile.instanceInfo
				//var iis:Vector.<InstanceInfo> = abcFile.instanceInfo;
				//for each (var ii:InstanceInfo in iis)
				//{
					/*var om:* = ii.classInfo.getSlotTraitByName("value");
					   trace(om);*/
					
					//var constructor:MethodInfo = ii.constructor;
					//var methodToModification:String = "com.classes.generated.RuntimeClass/RuntimeClass";
					//
					// если искомый метод найден
					//if (constructor.methodName == methodToModification)
					//{
						
						//var constructorBody:MethodBody = constructor.methodBody;
						//constructorBody.traits[0].
						//trace(constructorBody.opcodes);
						
							// то делаем внутри всё, что хотим, а после перекомпилируем метод
							// по его выражениям
					//}
						// вот так записывается имя метода-конструктора, когда будем искать их в классах
						// 
						//MAINS.other.editors.MAINS.other.editors.ScriptTestApplication/MAINS.other.editors.ScriptTestApplication"
						//trace("ii.constructor " + ii.constructor.methodName);
				//}
				
				/*var methodBody:MethodBody = abcFile.methodBodies[0];
				   trace(methodBody.opcodes);
				   trace(methodBody.toString());*/
			}
			catch (e:Error)
			{
				trace("DSPreloader ABCFile" + e);
			}
		
		/*	var abcFile:AbcFile = new AbcFile();
		   //addClassInfo
		   var abcBuilder:AbcBuilder = new AbcBuilder();
		   var binarySwf:ByteArray = abcBuilder.buildAndExport();
		   var file:FileReference = new FileReference();y6
		   file.save(binarySwf, "MyGeneratedClasses.swf");
		 */
		/*var len:int = classUnit.node.numChildren;
		   for (var i:int = 0; i < len; i++)
		   {
		   var token:IParserNode = classUnit.node.children[i];
		   //classUnit.sourceCode.getSlice(startLine:int, endLine:int):String;
		   gtrace(token);
		   }*/
		
			   // обработка полей
		/*var fields:Vector.<IField> = (classUnit as IClassType).fields;
		   var len:int = fields.length;
		   gtrace(len);*/
		
			   //for (i = 0; i < len; i++)
			   //{
			   //var field:IField = fields[i];
			   //gtrace(field.name);
		/*walkMember(field);
		   walkField(field);*/
			   //}
		
			   //gtrace(classUnit.typeNode.visibility);
			   //gtrace(classUnit.typeNode.name);
			   //gtrace(classUnit.typeNode.getAllMetaData(");
		
			   //classUnit.typeNode.
		
		/*var unit:ICompilationUnit = Main_PRICE2000.Main_PRICE20600.tracerr("unit.typeName " + unit.typeName);
		   Main_PRICE2000.gtracer("unit.typeNode " + unit.typeNode); // здесь можно получить содержимое класа
		   Main_PRICE2000.gtracer("unit.packageName " + unit.packageName);
		   Main_PRICE2000.gtracer("unit.packageNode " + unit.packageNode);
		   Main_PRICE2000.gtracer("unit.internalFunctions " + unit.internalFunctions);
		   Main_PRICE2000.gtracer(unit.node.getChild(0));*/
			   //trace("Голова нога плечо");
		/*  for each (var item:FunctionTypeNode in unit.internalFunctions)
		   {
		   Main_PRICE2000.gtracer(item.statements);
		   }
		   Main_PRICE2000.gtracer(unit);*/
		}
		
		protected function onCompilerError(e:CompilerErrorEvent):void
		{
			gtrace(e);
		}
		
		private function onCompilerInited(e:CompilerEvent):void
		{
			if (compiler.compilerInited)
			{
				gtrace("8:[COMPILER INITED]");
					//body = "trace(132)";
					//var fiof:int = as3code.lastIndexOf("{");
					//var fiof2:int = as3code.indexOf("}");
					//var bodyString:String = as3code.substring(fiof + 1 /*+16*/, fiof2 - 1);
					//var liveFuncTemp:String = as3code.indexOf("newAge():Number{"), 
					//body = bodyString;
				
					//this.scopeProxy = new ScopeProxy(null, null);
				/*this.scopeProxy = new Object()
				   scopeProxy["gtrace"] = gtrace;
				   scopeProxy["trace"] = trace;*/
				
					   //AirMei
				/*		  factory = new ASBuilderFactory();
				
				   var pr:ASProject = new ASProject(factory);
				   var book:ASBook = new ASBook(pr)
				   var cc:ASBookAccess = new ASBookAccess(book);*/
			}
			else
			{
				gtrace("2:Compiler not inited in MethodsReparator");
					//gtrace(CodeWindow.outputTA.getHtmlText() + "Compiler not inited in MethodsReparator");
			}
		}
		
		public function generateScriptFromFunctionBody(remoteScope:RemoteScope, body:String, domain:ClassProxyDomain = null, compiler:AS3CodeCompiler = null):ScriptBytecode
		{
			var useObjectProxies:Boolean = true;
			var context:ScriptContext = new ScriptContext(remoteScope, useObjectProxies, domain);
			//body = "trace(1111111111111111111111111);";
			gtrace("*************************");
			gtrace(body);
			gtrace("*************************");
			
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
	
	}

}