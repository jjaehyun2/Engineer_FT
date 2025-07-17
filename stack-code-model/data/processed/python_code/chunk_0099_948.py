package {

import flash.events.*;
import flash.net.XMLSocket;

import configuration.*;
import reader.*;

public class UIClientConnection {

    private const POLICY_SERVER_HOST:String = "localhost";
    private const POLICY_SERVER_PORT:Number = 3332;
    private const UI_SERVER_HOST:String = "localhost";
    private const UI_SERVER_PORT:Number = 3332;

    private var xmlIn:XML;
    private var xmlOut:XML;
    private var clientSocket:XMLSocket;

    private var connected:Boolean;

    public function UIClientConnection():void {
        init();

    }

    public function send(xml:XML):void {
        UIClient.debug("Event sent to server");
        clientSocket.send(xml);                     //sends the xml to server


        // UIClient.debug(xml.toXMLString()+"\n");

    }

    private function init():void {

        connected = false;

        ConfigurationReader.getInstance().loadXML(ObjectType.DEFAULT_XML, "public.connection.connect", initConnection);

    }

    private function initConnection(xml:XML):void {
        xmlOut = xml;

        connect(POLICY_SERVER_HOST,POLICY_SERVER_PORT); //connect to policy server

        //clientSocket.close();
        connected = true;

        connect(UI_SERVER_HOST,UI_SERVER_PORT); //connect to UI server
    }

    private function connect(host:String, port:Number):void {

        clientSocket = new XMLSocket();
        configureListeners(clientSocket);  
        clientSocket.connect(host, port);
    }

    private function configureListeners(dispatcher:IEventDispatcher):void {
        dispatcher.addEventListener(Event.CLOSE, closeHandler);
        dispatcher.addEventListener(Event.CONNECT, connectHandler);
        dispatcher.addEventListener(DataEvent.DATA, dataHandler);
        dispatcher.addEventListener(IOErrorEvent.IO_ERROR, ioErrorHandler);
        dispatcher.addEventListener(ProgressEvent.PROGRESS, progressHandler);
        dispatcher.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityErrorHandler);
    }

    private function closeHandler(event:Event):void {
        trace("closeHandler: " + event);
        UIClient.debug("CLOSED");
    }

    private function connectHandler(event:Event):void {
        trace("connectHandler: ");
        UIClient.debug("Connect event");
        clientSocket.send(xmlOut);
    }

    private function dataHandler(event:DataEvent):void {
        trace("dataHandler: " + event );
        UIClient.debug("Data event");
        xmlIn = XMLTools.validateXML(xmlIn, event.data);
        if (xmlIn != null) {
            UIClient.debug("XML is valid");
            this.documentReader.processDocument(xmlIn);
        }
        else {
            UIClient.debug("XML is not valid");
        }
    }

    private function ioErrorHandler(event:IOErrorEvent):void {
        trace("ioErrorHandler: " + event);
        UIClient.debug("IOERROR");
    }

    private function progressHandler(event:ProgressEvent):void {
        trace("progressHandler loaded:" + event.bytesLoaded + " total: " + event.bytesTotal);
        UIClient.debug("PROGRESS");
    }

    private function securityErrorHandler(event:SecurityErrorEvent):void {
        trace("securityErrorHandler: " + event);
        UIClient.debug("SECURITYERROR");
    }


}
}