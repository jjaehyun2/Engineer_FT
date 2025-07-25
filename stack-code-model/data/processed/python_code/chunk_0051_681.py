////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2007 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.messaging.channels
{

import flash.events.Event;
import flash.events.EventDispatcher;
import flash.events.HTTPStatusEvent;
import flash.events.IOErrorEvent;
import flash.events.ProgressEvent;
import flash.events.SecurityErrorEvent;
import flash.events.StatusEvent;
import flash.net.ObjectEncoding;
import flash.net.URLRequest;
import flash.net.URLRequestMethod;
import flash.net.URLStream;
import flash.net.URLVariables;
import flash.utils.ByteArray;

import mx.core.mx_internal;
import mx.logging.ILogger;
import mx.logging.Log;
import mx.messaging.Channel;
import mx.messaging.FlexClient;
import mx.messaging.events.MessageEvent;
import mx.messaging.messages.AbstractMessage;
import mx.messaging.messages.AcknowledgeMessage;
import mx.messaging.messages.CommandMessage;
import mx.messaging.messages.IMessage;

use namespace mx_internal;

/**
 *  Dispatched when the StreamingConnectionHandler receives a status command from the server.
 *
 *  @eventType flash.events.StatusEvent
 *
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion BlazeDS 4
 *  @productversion LCDS 3
 */
[Event(name="status", type="flash.events.StatusEvent")]

/**
 *  A helper class that is used by the streaming channels to open an internal
 *  HTTP connection to the server that is held open to allow the server to
 *  stream data down to the client with no poll overhead.
 *
 *  @langversion 3.0
 *  @playerversion Flash 9
 *  @playerversion AIR 1.1
 *  @productversion BlazeDS 4
 *  @productversion LCDS 3
 */
public class StreamingConnectionHandler extends EventDispatcher
{
    //--------------------------------------------------------------------------
    //
    // Public Static Constants
    //
    //--------------------------------------------------------------------------

    /**
     *  The code for the StatusEvent dispatched by this handler when a disconnect
     *  command is received from the server.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    public static const DISCONNECT_CODE:String = "disconnect";

    //--------------------------------------------------------------------------
    //
    // Private Static Constants
    //
    //--------------------------------------------------------------------------

    /**
     *  Parameter name for the command passed in the request for a new streaming connection.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const COMMAND_PARAM_NAME:String = "command";

    /**
     *  A request to open a streaming connection passes this 'command' in the request URI to the
     *  remote endpoint.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const OPEN_COMMAND:String = "open";

    /**
     *  A request to close a streaming connection passes this 'command' in the request URI to the
     *  remote endpoint.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const CLOSE_COMMAND:String = "close";

    /**
     *  Parameter name for the stream id; passed with commands for an existing streaming connection.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const STREAM_ID_PARAM_NAME:String = "streamId";

    /**
     *  Parameter name for the version param passed in the request for a new streaming connection.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const VERSION_PARAM_NAME:String = "version";

    /**
     *  Indicates the stream version used for this channel's stream connection.
     *  Currently just version 1. If the protocol over the wire needs to change in the future
     *  this gives us a way to indicate the change.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private static const VERSION_1:String = "1";

    // Constants for bytes used in parsing response chunks.
    private static const CR_BYTE:int = 13;
    private static const LF_BYTE:int = 10;
    private static const NULL_BYTE:int = 0;

    // Parse states; streamProgressHandler() uses these states to parse incoming HTTP response chunks.
    private static const INIT_STATE:int = 0;
    private static const CR_STATE:int = 1;
    private static const LF_STATE:int = 2;
    private static const SIZE_STATE:int = 3;
    private static const TEST_CHUNK_STATE:int = 4;
    private static const SKIP_STATE:int = 5;
    private static const DATA_STATE:int = 6;
    private static const RESET_BUFFER_STATE:int = 7;
    private static const CLOSED_STATE:int = 8;

    //--------------------------------------------------------------------------
    //
    // Constructor
    //
    //--------------------------------------------------------------------------

    /**
     *  Constructor.
     *
	 *  @param channel The Channel that uses this class.
	 *  @param log Reference to the logger for the associated Channel.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    public function StreamingConnectionHandler(channel:Channel, log:ILogger)
    {
        super();
        this.channel = channel;
        this._log = log;
    }

    //--------------------------------------------------------------------------
    //
    // Variables
    //
    //--------------------------------------------------------------------------

    /**
     * The Channel that uses this class.
  	 *
  	 *  @langversion 3.0
  	 *  @playerversion Flash 9
  	 *  @playerversion AIR 1.1
  	 *  @productversion BlazeDS 4
  	 *  @productversion LCDS 3
     */
     protected var channel:Channel;

    /**
     *  Byte buffer used to store the current chunk from the remote endpoint.
     *  Once a full chunk has been buffered, a message instance encoded in binary
     *  AMF format can be read from the chunk and dispatched.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    protected var chunkBuffer:ByteArray;

    /**
     *  Counter that keeps track of how many data bytes remain to be read for the current chunk.
     *  A sentinal value of -1 indicates an initial state (either waiting for the first chunk or
     *  just finished parsing the previous chunk).
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    protected var dataBytesToRead:int = -1;

    /**
     *  Index into the chunk buffer pointing to the first byte of chunk data.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    protected var dataOffset:int;

    /**
     *  @private
     *  Reference to the logger for the associated Channel.
     */
    protected var _log:ILogger;

    /**
     *  @private
     *  The server-assigned id for the streaming connection.
     */
    protected var streamId:String;

    /**
     *  @private
     *  Optional token to append to request URLs; generally contains a session token.
     */
    private var _appendToURL:String;

    /**
     *  Storage for the hex-format chunk size value from the byte stream.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private var hexChunkSize:String;

    /**
     *  Current parse state on the streaming connection.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private var state:int = INIT_STATE;

    /**
     *  URLStream used to open a streaming connection from the server to
     *  the client over HTTP.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private var streamingConnection:URLStream;

    /**
     *  URLStream used to close the original streaming connection opened from
     *  the server to the client over HTTP.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
	private var streamingConnectionCloser:URLStream;

    //--------------------------------------------------------------------------
    //
    // Public Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Used by the streaming channels to set up the streaming connection if
     *  necessary and issue the open request to the server.
     *
     *  @param appendToURL The string to append such as session id to the endpoint
     *  url while making the streaming connection request.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    public function openStreamingConnection(appendToURL:String=null):void
    {
        state = INIT_STATE;
        _appendToURL = appendToURL;

    	// Construct the streaming connection if needed.
        if (streamingConnection == null)
        {
            streamingConnection = new URLStream();
            streamingConnection.addEventListener(Event.OPEN, streamOpenHandler);
            streamingConnection.addEventListener(ProgressEvent.PROGRESS, streamProgressHandler);
            streamingConnection.addEventListener(Event.COMPLETE, streamCompleteHandler);
            streamingConnection.addEventListener(HTTPStatusEvent.HTTP_STATUS, streamHttpStatusHandler);
            streamingConnection.addEventListener(IOErrorEvent.IO_ERROR, streamIoErrorHandler);
            streamingConnection.addEventListener(SecurityErrorEvent.SECURITY_ERROR, streamSecurityErrorHandler);
        }

        // Open the streaming connection, only if not already requested to open.
        if (!streamingConnection.connected)
        {
            var request:URLRequest = new URLRequest();
            var url:String = channel.endpoint;

            if (url.charAt(url.length - 1) == '/')
                url = url.substring(0, url.length -1);

            if (_appendToURL != null)
                url += _appendToURL;

            request.url = url + "?" + COMMAND_PARAM_NAME + "=" + OPEN_COMMAND + "&" + VERSION_PARAM_NAME + "=" + VERSION_1;
            request.method = URLRequestMethod.POST;
            var postParams:URLVariables = new URLVariables();
            postParams[AbstractMessage.FLEX_CLIENT_ID_HEADER] = FlexClient.getInstance().id
            request.data = postParams;

			streamingConnection.load(request);
        }
    }

    /**
     *  Used by the streaming channels to shut down the streaming connection.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    public function closeStreamingConnection():void
    {
        state = CLOSED_STATE;
        chunkBuffer = null;
        hexChunkSize = null;
        dataBytesToRead = -1;
        dataOffset = 0;

        // First, close the existing connection.
        if (streamingConnection != null)
        {
            if (streamingConnection.connected)
            {
                try
                {
                    streamingConnection.close();
                }
                catch(ignore:Error)
                {
                }
            }
        }

        // Then, let the server know that streaming connection can be cleaned up.
        if (streamId != null)
        {
            if (streamingConnectionCloser == null)
            {
                var process:Function = function(event:Event):void
                {
                    if (streamingConnectionCloser.connected)
                    {
                        try
                        {
                            streamId = null;
                            streamingConnectionCloser.close();
                        }
                        catch (ignore:Error)
                        {
                        }
                    }
                }

                var ignore:Function = function(event:Event):void
                {
                    // Ignore.
                }

                streamingConnectionCloser = new URLStream();
                streamingConnectionCloser.addEventListener(Event.COMPLETE, process);
                streamingConnectionCloser.addEventListener(IOErrorEvent.IO_ERROR, process);
                // Ignore the following events.
                streamingConnectionCloser.addEventListener(HTTPStatusEvent.HTTP_STATUS, ignore);
                streamingConnectionCloser.addEventListener(SecurityErrorEvent.SECURITY_ERROR, ignore);
            }

            // Request the streaming connection close, only if not already requested to close.
            if (!streamingConnectionCloser.connected)
            {
                var request:URLRequest = new URLRequest();
                var url:String = channel.endpoint;
                if (_appendToURL != null)
                    url += _appendToURL;
                request.url = url + "?" + COMMAND_PARAM_NAME + "=" + CLOSE_COMMAND + "&"
                              + STREAM_ID_PARAM_NAME + "=" + streamId + "&" + VERSION_PARAM_NAME + "=" + VERSION_1;
                request.method = URLRequestMethod.POST;
                var postParams:URLVariables = new URLVariables();
                postParams[AbstractMessage.FLEX_CLIENT_ID_HEADER] = FlexClient.getInstance().id
                request.data = postParams;

                streamingConnectionCloser.load(request);
            }
        }
    }

    //--------------------------------------------------------------------------
    //
    // Protected Methods
    //
    //--------------------------------------------------------------------------

    /**
     *  Used by the streamProgressHandler to read a message. Default implementation
     *  returns null and subclasses must override this method.
     *
     *  @return Returns the message that was read.
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion BlazeDS 4
	 *  @productversion LCDS 3
     */
    protected function readMessage():IMessage
    {
        return null;
    }

    //--------------------------------------------------------------------------
    //
    // Private Methods
    //
    //--------------------------------------------------------------------------

    /**
    /**
     *  Handles a complete event that indicates that the streaming connection
     *  has been closed by the server by re-dispatching the event for the channel.
     *
     *  @param event The COMPLETE Event.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamCompleteHandler(event:Event):void
    {
        dispatchEvent(event);
    }

    /**
     *  Handles HTTP status events dispatched by the streaming connection by
     *  re-dispatching the event for the channel.
     *
     *  @param event The HTTPStatusEvent.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamHttpStatusHandler(event:HTTPStatusEvent):void
    {
        dispatchEvent(event);
    }

    /**
     *  Handles IO error events dispatched by the streaming connection by
     *  re-dispatching the event for the channel.
     *
     *  @param event The IOErrorEvent.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamIoErrorHandler(event:IOErrorEvent):void
    {
        dispatchEvent(event);
    }

    /**
     *  The open event is dispatched when the streaming connection has been established
     *  to the server, but it may still fail or be rejected so ignore this event and do
     *  not advance the channel to a connected state yet.
     *
     *  @param event The OPEN Event.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamOpenHandler(event:Event):void
    {
       // Ignore.
    }

    /**
     *  The arrival of data from the remote endpoint triggers progress events.
     *  The format of the data stream is HTTP Transfer-Encoding chunked, and each chunk contains either an object
     *  encoded in binary AMF format or a block of bytes to read off the network but skip any processing of.
     *
     *  @param event The ProgressEvent.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamProgressHandler(event:ProgressEvent):void
    {
        if (chunkBuffer == null)
        {
            chunkBuffer = new ByteArray();
            chunkBuffer.objectEncoding = ObjectEncoding.AMF3;
        }

        var n:int = streamingConnection.bytesAvailable;
        if (n > 0)
        {
            // Move available bytes to chunk buffer.
            streamingConnection.readBytes(chunkBuffer, chunkBuffer.length, n);

            // Parse chunk buffer. Currently no validation is done of the chunk format.
            // There's little need for it with our known server but validation could be added.
            var value:int; // Storage for current byte read.
            while (chunkBuffer.bytesAvailable > 0)
            {
                if (state == INIT_STATE)
                {
                    value = chunkBuffer.readByte();
                    if (value == NULL_BYTE) // Ignore the null heartbeat byte.
                        continue;

                    dataBytesToRead = -1;
                    hexChunkSize = "";
                    chunkBuffer.position--; // Push back byte read.
                    state = CR_STATE;
                }
                if (state == CR_STATE)
                {
                    value = chunkBuffer.readByte();

                    // This state skips past CRLF pairs but may also be hit at the start of a stream
                    // in which case we need to advance to the size state to finish reading the size header.
                    if (value == CR_BYTE)
                    {
                        state = LF_STATE;
                    }
                    else
                    {
                        // We seem to get into this state when a high number of messages
                        // are being streamed in a very short amount of time.
                        chunkBuffer.position--; // Push back byte read.
                        value = chunkBuffer.readByte();

                        if (value == LF_BYTE)
                        {
                            state = (dataBytesToRead == -1) ? SIZE_STATE : // Parsing a new chunk, read size next.
                                                            TEST_CHUNK_STATE; // Done with the size, now read the data.
                        }
                        else
                        {
                            chunkBuffer.position--; // Push back byte read.
                            state = SIZE_STATE;
                        }
                    }

                    if (chunkBuffer.bytesAvailable == 0)
                        break;
                }
                if (state == LF_STATE)
                {
                    value = chunkBuffer.readByte();

                    if (value == LF_BYTE)
                        state = (dataBytesToRead == -1) ? SIZE_STATE : // Parsing a new chunk, read size next.
                                                          TEST_CHUNK_STATE; // Done with the size, now read the data.

                    if (chunkBuffer.bytesAvailable == 0)
                        break;
                }
                if (state == SIZE_STATE)
                {
                    value = chunkBuffer.readByte();
                    if (value == NULL_BYTE) // Ignore the null heartbeat byte.
                        continue;

                    // CR indicates that we've finished reading the size.
                    if (value == CR_BYTE)
                    {
                        dataBytesToRead = parseInt(hexChunkSize, 16);
                        state = LF_STATE;
                    }
                    else // Hex digit.
                    {
                        hexChunkSize += String.fromCharCode(value);
                    }

                    if (chunkBuffer.bytesAvailable == 0)
                        break;
                }
                if (state == TEST_CHUNK_STATE)
                {
                    // A leading NULL byte in a chunk body indicates that the chunk should be read
                    // off the network but not processed further.
                    value = chunkBuffer.readByte();
                    dataOffset = chunkBuffer.position;
                    state = (value == NULL_BYTE) ? SKIP_STATE :
                                                   DATA_STATE;
                    chunkBuffer.position--;

                    if (chunkBuffer.bytesAvailable == 0)
                        break;
                }
                if (state == SKIP_STATE)
                {
                    if (chunkBuffer.bytesAvailable >= dataBytesToRead)
                    {
                        chunkBuffer.position += dataBytesToRead; // Skip over all bytes for the chunk.
                        state = RESET_BUFFER_STATE;
                    }
                    else // Wait for the rest of the chunk to arrive.
                    {
                        break;
                    }
                }
                if (state == DATA_STATE)
                {
                    if (chunkBuffer.bytesAvailable >= dataBytesToRead)
                    {
                        var message:IMessage = readMessage();
                        // Dispatch a message event from the channel.
                        // Prepare for the next chunk.
                        if (message != null)
                        {
                            if (Log.isDebug())
                                _log.debug("'{0}' channel got message\n{1}\n", channel.id, message.toString());

                            if ((message is AcknowledgeMessage) && (AcknowledgeMessage(message).correlationId == OPEN_COMMAND))
                            {
                                // Store the server-assigned stream id for use during disconnect.
                                streamId = String(message.body);
                                // Move the channel to a connected state.
                                var openEvent:Event = new Event(Event.OPEN);
                                dispatchEvent(openEvent);
                            }
                            else if ((message is CommandMessage) && (CommandMessage(message).operation == CommandMessage.DISCONNECT_OPERATION))
                            {
                                // Watch for stream disconnect commands from the server.
                                // When one is received, do not dispatch it, and instead notify the channel to
                                // shut down and not attempt to reconnect.
                                var statusEvent:StatusEvent = new StatusEvent(StatusEvent.STATUS, false, false, DISCONNECT_CODE, "status");
                                dispatchEvent(statusEvent);
                                // Exit parse loop - channel shut down will reset parser state.
                                return;
                            }
                            else  // Regular message; dispatch it.
                            {
                                channel.dispatchEvent(MessageEvent.createEvent(MessageEvent.MESSAGE, message));
                            }
                            // We've just finsihed the one point in the parse loop where we step outside of local control.
                            // The connection may now be closed, so check for this case here.
                            if (state == CLOSED_STATE)
                                return;

                        }
                        state = RESET_BUFFER_STATE;
                    }
                    else // Wait for the rest of the chunk to arrive.
                    {
                        break;
                    }
                }
                if (state == RESET_BUFFER_STATE)
                {
                    if (chunkBuffer.bytesAvailable > 0) // Copy unparsed bytes for the next chunk over into a new buffer.
                    {
                        for (var j:int = 0; j < chunkBuffer.bytesAvailable; j++)
                            var x:int = chunkBuffer[j];

                        var tempBuffer:ByteArray = new ByteArray();
                        tempBuffer.objectEncoding = ObjectEncoding.AMF3;
                        chunkBuffer.readBytes(tempBuffer, 0, chunkBuffer.bytesAvailable);
                        chunkBuffer = tempBuffer;
                    }
                    else // Nothing left in the buffer; let the GC collect the bytes for the old chunk.
                    {
                        chunkBuffer = new ByteArray();
                        chunkBuffer.objectEncoding = ObjectEncoding.AMF3;
                    }
                    state = INIT_STATE;

                    if (chunkBuffer.bytesAvailable == 0)
                        break;
                }
                if (state == CLOSED_STATE)
                {
                    return; // Exit parse loop.
                }
            }
        }
    }

    /**
     *  Handles security error events dispatched by the streaming connection by
     *  re-dispatching the event for the channel.
     *
     *  @param event The SecurityErrorEvent.
     *
     *  @langversion 3.0
     *  @playerversion Flash 9
     *  @playerversion AIR 1.1
     *  @productversion BlazeDS 4
     *  @productversion LCDS 3
     */
    private function streamSecurityErrorHandler(event:SecurityErrorEvent):void
    {
        dispatchEvent(event);
    }
}

}