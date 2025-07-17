package valueObjects
{
	[Bindable]
	public class Product
	{
		public var catID:Number;
		public var prodName:String;
		public var unitID:Number;
		public var cost:Number;
		public var listPrice:Number;
		public var description:String;
		public var isOrganic:Boolean;
		public var isLowFat:Boolean;
		public var imageName:String;
		
		public function Product( catID:Number, prodName:String, unitID:Number,
								 cost:Number, listPrice:Number, description:String,
								 isOrganic:Boolean, isLowFat:Boolean, imageName:String )
		{
			this.catID = catID;
			this.prodName = prodName;
			this.unitID = unitID;
			this.cost = cost;
			this.listPrice = listPrice;
			this.description = description;
			this.isOrganic = isOrganic;
			this.isLowFat = isLowFat;
			this.imageName = imageName;
		}
		
		public function toString():String {
			return "[Product]" + this.prodName;
		}
		
		public static function buildProduct( o:Object ):Product {
			var p:Product;
			p = new Product( o.catID, o.prodName, o.unitID,
				o.cost, o.listPrice, o.description, ( o.isOrganic == 'true' ),
				( o.isLowFat == 'true' ), o.imageName );
			return p;
		}
		
		public static function buildProductFromAttributes( data:XML ):Product {
			var p:Product;
			var isOrganic:Boolean = ( data.@isOrganic == "Yes" );
			var isLowFat:Boolean = ( data.@isLowFat == "Yes" );
			
			p = new Product( data.@catID,
				data.@prodName,
				data.@unitID,
				data.@cost, 
				data.@listPrice, 
				data.@description, 
				isOrganic, 
				isLowFat, 
				data.@imageName );
			
			return p;
		}
	}
}