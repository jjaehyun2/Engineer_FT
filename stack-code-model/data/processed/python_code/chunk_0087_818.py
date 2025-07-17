package com.lowoui_as.feature
{
	import com.lowoui_as.core.UIDialog;
	import com.greensock.TweenLite;
	import fl.motion.easing.*;

	public class DialogNotice extends UIDialog
	{
		public function DialogNotice()
		{
			super(0, 0, 0, 0, 1, 1);
		}

		/**
		 * params : dialogDurationTime
		 * -1 : no end notice
		 * >0 : n seconds later, call for closing this.
		 */
		override public function openAndUpdate()
		{
			super.openAndUpdate();

			if (dialogDurationTime > 0)
			{
				TweenLite.to(this, dialogDurationTime, {ease: Sine.easeOut, onComplete: closeDialog});
			}
		}
	}
}