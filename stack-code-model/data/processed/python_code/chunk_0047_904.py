﻿/*
  Copyright (c) 2010, Adobe Systems Incorporated
  All rights reserved.

  Redistribution and use in source and binary forms, with or without
  modification, are permitted provided that the following conditions are
  met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

  * Neither the name of Adobe Systems Incorporated nor the names of its
    contributors may be used to endorse or promote products derived from
    this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

package com.facebook.graph {

  import com.facebook.graph.core.AbstractFacebook;
  import com.facebook.graph.data.FQLMultiQuery;
  import com.facebook.graph.data.FacebookSession;
  import com.facebook.graph.net.FacebookRequest;
  import com.facebook.graph.utils.FacebookDataUtils;
  import com.facebook.graph.utils.IResultParser;
  import com.facebook.graph.windows.LoginWindow;
  
  import flash.net.SharedObject;
  import flash.net.URLRequestMethod;

  /**
   * For use in AIR, to access the Facebook Graph API from the desktop.
   *
   */
  public class FacebookDesktop extends AbstractFacebook {

    /**
     * @private
     *
     */
    protected static const SO_NAME:String
    = 'com.facebook.graph.FacebookDesktop';

    /**
     * @private
     *
     */
    protected static var _instance:FacebookDesktop;

    /**
     * @private
     *
     */
    protected static var _canInit:Boolean = false;

    /**
     * @private
     *
     */
    protected var _manageSession:Boolean = true;

    /**
     * @private
     *
     */
    protected var loginWindow:LoginWindow;

    /**
     * @private
     *
     */
    protected var applicationId:String;
	
	/**
	 * @private
	 *
	 */
	protected var initCallback:Function;

    /**
     * @private
     *
     */
    protected var loginCallback:Function;
	
	/**
	 * @private
	 *
	 */
	protected var logoutCallback:Function;

    /**
     * Creates a new FacebookDesktop instance
     *
     */
    public function FacebookDesktop() {
      super();

      if (_canInit == false) {
        throw new Error(
          'FacebookDesktop is an singleton and cannot be instantiated.'
        );
      }
    }

    /**
     * Initializes this Facebook singleton with your application ID.
     * You must call this method first.
     *
     * @param applicationId The application ID you created at
     * http://www.facebook.com/developers/apps.php
     *
     * @param callback (Optional) Method to call when initialization is complete.
     * The handler must have the signature of callback(success:Object, fail:Object);
     * Success will be a FacebookSession if successful, or null if not.
     *
     * @param accessToken (Optional) If you have a previously saved access_token, you can pass it in here.
     *
     */
    public static function init(applicationId:String,
                  callback:Function = null,
                  accessToken:String = null
    ):void {

      getInstance().init(applicationId, callback, accessToken);
    }

    /**
     * Opens a new login window so the current user can log in to Facebook.
     *
     * @param callback The method to call when login is successful.
     * The handler must have the signature of callback(success:Object, fail:Object);
     * Success will be a FacebookSession if successful, or null if not.
     *
     * @param extendedPermissions (Optional) Array of extended permissions
     * to ask the user for once they are logged in.
     *
     * For the most current list of extended permissions,
     * visit http://developers.facebook.com/docs/authentication/permissions
     *
     * @see http://developers.facebook.com/docs/authentication
     * @see http://developers.facebook.com/docs/authentication/permissions
     *
     */
    public static function login(callback:Function, ...extendedPermissions:Array):void {
      getInstance().login(callback, extendedPermissions);
    }
	
	public static function set locale(value:String):void {
		getInstance().locale = value;
	}

    /**
     * Setting to true (default), this class will manage
     * the session and access token internally.
     * Setting to false, no session management will occur
     * and the end developer must save the session manually.
     *
     */
    public static function set manageSession(value:Boolean):void {
      getInstance().manageSession = value;
    }

    /**
     * Clears a user's local session.
     * This method is synchronous, since
     * its method does not log the user out of Facebook,
     * only the current application.
	 * 
	 * @param callback (Optional) Method to call when logout is done.
	 * 
	 * @param appOrigin (Optional) The site url specified for your app. Required for clearing html window cookie.
     *
     */
    public static function logout(callback:Function=null, appOrigin:String=null):void {
      getInstance().logout(callback, appOrigin);
    }

    /**
     * Opens a new window that asks the current user for
     * extended permissions.
	 * 
	 * @param callback The method to call after request for permissions.
	 * 
	 * @param extendedPermissions Array of extended permissions to ask the user for once they are logged in.
	 * 
	 *
     * @see com.facebook.graph.net.FacebookDesktop#login()
     * @see http://developers.facebook.com/docs/authentication/permissions
     *
     */
    public static function
      requestExtendedPermissions(callback:Function, ...extendedPermissions:Array):void {
      getInstance().requestExtendedPermissions(callback, extendedPermissions);
    }

    /**
     * Makes a new request on the Facebook Graph API.
     *
     * @param method The method to call on the Graph API.
     * For example, to load the user's current friends, pass in /me/friends
     * @param callback Method that will be called when this request is complete
     * The handler must have the signature of callback(result:Object, fail:Object);
     * On success, result will be the object data returned from Facebook.
     * On fail, result will be null and fail will contain information about the error.

     *
     * @param params Any parameters to pass to Facebook.
     * For example, you can pass {file:myPhoto, message:'Some message'};
     * this will upload a photo to Facebook.
     * @param requestMethod
     * The URLRequestMethod used to send values to Facebook.
     * The graph API follows correct Request method conventions.
     * GET will return data from Facebook.
     * POST will send data to Facebook.
     * DELETE will delete an object from Facebook.
     *
     * @see flash.net.URLRequestMethod
     * @see http://developers.facebook.com/docs/api
     *
     */
    public static function api(method:String,
                     callback:Function,
                     params:* = null,
                     requestMethod:String = 'GET'
    ):void {

      return getInstance().api(method,
        callback,
        params,
        requestMethod
      );
    }
	
	/**
     * Returns a reference to the entire raw object
	 * Facebook returns (including paging, etc.).
     *
     * @param data The result object.
     *
     * @see http://developers.facebook.com/docs/api#reading
     *
     */
	public static function getRawResult(data:Object):Object {			
		return getInstance().getRawResult(data);
	}
	
	/**
     * Asks if another page exists
	 * after this result object.
     *
     * @param data The result object.
     *
     * @see http://developers.facebook.com/docs/api#reading
     *
     */
	public static function hasNext(data:Object):Boolean {
		var result:Object = getInstance().getRawResult(data);
		if(!result.paging){ return false; }
		return (result.paging.next != null);
	}
	
	/**
     * Asks if a page exists
	 * before this result object.
     *
     * @param data The result object.
     *
     * @see http://developers.facebook.com/docs/api#reading
     *
     */
	public static function hasPrevious(data:Object):Boolean {
		var result:Object = getInstance().getRawResult(data);
		if(!result.paging){ return false; }
		return (result.paging.previous != null);
	}
	
	/**
     * Retrieves the next page that is associated with result object passed in.
     *
     * @param data The result object.
	 * @param callback Method that will be called when this request is complete
     * The handler must have the signature of callback(result:Object, fail:Object);
     * On success, result will be the object data returned from Facebook.
     * On fail, result will be null and fail will contain information about the error.
	 * 
	 * @see com.facebook.graph.net.FacebookDesktop#request()
     * @see http://developers.facebook.com/docs/api#reading
     *
     */
	public static function nextPage(data:Object, callback:Function):void {
		getInstance().nextPage(data, callback);
	}
	
	/**
     * Retrieves the previous page that is associated with result object passed in.
     *
     * @param data The result object.
	 * @param callback Method that will be called when this request is complete
     * The handler must have the signature of callback(result:Object, fail:Object);
     * On success, result will be the object data returned from Facebook.
     * On fail, result will be null and fail will contain information about the error.
     *
	 * @see com.facebook.graph.net.FacebookDesktop#request()
     * @see http://developers.facebook.com/docs/api#reading
     *
     */
	public static function previousPage(data:Object, callback:Function):void {
		getInstance().previousPage(data, callback);
	}

    /**
     * Shortcut method to post data to Facebook.
     * Alternatively, you can call FacebookDesktop.request
     * and use POST for requestMethod.
     *
     * @see com.facebook.graph.net.FacebookDesktop#request()
     */
    public static function postData(method:String,
                    callback:Function,
                    params:* = null
    ):void {

      api(method, callback, params, URLRequestMethod.POST);
    }

    /**
     * Deletes an object from Facebook.
     * The current user must have granted extended permission
     * to delete the corresponding object,
     * or an error will be returned.
     *
     * @param method The id and connection of the object to delete.
     * For example, /POST_ID/like to remove a like from a message.
     *
     * @see http://developers.facebook.com/docs/api#deleting
     * @see com.facebook.graph.net.FacebookDesktop#request()
     *
     */
    public static function deleteObject(method:String,
                      callback:Function
    ):void {

      return getInstance().deleteObject(method, callback);
    }

	/**
	 * Executes an FQL query on api.facebook.com.
	 * 
	 * @param query The FQL query string to execute.
	 * @param values Replaces string values in the in the query. 
	 * ie. Replaces {digit} or {id} with the corresponding key-value in the values object 
	 * @see http://developers.facebook.com/docs/reference/fql/
	 * @see com.facebook.graph.net.Facebook#callRestAPI()
	 * 
	 */	
	public static function fqlQuery(query:String, callback:Function=null, values:Object=null):void {
		getInstance().fqlQuery(query, callback, values);
	}
	
	/**
	 * Executes an FQL multiquery on api.facebook.com.
	 * 
	 * @param queries FQLMultiQuery The FQL queries to execute.
	 * @param parser IResultParser The parser used to parse result into object of name/value pairs. 
	 * @see http://developers.facebook.com/docs/reference/fql/
	 * @see com.facebook.graph.net.Facebook#callRestAPI()
	 * 
	 */	
	public static function fqlMultiQuery(queries:FQLMultiQuery, callback:Function=null, parser:IResultParser=null):void {
		getInstance().fqlMultiQuery(queries, callback, parser);
	}

    /**
     * Used to make old style RESTful API calls on Facebook.
     * Normally, you would use the Graph API to request data.
     * This method is here in case you need to use an old method,
     * such as FQL.
     *
     * @param methodName Name of the method to call on
     * api.facebook.com (ex: fql.query).
     * @param values Any values to pass to this request.
     * @param requestMethod URLRequestMethod used to send data to Facebook.
     *
     * @see com.facebook.graph.net.FacebookDesktop#request()
     *
     */
    public static function callRestAPI(methodName:String,
                       callback:Function = null,
                       values:* = null,
                       requestMethod:String = 'GET'
    ):void {

      return getInstance().callRestAPI(methodName, callback, values, requestMethod);
    }

    /**
     * Utility method to format a picture URL,
     * in order to load an image from Facebook.
     *
     * @param id The id you wish to load an image from.
     * @param type The size of image to display from Facebook
     * (square, small, or large).
     *
     * @see http://developers.facebook.com/docs/api#pictures
     *
     */
    public static function getImageUrl(id:String,
                       type:String = null
    ):String {

      return getInstance().getImageUrl(id, type);
    }

    /**
     * Synchronous call to return the current user's session.
     *
     */
    public static function getSession():FacebookSession {
      return getInstance().session;
    }

    /**
     * @private
     *
     */
    protected function init(applicationId:String,
                callback:Function = null,
                accessToken:String = null
    ):void {
		
      initCallback = callback;

      this.applicationId = applicationId;
      if (accessToken != null) {
        session = new FacebookSession();
        session.accessToken = accessToken;
      } else if (_manageSession) {
        session = new FacebookSession();

        var so:SharedObject = SharedObject.getLocal(SO_NAME);
        session.accessToken = so.data.accessToken;
        session.expireDate = so.data.expireDate;
      }
	  
	  verifyAccessToken(); //make a call to load the user's data to verify current session, so it fires initCallback if applicable
    }

    /**
     * @private
     *
     */
    protected function verifyAccessToken():void {
      api('/me', handleUserLoad);
    }

    /**
     * @private
     *
     */
    protected function handleUserLoad(result:Object, error:Object):void {
      if (result) {
        session.uid = result.id;
        session.user = result;
        if (loginCallback != null) {
          loginCallback(session, null);
        }
		if (initCallback != null) {
			initCallback(session, null);
			initCallback = null;
		}
      } else {
        if (loginCallback != null) {
          loginCallback(null, error);
        }
		if (initCallback != null) {
			initCallback(null, error);
			initCallback = null;
		}
		session = null;
      }
    }

    /**
     * @private
     *
     */
    protected function login(callback:Function, ...extendedPermissions:Array):void {
      this.loginCallback = callback;

      if (applicationId == null) {
        throw new Error(
          'FacebookDesktop.init() needs to be called first.'
        );
      }

      loginWindow = new LoginWindow(handleLogin);
      loginWindow.open(applicationId,
        FacebookDataUtils.flattenArray(extendedPermissions)
      );
    }

    /**
     * @private
     *
     */
    protected function set manageSession(value:Boolean):void {
      _manageSession = value;
    }

    /**
     * @private
     *
     */
    protected function requestExtendedPermissions(
      callback:Function,
      ...extendedPermissions:Array
    ):void {

      if (applicationId == null) {
        throw new Error(
          'User must be logged in before asking for extended permissions.'
        );
      }
      login(callback, extendedPermissions);
    }

    /**
     * @private
     *
     */
    protected function handleLogin(result:Object, fail:Object):void {
      loginWindow.loginCallback = null;

      if (fail) {
		  if (loginCallback != null) {
        	loginCallback(null, fail);
		  }
        return;
      }

      session = new FacebookSession();
      session.accessToken = result.access_token;
      session.expireDate = (result.expires_in == 0) ? null : FacebookDataUtils.stringToDate(result.expires_in) ;
      session = session;

      if (_manageSession) {
        var so:SharedObject = SharedObject.getLocal(SO_NAME);
        so.data.accessToken = session.accessToken;
        so.data.expireDate = session.expireDate;
        so.flush();
      }

      verifyAccessToken();
    }
	
	protected function handleLogout(result:Object, fail:Object):void {
		//This is a specific case. Since we are hitting a different URL to logout, we do not get a normal result/fail
		if (logoutCallback != null) {
			logoutCallback(true); 
			logoutCallback = null;
		}
	}

    /**
     * @private
     *
     */
    protected function logout(callback:Function=null, appOrigin:String=null):void {
		logoutCallback = callback;
		
		//clears cookie
		var params:Object = {};
		if (session != null) {
			params.access_token = session.accessToken;
		}
		params.method = "auth.logout";
		params.next = "http://static.ak.fbcdn.net/connect/xd_proxy.php#origin="+(appOrigin?appOrigin:"");
//		var req:FacebookRequest = new FacebookRequest("https://www.facebook.com/logout.php");
		var req:FacebookRequest = new FacebookRequest("http://m.facebook.com/logout.php?confirm=1");
		openRequests[req] = handleLogout;
		req.call("", params, handleRequestLoad);
		
      var so:SharedObject = SharedObject.getLocal(SO_NAME);
      so.clear();
      so.flush();

      session = null;
    }

    /**
     * @private
     *
     */
    protected static function getInstance():FacebookDesktop {
      if (_instance == null) {
        _canInit = true;
        _instance = new FacebookDesktop();
        _canInit = false;
      }
      return _instance;
    }
  }
}