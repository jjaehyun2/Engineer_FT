/*
 * Copyright the original author or authors.
 * 
 * Licensed under the MOZILLA PUBLIC LICENSE, Version 1.1 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *      http://www.mozilla.org/MPL/MPL-1.1.html
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
	 
package com.bourre.media 
{
	import com.bourre.events.BasicEvent;		
	
	/**
	 * The GlobalSoundManagerEvent class.
	 * 
	 * <p>TODO Documentation.</p>
	 * 
	 * @author 	Aigret Axel
	 */
	public class GlobalSoundManagerEvent extends BasicEvent
	{

		public static var onGlobalSoundChangeEVENT : String = new String( "onGlobalSoundChange" );
		
		// Can be null if no global sound set
		protected var _oSTDI : SoundTransformInfo; 
		
		public function GlobalSoundManagerEvent( oSTDI : SoundTransformInfo)
		{ 
			super( onGlobalSoundChangeEVENT );
			_oSTDI =  oSTDI ;
		}
	
		public function getSoundTransformInfo() : SoundTransformInfo
		{
			return _oSTDI;
		}
		
		public function hasSoundTransformInfo() : Boolean
		{
			return _oSTDI != null ;
		}
	
	}
}