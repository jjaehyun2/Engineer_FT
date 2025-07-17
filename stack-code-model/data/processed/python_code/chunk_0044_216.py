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
package flexUnitTests.flexUnit4.suites.frameworkSuite.cases.helper {
	import flash.events.TimerEvent;
	import flash.utils.Timer;
	
	import org.flexunit.runner.external.ExternalDependencyToken;
	import org.flexunit.runner.external.IExternalDependencyData;
	import org.flexunit.runner.external.IExternalDependencyLoader;

	public class ParamDataExt implements IExternalDependencyData {
		private var dToken:ExternalDependencyToken;
		private var timer:Timer;
		private var _data:Array;

		public function get data():Array {
			return _data;
		}

		private function success( data:TimerEvent ):void {
			timer.removeEventListener(TimerEvent.TIMER_COMPLETE, success );
			_data = [ [ 0, 0 ], [ 1, 2 ], [ 2, 4 ] ];
			dToken.notifyResult( _data );
		}
		
		private function failure( info:* ):void {
			_data = null;
			//dToken.notifyResult( fakeData );
			//dToken.notifyFault( info.fault.message );
			dToken.notifyFault( "Totally broken" );
		}
		
		public function retrieveDependency( testClass:Class ):ExternalDependencyToken {
			timer.start();

			return dToken;
		}
		
		public function ParamDataExt( url:String ) {
			timer = new Timer( 250, 1 );
			timer .addEventListener(TimerEvent.TIMER_COMPLETE, success );
			//Just fake this with a timer to illustrate the point

			dToken = new ExternalDependencyToken();
		}
	}
}