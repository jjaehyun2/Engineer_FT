/*
* NEC Enterprise Communication Technologies, Inc.
* Copyright 2014
*/ 
package com.necsphere.generated
{
	[Bindable]
	[RemoteClass(alias="com.spherecom.spring.remoteobject.ClientInfo")]
	public class ClientInfo
	{
		public static const CLIENT_TYPE_ANDROID		: String	= "MobileClientAndroid";
		public static const CLIENT_TYPE_BCT			: String	= "BCTClient";
		public static const CLIENT_TYPE_IOS			: String	= "MobileClientIOS";
		public static const CLIENT_TYPE_OTHER		: String	= "Other";
		public static const CLIENT_TYPE_OUTLOOK		: String	= "OutlookConnect";
		public static const CLIENT_TYPE_RIASERVER	: String	= "RIAServer";
		public static const CLIENT_TYPE_UCCLIENT	: String	= "UCClient";
		public static const CLIENT_TYPE_UC700		: String	= "UC700";
		
		public var appVersion	: String;
		public var friendlyName	: String;
		public var ipAddress	: String;
		public var type			: String;
		
	}
}