/*
* Copyright (c) 2011 Research In Motion Limited.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

package blackberry.custom.accelerometer
{
	import flash.net.URLRequest;
	import flash.events.AccelerometerEvent;
	import flash.sensors.Accelerometer;

	import webworks.extension.DefaultExtension;
	
	public class CustomAccelerometer extends DefaultExtension
	{
		private var accelerometer:Accelerometer;        
		private var accelX:Number = 0;
	
		public function CustomAccelerometer() {
			super();
		}

		override public function getFeatureList():Array {
			return new Array ("blackberry.custom.accelerometer");
		}
		
		public function startAccelerometer():void {
			accelerometer = new Accelerometer();
			accelerometer.addEventListener(AccelerometerEvent.UPDATE, accUpdateHandler);
		}

		public function getAccelX():Number {
			return accelX;
		}

		private final function accUpdateHandler(event:AccelerometerEvent):void {
			accelX = event.accelerationX;
		}
	}
}