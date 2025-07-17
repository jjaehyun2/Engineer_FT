package kitaec.services {
import flash.events.Event;
import flash.net.URLRequestMethod;

import kitaec.controller.Controller;

import kitaec.model.Model;

import mx.controls.Alert;
import mx.rpc.AsyncToken;

import mx.rpc.events.FaultEvent;
import mx.rpc.events.ResultEvent;
import mx.rpc.http.HTTPService;

public class BaseService extends HTTPService {

    public static const RESPONSE_STATUS_OK:String = "OK";
    public static const RESPONSE_STATUS_ERROR:String = "ERROR";

    public static const SUCCESS_EVENT:String = "success";

    public var result:Object;
    public var resultStr:String; // For Testing
    public var callBackFunction:Function;

    protected var model:Model = Model.getInstance();
    protected var controller:Controller = Controller.getInstance();

    public function BaseService() {
        useProxy = false;
        showBusyCursor = true;
        method = URLRequestMethod.POST;
    }

    override public function send(parameters:Object = null):AsyncToken {
        addEventListener(ResultEvent.RESULT, onResult);
        addEventListener(FaultEvent.FAULT, onFault);


        model.isShowLoading = true;
        return super.send(parameters);
    }

    protected function callBack():void {
        if(callBackFunction != null) {
            callBackFunction();
        }
    }

    public function onResult(event:ResultEvent):void {
        resultStr = event.result.toString();
        result = event.result != "" ? JSON.parse(event.result.toString()) : null;
        removeEventListener(ResultEvent.RESULT, onResult);
        removeEventListener(FaultEvent.FAULT, onFault);
        dispatchEvent(new Event(SUCCESS_EVENT));
        model.isShowLoading = false;
    }

    public function onFault(event:FaultEvent):void {
        removeEventListener(ResultEvent.RESULT, onResult);
        removeEventListener(FaultEvent.FAULT, onFault);

        Alert.show(event.fault.faultDetail, event.fault.faultString);
        model.isShowLoading = false;
    }
}
}