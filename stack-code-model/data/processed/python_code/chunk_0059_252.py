/*
 *      _________  __      __
 *    _/        / / /____ / /________ ____ ____  ___
 *   _/        / / __/ -_) __/ __/ _ `/ _ `/ _ \/ _ \
 *  _/________/  \__/\__/\__/_/  \_,_/\_, /\___/_//_/
 *                                   /___/
 * 
 * Tetragon : Game Engine for multi-platform ActionScript projects.
 * http://www.tetragonengine.com/ - Copyright (C) 2012 Sascha Balkau
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package tetragon
{
	import tetragon.audio.AudioManager;
	import tetragon.command.Command;
	import tetragon.command.CommandManager;
	import tetragon.command.env.StartupApplicationCommand;
	import tetragon.core.exception.SingletonException;
	import tetragon.data.Params;
	import tetragon.data.Registry;
	import tetragon.data.Settings;
	import tetragon.debug.Console;
	import tetragon.debug.Log;
	import tetragon.debug.StatsMonitor;
	import tetragon.entity.EntityFactory;
	import tetragon.entity.EntityManager;
	import tetragon.entity.EntitySystemManager;
	import tetragon.env.preload.IPreloader;
	import tetragon.env.settings.LocalSettingsManager;
	import tetragon.file.IFileAPIProxy;
	import tetragon.file.resource.ResourceManager;
	import tetragon.input.KeyInputManager;
	import tetragon.modules.ModuleManager;
	import tetragon.state.StateManager;
	import tetragon.systems.gl.GameLoop;
	import tetragon.util.display.StageReference;
	import tetragon.util.time.CallLater;
	import tetragon.view.ScreenManager;
	import tetragon.view.stage3d.Stage3DManager;
	import tetragon.view.theme.UIThemeManager;

	import flash.display.DisplayObjectContainer;
	import flash.display.Stage;
	import flash.display.StageDisplayState;
	import flash.display3D.Context3D;
	import flash.events.ErrorEvent;
	import flash.events.UncaughtErrorEvent;
	import flash.external.ExternalInterface;
	
	
	/**
	 * Main acts as a central hub for the engine from which all other engine sub-systems
	 * and the startup phase are initiated. It also provides references to often-used
	 * classes and objects.
	 */
	public final class Main
	{
		//-----------------------------------------------------------------------------------------
		// Properties
		//-----------------------------------------------------------------------------------------
		
		/** @private */
		private static var _instance:Main;
		/** @private */
		private static var _singletonLock:Boolean;
		
		/** @private */
		public static var params:Params;
		
		/** @private */
		private var _contextView:DisplayObjectContainer;
		/** @private */
		private var _appInfo:IAppInfo;
		/** @private */
		private var _registry:Registry;
		/** @private */
		private var _setups:Array;
		/** @private */
		private var _resourceBundleClass:Class;
		
		/** @private */
		private var _classRegistry:ClassRegistry;
		/** @private */
		private var _moduleManager:ModuleManager;
		/** @private */
		private var _commandManager:CommandManager;
		/** @private */
		private var _resourceManager:ResourceManager;
		/** @private */
		private var _screenManager:ScreenManager;
		/** @private */
		private var _stateManager:StateManager;
		/** @private */
		private var _themeManager:UIThemeManager;
		/** @private */
		private var _localSettingsManager:LocalSettingsManager;
		/** @private */
		//private var _renderBufferManager:RenderBufferManager;
		/** @private */
		private var _stage3DManager:Stage3DManager;
		/** @private */
		private var _keyInputManager:KeyInputManager;
		/** @private */
		private var _gameLoop:GameLoop;
		/** @private */
		private var _entityManager:EntityManager;
		/** @private */
		private var _entitySystemManager:EntitySystemManager;
		/** @private */
		private var _entityFactory:EntityFactory;
		/** @private */
		private var _audioManager:AudioManager;
		/** @private */
		private var _fileAPIProxy:IFileAPIProxy;
		
		
		//-----------------------------------------------------------------------------------------
		// Constructor
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Constructs a new App instance.
		 */
		public function Main()
		{
			if (!_singletonLock) throw new SingletonException(this);
		}
		
		
		/**
		 * Initializes Main.
		 * 
		 * @param contextView
		 * @param appInfo
		 * @param setups
		 * @param resourceBundleClass
		 * @param fileAPIProxy
		 */
		public function init(contextView:DisplayObjectContainer, appInfo:IAppInfo,
			setups:Array, resourceBundleClass:Class, fileAPIProxy:IFileAPIProxy):void
		{
			_contextView = contextView;
			_appInfo = appInfo;
			_setups = setups;
			_resourceBundleClass = resourceBundleClass;
			_fileAPIProxy = fileAPIProxy;
			
			setup();
			
			/* Initiate startup phase. */
			commandManager.execute(new StartupApplicationCommand(), onStartupComplete);
		}
		
		
		/**
		 * Returns a String Representation of the class.
		 * 
		 * @return A String Representation of the class.
		 */
		public function toString():String
		{
			return "Main";
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Accessors
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Returns the singleton instance of the class.
		 */
		public static function get instance():Main
		{
			if (_instance == null)
			{
				_singletonLock = true;
				_instance = new Main();
				_singletonLock = false;
			}
			return _instance;
		}
		
		
		/**
		 * A reference to the context view.
		 */
		public function get contextView():DisplayObjectContainer
		{
			return _contextView;
		}
		
		
		/**
		 * A reference to the stage.
		 */
		public function get stage():Stage
		{
			return _contextView.stage;
		}
		
		
		/**
		 * A reference to the base nativeWindow of the application if it is supported by the
		 * build type. Otherwise it returns the base display object container instead.
		 */
		public function get baseWindow():*
		{
			if (appInfo.buildType == BuildType.DESKTOP && stage['nativeWindow'])
			{
				return stage['nativeWindow'];
			}
			return _contextView;
		}
		
		
		/**
		 * Determines whether the application is in fullscreen mode (<code>true</code>) or not
		 * (<code>false</code>).
		 */
		public function get isFullscreen():Boolean
		{
			return (stage.displayState == StageDisplayState['FULL_SCREEN_INTERACTIVE']
				|| stage.displayState == StageDisplayState.FULL_SCREEN);
		}
		
		
		/**
		 * A reference to the console.
		 */
		public function get console():Console
		{
			return _screenManager.console;
		}


		/**
		 * A reference to the stats monitor.
		 */
		public function get statsMonitor():StatsMonitor
		{
			return _screenManager.statsMonitor;
		}
		
		
		/**
		 * A reference to the class registry.
		 */
		public function get classRegistry():ClassRegistry
		{
			return _classRegistry;
		}


		/**
		 * A reference to the module manager.
		 */
		public function get moduleManager():ModuleManager
		{
			return _moduleManager;
		}
		
		
		/**
		 * A reference to the command manager.
		 */
		public function get commandManager():CommandManager
		{
			return _commandManager;
		}


		/**
		 * A reference to the resource manager.
		 */
		public function get resourceManager():ResourceManager
		{
			return _resourceManager;
		}


		/**
		 * A reference to the screen manager.
		 */
		public function get screenManager():ScreenManager
		{
			return _screenManager;
		}


		/**
		 * A reference to the state manager.
		 */
		public function get stateManager():StateManager
		{
			return _stateManager;
		}


		/**
		 * A reference to the theme manager.
		 */
		public function get themeManager():UIThemeManager
		{
			return _themeManager;
		}
		
		
		/**
		 * A reference to the localsettings manager.
		 */
		public function get localSettingsManager():LocalSettingsManager
		{
			return _localSettingsManager;
		}


		/**
		 * A reference to the renderbuffer manager.
		 */
		//public function get renderBufferManager():RenderBufferManager
		//{
		//	if (!_renderBufferManager) _renderBufferManager = new RenderBufferManager();
		//	return _renderBufferManager;
		//}


		/**
		 * A reference to the stage3d manager.
		 */
		public function get stage3DManager():Stage3DManager
		{
			if (!_stage3DManager) _stage3DManager = new Stage3DManager(stage);
			return _stage3DManager;
		}
		
		
		/**
		 * A reference to the key input manager.
		 */
		public function get keyInputManager():KeyInputManager
		{
			return _keyInputManager;
		}
		
		
		/**
		 * A reference to the game loop.
		 */
		public function get gameLoop():GameLoop
		{
			return _gameLoop;
		}
		
		
		/**
		 * A reference to the entity manager.
		 */
		public function get entityManager():EntityManager
		{
			return _entityManager;
		}


		/**
		 * A reference to the entity system manager.
		 */
		public function get entitySystemManager():EntitySystemManager
		{
			return _entitySystemManager;
		}


		/**
		 * A reference to the entity factory.
		 */
		public function get entityFactory():EntityFactory
		{
			return _entityFactory;
		}
		
		
		/**
		 * A reference to the audio manager.
		 */
		public function get audioManager():AudioManager
		{
			if (!_audioManager)
			{
				_audioManager = new AudioManager(this);
				_audioManager.init();
			}
			return _audioManager;
		}
		
		
		public function get fileAPIProxy():IFileAPIProxy
		{
			return _fileAPIProxy;
		}
		
		
		/**
		 * A reference to the app info object.
		 */
		public function get appInfo():IAppInfo
		{
			return _appInfo;
		}


		/**
		 * A reference to the data registry.
		 */
		public function get registry():Registry
		{
			return _registry;
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Private Accessors
		//-----------------------------------------------------------------------------------------
		
		/**
		 * An array of all used application setups. Only used internally. Do not touch!
		 * @private
		 */
		public function get setups():Array
		{
			return _setups.concat();
		}
		
		
		/**
		 * The resource bundle class used by the application. Only used internally.
		 * Do not touch!
		 * @private
		 */
		public function get resourceBundleClass():Class
		{
			return _resourceBundleClass;
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Callback Handlers
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Invoked after the application init phase has finished.
		 * @private
		 * 
		 * @param command The application init command that executed the init phase.
		 */
		private function onStartupComplete(command:Command):void
		{
			/* Start all registered and autoStart-set modules. */
			moduleManager.allModulesCompleteSignal.addOnce(onAllModulesComplete);
			moduleManager.startModules(true);
		}
		
		
		/**
		 * Invoked after all modules (async or not) are started and complete.
		 * @private
		 */
		private function onAllModulesComplete():void
		{
			/* Check if screen manager should be enabled! It can be disabled for debugging. */
			var screenManagerEnabled:Boolean = true;
			if (_registry.settings.hasProperty(Settings.SCREEN_MANAGER_ENABLED))
			{
				screenManagerEnabled = _registry.settings.getBoolean(Settings.SCREEN_MANAGER_ENABLED);
			}
			
			if (screenManagerEnabled)
			{
				CallLater.add(function():void
				{
					if (_contextView is IPreloader) (_contextView as IPreloader).dispose();
					/* Time to init the screen manager. */
					screenManager.screenManagerReadySignal.addOnce(onScreenManagerReady);
					screenManager.init();
				});
			}
			else
			{
				Log.notice("ScreenManager is disabled!", this);
			}
		}
		
		
		/**
		 * @private
		 */
		private function onScreenManagerReady(context3D:Context3D):void
		{
			screenManager.screenManagerReadySignal.remove(onScreenManagerReady);
			CallLater.add(screenManager.start);
		}
		
		
		/**
		 * Global Error Handler. Only used in release builds!
		 * @private
		 */
		private function onUncaughtError(e:UncaughtErrorEvent):void 
		{
			e.preventDefault();
			var msg:String;
			if (e.error is Error)
			{
				var e1:Error = Error(e.error);
				msg = "Name: " + e1.name + ", ErrorID: " + e1.errorID
					+ ", Message: \"" + e1.message + "\""
					+ (e1.getStackTrace() ? "\n" + e1.getStackTrace() : "") + ".";
				Log.error("Uncaught error occured - " + msg);
			}
			else if (e.error is ErrorEvent)
			{
				var e2:ErrorEvent = ErrorEvent(e.error);
				msg = "ErrorID: " + e2.errorID + ", Text: \"" + e2.text + "\".";
				Log.error("Uncaught error event occured - " + msg);
			}
			else
			{
				Log.error("Uncaught error occured - something went abysmally wrong!\n" + e.error);
			}
		}
		
		
		//-----------------------------------------------------------------------------------------
		// Private Methods
		//-----------------------------------------------------------------------------------------
		
		/**
		 * Executes tasks that need to be done before the application startup phase is being
		 * executed. This typically includes creating objects that exist throught the whole
		 * application life time.
		 * 
		 * @private
		 */
		private function setup():void
		{
			/* Init log as early as possible. */
			Log.init();
			
			/* Set up global error listener if this is a release version. */
			if (!appInfo.isDebug)
			{
				contextView.loaderInfo.uncaughtErrorEvents.addEventListener(
					UncaughtErrorEvent.UNCAUGHT_ERROR, onUncaughtError);
			}
			
			/* Call JavaScript function to give keyboard focus to web-based Flash content. */
			if (appInfo.buildType == BuildType.WEB && ExternalInterface.available)
			{
				ExternalInterface.call("onFlashContentLoaded");
			}
			
			/* Ignore whitespace on all XML data files. */
			XML.ignoreWhitespace = true;
			XML.ignoreProcessingInstructions = true;
			XML.ignoreComments = true;
			
			/* Set contextview stage on StageReference. */
			StageReference.stage = _contextView.stage;
			
			/* Create default objects and managers. */
			_registry = new Registry();
			_classRegistry = new ClassRegistry();
			_commandManager = new CommandManager();
			_resourceManager = new ResourceManager();
			_moduleManager = new ModuleManager();
			_screenManager = new ScreenManager();
			_stateManager = new StateManager();
			_themeManager = UIThemeManager.instance;
			_localSettingsManager = new LocalSettingsManager();
			_keyInputManager = new KeyInputManager();
			
			_gameLoop = new GameLoop();
			_entityManager = new EntityManager();
			_entitySystemManager = new EntitySystemManager();
			_entityFactory = new EntityFactory();
			
			/* Register default systems. */
			_classRegistry.registerSystem(GameLoop.SYSTEM_ID, _gameLoop);
		}
	}
}