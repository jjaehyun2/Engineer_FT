package com.playfab
{
    import flash.utils.Dictionary;

    public class PlayFabSettings
    {
        public static var ProductionEnvironmentURL:String = ".playfabapi.com";
        public static var RequestGetParams:Dictionary = new Dictionary();
        {
            RequestGetParams["sdk"] = PlayFabVersion.getVersionString();
        }
        public static var VerticalName:String = null; // The name of a customer vertical. This is only for customers running a private cluster. Generally you shouldn't touch this
        public static var TitleId:String = null; // You must set this value for PlayFabSdk to work properly (Found in the Game Manager for your title, at the PlayFab Website)
        public static var GlobalErrorHandler:Function;
        public static var EntityToken:String = null; // Internal variable used for Entity API Access (basically Entity Login)
        public static var DeveloperSecretKey:String = null; // You must set this value for PlayFabSdk to work properly (Found in the Game Manager for your title, at the PlayFab Website)
        public static var ClientSessionTicket:String = null; // This is set
        public static var AdvertisingIdType:String = null; // Set this to the appropriate AD_TYPE_X constant below
        public static var AdvertisingIdValue:String = null; // Set this to corresponding device value

        // DisableAdvertising is provided for completeness, but changing it is not suggested
        // Disabling this may prevent your advertising-related PlayFab marketplace partners from working correctly
        public static var DisableAdvertising:Boolean = false;
        public static const AD_TYPE_IDFA:String = "Idfa";
        public static const AD_TYPE_ANDROID_ID:String = "Adid";

        public static function GetURL(urlPath:String):String
        {
            var baseUrl:String = ProductionEnvironmentURL;
            var fullUrl:String;
            if(baseUrl.indexOf("http") != 0)
            {
                if(VerticalName != null)
                {
                    fullUrl = "https://" + VerticalName;
                }
                else
                {
                    fullUrl = "https://" + TitleId;
                }

                fullUrl = fullUrl + baseUrl + urlPath;
            }
            else
            {
                fullUrl = baseUrl + urlPath;
            }

            var getParams:Dictionary = RequestGetParams;
            var firstParam:Boolean = true;
            for(var key:String in getParams)
            {
                var value:String = getParams[key];

                if(firstParam)
                {
                    fullUrl += "?";
                    firstParam = false;
                }
                else
                {
                    fullUrl += "&";
                }

                fullUrl = fullUrl + key + "=" + value;
            }

            return fullUrl;
        }
    }
}