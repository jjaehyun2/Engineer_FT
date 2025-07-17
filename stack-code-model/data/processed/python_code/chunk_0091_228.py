package devoron.data.core.base
{
	
	/**
	 * DataStructursBinding
	 * @author Devoron
	 */
	public class DataStructursBinding implements ISerializeObserver
	{
		protected var dataStructurs:Vector.<DataStructur> = new Vector.<DataStructur>;
		
		public function DataStructursBinding(ds1:DataStructur, ds2:DataStructur, ...dss)
		{
			addDataStructur(ds1);
			addDataStructur(ds2);
			var ds:DataStructur;
			if (dss)
				for each (ds in dss)
					addDataStructur(ds);
		}
		
		public function addDataStructur(ds:DataStructur):void
		{
			ds.addSerializeObserver(this);
			dataStructurs.push(ds);
		}
		
		public function removeDataStructur(ds:DataStructur):void
		{
			ds.addSerializeObserver(this);
			var id:int = dataStructurs.indexOf(ds);
			if (id != -1)
				dataStructurs.removeAt(id);
		}
		
		/* INTERFACE devoron.data.core.ISerializeObserver */
		
		public function setSerializedData(source:DataStructur, data:String):void
		{
			var ds:DataStructur;
			//for each (ds in dss) {
				//ds.
				//addDataStructur(ds);
			//}
		
			// если обновилась одна из структур, то требуется обновить связанные структуры
			//gtrace(dataStructurs);
		
		}
	
	}

}