/**
 * Created by newkrok on 09/04/16.
 */
package ageofai.fruit.model
{
	import ageofai.constant.CCollectableValues;
	import ageofai.fruit.event.FruitEvent;
	import ageofai.fruit.vo.FruitVO;

	import common.mvc.model.base.BaseModel;

	public class FruitModel extends BaseModel implements IFruitModel
	{
		private var _fruits:Vector.<FruitVO>;
		private var _remainValue:int = CCollectableValues.FRUIT_AMOUNT_VALUE;

		public function FruitModel()
		{
			this._fruits = new Vector.<FruitVO>();
		}

		public function updateValueAmount( value:Number ):void
		{
			this._remainValue = value;

			if( value <= 0 )
			{
				var event:FruitEvent = new FruitEvent( FruitEvent.FRUIT_RUN_OUT );
			}
			else
			{
				event = new FruitEvent( FruitEvent.FRUIT_AMOUNT_UPDATED );
				event.valueAmount = value;
			}

			this.dispatch( event );
		}

		public function getFruitAmountById( id:int ):int
		{
			var result:int;

			for ( var i:int = 0; i < this._fruits.length; i++ )
			{
				if ( this._fruits[ i ].id == id )
				{
					result = this._fruits[ i ].amount;

					break;
				}
			}

			return result;
		}

		public function addFruit( fruitVO:FruitVO ):void
		{
			this._fruits.push( fruitVO );
		}

		public function getFruits():Vector.<FruitVO>
		{
			return this._fruits;
		}
	}
}