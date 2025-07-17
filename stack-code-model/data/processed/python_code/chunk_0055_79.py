package com.ryzko.im.protocols.gadu.packets.outbound
{
	public class OutboundPacketType
	{
		
		//Zmiana stanu przed GG 8.0
		public static var GG_NEW_STATUS:int					= 0x0002;
		//Pong
		public static var GG_PONG:int 						= 0x0007;
		//Ping
		public static var GG_PING:int 						= 0x0008;
		//Wysłanie wiadomości przed GG 8.0
		public static var GG_SEND_MSG:int 					= 0x000b;
		//Logowanie przed GG 6.0
		public static var GG_LOGIN:int 						= 0x000c;
		//Dodanie do listy kontaktów
		public static var GG_ADD_NOTIFY:int					= 0x000d;
		//Usunięcie z listy kontaktów
		public static var GG_REMOVE_NOTIFY:int 				= 0x000e;
		//Początkowy fragment listy kontaktów 
		//większej niż 400 wpisów
		public static var GG_NOTIFY_FIRST:int				= 0x000f;
		//Ostatni fragment listy kontaktów
		public static var GG_NOTIFY_LAST:int 				= 0x0010;
		//Lista kontaktów jest pusta
		public static var GG_LIST_EMPTY:int 				= 0x0012;
		//Logowanie przed GG 6.0
		public static var GG_LOGIN_EXT:int 					= 0x0013;
		//Zapytanie katalogu publicznego
		public static var GG_PUBDIR50_REQUEST:int 			= 0x0014;
		//Logowanie przed GG 7.7
		public static var GG_LOGIN60:int 					= 0x0015;
		//Zapytanie listy kontaktów na serwerze 
		//przed Nowym Gadu-Gadu
		public static var GG_USERLIST_REQUEST:int 			= 0x0016;
		//Logowanie przed GG 8.0
		public static var GG_LOGIN70:int 					= 0x0019;
		//???
		public static var GG_DCC7_INFO:int 					= 0x001f;
		//Informacje o chęci nawiązania połączenia DCC
		public static var GG_DCC7_NEW:int 					= 0x0020;
		//Zaakceptowanie połączenia DCC
		public static var GG_DCC7_ACCEPT:int 				= 0x0021;
		//Odrzucenie połączenia DCC
		public static var GG_DCC7_REJECT:int 				= 0x0022;
		//???
		public static var GG_DCC7_ID_REQUEST:int 			= 0x0023;
		//???
		public static var GG_DCC7_DUNNO1:int 				= 0x0024;
		//Informacje o chęci nawiązania połączenia DCC
		public static var GG_DCC7_ABORT:int 				= 0x0025;
		//Zmiana stanu przed Nowym Gadu-Gadu
		public static var GG_NEW_STATUS80BETA:int 			= 0x0028;
		//Logowanie przed Nowym Gadu-Gadu
		public static var GG_LOGIN80BETA:int 				= 0x0029;
		//Wysłanie wiadomości
		public static var GG_SEND_MSG80:int 				= 0x002d;
		//Zapytanie listy kontaktów na serwerze 
		//przed Gadu-Gadu 10
		public static var GG_USERLIST_REQUEST80:int 		= 0x002f;
		//Logowanie
		public static var GG_LOGIN80:int 					= 0x0031;
		//Zmiana stanu
		public static var GG_NEW_STATUS80:int				= 0x0038;
		//Zapytanie listy kontaktów na serwerze
		public static var GG_USERLIST_REQUEST100:int 		= 0x0040;


		
		
		
		
		
		
		
		public function OutboundPacketType()
		{
		}

	}
}