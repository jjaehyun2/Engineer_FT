class com.pixelbreaker.ui.MouseWheel
{
    static var isMac, macBroadcaster;
    function MouseWheel()
    {
    } // End of the function
    static function main()
    {
        isMac = System.capabilities.os.toLowerCase().indexOf("mac") != -1;
        if (com.pixelbreaker.ui.MouseWheel.isMac)
        {
            macBroadcaster = new com.pixelbreaker.event.EventBroadcaster();
            flash.external.ExternalInterface.addCallback("externalMouseEvent", com.pixelbreaker.ui.MouseWheel, com.pixelbreaker.ui.MouseWheel.externalMouseEvent);
        } // end if
    } // End of the function
    static function addListener(obj)
    {
        if (!com.pixelbreaker.ui.MouseWheel.isMac)
        {
            com.pixelbreaker.ui.MouseWheel.main();
        } // end if
        if (com.pixelbreaker.ui.MouseWheel.isMac)
        {
            com.pixelbreaker.ui.MouseWheel.macBroadcaster.addListener(obj);
        }
        else
        {
            Mouse.addListener(obj);
        } // end else if
    } // End of the function
    static function removeListener(obj)
    {
        if (com.pixelbreaker.ui.MouseWheel.isMac)
        {
            com.pixelbreaker.ui.MouseWheel.macBroadcaster.removeListener(obj);
        }
        else
        {
            Mouse.removeListener(obj);
        } // end else if
    } // End of the function
    static function externalMouseEvent(delta)
    {
        com.pixelbreaker.ui.MouseWheel.macBroadcaster.broadcastMessage("onMouseWheel", delta);
    } // End of the function
} // End of Class