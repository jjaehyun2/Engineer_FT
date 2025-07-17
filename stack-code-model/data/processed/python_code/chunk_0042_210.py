package org.avManager.model
{
	import mx.collections.ArrayCollection;
	
	import org.avManager.model.data.ClassificationData;

	public final class ClassificationManager
	{
		
		private static var _instance:ClassificationManager;
		
		[Bindable]
		private var _classificationDataList:ArrayCollection = new ArrayCollection();
		
		private var _initCallback:Function;
		
		private var _saveIndex:int = 0;
		
		private var _saveCallback:Function;
		
		public function ClassificationManager(t:T)
		{
		}
		
		public function init(callback:Function):void{
			_initCallback = callback;
			SQLiteManager.instance.classificationTable.query(onQuery);
		}
		
		public function save(callback:Function = null):void{
			_saveCallback = callback;
			this.saveClassificationData();
		}
		
		private function saveClassificationData():void{
			if(_saveIndex >= this._classificationDataList.length){
				if(_saveCallback != null) _saveCallback();
			}else{
				var classificationData:ClassificationData = this._classificationDataList.getItemAt(_saveIndex++) as ClassificationData;
				if(classificationData.needDelete){
					SQLiteManager.instance.classificationTable.del(classificationData.id, saveClassificationData);
				}else if(classificationData.needInsert){
					classificationData.needInsert = false;
					SQLiteManager.instance.classificationTable.insert(classificationData, saveClassificationData);
				}else if(classificationData.needUpdate){
					classificationData.needUpdate = false;
					SQLiteManager.instance.classificationTable.update(classificationData, saveClassificationData);
				}else{
					this.saveClassificationData();
				}
			}
		}
		
		public function getClassificationByIndex(index:int):ClassificationData{
			return this._classificationDataList.getItemAt(index) as ClassificationData;
		}
		
		public function getClassificationByID(id:int):ClassificationData{
			for each(var classificationData:ClassificationData in this._classificationDataList){
				if(classificationData.id == id) return classificationData;
			}
			return null;
		}
		
		public function getClassificationByName(name:String):ClassificationData{
			for each(var classificationData:ClassificationData in this._classificationDataList){
				if(classificationData.name == name) return classificationData;
			}
			return null;
		}
		
		public function createClassification(name:String):ClassificationData{
			var classificationData:ClassificationData = getClassificationByName(name);
			if(!classificationData){
				classificationData = new ClassificationData(_classificationDataList.length + 1);
				classificationData.needInsert = true;
				classificationData.name = name;
				_classificationDataList.addItem(classificationData);
			}
			return classificationData;
		}
		
		private function onQuery(result:Array):void{
			if(result){
				const l:int = result.length;
				var classificationData:ClassificationData;
				for(var i:int = 0;i < l;i++){
					classificationData = new ClassificationData(result[i].ID);
					classificationData.needInsert = false;
					classificationData.name = result[i].NAME;
					this._classificationDataList.addItem(classificationData);
					classificationData.needUpdate = false;
				}				
			}
			_initCallback();
		}
		
		public function get classificationDataList():ArrayCollection
		{
			return _classificationDataList;
		}
		
		public static function get instance():ClassificationManager{
			if(!_instance) _instance = new ClassificationManager(new T());
			return _instance;
		}

	}
}

final class T{}