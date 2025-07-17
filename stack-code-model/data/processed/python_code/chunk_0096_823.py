package services.vo.backend
{
	import mx.collections.ArrayCollection;
	
	[RemoteClass(alias="MapCollection")]
	public class CollectionObjectVO
	{
	 	public var aObjects:Array = new Array();
 
        public function CollectionConstructor(aObjects:Array):void
        { 
            this.aObjects = aObjects;
        }
	}
}