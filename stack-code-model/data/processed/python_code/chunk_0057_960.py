/**
 * ---------------------------------------------------------------------------
 *   Copyright (C) 2008 0x6e6562
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 * ---------------------------------------------------------------------------
 **/
package org.amqp.io
{
    import com.hurlant.crypto.tls.TLSConfig;
    import com.hurlant.crypto.tls.TLSSocket;

    import org.amqp.ConnectionParameters;
    import org.amqp.IODelegate;

    public class TLSDelegate extends TLSSocket implements IODelegate
    {
        public function TLSDelegate(host:String=null, port:int=0, config:TLSConfig=null)
        {
            super(host, port, config);
        }

        public function isConnected():Boolean {
            return super.connected;
        }

        public function open(params:ConnectionParameters):void {
            super.connect(params.serverhost, params.port, params.options);
        }
    }
}