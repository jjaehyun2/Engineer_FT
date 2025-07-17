package services.events.miscellaneous.vat
{
	import services.cairngorm.BaseEvent;
	import services.vo.backend.VatObjectVO;
	
	import mx.collections.ArrayCollection;

	public class DeleteVATEvent extends BaseEvent
	{
		public var index:int;
		public var targetArray:ArrayCollection = new ArrayCollection();
		public var vat:VatObjectVO = new VatObjectVO();
		
		public function DeleteVATEvent(type:String)
		{
			super(type);
		}
		
	}
}