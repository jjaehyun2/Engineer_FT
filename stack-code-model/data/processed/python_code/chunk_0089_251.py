package framework.controllers.macros
{
	import flash.events.IEventDispatcher;
	
	import eu.alebianco.robotlegs.utils.impl.SequenceMacro;
	
	import framework.controllers.LoadBoardCategoriesCommand;
	import framework.controllers.LoadBoardContainersCommand;
	import framework.controllers.LoadBoardTasksCommand;
	import framework.controllers.SaveSharedObjectCommand;
	import framework.events.BoardEvent;
	import framework.events.SharedObjectEvent;
	import framework.models.BoardModel;
	import framework.models.vo.SharedObjectVO;
	
	public class BoardDataMacro extends SequenceMacro {
		
		[Inject] public var event:BoardEvent;
		[Inject] public var boardModel:BoardModel;
		[Inject] public var eventDispatcher:IEventDispatcher;
		//[Inject] public var injector:IInjector;
		
		public override function prepare():void {
			
			boardModel.selectedBoardId = event.boardId;
			
			//var sOVO:SharedObjectVO = new SharedObjectVO(SharedObjectVO.LAST_SELECTED_BOARD_ID, event.boardId, false);
			//injector.injectInto(sOVO);
			
			//add(SaveSharedObjectCommand).withPayloads(sOVO);
			add(LoadBoardCategoriesCommand).withPayloads(event);
			add(LoadBoardContainersCommand).withPayloads(event);
			add(LoadBoardTasksCommand).withPayloads(event);
			
			this.registerCompleteCallback(onBoardDataComplete);
		}
		
		protected function onBoardDataComplete(success:Boolean):void {
			//trace("BoardDataMacro::onBoardDataLoaded");
			eventDispatcher.dispatchEvent(new BoardEvent(BoardEvent.BOARD_LOADED));
			eventDispatcher.dispatchEvent(new SharedObjectEvent(SharedObjectEvent.SAVE, SharedObjectVO.LAST_SELECTED_BOARD_ID, event.boardId));
		}
	}
}