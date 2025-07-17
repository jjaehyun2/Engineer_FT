package com.yjacket.taskerTasker.model
{
	[Bindable]
	[RemoteClass(alias="IdleTask")]
	public final class IdleTask extends Task
	{
		public function IdleTask()
		{
			super("IDLE");
			_isIdle = true;
		}
	}
}