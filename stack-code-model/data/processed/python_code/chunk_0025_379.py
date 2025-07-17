package com.github.asyncmc.mojang.api.flash.api {

import org.openapitools.common.ApiInvoker;
import org.openapitools.exception.ApiErrorCodes;
import org.openapitools.exception.ApiError;
import org.openapitools.common.ApiUserCredentials;
import org.openapitools.event.Response;
import org.openapitools.common.OpenApi;
import com.github.asyncmc.mojang.api.flash.model.Error;
import flash.filesystem.File;
import com.github.asyncmc.mojang.api.flash.model.SkinModel;

import mx.rpc.AsyncToken;
import mx.utils.UIDUtil;
import flash.utils.Dictionary;
import flash.events.EventDispatcher;

public class SkinOperationsApi extends OpenApi {
    /**
    * Constructor for the SkinOperationsApi api client
    * @param apiCredentials Wrapper object for tokens and hostName required towards authentication
    * @param eventDispatcher Optional event dispatcher that when provided is used by the SDK to dispatch any Response
    */
    public function SkinOperationsApi(apiCredentials: ApiUserCredentials, eventDispatcher: EventDispatcher = null) {
        super(apiCredentials, eventDispatcher);
    }

        public static const event_change_player_skin: String = "change_player_skin";
        public static const event_reset_player_skin: String = "reset_player_skin";
        public static const event_upload_player_skin: String = "upload_player_skin";


    /*
     * Returns void 
     */
    public function change_player_skin (strippedUuid: String, url: String, model: SkinModel): String {
        // create path and map variables
        var path: String = "/user/profile/{stripped_uuid}/skin".replace(/{format}/g,"xml").replace("{" + "stripped_uuid" + "}", getApiInvoker().escapeString(strippedUuid));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
        if(        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "change_player_skin";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function reset_player_skin (strippedUuid: String): String {
        // create path and map variables
        var path: String = "/user/profile/{stripped_uuid}/skin".replace(/{format}/g,"xml").replace("{" + "stripped_uuid" + "}", getApiInvoker().escapeString(strippedUuid));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "DELETE", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "reset_player_skin";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function upload_player_skin (strippedUuid: String, file: File, model: SkinModel): String {
        // create path and map variables
        var path: String = "/user/profile/{stripped_uuid}/skin".replace(/{format}/g,"xml").replace("{" + "stripped_uuid" + "}", getApiInvoker().escapeString(strippedUuid));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
        if(        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "PUT", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "upload_player_skin";

        token.returnType = null ;
        return requestId;

    }
}
}