package services.command.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.individual.SaveProfilesEvent;
	import services.vo.profiles.ProfilePersonViewVO;
	
	import mx.collections.ArrayCollection;

	public class SaveProfilesCommand extends BaseCommand
	{
		override public function execute(event:CairngormEvent):void
		{
			_event = SaveProfilesEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.saveProfiles(_event as SaveProfilesEvent);
			
			super.execute(event);
		}
		
		override public function result(data:Object):void
		{
			var item:ProfilePersonViewVO = data as ProfilePersonViewVO;
			if ((_event as SaveProfilesEvent).index != -1) // if == -1 -> Check In
			{
				var provider:ArrayCollection = model.profilesModule.individualPageList;
				if ((_event as SaveProfilesEvent).index != provider.length)
				{
					// edit mode
					provider.removeItemAt((_event as SaveProfilesEvent).index);
					provider.addItemAt(item, (_event as SaveProfilesEvent).index);
				}
				else
				{
					// add mode
					provider.addItemAt(item, (_event as SaveProfilesEvent).index);
				}
			}
			
			super.result(data);
		}
	}
}