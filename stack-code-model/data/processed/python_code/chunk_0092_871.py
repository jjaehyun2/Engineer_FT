////////////////////////////////////////////////////////////////////////////////
//
//  CODE11.COM
//  Copyright 2011
//  licenced under GPU
//
//  @author		Romeo Copaciu romeo.copaciu@code11.com
//  @date		24 May 2011
//  @version	1.0
//  @site		code11.com
//
////////////////////////////////////////////////////////////////////////////////

package com.code11.google.login.events
{
	import com.code11.google.login.AuthenticatedUser;
	
	import flash.events.Event;
	
	public class LoginEvent extends Event
	{
		
		public static const SUCCESS:String = "success";
		public static const FAILED:String = "failed";
		
		public var user:AuthenticatedUser;
		public function LoginEvent(type:String, user:AuthenticatedUser)
		{
			super(type, bubbles, cancelable);
			this.user = user;
		}
	}
}