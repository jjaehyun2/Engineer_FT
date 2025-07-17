package {
import flash.display.*;
import flash.text.*;
import flash.net.*;
import flash.events.*;

import com.adobe.serialization.json.JSON;
import flash.external.ExternalInterface;

/**
 * 图片上传控件
 * 参数： {jsId:回调js的时候都会传这个用于支持多实例,fontSize:按钮的字体大小,txt:按钮显示的文本}
 * JS需要提供window.swfNotice 方法,用来接受回调
 * 回调的参数是JSON字符串，event分别可能是:ready,imgUrl,uploadError,uploadSuccess
 * 格式:  {jsId:xxxx, version:swfInput版本只有ready有,msg:消息提示,data:数据}
 * JS可以调用submitForm来提交表单
 * Created by ouchuanyu on 14/12/7.
 */
public class ImageUpload extends Sprite{
    private static var VERSION : String = "1.0.0";
    // 文件引用
    private var fileRef : FileReference = new FileReference();
    private var jsId : * = null;
    private var fileTypes : String = "*.jpg;*.jpeg;*.png";

    public function ImageUpload() {
        if (stage){
            init();
        }else{
            addEventListener(Event.ADDED_TO_STAGE, init);
        }
    }

    // 初始化方法
    private function init(e:Event = null):void{
        removeEventListener(Event.ADDED_TO_STAGE, init);

        //JS传过来的参数
        var param:Object = root.loaderInfo.parameters;

        jsId = param["jsId"];
        if(param["fileTypes"]){
            fileTypes = param["fileTypes"];
        }

        //按钮的初始化
        this.buttonMode = true;
        this.stage.align = StageAlign.TOP_LEFT;
        this.stage.scaleMode = StageScaleMode.NO_SCALE;
        var textField : TextField = new TextField();
        var format : TextFormat = new TextFormat();
        format.align = "center";
        format.size = param["fontSize"];
        textField.htmlText = param["txt"];
        textField.selectable = false;
        textField.x = 0;
        textField.y = (stage.stageHeight - param["fontSize"])/2 - 5;
        textField.setTextFormat(format);
        textField.width = stage.stageWidth;
        stage.addChild(textField);

        // 初始化事件
        fileRef.addEventListener(Event.SELECT, selectedImg);
        fileRef.addEventListener(Event.COMPLETE, imgLoaded);
        stage.addEventListener(MouseEvent.CLICK,selectFile);
        // 注册监听, 用于JS调用提交表单
        ExternalInterface.addCallback("swfSubmit",swfSubmit);

        // 通知JS加载完成
        ExternalInterface.call("swfNotice", JSON.encode({
            version : VERSION,
            jsId : jsId,
            event : "ready",
            msg : "SWFInput ready."
        }));
    }

    // 图片选择完成的监听处理
    private function imgLoaded(e:Event):void {
        var base64Data:String = Base64.encode(fileRef.data);
        base64Data = "data:image/"+fileRef.type.substring(1)+";base64," + base64Data;

        // 选择了文件后,通知JS图片的base64URL用于图片预览
        ExternalInterface.call("swfNotice", JSON.encode({
            jsId : jsId,
            event : "imgUrl",
            data : {
                base64Data : base64Data,
                name : fileRef.name,
                size : fileRef.size
            }
        }));
        //ExternalInterface.call("swfNotice", "imgUrl", base64Data, fileRef.name, fileRef.size);
    }

    // 图片选择事件监听
    private function selectedImg(e:Event):void {
        fileRef.load();
    }

    // 按钮点击事件处理
    public function selectFile(e : MouseEvent):void {
        var imgFilter : FileFilter = new FileFilter("Image", fileTypes);
        fileRef.browse(new Array(imgFilter));
    }

    // JS调用提交表单
    public function swfSubmit(url : String, dataStr : String):void{
        // JS传过来的表单数据
        var dataArr : Array = JSON.decode(dataStr);
        // 表单数据封装
        var form:MsMultiPartFormData = new MsMultiPartFormData();
        for(var i : Number = 0; i<dataArr.length; i++){
            if(dataArr[i].type == "file"){
                if(fileRef.data != null){
                    form.AddStreamFile(dataArr[i].name, fileRef.name, fileRef.data);
                }
            }else{
                form.AddFormField(dataArr[i].name, dataArr[i].val);
            }
        }
        form.PrepareFormData();

        // http请求封装
        var request:URLRequest=new URLRequest(url);
        var header:URLRequestHeader = new URLRequestHeader ("Content-Type", "multipart/form-data; boundary="+form.Boundary);
        request.requestHeaders.push(header);
        request.method="POST";
        request.data = form.GetFormData();

        // http请求
        var urlLoader : URLLoader = new URLLoader();
        urlLoader.dataFormat = URLLoaderDataFormat.TEXT;
        urlLoader.addEventListener(Event.COMPLETE,uploadSuccess);
        urlLoader.addEventListener(HTTPStatusEvent.HTTP_STATUS,httpStatus);
        urlLoader.addEventListener(IOErrorEvent.IO_ERROR, uploadFailure);
        urlLoader.load(request);

    }

    // 表单提交失败
    private function uploadFailure(e : IOErrorEvent):void{
        ExternalInterface.call("swfNotice", JSON.encode({
            jsId : jsId,
            event : "uploadError",
            msg : e.toString()
        }));
        //ExternalInterface.call("swfNotice", "uploadError", e.toString());
    }

    // http code， 要处理非200的
    private function httpStatus(e : HTTPStatusEvent):void{
        if(e.status != 200){
            ExternalInterface.call("swfNotice", JSON.encode({
                jsId : jsId,
                event : "uploadError",
                code : e.status
            }));
        }
    }

    // 表单提交成功
    private function uploadSuccess(e : Event):void{
        var loader : URLLoader = URLLoader(e.target);
        var resultStr : String = loader.data as String;
        ExternalInterface.call("swfNotice", JSON.encode({
            jsId : jsId,
            event : "uploadSuccess",
            data : JSON.decode(resultStr)
        }));
    }
}
}