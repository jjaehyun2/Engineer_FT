/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.flexunit.listeners
{
	import flash.events.DataEvent;
	import flash.events.Event;
	import flash.events.EventDispatcher;
	import flash.events.IOErrorEvent;
	import flash.events.SecurityErrorEvent;
	import flash.events.TimerEvent;
	import flash.net.XMLSocket;
	import flash.utils.Timer;
	
	import org.flexunit.listeners.closer.ApplicationCloser;
	import org.flexunit.listeners.closer.StandAloneFlashPlayerCloser;
	import org.flexunit.reporting.FailureFormatter;
	import org.flexunit.runner.Descriptor;
	import org.flexunit.runner.IDescription;
	import org.flexunit.runner.Result;
	import org.flexunit.runner.notification.Failure;
	import org.flexunit.runner.notification.IAsyncStartupRunListener;
	import org.flexunit.runner.notification.ITemporalRunListener;
	import org.flexunit.runner.notification.async.AsyncListenerWatcher;
	
	public class CIListener extends EventDispatcher implements IAsyncStartupRunListener, ITemporalRunListener
	{
		protected static const DEFAULT_PORT : uint = 1024;
		protected static const DEFAULT_SERVER : String = "127.0.0.1";
		private static const SUCCESS:String = "success";
		private static const ERROR:String = "error";
		private static const FAILURE:String = "failure";
		private static const IGNORE:String = "ignore";
		
		private var successes:Array = new Array();
		private var ignores:Array = new Array();
		
		private var _ready:Boolean = false;
		
		private static const END_OF_TEST_ACK : String ="<endOfTestRunAck/>";
		private static const END_OF_TEST_RUN : String = "<endOfTestRun/>";
		private static const START_OF_TEST_RUN_ACK : String = "<startOfTestRunAck/>";
		
		private var socket:XMLSocket;
		
		[Inspectable]
		public var port : uint;
		
		[Inspectable]
		public var server : String; //this is local host. same machine
		
		public var closer : ApplicationCloser;
		
		private var lastFailedTest:IDescription;
		private var timeOut:Timer;
		private var lastTestTime:Number = 0;
		
		public function CIListener(port : uint = DEFAULT_PORT, server : String = DEFAULT_SERVER) 
		{
			this.port = port;
			this.server = server;
			this.closer = new StandAloneFlashPlayerCloser(); //default application closer
			
			socket = new XMLSocket ();
			socket.addEventListener( DataEvent.DATA, dataHandler );
			socket.addEventListener( Event.CONNECT, handleConnect );
			socket.addEventListener( IOErrorEvent.IO_ERROR, errorHandler);
			socket.addEventListener( SecurityErrorEvent.SECURITY_ERROR,errorHandler);
			socket.addEventListener( Event.CLOSE,errorHandler);
			
			timeOut = new Timer( 2000, 1 );
			timeOut.addEventListener(TimerEvent.TIMER_COMPLETE, declareBroken, false, 0, true );
			timeOut.start();

			try
			{
				socket.connect( server, port );
				timeOut.stop();
			} catch (e:Error) {
				//This needs to be more than a trace
				trace (e.message);
			}
		}
		
		private function declareBroken( event:TimerEvent ):void {
			errorHandler( new Event( "broken") );
		}
		
		[Bindable(event="listenerReady")]
		public function get ready():Boolean 
		{
			return _ready;
		}

		private function setStatusReady():void {
			_ready = true;
			dispatchEvent( new Event( AsyncListenerWatcher.LISTENER_READY ) );
		}

		private function getTestCount( description:IDescription ):int 
		{
			return description.testCount;
		}

		public function testTimed( description:IDescription, runTime:Number ):void {
			if(!runTime || isNaN(runTime))
         {
            lastTestTime = 0;
         }
         else
         {
            lastTestTime = runTime;
         }
         
			//trace( description.displayName + " took " + runTime + " ms " );
		}
		
		public function testRunStarted( description:IDescription ):void
		{
			//Since description tells us nothing about failure, error, and skip counts, this is 
		   //computed by the Ant task as the process executes and no work is needed to signify
		   //the start of a test run.
		}
		
		public function testRunFinished( result:Result ):void 
		{
			sendResults(END_OF_TEST_RUN);
		}
		
		public function testStarted( description:IDescription ):void 
		{
			// called before each test
		}
		
		public function testFinished( description:IDescription ):void 
		{
			// called after each test
			if(!lastFailedTest || description.displayName != lastFailedTest.displayName){
				var desc:Descriptor = getDescriptorFromDescription(description);
				sendResults("<testcase classname=\""+desc.suite+"\" name=\""+desc.method+"\" time=\"" + lastTestTime  + "\" status=\""+SUCCESS+"\" />");
			}
		}
		
		public function testAssumptionFailure( failure:Failure ):void 
		{
			// called on assumptionFail
		}
		
		public function testIgnored( description:IDescription ):void 
		{
			// called on ignored test if we want to send ignore to ant.
			var descriptor:Descriptor = getDescriptorFromDescription(description);

			var xml:String =
				"<testcase classname=\""+descriptor.suite+"\" name=\""+descriptor.method+"\" time=\"" + lastTestTime  + "\" status=\""+IGNORE+"\">"
				+ "<skipped />"
				+ "</testcase>";

			sendResults( xml );
		}
		
		
		public function testFailure( failure:Failure ):void 
		{
			// called on a test failure
			lastFailedTest = failure.description;
			var descriptor:Descriptor =
				getDescriptorFromDescription(failure.description);
			var type : String = failure.description.displayName
			var message : String = failure.message;
			var stackTrace : String = failure.stackTrace;
			var methodName : String = descriptor.method;
			
			if ( stackTrace != null ) stackTrace = stackTrace.toString();
			
			stackTrace = FailureFormatter.xmlEscapeMessage( stackTrace );
			message = FailureFormatter.xmlEscapeMessage( message );
 
			var xml : String = null;
			
			if(FailureFormatter.isError(failure.exception)) 
			{
				xml =
					"<testcase classname=\""+descriptor.suite+"\" name=\""+descriptor.method+"\" time=\"" + lastTestTime  + "\" status=\""+ERROR+"\">"
					+ "<error message=\"" + message + "\" type=\""+ type +"\" >"
					+ "<![CDATA[" + stackTrace + "]]>"
					+ "</error>"
					+ "</testcase>";
			}
			else 
			{
				xml =
					"<testcase classname=\""+descriptor.suite+"\" name=\""+descriptor.method+"\" time=\"" + lastTestTime  + "\" status=\""+FAILURE+"\">"
					+ "<failure message=\"" + message + "\" type=\""+ type +"\" >"
					+ "<![CDATA[" + stackTrace + "]]>"
					+ "</failure>"
					+ "</testcase>";
			}
			
			sendResults(xml);
		}
		
		/*
		* Internal methods
		*/
		private function getDescriptorFromDescription( description:IDescription ):Descriptor
		{
			// reads relavent data from descriptor
			/**
			 * JAdkins - 7/27/07 - FXU-53 - Listener was returning a null value for the test class
			 * causing no data to be returned.  If length of array is greater than 1, then class is
			 * not in the default package.  If array length is 1, then test class is default package
			 * and formats accordingly.
			 **/
			var descriptor:Descriptor = new Descriptor();
			var descriptionArray:Array = description.displayName.split("::");
			var classMethod:String;
			if ( descriptionArray.length > 1 ) 
			{
				descriptor.path = descriptionArray[0];
				classMethod =  descriptionArray[1];
			} 
			else 
			{
				classMethod =  descriptionArray[0];
			}
			var classMethodArray:Array = classMethod.split(".");
			descriptor.suite = ( descriptor.path == "" ) ?  classMethodArray[0] :
				descriptor.path + "::" + classMethodArray[0];
			descriptor.method = classMethodArray[1];
			return descriptor;
		}
		
		protected function sendResults(msg:String):void
		{
			if(socket.connected)
			{
				socket.send( msg );				
			}
			
			trace(msg);
		}
		
		private function handleConnect(event:Event):void
		{
			//This is a good start, but we are no longer considering this a valid
			//time to begin sending results
			//We are going to wait until we get some data first
			//_ready = true;
			//dispatchEvent( new Event( AsyncListenerWatcher.LISTENER_READY ) );
		}

		private function errorHandler(event:Event):void
		{
			if ( !ready ) {
				//If we are not yet ready and received this, just inform the core so it can move on
				dispatchEvent( new Event( AsyncListenerWatcher.LISTENER_FAILED ) );
			} else {
				//If on the other hand we were ready once, then the core is counting on us... so, if something goes
				//wrong now, we are likely hung up. For now we are simply going to bail out of this process
				exit();
			}
		}

		private function dataHandler( event : DataEvent ) : void
		{
			var data : String = event.data;

			// If we received an acknowledgement on startup, the java server is read and we can start sending.			
			if ( data == START_OF_TEST_RUN_ACK ) {
				setStatusReady();
			} else if ( data == END_OF_TEST_ACK ) {
				// If we received an acknowledgement finish-up.
				// Close the socket.
				socket.close();
				exit();
			}
		}
		
		/**
		 * Exit the test runner by calling the ApplicationCloser.
		 */
		protected function exit() : void
		{
			this.closer.close();
		}
	}
}