package services.command.profiles.individual
{
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.profiles.ProfileDelegate;
	import services.cairngorm.BaseCommand;
	import services.events.profiles.individual.GetWishesListEvent;
	import services.vo.GlobalStorage;
	import services.vo.common.wishes.ItemsWishVO;
	import services.vo.common.wishes.SettingsWishVO;
	import services.vo.profiles.ProfileSpecialWishesVO;
	
	import mx.collections.ArrayCollection;

	public class GetWishesListCommand extends BaseCommand
	{
		/**
		 *  @override
		 */
		override public function execute(event:CairngormEvent):void
		{
			_event = GetWishesListEvent(event);
			var delegate:ProfileDelegate = new ProfileDelegate(this);
			delegate.getWishesList(_event as GetWishesListEvent);
			
			super.execute(event);
		}
		/**
		 *  @override
		 */
		override public function result(data:Object):void
		{
			var i:ItemsWishVO;
			var i2:SettingsWishVO;
			
			GlobalStorage.wishes = data as ProfileSpecialWishesVO;
			
			var allWishes:Array = GlobalStorage.wishes.aItems.concat(GlobalStorage.wishes.aSettings);
			model.profilesModule.wishesList = new ArrayCollection(allWishes);
			
			super.result(data);
		}
	}
}