package services.command.roomSettings
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.roomSettings.RoomSettingsDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.roomSettings.DeleteRoomSettingEvent;
	import services.vo.backend.RoomSettingObjectVO;

	public class DeleteRoomSettingCommand extends BaseCommand
	{
		
		override public function execute(event:CairngormEvent):void
		{
			_event = DeleteRoomSettingEvent( event );
			var delegate:RoomSettingsDelegate = new RoomSettingsDelegate( this );
			
			delegate.deleteRoomSetting(_event as DeleteRoomSettingEvent);
			super.execute( event );
		}
		
		override public function result(data:Object):void
		{
			var realIndex:int;
			if (data != null)
			{
				for(var i:int=0;i<model.roomSettingsModule.roomSettingsDP.length;i++)
					if((model.roomSettingsModule.roomSettingsDP.getItemAt(i) as RoomSettingObjectVO).iRsettingId == (_event as DeleteRoomSettingEvent).roomSetting.iRsettingId)
					{
						realIndex = i;
						break;
					}
				
	
				model.roomSettingsModule.roomSettingsDP.removeItemAt(realIndex);
				if (realIndex!=(_event as DeleteRoomSettingEvent).index) // becouse if(search.text == "") rsData.dataProvider = model.roomSettingsModule.roomSettingsDP;
				(_event as DeleteRoomSettingEvent).targetArray.removeItemAt((_event as DeleteRoomSettingEvent).index);
			}			
			super.result( data );
		}
		
	}
}