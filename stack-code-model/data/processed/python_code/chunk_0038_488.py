package services.business.miscellaneous.loyaltyPrograms
{
	import services.cairngorm.BaseDelegate;
	import services.events.miscellaneous.loyaltyPrograms.AddLoyaltyProgramEvent;
	import services.events.miscellaneous.loyaltyPrograms.DeleteLoyaltyProgramEvent;
	import services.events.miscellaneous.loyaltyPrograms.GetLoyaltyProgramsEvent;
	import framework.module.CommonModule;
	import services.Services;
	import services.vo.GlobalStorage;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;


	/**
	* The LoyaltyProgramsDelegate class is
	*
	* @author Viktor Potapov / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-10-05 11:28:29 +0300 (Mon, 05 Oct 2009) $
	*
	*/
	public class LoyaltyProgramsDelegate extends BaseDelegate
	{
		public static const SAVE_LOYALTY_PROGRAMS:String = "SaveLoyaltyPrograms";
		public static const DELETE_LOYALTY_PROGRAM:String = "DeleteLoyaltyPrograms";
		public static const GET_LOYALTY_PROGRAMS_LIST:String = "GetLoyaltyProgramsList";

		
		/**
		 *  CountryDelegate. Constructor.
		 *  
		 *  @param responder:IResponder - contact provider for any service.
		 */
		public function LoyaltyProgramsDelegate(responder:IResponder)
		{
			super(responder);
		}
		/**
		 *  Remote call to add loyalty program.
		 *  
		 *  @param event:AddLoyaltyProgramEvent
		 */
		public function addLoyaltyProgram(event:AddLoyaltyProgramEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOYALTY_PROGRAMS).getOperation(SAVE_LOYALTY_PROGRAMS).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOYALTY_PROGRAMS).getOperation(SAVE_LOYALTY_PROGRAMS).send(CommonModule.userOptions, event.program);
		}
	
		/**
		 *  Remote call to delete loyalty program.
		 *  
		 *  @param event:DeleteLoyaltyProgramEvent
		 */
		public function deleteLoyaltyProgram(event:DeleteLoyaltyProgramEvent):void
		{
			service.getRemoteObject(Services.SERVICE_LOYALTY_PROGRAMS).getOperation(DELETE_LOYALTY_PROGRAM).addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_LOYALTY_PROGRAMS).getOperation(DELETE_LOYALTY_PROGRAM).send(CommonModule.userOptions, event.program);
		}
		
		
		/**
		 *  Remote call to get loyalty program.
		 *  
		 *  @param event:GetLoyaltyProgramEvent
		 */
		public function getLoyaltyProgram(event:GetLoyaltyProgramsEvent):void
		{
			operation = service.getRemoteObject(Services.SERVICE_LOYALTY_PROGRAMS).getOperation(GET_LOYALTY_PROGRAMS_LIST);
			operation.addEventListener(ResultEvent.RESULT, handleResult);
			operation.send(CommonModule.userOptions);
		}
		
	}
}