/**
 * Created by max.rozdobudko@gmail.com on 6/2/18.
 */
package com.github.airext {
import com.github.airext.core.documents;

import flash.external.ExtensionContext;
import flash.filesystem.File;
import flash.filesystem.FileMode;
import flash.filesystem.FileStream;

use namespace documents;

public class Documents {
    
    //--------------------------------------------------------------------------
    //
    //  Class methods
    //
    //--------------------------------------------------------------------------

    documents static const EXTENSION_ID:String = "com.github.airext.Documents";

    //--------------------------------------------------------------------------
    //
    //  Class properties
    //
    //--------------------------------------------------------------------------

    //-------------------------------------
    //  context
    //-------------------------------------

    private static var _context: ExtensionContext;
    documents static function get context(): ExtensionContext {
        if (_context == null) {
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

    public static function get isSupported(): Boolean {
        return context != null && context.call("isSupported");
    }

    //-------------------------------------
    //  sharedInstance
    //-------------------------------------

    private static var instance: Documents;

    public static function get shared(): Documents {
        if (instance == null) {
            new Documents();
        }
        return instance;
    }

    //-------------------------------------
    //  extensionVersion
    //-------------------------------------

    private static var _extensionVersion: String = null;

    /**
     * Returns version of extension
     * @return extension version
     */
    public static function get extensionVersion(): String
    {
        if (_extensionVersion == null) {
            try {
                var extension_xml: File = ExtensionContext.getExtensionDirectory(EXTENSION_ID).resolvePath("META-INF/ANE/extension.xml");
                if (extension_xml.exists) {
                    var stream:FileStream = new FileStream();
                    stream.open(extension_xml, FileMode.READ);

                    var extension:XML = new XML(stream.readUTFBytes(stream.bytesAvailable));
                    stream.close();

                    var ns:Namespace = extension.namespace();

                    _extensionVersion = extension.ns::versionNumber;
                }
            } catch (error:Error) {
                // ignore
            }
        }

        return _extensionVersion;
    }

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    public function Documents() {
        super();
        instance = this;
    }

    //--------------------------------------------------------------------------
    //
    //  Methods
    //
    //--------------------------------------------------------------------------

    public function previewDocumentWithPath(path: String): void {
        context.call("preview", path);
    }

    public function clearDocumentWithPath(path: String): void {
        context.call("clear", path);
    }

}
}