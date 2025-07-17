package com.ats.helpers {

    public class DeviceSettings {

        public var deviceId:String;
        public var automaticPort:Boolean;
        public var usbMode:Boolean;
        public var port:int = 8080;

        public function DeviceSettings(deviceId:String, port:int = -1, automaticPort:Boolean = true, usbMode:Boolean = true) {
            this.deviceId = deviceId.toLowerCase()
            this.automaticPort = automaticPort
            this.usbMode = usbMode

            if (port == -1) {
				if(usbMode){
					this.port = DeviceSettingsHelper.shared.nextPortAvailable();
				}
            } else {
                this.port = port
            }
        }

        public function toString():String {
            return deviceId + "==" + [automaticPort.toString(), usbMode.toString(), port.toString()].join(";")
        }

        // custom init
        public static function initFromDeviceSettingsString(string:String):DeviceSettings {
            var array:Array = string.split("==")
            if (array.length != 2) {
                return null
            }

            var deviceId:String = array[0]
            if (deviceId == "") {
                return null
            }

            var parametersString:String = array[1]
            var parameters:Array = parametersString.split(";")
            if (parameters.length != 3) {
                return null
            }

            var automaticPort:Boolean = parameters[0] == "true"
            var usbMode:Boolean = parameters[1] == "true"
            var port:int = parseInt(parameters[2])

            return new DeviceSettings(deviceId, port, automaticPort, usbMode)
        }

        public function save():void {
            DeviceSettingsHelper.shared.save(this)
        }
    }
}