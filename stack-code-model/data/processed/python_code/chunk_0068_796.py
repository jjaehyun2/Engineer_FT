package {

import flash.events.*;
import flash.net.XMLSocket;

import reader.*;

public class UIClientConnection {

    private var xmlIn:XML;
    private var xmlOut:XML;
    private var clientSocket:XMLSocket;
    private var documentReader:UIDocumentReader;

    private var connected:Boolean;

    public function UIClientConnection(display:Display):void {

        this.documentReader = new UIDocumentReader(display, this);
        init();
        connected = false;
    }

    public function send(xml:XML):void {
        UIClient.debug("Event sent to server\n");
        clientSocket.send(xml);
        //UIClient.debug(xml.toXMLString()+"\n");

    }

    private function init():void {
        xmlOut =
        <UIProtocol version="1.0">
            <events>
                <event id="public.connection.connect">
                    <!-- description of client -->
                </event>
            </events>
        </UIProtocol>;
        clientSocket = new XMLSocket();

        configureListeners(clientSocket);
        clientSocket.connect("localhost", 3333);

        //clientSocket.close();
        connected = true;

        clientSocket = new XMLSocket();
        configureListeners(clientSocket);  
        clientSocket.connect("localhost", 3332);
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
        UIClient.debug("CLOSED\n");
    }

    private function connectHandler(event:Event):void {
        trace("connectHandler: ");
        UIClient.debug("Connect event" + "\n");
        clientSocket.send(xmlOut);
    }

    private function dataHandler(event:DataEvent):void {
        trace("dataHandler: " + event);
        UIClient.debug("Data event\n");
        xmlIn = XMLTools.validateXML(xmlIn, event.data);
        if (xmlIn != null) {
            UIClient.debug("XML is valid\n");
            this.documentReader.processDocument(xmlIn);
        }
        else {
            UIClient.debug("XML is not valid\n");
        }
    }

    private function ioErrorHandler(event:IOErrorEvent):void {
        trace("ioErrorHandler: " + event);
        UIClient.debug("IOERROR\n");
    }

    private function progressHandler(event:ProgressEvent):void {
        trace("progressHandler loaded:" + event.bytesLoaded + " total: " + event.bytesTotal);
        UIClient.debug("PROGRESS\n");
    }

    private function securityErrorHandler(event:SecurityErrorEvent):void {
        trace("securityErrorHandler: " + event);
        UIClient.debug("SECURITYERROR\n");
    }


}
}