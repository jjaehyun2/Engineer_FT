package services.business.inHouse
{
	import services.cairngorm.BaseDelegate;
	import services.events.inHouse.AttachConferenceRoomToAccountEvent;
	import services.events.inHouse.DeleteMessageEvent;
	import services.events.inHouse.GetAvailableRoomsListEvent;
	import services.events.inHouse.GetConferenceRoomStatusEvent;
	import services.events.inHouse.GetInHouseStateEvent;
	import services.events.inHouse.GetMessageHistoryEvent;
	import services.events.inHouse.GetPackagesEvent;
	import services.events.inHouse.GetVirtualRoutingEvent;
	import services.events.inHouse.MarkMessageAsReadEvent;
	import services.events.inHouse.MoveRoomEvent;
	import services.events.inHouse.SaveMessageEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	public class InHouseDelegate extends BaseDelegate
	{
		public static const GET_IN_HOUSE_STATE:String = "GetInHouseState";
		public static const GET_MESSAGE_HISTORY:String = "GetMessageHistory";
		public static const GET_PACKAGES:String = "GetPackages";
		public static const SAVE_MESSAGES:String = "SaveMessage";
		public static const DELETE_MESSAGES:String = "DeleteMessage";
		public static const MARK_MESSAGE_AS_READ:String = "MarkMessageAsRead";
		public static const GET_AVAILABLE_ROOM_LIST:String = "GetAvailableRoomsList";
		public static const MOVE_ROOM:String = "MoveRoom";
		public static const GET_VIRTUAL_ROUTING:String = "GetVirtualRouting";
		public static const GET_CONFERENCE_ROOM_STATUS:String = "GetConferenceRoomStatus";
		public static const ATTACH_CONFERENCE_ROOM_TO_ACCOUNT:String = "AttachConferenceRoomToAccount";
		
		/**
		 *  CheckInDelegate. Constructor.
		 *  
		 *  @param responder:IResponder - contact provider for any service.
		 */
		public function InHouseDelegate(responder:IResponder)
		{
			super(responder);
		}
		
		/**
		 *  Remote call to get in house state.
		 *  
		 *  @param event:GetInHouseStateEvent
		 */
		public function getInHouseState(event:GetInHouseStateEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_IN_HOUSE_STATE);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.hotelId, event.searchPattern, event.page, event.count);
		}
		/**
		 *  Remote call to get message's history.
		 *  
		 *  @param event:GetMessageHistoryEvent
		 */
		public function getMessageHistory(event:GetMessageHistoryEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_MESSAGE_HISTORY);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.profileId);
		}
		/**
		 *  Remote call to save message to guest.
		 *  
		 *  @param event:SaveMessageEvent
		 */
		public function saveMessage(event:SaveMessageEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(SAVE_MESSAGES);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.message, event.profileId);
		}
		/**
		 *  Remote call to delete message for guest.
		 *  
		 *  @param event:DeleteMessageEvent
		 */
		public function deleteMessage(event:DeleteMessageEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(DELETE_MESSAGES);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.messageId);
		}
		/**
		 *  Remote call to mark message as read for guest.
		 *  
		 *  @param event:DeleteMessageEvent
		 */
		public function markMessageAsRead(event:MarkMessageAsReadEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(MARK_MESSAGE_AS_READ);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.messageId);
		}
		/**
		 *  Remote call to get available room list.
		 *  
		 *  @param event:GetAvailableRoomsListEvent
		 */
		public function getAvailableRoomsList(event:GetAvailableRoomsListEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_AVAILABLE_ROOM_LIST);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.profileId, event.orderId, event.hotelId, event.stage);
		}
		/**
		 *  Remote call to assign guest to other room.
		 *  
		 *  @param event:MoveRoomEvent
		 */
		public function moveRoom(event:MoveRoomEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(MOVE_ROOM);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.roomIdFrom, event.roomIdTo,
					event.orderDateDep, event.isNeedToUnassign,
					event.isNeedToChangeRate, event.rateChange);
		}
		/**
		 *  Remote call to get routiong for virtual room.
		 *  
		 *  @param event:GetVirtualRoutingEvent
		 */
		public function getVirtualRouting(event:GetVirtualRoutingEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_VIRTUAL_ROUTING);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.roomId, event.date);
		}
		/**
		 *  Remote call to get state for conference room.
		 *  
		 *  @param event:GetConferenceRoomStatusEvent
		 */
		public function getConferenceRoomStatus(event:GetConferenceRoomStatusEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_CONFERENCE_ROOM_STATUS);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.confRoomId, event.hotelId);
		}
		/**
		 *  Remote call to attach conference room to account (person or company).
		 *  
		 *  @param event:AttachConferenceRoomToAccountEvent
		 */
		public function attachConferenceRoomToAccount(event:AttachConferenceRoomToAccountEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(ATTACH_CONFERENCE_ROOM_TO_ACCOUNT);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.confRoomId, event.hotelId, event.profileId, event.isCompany);
		}
		
		public function getPackages(event:GetPackagesEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_IN_HOUSE).getOperation(GET_PACKAGES);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions, event.packageRequest, event.departureDate);
		}
	}
}