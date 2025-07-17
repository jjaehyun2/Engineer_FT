/**
 * Created by vizoli on 4/9/16.
 */
package ageofai.villager.vo
{
    import ageofai.unit.vo.UnitVO;
    import ageofai.villager.constant.CVillagerStatus;

    public class VillagerVO extends UnitVO
    {

        public function VillagerVO()
        {
            this.status = CVillagerStatus.IDLE;
        }

    }
}