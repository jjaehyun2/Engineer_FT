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
 
package org.puremvc.as3.multicore.utilities.fabrication.patterns.command.mock {
    import com.anywebcam.mock.Mock;

    import org.puremvc.as3.multicore.interfaces.IMediator;
    import org.puremvc.as3.multicore.interfaces.IProxy;
    import org.puremvc.as3.multicore.utilities.fabrication.addons.IMockable;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.*;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.mediator.FlexMediator;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.proxy.FabricationProxy;

    /**
	 * @author Darshan Sawardekar
	 */
	public class SimpleFabricationCommandTestMock extends SimpleFabricationCommand implements IMockable {

        [InjectProxy]
        public var injectedProxy:FabricationProxy;

        [InjectProxy(name="MyProxy")]
        public var injectedProxyByName:IProxy;

        [InjectMediator]
        public var injectedMediator:FlexMediator;

        [InjectMediator(name="MyMediator")]
        public var injectedMediatorByName:IMediator;

		private var _mock:Mock;
		
		public function SimpleFabricationCommandTestMock() {
			super();
		}
		
		public function get mock():Mock {
			if (_mock == null) {
				_mock = new Mock(this, true);
			}
			
			return _mock;
		}


    }
}