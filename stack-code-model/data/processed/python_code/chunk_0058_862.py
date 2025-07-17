/**
 * Created by vizoli on 4/9/16.
 */
package ageofai.cost.vo
{
    public class CostVO
    {

        public var food:int;
        public var wood:int;
        public var gold:int;

        public function CostVO( food:int, wood:int, gold:int )
        {
            this.food = food;
            this.wood = wood;
            this.gold = gold;
        }

    }
}