/**
 * Created by vizoli on 4/8/16.
 */
package ageofai.unit.model
{
    import ageofai.unit.base.IUnitView;

    import common.mvc.model.base.BaseModel;

    public class UnitModel extends BaseModel implements IUnitModel
    {
        private var _units:Vector.<IUnitView>;

        public function getUnits():Vector.<IUnitView>
        {
            return this._units;
        }

        public function addUnit( unit:IUnitView ):void
        {
            this._units.push( unit );
        }
    }
}