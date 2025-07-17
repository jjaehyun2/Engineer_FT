package
{
	import com.game.building.prod.Producter1;
	import com.game.building.prod.Producter2;
	import com.game.building.prod.Producter3;
	import com.game.building.prod.ProducterMore;
	import com.game.building.prod.ProducterResource;
	import com.game.building.prod.ProducterRush;

	public class Factory
	{
		public static const P1:String="Plane1";
		public static const P2:String="Plane2";
		public static const P3:String="Plane3";
		public static const P4:String="PlaneMore";
		public static const P5:String="PlaneRush";
		public static const P6:String="PlaneResource";
		
		public static const VEC:Vector.<String> = Vector.<String>([P1,P2,P3,P4,P5,P6]);
		public static const NEED:Vector.<int> = Vector.<int>([0,1,2,3,4,5]);
		public function Factory()
		{
		}
		
		public static function SwitchUrl(type:String):String{
			switch(type){
				case P1:
					return "produce_red";
				case P2:
					return "produce_blue";
				case P3:
					return "produce_green";
				case P4:
					return "produce_red";
				case P5:
					return "produce_blue";
				case P6:
					return "produce_blue";
				default:
					return "produce_green";
			}
		}
		
		public static function SwitchColor(type:String):uint{
			switch(type){
				case P1:
					return 0xff0000;
				case P2:
					return 0x00ff00;
				case P3:
					return 0xffff00;
				case P4:
					return 0x0000ff;
				case P5:
					return 0x00ffff;
				case P6:
					return 0x2222ff;
				default:
					return 0xff0000;
			}
		}
		
		public static function GetCreateCost(type:String):int{
			var cost:int = BatteryDataFactory.GetPrice(type,0);
			return Research.getInstance().valueChange(Research.RESEARCH_5,cost);
		}
		
		public static function CreateBattery(tx:Number,ty:Number,type:String):Producter1{
			var unitProducter:Producter1;
			switch(type){
				case P1:
					unitProducter = new Producter1;
					break;
				case P2:
					unitProducter = new Producter2;
					break;
				case P3:
					unitProducter = new Producter3;
					break;
				case P4:
					unitProducter = new ProducterRush;
					break;
				case P5:
					unitProducter = new ProducterMore;
					break;
				case P6:
					unitProducter = new ProducterResource;
					break;
			}
			unitProducter.x = tx;
			unitProducter.y = ty;
			UnitManager.getInstance().sceneSprite.addChild(unitProducter);
			UnitManager.getInstance().track.add(unitProducter);
			return unitProducter;
		}
	}
}