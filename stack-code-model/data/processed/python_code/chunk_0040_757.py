package utils
{
	import flash.net.SharedObject;
	
	import model.AppModel;
	
	import mx.collections.ArrayCollection;
	
	import vo.ProductTodayVO;

	public class AppUtils
	{
		[Bindable]
		private var appModel:AppModel = AppModel.getInstance();
		public function saveData():void
		{
			appModel.sharedObject.data.productsToday = appModel.productsToday;
			appModel.sharedObject.flush();
		}
		
		public function readData():void
		{
			appModel.productsToday = appModel.sharedObject.data.productsToday;
			if(appModel.productsToday == null)
			{
				appModel.productsToday = new ArrayCollection();
			}
			else
			{
				for (var i:int = 0; i< appModel.productsToday.length; i++)
				{
						
					var item:Object = appModel.productsToday[i];
					if(item.date < appModel.currentDate)
					{
						appModel.productsToday = new ArrayCollection();
						return;
					}
					appModel.productsToday[i] = new ProductTodayVO(item.date, 
											  item.categoryId,
											  item.productId,
											  item.weight);
				}
			}
		}
	}
}