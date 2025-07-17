/**
 * Metagûsto AMFetamine
 * Copyright (C) 2008 Metagûsto
 * Website: https://github.com/metagusto/amfetamine
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.metagusto.logging {

import com.metagusto.remoting.RemoteAmfGateway;

import flash.events.Event;
import flash.net.Responder;

import mx.controls.Alert;
import mx.logging.ILogger;
import mx.rpc.events.FaultEvent;
import mx.rpc.events.ResultEvent;

/**
 * RemoteLogger
 * -----------------------------------------------------------------------------
 * This class implements a remote logger system usefull to stream log messages
 * from flash client to AMFetamine server.
 *
 * @author metagûsto
 */
public class RemoteLogger implements ILogger {
    private static var _instance:RemoteLogger;
    protected var _gateway:RemoteAmfGateway;
    protected var _lastMessage:String = null;
    protected var _defautlResponder:Responder;

    /**
     * Singleton Implementation for AS3
     */
    public static function getInstance():RemoteLogger {
        if (_instance == null)
            _instance = new RemoteLogger(arguments.callee);
        return _instance;
    }

    /**
     * Default constructor (called by singleton only)
     */
    public function RemoteLogger(caller:Function = null) {
        if (caller != RemoteLogger.getInstance)
            throw new Error("RemoteLogger is a singleton class, use getInstance() instead");
        if (RemoteLogger._instance != null)
            throw new Error("Assert failure. Only one instance should be instantiated");

        // Initializing instance
        this._gateway = new RemoteAmfGateway();
        this._defautlResponder = new Responder(onDeliverySuccess, onDeliveryFailure);
    }

    /**
     * Sets the gateway instance used for communication
     * @return RemoteGateway
     */
    public function set gateway(value:RemoteAmfGateway):void {
        this._gateway = value;
    }

    /**
     * Returns the gateway instance
     * @return RemoteGateway
     */
    public function get gateway():RemoteAmfGateway {
        return (this._gateway);
    }

    /**
     * Logs a message of level INFO
     */
    public function info(message:String, ...parameters):void {
        this._gateway.call("com.metagusto.RemoteLoggerService.info", this._defautlResponder, message);
    }

    /**
     * Logs a message of level WARNING
     */
    public function warn(message:String, ...parameters):void {
        this._gateway.call("com.metagusto.RemoteLoggerService.warn", this._defautlResponder, message);
    }

    /**
     * Logs a message of level ERROR
     */
    public function error(message:String, ...parameters):void {
        this._gateway.call("com.metagusto.RemoteLoggerService.error", this._defautlResponder, message);
    }

    /**
     * Logs a message of level DEBUG
     */
    public function debug(message:String, ...parameters):void {
        this._gateway.call("com.metagusto.RemoteLoggerService.debug", this._defautlResponder, message);
    }

    /**
     * Sinonimous function of error(). Added just for ILogger compatibility
     */
    public function fatal(message:String, ...parameters):void {
        this.error(message, parameters);
    }

    /**
     * Listener method for success message delivery
     */
    protected function onDeliverySuccess(result:ResultEvent):void {
        this._lastMessage = null;
    }

    /**
     * Listener method for failed message delivery
     */
    protected function onDeliveryFailure(result:FaultEvent):void {
        var logErrorEvent:RemoteLogErrorEvent = new RemoteLogErrorEvent(this._lastMessage, result);
        this._lastMessage = null;
        dispatchEvent(logErrorEvent);
    }
}
}