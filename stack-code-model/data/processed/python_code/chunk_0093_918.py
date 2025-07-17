package org.pong.mvcs.view 
{
	import feathers.controls.Screen;
	import org.pong.utils.graphic.GraphicUtils;
	import starling.events.Event;
	
	/**
	 * 
	 * AbstractMediator is base view for all screen components.
	 * 
	 * @author mc
	 */
	public class AbstractScreenView extends Screen implements IView
	{	
		/**
		 * GraphicUtils is AssetsManager util waper that privides easy access to graphic resources.
		 */
		private var _graphicUtils:GraphicUtils;
		
		/**
		 * GraphicUtil getter.
		 */
		public function get graphicUtils():GraphicUtils
		{
			return _graphicUtils;
		}
		
		/**
		 * GraphicUtil setter.
		 */
		public function set graphicUtils(value:GraphicUtils):void 
		{
			_graphicUtils = value;
		}
		
		/**
		 * const
		 */
		public function AbstractScreenView()
		{
			super();
			
			setEventListeners();
		}
		
		/**
		 * Event listener setter.
		 */
		protected function setEventListeners():void
		{
			this.addEventListener(Event.REMOVED_FROM_STAGE, onRemovedFromStage);
			this.addEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
		}
		
		/**
		 * Internal listener
		 * 
		 * @private
		 */
		private function onAddedToStage(event:Event):void
		{
			this.removeEventListener(Event.ADDED_TO_STAGE, onAddedToStage);
			
			added();
		}	
		
		/**
		 * 
		 * Called once component is added to stage
		 */
		public function added():void
		{
			trace( this + ", added()" );
		}

		/**
		 * Internal listenr
		 * 
		 * @private
		 */
		public function onRemovedFromStage(event:Event):void
		{
			this.removeEventListener(Event.REMOVED_FROM_STAGE, onRemovedFromStage);
			
			removed();
		}
		
		/**
		 * Destructor
		 * 
		 * @private
		 */
		public function removed():void
		{
			trace( this + ", removed()" );
			
			this.dispose();
		}
		
		/**
		 * 
		 * Called once every frame as respons to Tick signal.
		 * 
		 * @param	passedTime Time passed since the last tick
		 */
		public function update(passedTime:Number):void
		{
		}
	}

}