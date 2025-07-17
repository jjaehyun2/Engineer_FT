package org.openapitools.client.api {

import org.openapitools.common.ApiInvoker;
import org.openapitools.exception.ApiErrorCodes;
import org.openapitools.exception.ApiError;
import org.openapitools.common.ApiUserCredentials;
import org.openapitools.event.Response;
import org.openapitools.common.OpenApi;
import org.openapitools.client.model.ComputerSet;
import org.openapitools.client.model.FreeStyleBuild;
import org.openapitools.client.model.FreeStyleProject;
import org.openapitools.client.model.Hudson;
import org.openapitools.client.model.ListView;
import org.openapitools.client.model.Queue;

import mx.rpc.AsyncToken;
import mx.utils.UIDUtil;
import flash.utils.Dictionary;
import flash.events.EventDispatcher;

public class RemoteAccessApi extends OpenApi {
    /**
    * Constructor for the RemoteAccessApi api client
    * @param apiCredentials Wrapper object for tokens and hostName required towards authentication
    * @param eventDispatcher Optional event dispatcher that when provided is used by the SDK to dispatch any Response
    */
    public function RemoteAccessApi(apiCredentials: ApiUserCredentials, eventDispatcher: EventDispatcher = null) {
        super(apiCredentials, eventDispatcher);
    }

        public static const event_get_computer: String = "get_computer";
        public static const event_get_jenkins: String = "get_jenkins";
        public static const event_get_job: String = "get_job";
        public static const event_get_job_config: String = "get_job_config";
        public static const event_get_job_last_build: String = "get_job_last_build";
        public static const event_get_job_progressive_text: String = "get_job_progressive_text";
        public static const event_get_queue: String = "get_queue";
        public static const event_get_queue_item: String = "get_queue_item";
        public static const event_get_view: String = "get_view";
        public static const event_get_view_config: String = "get_view_config";
        public static const event_head_jenkins: String = "head_jenkins";
        public static const event_post_create_item: String = "post_create_item";
        public static const event_post_create_view: String = "post_create_view";
        public static const event_post_job_build: String = "post_job_build";
        public static const event_post_job_config: String = "post_job_config";
        public static const event_post_job_delete: String = "post_job_delete";
        public static const event_post_job_disable: String = "post_job_disable";
        public static const event_post_job_enable: String = "post_job_enable";
        public static const event_post_job_last_build_stop: String = "post_job_last_build_stop";
        public static const event_post_view_config: String = "post_view_config";


    /*
     * Returns ComputerSet 
     */
    public function get_computer (depth: Number): String {
        // create path and map variables
        var path: String = "/computer/api/json".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(depth))
            queryParams["depth"] = toPathValue(depth);

        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_computer";

        token.returnType = ComputerSet;
        return requestId;

    }

    /*
     * Returns Hudson 
     */
    public function get_jenkins (): String {
        // create path and map variables
        var path: String = "/api/json".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();


        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_jenkins";

        token.returnType = Hudson;
        return requestId;

    }

    /*
     * Returns FreeStyleProject 
     */
    public function get_job (name: String): String {
        // create path and map variables
        var path: String = "/job/{name}/api/json".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_job";

        token.returnType = FreeStyleProject;
        return requestId;

    }

    /*
     * Returns String 
     */
    public function get_job_config (name: String): String {
        // create path and map variables
        var path: String = "/job/{name}/config.xml".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_job_config";

        token.returnType = String;
        return requestId;

    }

    /*
     * Returns FreeStyleBuild 
     */
    public function get_job_last_build (name: String): String {
        // create path and map variables
        var path: String = "/job/{name}/lastBuild/api/json".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_job_last_build";

        token.returnType = FreeStyleBuild;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function get_job_progressive_text (name: String, number: String, start: String): String {
        // create path and map variables
        var path: String = "/job/{name}/{number}/logText/progressiveText".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name)).replace("{" + "number" + "}", getApiInvoker().escapeString(number));

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

        if("null" != String(start))
            queryParams["start"] = toPathValue(start);

        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_job_progressive_text";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns Queue 
     */
    public function get_queue (): String {
        // create path and map variables
        var path: String = "/queue/api/json".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();


        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_queue";

        token.returnType = Queue;
        return requestId;

    }

    /*
     * Returns Queue 
     */
    public function get_queue_item (number: String): String {
        // create path and map variables
        var path: String = "/queue/item/{number}/api/json".replace(/{format}/g,"xml").replace("{" + "number" + "}", getApiInvoker().escapeString(number));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_queue_item";

        token.returnType = Queue;
        return requestId;

    }

    /*
     * Returns ListView 
     */
    public function get_view (name: String): String {
        // create path and map variables
        var path: String = "/view/{name}/api/json".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_view";

        token.returnType = ListView;
        return requestId;

    }

    /*
     * Returns String 
     */
    public function get_view_config (name: String): String {
        // create path and map variables
        var path: String = "/view/{name}/config.xml".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if() {
            throw new ApiError(400, "missing required params");
        }

        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "GET", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "get_view_config";

        token.returnType = String;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function head_jenkins (): String {
        // create path and map variables
        var path: String = "/api/json".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();


        
        
        var token:AsyncToken = getApiInvoker().invokeAPI(path, "HEAD", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "head_jenkins";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_create_item (name: String, from: String, mode: String, jenkinsCrumb: String, contentType: String, body: String): String {
        // create path and map variables
        var path: String = "/createItem".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
        if(        // verify required params are set
        if(        // verify required params are set
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
) {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }
) {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(name))
            queryParams["name"] = toPathValue(name);
if("null" != String(from))
            queryParams["from"] = toPathValue(from);
if("null" != String(mode))
            queryParams["mode"] = toPathValue(mode);

        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);
headerParams["Content-Type"] = toPathValue(contentType);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, body, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_create_item";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_create_view (name: String, jenkinsCrumb: String, contentType: String, body: String): String {
        // create path and map variables
        var path: String = "/createView".replace(/{format}/g,"xml");

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
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
) {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(name))
            queryParams["name"] = toPathValue(name);

        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);
headerParams["Content-Type"] = toPathValue(contentType);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, body, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_create_view";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_build (name: String, json: String, token: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/build".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

        // query params
        var queryParams: Dictionary = new Dictionary();
        var headerParams: Dictionary = new Dictionary();

        // verify required params are set
        if(        // verify required params are set
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
) {
            throw new ApiError(400, "missing required params");
        }

        if("null" != String(json))
            queryParams["json"] = toPathValue(json);
if("null" != String(token))
            queryParams["token"] = toPathValue(token);

        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_build";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_config (name: String, body: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/config.xml".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, body, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_config";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_delete (name: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/doDelete".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_delete";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_disable (name: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/disable".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_disable";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_enable (name: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/enable".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_enable";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_job_last_build_stop (name: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/job/{name}/lastBuild/stop".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, null, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_job_last_build_stop";

        token.returnType = null ;
        return requestId;

    }

    /*
     * Returns void 
     */
    public function post_view_config (name: String, body: String, jenkinsCrumb: String): String {
        // create path and map variables
        var path: String = "/view/{name}/config.xml".replace(/{format}/g,"xml").replace("{" + "name" + "}", getApiInvoker().escapeString(name));

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

        
        headerParams["Jenkins-Crumb"] = toPathValue(jenkinsCrumb);

        var token:AsyncToken = getApiInvoker().invokeAPI(path, "POST", queryParams, body, headerParams);

        var requestId: String = getUniqueId();

        token.requestId = requestId;
        token.completionEventType = "post_view_config";

        token.returnType = null ;
        return requestId;

    }
}
}