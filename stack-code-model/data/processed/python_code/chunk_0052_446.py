package services.business.rates.packages
{
	import services.cairngorm.BaseDelegate;
	import services.events.rates.packages.DeletePackageEvent;
	import services.events.rates.packages.DeleteTransactionEvent;
	import services.events.rates.packages.GetPackageEvent;
	import services.events.rates.packages.GetPackagesCountEvent;
	import services.events.rates.packages.GetPackagesPageEvent;
	import services.events.rates.packages.GetTransactionGroupListEvent;
	import services.events.rates.packages.GetTransactionItemCountEvent;
	import services.events.rates.packages.GetTransactionItemPageEvent;
	import services.events.rates.packages.GetTransactionListEvent;
	import services.events.rates.packages.SavePackageEvent;
	import services.events.rates.packages.SaveTransactionEvent;
	import framework.module.CommonModule;
	import services.Services;
	
	import h2olib.utils.DateUtils;
	
	import mx.rpc.IResponder;
	import mx.rpc.events.ResultEvent;

	/**
	* The PackageDelegate class is
	*
	* @author Anton Kirzyk / Ramada
	*
	* @version $Revision 1.0 $ $Date: 2009-07-18 11:52:03 +0300 (Сб, 18 июл 2009) $
	*
	*/
	public class PackageDelegate extends BaseDelegate
	{
		public function PackageDelegate(responder:IResponder)
		{
			super(responder);
		}


		public function deletePackage(event:DeletePackageEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("deletePackage").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("deletePackage").send(CommonModule.userOptions,event.iPackageId);
		}

		public function deleteTransaction(event:DeleteTransactionEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("deleteTransaction").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("deleteTransaction").send(CommonModule.userOptions,event.iPackageId,event.iTransactionToDeleteId);
		}

		public function getPackage(event:GetPackageEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackage").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackage").send(CommonModule.userOptions,event.iPackageId);
		}

		public function getPackagesCount(event:GetPackagesCountEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesCount").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesCount").send(CommonModule.userOptions,event.packageRequest);
		}

		public function getPackagesPage(event:GetPackagesPageEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesPage").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getPackagesPage").send(CommonModule.userOptions,event.packageRequest,event.iPage,event.iCount);
		}

		public function getGroupList(event:GetTransactionGroupListEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getGroupList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getGroupList").send(CommonModule.userOptions,event.sGroupName, event.iHotelId);
		}

		public function getItemCount(event:GetTransactionItemCountEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getItemCount").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getItemCount").send(CommonModule.userOptions,event.iGroupId,event.sItemName);
		}

		public function getTransactionItemPage(event:GetTransactionItemPageEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getItemPage").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getItemPage").send(CommonModule.userOptions,event.iGroupId,event.sItemName,event.iPage,event.iCount);
		}

		public function getTransactionList(event:GetTransactionListEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getTransactionList").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("getTransactionList").send(CommonModule.userOptions,event.iPackageId);
		}

		public function savePackage(event:SavePackageEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("savePackage").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("savePackage").send(CommonModule.userOptions,event.packageForSave);
		}

		public function saveTransaction(event:SaveTransactionEvent):void
		{
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("saveTransaction").addEventListener(ResultEvent.RESULT, handleResult);
			service.getRemoteObject(Services.SERVICE_PACKAGES).getOperation("saveTransaction").send(CommonModule.userOptions,event.iPackageId,event.oMapTransaction);
		}

	}
}