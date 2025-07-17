class mx.video.VideoError extends Error
{
    var _code, message, name, __get__code;
    function VideoError(errCode, msg)
    {
        super();
        _code = errCode;
        message = "" + errCode + ": " + mx.video.VideoError.ERROR_MSG[errCode - mx.video.VideoError.BASE_ERROR_CODE] + (msg == undefined ? ("") : (": " + msg));
        name = "VideoError";
    } // End of the function
    function get code()
    {
        return (_code);
    } // End of the function
    static var version = "1.0.1.10";
    static var shortVersion = "1.0.1";
    static var BASE_ERROR_CODE = 1000;
    static var NO_CONNECTION = 1000;
    static var NO_CUE_POINT_MATCH = 1001;
    static var ILLEGAL_CUE_POINT = 1002;
    static var INVALID_SEEK = 1003;
    static var INVALID_CONTENT_PATH = 1004;
    static var INVALID_XML = 1005;
    static var NO_BITRATE_MATCH = 1006;
    static var DELETE_DEFAULT_PLAYER = 1007;
    static var ERROR_MSG = ["Unable to make connection to server or to find FLV on server", "No matching cue point found", "Illegal cue point", "Invalid seek", "Invalid contentPath", "Invalid xml", "No bitrate match, must be no default flv", "Cannot delete default VideoPlayer"];
} // End of Class