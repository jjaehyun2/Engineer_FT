package services.command.frontend
{
	import com.adobe.cairngorm.commands.ICommand;
	import com.adobe.cairngorm.control.CairngormEvent;
	
	import services.business.frontend.GetAddressByZipDelegate;
	import services.events.frontend.GetAddressByZipEvent;
	import framework.model.AppModelLocator;
	import services.vo.frontend.AddressByZipVO;
	import services.vo.frontend.AddressVO;
	
	import mx.collections.ArrayCollection;
	import mx.rpc.IResponder;
	/**
	 *  Command for find addreses by zip code.
	 *  
	 *  @author Artemyev Dmitriy
	 *  @date 05.06.2009
	 */
	public class GetAddressByZipCommand implements ICommand, IResponder
	{
		/**
		 *  This property contains the model with all data.
		 *  
		 *  @see framework.model.RModel
		 */
		private var model:AppModelLocator = AppModelLocator.getInstance();
		/**
		 *  Interface method. 
		 *  <p>Execute for forwarding the event to the method
		 *  <code>findAddressByZip()</code>.
		 *  
		 *  @param event:CairngormEvent
		 *  
		 *  @see services.events.frontend.GetAddressByZipEvent
		 *  @see services.business.frontend.GetAddressByZipDelegate
		 */
		public function execute(event:CairngormEvent):void
		{
			var evt:GetAddressByZipEvent = GetAddressByZipEvent( event );
			var delegate:GetAddressByZipDelegate = new GetAddressByZipDelegate( this );
			
			delegate.findAddressByZip(evt);
		}
		/**
		 *  The handler to get result of the execution by remote call for
		 *  <code>findAddressByZip()</code>.
		 *  <p>This method is called by a service when the return value
		 *  has been received.
		 *   
		 *  @param data:Object - result of the remote call.
		 */
		public function result(data:Object):void
		{
			// TODO: make hierarhical data by result
			var address:ArrayCollection = new ArrayCollection(data as Array);
			
			for(var i:int = 0; i < address.length; i++)
			{
				var item:AddressVO = makeAddressVO(address.getItemAt(i));
				var index:int = checkZipCode(item.sZipCode);
				var add:AddressByZipVO = new AddressByZipVO();
				
				if (index == -1)
				{
					add.zipCode = item.sZipCode;
					add.address = new ArrayCollection([item]);
					
					model.profilesModule.addressByZip.addItem(add);
				}
				else
				{
					add = model.profilesModule.addressByZip.getItemAt(index) as AddressByZipVO;
					
					add.address.addItem(add);
					model.profilesModule.addressByZip.setItemAt(add, index);
				}
			}
			
			model.appEnabled--;
		}
		
		private function checkZipCode(code:String):int
		{
			var provider:ArrayCollection = model.profilesModule.addressByZip;
			
			for(var i:int = 0; i < provider.length; i++)
			{
				var item:AddressByZipVO = provider.getItemAt(i) as AddressByZipVO;
				if (item.zipCode == code) return i;
			}
			
			return -1;
		}
		
		private function makeAddressVO(o:Object):AddressVO
		{
			var res:AddressVO = new AddressVO();
			
			for(var prop:String in o)
			{
				res[prop] = o[prop];
			}
			
			return res;
		}
		
		/**
		 *  The handler of faulting the execution by remote call for
		 *  <code>findAddressByZip()</code>.
		 *  <p>This method is called by a service when an error has been
		 *  received.
		 *  
		 *  @param info:Object - info about fault message
		 */
		public function fault(info:Object):void
		{
			model.appEnabled--;
		}
	}
}