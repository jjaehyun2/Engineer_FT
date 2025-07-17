package com.ats.device.running.android {

    import avmplus.getQualifiedClassName;
    
    import com.ats.helpers.DeviceSettings;
    import com.ats.helpers.DeviceSettingsHelper;
    import com.ats.helpers.NetworkUtils;
    import com.ats.helpers.PortSwitcher;
    import com.ats.servers.tcp.ProxyServer;
    import com.ats.servers.udp.CaptureServer;
    
    import flash.events.Event;

    public class AndroidUsbDevice extends AndroidDevice {

        private var proxyServer:ProxyServer;
        private var captureServer:CaptureServer;

        private var webServerPort:int;
        private var captureServerPort:int;
        private var webSocketServerPort:int;
        private var webSocketClientPort:int;
		
        public function AndroidUsbDevice(id:String, simulator:Boolean, automaticPort:Boolean, port:String) {

            super(id, simulator);

            this.usbMode = true
            this.automaticPort = automaticPort
            this.port = port
        }
		
        override public function close():void {

            if (captureServer != null) {
                captureServer.close();
				captureServer = null;
            }
			
			if (proxyServer != null) {
				proxyServer.close();
				proxyServer = null;
			}

			super.close();
        }

        // ----

        private function fetchLocalPort():void {
            printDebugLogs("Fetching local port")
            setupWebServer(parseInt(port))
        }

        // ----

        private function setupWebServer(port:int):void {
			proxyServer = new ProxyServer();
			proxyServer.addEventListener(ProxyServer.WEB_SERVER_INITIALIZED, proxyServerInitializedHandler, false, 0, true);
			proxyServer.addEventListener(ProxyServer.WEB_SERVER_STARTED, proxyServerStartedHandler, false, 0, true);
			proxyServer.addEventListener(ProxyServer.WEB_SERVER_ERROR, proxyServerErrorHandler, false, 0, true);
			
			proxyServer.bind(port, automaticPort);
        }

        // -- Web Server Events

        private function proxyServerInitializedHandler(event:Event):void {
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_INITIALIZED, proxyServerInitializedHandler);
            webServerPort = proxyServer.localPort;

			captureServer = new CaptureServer();
			captureServer.addEventListener(CaptureServer.CAPTURE_SERVER_INITIALIZED, captureServerInitializedHandler, false, 0, true);
			captureServer.addEventListener(CaptureServer.CAPTURE_SERVER_STARTED, captureServerStartedHandler, false, 0, true);
			captureServer.addEventListener(CaptureServer.CAPTURE_SERVER_ERROR, captureServerErrorHandler, false, 0, true);
			captureServer.bind();
        }

        private function proxyServerStartedHandler(event:Event):void {
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_STARTED, proxyServerStartedHandler);
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_ERROR, proxyServerErrorHandler);
			
            // -- save port
            var portSettings:DeviceSettings = DeviceSettingsHelper.shared.settingsForDevice(adbIdentifier)
            portSettings.port = proxyServer.localPort;
            portSettings.save()

            port = portSettings.port.toString()
            // -- end

            captureServer.setupWebSocket(webSocketClientPort);
        }

        private function proxyServerErrorHandler(event:Event):void {
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_INITIALIZED, proxyServerInitializedHandler);
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_STARTED, proxyServerStartedHandler);
			proxyServer.removeEventListener(ProxyServer.WEB_SERVER_ERROR, proxyServerErrorHandler);

			proxyServer.close();
			
            usbError("Port " + port + " is already in use");
        }

        // -- Capture Server Events

        private function captureServerInitializedHandler(event:Event):void {
            captureServer.removeEventListener(CaptureServer.CAPTURE_SERVER_INITIALIZED, captureServerInitializedHandler);
            captureServerPort = captureServer.getLocalPort();

            startDriver();
        }

        private function captureServerStartedHandler(event:Event):void {
            captureServer.removeEventListener(CaptureServer.CAPTURE_SERVER_STARTED, captureServerStartedHandler);
			captureServer.removeEventListener(ProxyServer.WEB_SERVER_ERROR, captureServerErrorHandler);
        }

        private function captureServerErrorHandler(event:Event):void {
            captureServer.removeEventListener(ProxyServer.WEB_SERVER_INITIALIZED, captureServerInitializedHandler);
            captureServer.removeEventListener(ProxyServer.WEB_SERVER_STARTED, captureServerStartedHandler);
            captureServer.removeEventListener(ProxyServer.WEB_SERVER_ERROR, captureServerErrorHandler);

            usbError("Capture server initialization error");
        }

        private static function getWebSocketServerPort(data:String):int {
            var array:Array = data.split("\n");
            for each(var line:String in array) {
                if (line.indexOf("ATS_WEB_SOCKET_SERVER_START") > -1) {
                    var parameters:Array = line.split("=");
                    var subparameters:Array = (parameters[1] as String).split(":");
                    return parseInt(subparameters[1]);
                }
            }

            return -1;
        }

        // -- Native Process Exit Events

        private static function getWebSocketServerError(data:String):String {
            var array:Array = data.split("\n");
            for each(var line:String in array) {
                if (line.indexOf("ATS_WEB_SOCKET_SERVER_ERROR") > -1) {
                    var firstIndex:int = line.length;
                    var lastIndex:int = line.lastIndexOf("ATS_WEB_SOCKET_SERVER_ERROR:") + "ATS_WEB_SOCKET_SERVER_ERROR:".length;
                    return line.substring(lastIndex, firstIndex);
                }
            }

            return "";
        }

        override protected function executeDriver():void {
			if (automaticPort) {
				fetchLocalPort()
			} else {
				setupWebServer(parseInt(port))
			}
        }
		
		private function startDriver():void{
			var arguments:Vector.<String> = new <String>[
				"-s", id, "shell", "am", "instrument", "-w",
				"-e", "ipAddress", ip,
				"-e", "atsPort", port,
				"-e", "usbMode", String(usbMode),
				"-e", "udpPort", String(captureServerPort),
				"-e", "rootBounds", screenBounds,
				"-e", "debug", "false",
				"-e", "class", ANDROID_DRIVER + ".AtsRunnerUsb", ANDROID_DRIVER + ANDROID_JUNIT_RUNNER
			]
			startTestProcess(arguments);
		}

        override protected function fetchIpAddress():void {
            printDebugLogs("Fetching ip address")

            ip = NetworkUtils.getClientLocalIpAddress();
            if (ip != null) {
                uninstallDriver();
            } else {
                usbError("Retrieve local address error");
            }
        }

        private function setupPortForwarding():void {
            webSocketClientPort = PortSwitcher.getAvailableLocalPort();
				
			var adbProcess:AdbProcess = new AdbProcess()
			adbProcess.addEventListener(AdbProcessEvent.ADB_EXIT, forwardPortExitHandler, false, 0, true);
			adbProcess.execute(new <String>["-s", id, "forward", "tcp:" + webSocketClientPort, "tcp:" + webSocketServerPort])
        }

        override protected function onExecuteOutput(ev:AdbProcessEvent):void {
            super.onExecuteOutput(ev)

            if (ev.output.indexOf("ATS_WEB_SOCKET_SERVER_START:") > -1) {
                webSocketServerPort = getWebSocketServerPort(ev.output);
                setupPortForwarding();
            } else if (ev.output.indexOf("ATS_WEB_SOCKET_SERVER_ERROR") > -1) {
                var webSocketServerError:String = getWebSocketServerError(ev.output);
                trace("WebSocketServer error -> " + getQualifiedClassName(this) + " " + id + " " + webSocketServerError);
            } else if (ev.output.indexOf("ATS_WEB_SOCKET_SERVER_STOP") > -1) {
                trace("WebSocketServer stopped -> " + getQualifiedClassName(this) + id);
            }
        }

        private function forwardPortExitHandler(ev:AdbProcessEvent):void {
			ev.currentTarget.removeEventListener(AdbProcessEvent.ADB_EXIT, forwardPortExitHandler);
			proxyServer.setupWebSocket(webSocketClientPort);
        }
    }
}