/**
 * Copyright (C) 2008 Darshan Sawardekar.
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
 
package org.puremvc.as3.multicore.utilities.fabrication.core.mock {
    import com.anywebcam.mock.Mock;

    import org.puremvc.as3.multicore.interfaces.IProxy;
    import org.puremvc.as3.multicore.utilities.fabrication.addons.IMockable;
    import org.puremvc.as3.multicore.utilities.fabrication.core.*;

    /**
	 * @author Darshan Sawardekar
	 */
	public class FabricationModelMock extends FabricationModel implements IMockable {
		
		public var _mock:Mock;
		
		static public function getInstance(multitonKey:String):FabricationModelMock {
			if (instanceMap[multitonKey] == null) {
				instanceMap[multitonKey] = new FabricationModelMock(multitonKey);
			}
			
			return instanceMap[multitonKey] as FabricationModelMock;
		}
		
		public function FabricationModelMock(multitonKey:String) {
			super(multitonKey);
		}
		
		public function get mock():Mock {
			if (_mock == null) {
				_mock = new Mock(this, true);
			}
			
			return _mock;
		}
		
		override public function dispose():void {
			mock.dispose();
		}
		
		override public function registerProxy(proxy:IProxy):void {
			mock.registerProxy(proxy);
		}
		
		override public function hasProxy(proxyName:String):Boolean {
			return mock.hasProxy(proxyName);
		}
		
		override public function removeProxy(proxyName:String):IProxy {
			return mock.removeProxy(proxyName);
		}
		
		override public function retrieveProxy(proxyName:String):IProxy {
			return mock.retrieveProxy(proxyName);
		}
		
		override protected function initializeModel():void {
			mock.initializeModel();
		}
		
	}
}