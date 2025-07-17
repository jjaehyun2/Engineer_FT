package com.likya.pinara.model {
	
	// import flash.events.;
	// import flash.events.EventDispatcher;
	import org.apache.royale.events.Event;
	import org.apache.royale.events.EventDispatcher;
	
	
	public class User extends EventDispatcher
	{
		
		private static const ROLES_CHANGED:String = "rolesChanged";
		
		[Bindable]
		public var username:String;
		
		private var _password:String;
		public function get password():String
		{
			return _password;
		}
		public function set password(password:String):void
		{
			_password = password;
		}
		
		private var _roleinfo:String;
		public function get roleinfo():String
		{
			return _roleinfo;
		}
		public function set roleinfo(_roleinfo:String):void
		{
			_roleinfo = _roleinfo;
		}

		
		private var _statuinfo:String;
		public function get statuinfo():String
		{
			return _statuinfo;
		}
		public function set statuinfo(statuinfo:String):void
		{
			_statuinfo = statuinfo;
		}
		
		private var _roles:Array;
		
		public function get roles():Array
		{
			return _roles;
		}
		public function set roles(a:Array):void
		{
			_roles = a;
			dispatchEvent(new Event(ROLES_CHANGED));
		}
		
		public function User(username:String = "", password:String = "")
		{
			this.username = username;
			this.password = password;
		}
		
		[Bindable(event=ROLES_CHANGED)]
		public function hasRole(userRole:UserRole):Boolean
		{
			if(roles != null)
			{
				for each(var role:UserRole in roles)
				{
					/*if(role.equals(userRole))
					{
						return true;
					}*/
				}
				return false;
			}
			return false;
		}
		
	}
}