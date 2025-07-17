package com.ryzko.im.protocols.gadu.user
{

	/**
	 * 
	 * @author Ry2y
	 * 
	 */	
	public class RemoteUser extends User
	{
		
		public function RemoteUser(uin:String, status:int, description:String)
		{
			this.uid = uin;
			this.status = status;
			this.description = description;
		}

	}
}