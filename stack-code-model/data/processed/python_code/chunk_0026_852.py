package com.tourism_in_lviv.air.controller.context
{
	import com.tourism_in_lviv.air.controller.comand.core.MapCommands;
	import com.tourism_in_lviv.air.controller.comand.core.MapModels;
	import com.tourism_in_lviv.air.controller.comand.core.MapServices;
	import com.tourism_in_lviv.air.controller.comand.core.MapViews;
	
	import flash.display.DisplayObjectContainer;
	
	import org.robotlegs.base.ContextEvent;
	import org.robotlegs.base.GuardedSignalCommandMap;
	import org.robotlegs.core.IGuardedSignalCommandMap;
	import org.robotlegs.mvcs.SignalContext;

	public class TourismInLvivContext extends SignalContext
	{
		public function TourismInLvivContext( contextView:DisplayObjectContainer = null, autoStartup:Boolean = true )
		{
			signalCommandMap = new GuardedSignalCommandMap( injector.createChild( injector.applicationDomain ));
			super( contextView, autoStartup );
		}

		override public function startup():void
		{
			mapMappingCommands();
			
			super.startup();
		}
		
		override protected function mapInjections():void
		{
			super.mapInjections();
			
			injector.mapValue( IGuardedSignalCommandMap, signalCommandMap );
		}

		protected function mapMappingCommands():void
		{
			commandMap.mapEvent( ContextEvent.STARTUP_COMPLETE, MapCommands, ContextEvent, true );
			commandMap.mapEvent( ContextEvent.STARTUP_COMPLETE, MapModels, ContextEvent, true );
			commandMap.mapEvent( ContextEvent.STARTUP_COMPLETE, MapServices, ContextEvent, true );
			commandMap.mapEvent( ContextEvent.STARTUP_COMPLETE, MapViews, ContextEvent, true );
		}
	}
}