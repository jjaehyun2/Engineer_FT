﻿
/* AS3
	Copyright 2008
*/

package com.neopets.projects.gameEngine.shell
{
	import com.neopets.examples.gameShellExample.GameEngineDemo;
	import com.neopets.examples.gameShellExample.GameEngineDemoBiosSetup;
	import com.neopets.projects.neopetsGameShell.events.GameShell_Events;
	import com.neopets.projects.np9.gameEngine.NP9_GameDocument;
	import com.neopets.projects.np9.system.NP9_BIOS;
	import com.neopets.util.events.CustomEvent;
	
	/**
	 *	This is for the FLA. It Is the Interface document Class and Holds the GameShell_Interface.
	 *	> For this Version of the GameShell it will have an embeded NP9_GamingSystem
	 *  > For this Version of the GameShell it will have an embeded NP9_BIOS
	 * 
	 *	@langversion ActionScript 3.0
	 *	@playerversion Flash 9.0
	 *	@Pattern GameEngine
	 * 
	 *	@author Clive Henrick
	 *	@since  01.07.2009
	 */
	 
	public class GameEngineShell extends NP9_GameDocument
	{
		
		//--------------------------------------
		// CLASS CONSTANTS
		//--------------------------------------
		
		
		public const SEND_THROUGH_CMD:String = "Send_A_Cmd_ToParent";
		public const INTERNAL_TESTING:Boolean = false;
		
		
		//--------------------------------------
		//  PRIVATE VARIABLES
		//--------------------------------------
		
		private var mGameEngineDemo:GameEngineDemo;
		private var mLocalPathway:String;
		private var mGameShell_Events:GameShell_Events;
		private var mConfigXML:XML;
		
		public var mcBIOS:NP9_BIOS;
		
		//--------------------------------------
		//  CONSTRUCTOR
		//--------------------------------------
		
		public function GameEngineShell(pLocalPathwayURL:String = null):void{
			
			setupVars();
			mcBIOS.localPathway =  (pLocalPathwayURL != null) ?  pLocalPathwayURL : mcBIOS.localPathway;                                                                                                                                                          
			
			super();
			
			if (mcBIOS.localTesting)
			{
				init(mcBIOS);
			}
			
		}
		
		
		//--------------------------------------
		//  GETTER/SETTERS
		//--------------------------------------

		
		//--------------------------------------
		//  PUBLIC METHODS
		//--------------------------------------
		
		/**
		 * This for the Shell Application to Pass Info when used in the Game Shell not the FLA
		 */
		 
		public function externalData(pLocalPathwayURL:String = null, pGameShell_Events:GameShell_Events = null, pConfigXML:XML = null):void
		{
			
			mcBIOS.localPathway =  (pLocalPathwayURL != null) ?  pLocalPathwayURL : mcBIOS.localPathway;                                                                                                                                                          
			mGameShell_Events = (pGameShell_Events != null) ? pGameShell_Events : null;
			mConfigXML = (pConfigXML != null) ? pConfigXML : null;
			init(mcBIOS);
			triggerOfflineMode();
			
		}
		
		//--------------------------------------
		//  EVENT HANDLERS
		//--------------------------------------
		
		/**
		 * @Note: Sends Message Through the Shell to anything listening
		 * @param	evt.oData.CMD		String		The Desired Command
		 * @param	evt.oData.PARAM		Object		The Desired Paramaters
		 */
		 	
		public function sendThroughEvent(evt:CustomEvent):void
		{
			if (evt.oData.CMD == mGameEngineDemo.GAME_ENGINE_CLEANED)
			{
				cleanupGameEngineShell(evt);		
			}
			else
			{
				var tPassedObj:Object = evt.oData;
				this.dispatchEvent(new CustomEvent(tPassedObj,SEND_THROUGH_CMD));	
			}
		}
		
		//--------------------------------------
		//  PRIVATE & PROTECTED INSTANCE METHODS
		//--------------------------------------
		
		/**
		 * @Note: that you know its time to continue Code after the NP9 System has been loaded.
		 * @Note: This is called from the Game on Frame 2, when its triggered by the NP9_Loader_Control
		 *		>This is Triggered by the NP9_Loader_Control
		 *		>At function Main - _STARTGAME:
		 * 	@Note: If This will use local Files for loading if offline.
		**/
		 
		protected override function gameEngineUpdate():void
		{
			var tRealPathway:String;
		
			mcBIOS.localTesting = bOffline;
			
			if (bOffline)
			{
				mcBIOS.finalPathway = mcBIOS.localPathway;	
			}
			else
			{
				mcBIOS.finalPathway = _GAMINGSYSTEM.getImageServer() + mcBIOS.localPathway;	
			}	
			
			mGameEngineDemo.init(this,mcBIOS.finalPathway);	
			
		}
		
		/**
		 * Cleanup Memory for Quiting the Shell.
		 * 	> Cleanup the DisplayList
		 *  > mGameEngineDemo to Null
		 * 	> Dispatch the Event Saying it is Done with memeory CleanUp
		 */
		 
		private function cleanupGameEngineShell(evt:CustomEvent = null):void
		{
			
			while (numChildren) 
			{    
				removeChildAt(0);
			}	
			
			mGameEngineDemo = null;
			var tPassedObj:Object = evt.oData;
			this.dispatchEvent(new CustomEvent(tPassedObj,SEND_THROUGH_CMD));	
		}
		
		
		/**
		 * Setup Class Variables
		 */
		 
		private function setupVars():void
		{
			mGameEngineDemo = new GameEngineDemo();
			mGameEngineDemo.addEventListener(mGameEngineDemo.SEND_THROUGH_CMD,sendThroughEvent,false,0,true);	
			
			mcBIOS = (mcBIOS != null) ? mcBIOS : new NP9_BIOS();
			
			//Setup BIOS
			mcBIOS.debug = false;
			mcBIOS.translation = true;
			mcBIOS.trans_debug =  false;
			mcBIOS.dictionary = false;
			mcBIOS.game_id =  1105
			mcBIOS.game_lang = "en";
			mcBIOS.meterX = 200;
			mcBIOS.meterY = 200;
			mcBIOS.script_server = "dev.neopets.com";
			mcBIOS.game_server = "images50.neopets.com";
			mcBIOS.metervisible = true;
			mcBIOS.localTesting = true;
			mcBIOS.localPathway =  "games/gameEngineTest/include/";
			mcBIOS.game_datestamp =  "04/27/09";
			mcBIOS.game_timestamp = "8:31AM";
			mcBIOS.game_infostamp = "GameEngineDemo_Beta1";
			mcBIOS.iBIOSWidth = 650;
			mcBIOS.iBIOSHeight = 600;
			mcBIOS.width = mcBIOS.iBIOSWidth;
			mcBIOS.height = mcBIOS.iBIOSHeight;
		}
		
		
	}
	
}