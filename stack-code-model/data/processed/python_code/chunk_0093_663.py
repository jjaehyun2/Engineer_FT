package com.github.asyncmc.mojang.sessions.flash.api {

import org.openapitools.common.ApiInvoker;
import org.openapitools.exception.ApiErrorCodes;
import org.openapitools.exception.ApiError;
import org.openapitools.common.ApiUserCredentials;
import org.openapitools.event.Response;
import org.openapitools.common.OpenApi;
import com.github.asyncmc.mojang.sessions.flash.model.PlayerProfile;
import com.github.asyncmc.mojang.sessions.flash.model.SessionApiError;

import mx.rpc.AsyncToken;
import mx.utils.UIDUtil;
import flash.utils.Dictionary;
import flash.events.EventDispatcher;

public class LoginApi extends OpenApi {
    /**
    * Constructor for the LoginApi api client
    * @param apiCredentials Wrapper object for tokens and hostName required towards authentication
    * @param eventDispatcher Optional event dispatcher that when provided is used by the SDK to dispatch any Response
    */
    public function LoginApi(apiCredentials: ApiUserCredentials, eventDispatcher: EventDispatcher = null) {
        super(apiCredentials, eventDispatcher);
    }

        public static const event_get_player_profile: String = "get_player_profile";


    /*
     * Returns PlayerProfile 
     */
    public function get_player_profile (strippedUuid: String, unsigned: Boolean): String {
        // create path and map variables
        var path: String = "/session/minecraft/profile/{stripped_uuid}".replace(/{format}/g,"xml").replace("{" + "stripped_uuid" + "}", getApiInvoker().escapeString(strippedUuid));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(unsigned))
            queryParams["unsigned"] = toPathValue(unsigned);

        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_player_profile";

        token.returnType = PlayerProfile;
        return requestId;

    }
}
}