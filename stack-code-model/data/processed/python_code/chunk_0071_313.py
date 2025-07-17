package devoron.sdk.server
{
	import devoron.as3code.ScriptContext;
	import devoron.as3code.ClassProxyDomain;
	import devoron.studio.codeeditor.livecode.LiveCodeStrategy;
	import devoron.studio.compiler.RemoteScope;
	import devoron.studio.compiler.ScopeProxy;
	import devoron.studio.compiler.ScriptBytecode;
	import devoron.studio.compiler.events.ScriptErrorEvent;
	import devoron.studio.compiler.events.ScriptEvent;
	import flash.system.ApplicationDomain;
	import flash.utils.ByteArray;
	import flash.utils.Proxy;
	
	/**
	 * LiveClientLoader
	 * @author Devoron
	 */
	public class LiveClientLoader
	{
		
		public function LiveClientLoader()
		{
		
		}
		
		public function loadScriptByteCode(bytes:ByteArray, targetName:String):void{
			var classScope:RemoteScope = LiveCodeStrategy.scopeProxy;
			var context:ScriptContext = new ScriptContext(classScope, true, new ClassProxyDomain(ApplicationDomain.currentDomain));
			var script:ScriptBytecode = new ScriptBytecode(context, bytes);
			script.name = targetName;
			loadScript(script, targetName);
		}
		
		public function loadScript(script:ScriptBytecode, targetName:String):void
		{
			var nm:String = targetName;
			var classScope:RemoteScope = LiveCodeStrategy.scopeProxy;
			classScope[nm] = script.exe;
			script.name = nm;
			script.addEventListener(ScriptEvent.LOAD, onScriptLoad);
			script.addEventListener(ScriptErrorEvent.SCRIPT_ERROR, onScriptError);
			script.load();
		}
		
		private function onScriptLoad(e:ScriptEvent):void
		{
			try
			{
				/*var scope:ScopeProxy = new ScopeProxy(null, null);
				   scopeProxy.gtrace = gtrace;
				   scopeProxy.trace = gtrace;
				   scopeProxy.stage = AsWingManager.getStage();*/
				
				//gtrace("4:script complete " + e.script.exe(LiveControllerCodeStrategy.scopeProxy));
				// в скрипт нужно отправлять локальные scope - аргументы функции
				//this.localScope = new ScopeProxy(null, null);
				//var collect:
				
				// localScope для конкретно этого метода
				var localScope:ScopeProxy = LiveCodeStrategy.classesProxyHash.get((e.currentTarget as ScriptBytecode).name);
				// добавить его на уровне родителя
				
				var classScope:Proxy = LiveCodeStrategy.scopeProxy;
				gtrace(classScope);
				var allLocalScopes:Array = LiveCodeStrategy.classesProxyHash.keys();
				
				var nm:String = (e.currentTarget as ScriptBytecode).name;
				//LiveControllerCodeStrategy.scopeProxy[nm]= e.script.exe;
				
				//localScope.parentProxy[(e.currentTarget as ScriptBytecode).name]= e.script.exe;
				
				// до запуска скрипта и во время его выполнения я могу устанавливать новые значения в 
				
				// добавить что-то во все local-scope, усли нужно
				var localScopeProxy:Proxy;
				for each (var localScopeName:String in allLocalScopes)
				{
					localScopeProxy = LiveCodeStrategy.classesProxyHash.get(localScopeName);
					gtrace("8:" + localScopeName + "    " + localScopeProxy);
						//scope[(e.currentTarget as ScriptBytecode).name] = e.script.exe;
					
						//scope[(e.currentTarget as ScriptBytecode).name] = e.script.exe;
				}
				gtrace("4:script complete " + e.script.exe( /*classScope*/));
			}
			catch (error:Error)
			{
				gtrace(error);
			}
		}
		
		protected function onScriptError(e:ScriptErrorEvent):void
		{
			gtrace(e);
		}
	
	}

}