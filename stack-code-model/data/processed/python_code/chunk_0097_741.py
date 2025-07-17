/**
 * Created by newkrok on 22/10/16.
 */
package net.fpp.pandastory.config.character
{
	import net.fpp.pandastory.vo.CharacterVO;

	public class EvilPandaCharacterVO extends CharacterVO
	{
		public function EvilPandaCharacterVO()
		{
			this.name = 'Evil Panda';

			this.headSkin = '_source/panda_character/head_2';
			this.bodySkin = '_source/panda_character/body_2';
			this.armSkin = '_source/panda_character/arm_2';
			this.legSkin = '_source/panda_character/leg_2';

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