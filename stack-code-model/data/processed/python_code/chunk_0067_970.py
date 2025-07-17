package com.arxterra.utils
{
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.events.TimerEvent;
	import flash.net.URLLoader;
	import flash.net.URLRequest;
	import flash.utils.Timer;
	
	import com.arxterra.events.UtilityEvent;
	
	[Event(name="declination", type="com.arxterra.events.UtilityEvent")]

	public class DeclinationUtil extends NonUIComponentBase
	{
		// static constants and properties
		
		private static const __DEFAULT_INTERVAL:int = 60;
		private static const __URL_BASE:String = 'http://www.ngdc.noaa.gov/geomag-web/calculators/calculateDeclination';
		private static const __URL_SFX:String = '&resultFormat=xml';
		
		private static var __instance:DeclinationUtil;
		
		// constructor and instance
		
		/**
		 * singleton instance of DeclinationUtil
		 */
		public static function get instance ( ) : DeclinationUtil
		{
			if ( !__instance )
			{
				__instance = new DeclinationUtil ( new SingletonEnforcer() );
			}
			return __instance;
		}
		
		/**
		 * Singleton: use static property <em>instance</em> to access singleton instance,
		 * then call updateFromGPS whenever you get a reading.
		 */	
		public function DeclinationUtil ( enforcer:SingletonEnforcer )
		{
			super();
			_tmrLookup = new Timer ( _iMinutes * 60000, 0 );
			_tmrLookup.addEventListener ( TimerEvent.TIMER, _Lookup );
		}
		
		
		// public properties and get/set methods
		
		public function get active ( ) : Boolean
		{
			return _bActive;
		}
		
		public function get declination ( ) : Number
		{
			return _nDeclination;
		}
		
		/**
		 * Minutes between lookups (default = 60)
		 */
		public function get lookupInterval():int
		{
			return _iMinutes;
		}
		public function set lookupInterval(value:int):void
		{
			_iMinutes = value;
			_tmrLookup.delay = _iMinutes * 3600;
		}
		
		
		// public methods
		
		public function activeSet ( value:Boolean ) : void
		{
			if ( value )
			{
				start ( );
			}
			else
			{
				stop ( );
			}
		}
		
		public function setCoordinates ( lat:Number, lon:Number ) : void
		{
			_nLat = lat;
			_nLon = lon;
			if ( _bGeoInited )
				return;
			
			// now that we have a lat lon to work with, if active
			// send our first request, and start the timer
			_bGeoInited = true;
			_urlLdr = new URLLoader ( );
			_urlLdr.addEventListener ( Event.COMPLETE, _LookupCompleted );
			_urlLdr.addEventListener ( IOErrorEvent.IO_ERROR, _LookupErrorIO );
			_urlLdr.addEventListener ( SecurityErrorEvent.SECURITY_ERROR, _LookupErrorSec );
			if ( _bActive )
			{
				_LookupsStart ( );
			}
		}
		
		public function start ( ) : void
		{
			_bActive = true;
			if ( _bGeoInited )
				_LookupsStart ( );
		}
		
		public function stop ( ) : void
		{
			_bActive = false;
			if ( _bGeoInited )
				_tmrLookup.stop ( );
		}
		
		// private properties
		
		private var _bActive:Boolean = false;
		private var _bGeoInited:Boolean = false;
		private var _iMinutes:int = __DEFAULT_INTERVAL;
		private var _nDeclination:Number = 0;
		private var _nLat:Number;
		private var _nLon:Number;
		private var _nPrevLat:Number;
		private var _nPrevLon:Number;
		private var _nUpdateTime:Number = 0;
		private var _tmrLookup:Timer;
		private var _urlLdr:URLLoader;
		
		
		// private methods
		
		private function _Lookup ( event:TimerEvent = null ) : void
		{
			if ( _nPrevLat == _nLat && _nPrevLon == _nLon )
				return;
			
			_nPrevLat = _nLat;
			_nPrevLon = _nLon;
			var req:URLRequest = new URLRequest ( __URL_BASE + '?lat1=' + _nLat + '&lon1=' + _nLon + __URL_SFX );
			_urlLdr.load ( req );
		}
		
		private function _LookupCompleted ( event:Event ) : void
		{
			var xml:XML;
			var nDec:Number;
			try
			{
				xml = new XML ( _urlLdr.data );
				nDec = Number ( xml.result.declination );
				if ( isNaN ( nDec ) )
				{
					_debugOut ( 'error_declin_parse', true, [ '[isNaN]' ] );
				}
				else
				{
					_nDeclination = nDec;
					_callLater ( _Report );
				}
			}
			catch ( err:Error )
			{
				_debugOut ( 'error_declin_parse', true, [ err.message ] );
			}
		}
		
		private function _LookupErrorIO ( event:IOErrorEvent ) : void
		{
			_debugOut ( 'error_declin_io', true, [ event.errorID, event.text ] );
		}
		
		private function _LookupErrorSec ( event:SecurityErrorEvent ) : void
		{
			_debugOut ( 'error_declin_sec', true, [ event.text ] );
		}
		
		private function _LookupsStart ( ) : void
		{
			_tmrLookup.start ( );
			_Lookup ( );
		}
		
		private function _Report ( ) : void
		{
			if ( eventRelay && eventRelay.hasEventListener ( UtilityEvent.DECLINATION ) )
			{
				eventRelay.dispatchEvent ( new UtilityEvent ( UtilityEvent.DECLINATION, { declination: _nDeclination } ) );
			}
			// if eventRelay is not used, listeners will have to be set directly on the subclass instance
			if ( hasEventListener ( UtilityEvent.DECLINATION ) )
			{
				dispatchEvent ( new UtilityEvent ( UtilityEvent.DECLINATION, { declination: _nDeclination } ) );
			}
		}
	}
}
class SingletonEnforcer {}