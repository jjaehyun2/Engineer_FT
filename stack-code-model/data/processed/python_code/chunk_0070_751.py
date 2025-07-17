package com.tuarua {
public class Spotlight {
    public function Spotlight() {
    }
    /** Disposes the ANE */
    public static function dispose():void {
        if (SpotlightANEContext.context != null) SpotlightANEContext.dispose();
    }
}
}