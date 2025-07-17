/**
 * Created by newkrok on 22/10/16.
 */
package net.fpp.pandastory.config.character
{
	import net.fpp.pandastory.vo.CharacterVO;

	public class PandaCharacterVO extends CharacterVO
	{
		public function PandaCharacterVO()
		{
			this.name = 'Panda';

			this.headSkin = '_source/panda_character/head_1';
			this.bodySkin = '_source/panda_character/body_1';
			this.armSkin = '_source/panda_character/arm_1';
			this.legSkin = '_source/panda_character/leg_1';

			this.maxSpeed = 7;
			this.maxSpeedOnAir = 7;

			this.acceleration = .8;
			this.accelerationOnAir = .2;

			this.deceleration = .6;
			this.decelerationOnAir = .6;

			this.jumpPower = 8;
			this.maximumJumpPush = 5;
		}
	}
}