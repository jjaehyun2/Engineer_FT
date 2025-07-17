/**
 * Created by mobitile on 12/5/15.
 */
package com.github.airext.bridge.test {
import com.github.airext.bridge.bridge;
import com.github.airext.bridge.test.core.bridge_test;

import flash.external.ExtensionContext;
import flash.filesystem.File;
import flash.filesystem.FileMode;
import flash.filesystem.FileStream;

use namespace bridge_test;

public class BridgeTest
{
    //--------------------------------------------------------------------------
    //
    //  Class constants
    //
    //--------------------------------------------------------------------------

    bridge_test static const EXTENSION_ID:String = "com.github.airext.bridge.test";

    //--------------------------------------------------------------------------
    //
    //  Class properties
    //
    //--------------------------------------------------------------------------

    private static var _context:ExtensionContext;

    bridge_test static function get context():ExtensionContext
    {
        if (_context == null)
        {
            _context = ExtensionContext.createExtensionContext(EXTENSION_ID, null);
        }

        return _context;
    }

    //--------------------------------------------------------------------------
    //
    //  Class methods
    //
    //--------------------------------------------------------------------------

    //-------------------------------------
    //  isSupported
    //-------------------------------------

    /**
     * Indicates if extension is supported on current platform.
     */
    public static function isSupported():Boolean
    {
        return context != null && context.call("isSupported");
    }

    //-------------------------------------
    //  extensionVersion
    //-------------------------------------

    private static var _extensionVersion:String = null;

    /**
     * Returns version of extension
     * @return extension version
     */
    public static function extensionVersion():String
    {
        if (_extensionVersion == null)
        {
            try
            {
                var extension_xml:File = ExtensionContext.getExtensionDirectory(EXTENSION_ID).resolvePath("META-INF/ANE/extension.xml");

                if (extension_xml.exists)
                {
                    var stream:FileStream = new FileStream();
                    stream.open(extension_xml, FileMode.READ);

                    var extension:XML = new XML(stream.readUTFBytes(stream.bytesAvailable));
                    stream.close();

                    var ns:Namespace = extension.namespace();

                    _extensionVersion = extension.ns::versionNumber;
                }
            }
            catch (error:Error)
            {
                // ignore
            }
        }

        return _extensionVersion;
    }

    //-------------------------------------
    //  testResult
    //-------------------------------------

    public function testResult(callback:Function):void
    {
        bridge(context).call("testResult").callback(callback);
    }

    //-------------------------------------
    //  testError
    //-------------------------------------

    public function testError(callback:Function):void
    {
        bridge(context).call("testError").callback(callback);
    }

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    public function BridgeTest()
    {
    }
}
}