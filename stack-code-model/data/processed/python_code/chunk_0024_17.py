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

package com.code11.google.login
{

	public class AuthenticatedUser 
	{
		public var token:String;
		public var email:String;
		public var password:String;
		public var authenticated:Boolean;
		public var loggedInTime:Date;
		
		
		public function AuthenticatedUser()
		{
			super();
		}
	}
}