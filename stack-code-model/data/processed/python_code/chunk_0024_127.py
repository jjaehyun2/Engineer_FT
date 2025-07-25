package assets.components
{
	import com.hp.asi.hpic4vc.ui.Hpic4vc_storage_providerProxy;
	import com.hp.asi.hpic4vc.ui.model.DataGridWrapper;
	import com.hp.asi.hpic4vc.ui.model.PageModel;
	import com.hp.asi.hpic4vc.ui.model.TabModel;
	import com.hp.asi.hpic4vc.ui.model.TableModel;
	import com.hp.asi.hpic4vc.ui.utils.Helper;
	import com.vmware.core.model.IResourceReference;
	import com.vmware.flexutil.events.MethodReturnEvent;
	
	import flash.events.EventDispatcher;
	import flash.utils.setTimeout;
	
	import mx.collections.ArrayCollection;
	import mx.controls.Alert;
	import mx.logging.ILogger;
	import mx.logging.Log;

	public class Hpic4vc_StorageMediator extends Hpic4vc_BaseMediator {
		private var _view:Hpic4vc_Storage;
		private var _proxyStorage:Hpic4vc_storage_providerProxy;
		private var count:int = 0;
		
		private static var _logger:ILogger = Log.getLogger("Hpic4vc_StorageMediator");
		
		[View]
		/**
		 * The mediator's view.
		 */
		public function get view():Hpic4vc_Storage {
			return _view;
		}
		
		/** @private */
		public function set view(value:Hpic4vc_Storage):void {
			_view = value;
			_proxyStorage = new Hpic4vc_storage_providerProxy();
		}
		
		
		/**public function set contextObject(value:Object):void {
			_contextObject = _view._contextObject;
			if (_contextObject != null && IResourceReference(value) != null) {  
				if (_contextObject.uid != IResourceReference(value).uid) {
					clearData();
					return;
				}
			}
			requestData();
		}**/
		
		override protected function clearData():void {
			_view = null;
		}
		
		override protected function refreshPageContent():void{
			//intentionally left blank so tabs are not refreshed when user clicks
			//refresh button.  The children tabs will handle the refresh on their own.
		}
		
		override protected function requestData():void {
			if (_contextObject != null) {
				_logger.debug("Requesting HPIC4VC Storage Page data.");
				_proxyStorage.getStoragePages(_contextObject.uid, onGettingResult, _contextObject);
			} else {
				_logger.warn("ContextObject is null, hence not requesting data.");
				return;
			}
		}
		
		private function onGettingResult(event:MethodReturnEvent):void {
			if (_view != null) {
				_logger.debug("Received HPIC4VC Storage Page data in onGettingResult()");
				_view.noTabsFound = "";
				_view.errorFoundLabel = "";
				
				if (event == null) {
					_view.errorFoundLabel = Helper.getString("errorOccurred");
					return;
				} else if (event.error != null) {
					_logger.warn("DeliveryInDoubt exception occurred.  Count: " + count.toString());
					if (event.error.toString().match("DeliveryInDoubt")) {
						// Re try to request data for not more than 2 times
						if (count < 2) {
							count ++;
							requestData();
							return;
						} else {
							_view.errorFoundLabel = event.error.message;
							return;
						}
					} else {
						_view.errorFoundLabel = event.error.message;
						return;
					}
				} else if (event.result == null) {
					_view.errorFoundLabel = Helper.getString("errorOccurred");
					return;
				} else if ((event.result as PageModel).errorMessage != null) {
					_view.errorFoundLabel = (event.result as PageModel).errorMessage;
					return;
				} else if ((event.result as PageModel).informationMessage != null) {
					_view.noTabsFound = (event.result as PageModel).informationMessage;
					return;
				}
				
				var storagePage:PageModel = event.result as PageModel;
				
				if (storagePage.tabs.length >= 1) {
					var subTabs:ArrayCollection = (storagePage.tabs.getItemAt(0) as TabModel).subTabs;
					
					// Sort the tabs as per the order specified.
					Helper.sortArrayCollection(subTabs, "order", true);
					
					_view.storageTabs = subTabs;
					
	                // Get the tabModel.
					for (var i:int = 0; i < subTabs.length; i++) 
					{
						var item:TabModel = subTabs.getItemAt(i) as TabModel;
						if (item.displayNameKey == "Summary") {
							_view.summaryTabModel = item;
						} else if (item.displayNameKey == "Storage_Volumes") {
							_view.storageVolumesTabModel = item;
						} else if (item.displayNameKey == "Virtual_Disks") {
							_view.virtualDisksTabModel = item;
						} else if (item.displayNameKey == "HBAs") {
							_view.hbasTabModel = item;
						} else if (item.displayNameKey == "Paths") {
							_view.pathsTabModel = item;
						} else if (item.displayNameKey == "Replications") {
							_view.replicationsTabModel = item;
						} else if (item.displayNameKey == "VMs_to_Volumes") {
							_view.vmsToVolumesTabModel = item;
						} 
					}
				}
			}
			else {
				_logger.warn("View is null.  Returning from onGettingResult() for the Storage Pages.");
				return;
			}
		}
	}
}