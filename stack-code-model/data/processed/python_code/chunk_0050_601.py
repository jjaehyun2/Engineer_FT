/*
 * Copyright (C) 2006 Claus Wahlers and Max Herkender
 *
 * This software is provided 'as-is', without any express or implied
 * warranty.  In no event will the authors be held liable for any damages
 * arising from the use of this software.
 *
 * Permission is granted to anyone to use this software for any purpose,
 * including commercial applications, and to alter it and redistribute it
 * freely, subject to the following restrictions:
 *
 * 1. The origin of this software must not be misrepresented; you must not
 *    claim that you wrote the original software. If you use this software
 *    in a product, an acknowledgment in the product documentation would be
 *    appreciated but is not required.
 * 2. Altered source versions must be plainly marked as such, and must not be
 *    misrepresented as being the original software.
 * 3. This notice may not be removed or altered from any source distribution.
 */

package com.codeazur.fzip
{
	import flash.events.*;
	import flash.net.URLRequest;
	import flash.net.URLStream;
	import flash.text.*;
	import flash.utils.*;

	/**
	 * Dispatched when a file contained in a ZIP archive has 
	 * loaded successfully.
	 *
	 * @eventType deng.fzip.FZipEvent.FILE_LOADED
	 */
	[Event(name="fileLoaded", type="deng.fzip.FZipEvent")]

	/**
	 * Dispatched when an error is encountered while parsing a 
	 * ZIP Archive.
	 *
	 * @eventType deng.fzip.FZipErrorEvent.PARSE_ERROR
	 */
	[Event(name="parseError", type="deng.fzip.FZipErrorEvent")]

	/**
	 * Dispatched when data has loaded successfully. 
	 *
	 * @eventType flash.events.Event.COMPLETE 
	 */
	[Event(name="complete", type="flash.events.Event")]

	/**
	 * Dispatched if a call to FZip.load() attempts to access data 
	 * over HTTP, and the current Flash Player is able to detect 
	 * and return the status code for the request. (Some browser 
	 * environments may not be able to provide this information.) 
	 * Note that the httpStatus (if any) will be sent before (and 
	 * in addition to) any complete or error event
	 *
	 * @eventType flash.events.HTTPStatusEvent.HTTP_STATUS 
	 */
	[Event(name="httpStatus", type="flash.events.HTTPStatusEvent")]

	/**
	 * Dispatched when an input/output error occurs that causes a 
	 * load operation to fail. 
	 *
	 * @eventType flash.events.IOErrorEvent.IO_ERROR
	 */
	[Event(name="ioError", type="flash.events.IOErrorEvent")]

	/**
	 * Dispatched when a load operation starts.
	 *
	 * @eventType flash.events.Event.OPEN
	 */
	 
	[Event(name="open", type="flash.events.Event")]

	/**
	 * Dispatched when data is received as the download operation 
	 * progresses.
	 *
	 * @eventType flash.events.ProgressEvent.PROGRESS
	 */
	[Event(name="progress", type="flash.events.ProgressEvent")]

	/**
	 * Dispatched if a call to FZip.load() attempts to load data 
	 * from a server outside the security sandbox. 
	 * 
	 * @eventType flash.events.SecurityErrorEvent.SECURITY_ERROR
	 */
	[Event(name="securityError", type="flash.events.SecurityErrorEvent")]


	/**
	 * Loads and parses ZIP archives.
	 * 
	 * <p>FZip is able to process, create and modify standard ZIP archives as described in the
	 * <a href="http://www.pkware.com/business_and_developers/developer/popups/appnote.txt">PKZIP file format documentation</a>.</p>
	 * 
	 * <p>Limitations:</p>
	 * <ul>
	 * <li>ZIP feature versions &gt; 2.0 are not supported</li>
	 * <li>ZIP archives containing data descriptor records are not supported.</li>
	 * <li>If running in the Flash Player browser plugin, FZip requires ZIPs to be 
	 * patched (Adler32 checksums need to be added). This is not required if
	 * FZip runs in the Adobe AIR runtime or if files contained in the ZIP 
	 * are not compressed.</li>
	 * </ul>
	 */		
	public class FZip extends EventDispatcher
	{
		private var filesList:Array;
		private var filesDict:Dictionary;

		private var urlStream:URLStream;
		private var charEncoding:String;
		private var parseFunc:Function;
		private var currentFile:FZipFile;

		/**
		 * Constructor
		 * 
		 * @param filenameEncoding The character encoding used for filenames
		 * contained in the zip. If unspecified, unicode ("utf-8") is used.
		 * Older zips commonly use encoding "IBM437" (aka "cp437"),
		 * while other European countries use "ibm850".
		 * @see http://livedocs.adobe.com/labs/as3preview/langref/charset-codes.html
		 */		
		public function FZip(filenameEncoding:String = "utf-8") {
			super();
			charEncoding = filenameEncoding;
			parseFunc = parseIdle;
		}

		/**
		 * Indicates whether a file is currently being processed or not.
		 */		
		public function get active():Boolean {
			return (parseFunc !== parseIdle);
		}

		/**
		 * Begins downloading the ZIP archive specified by the request
		 * parameter.
		 * 
		 * @param request A URLRequest object specifying the URL of a ZIP archive
		 * to download. 
		 * If the value of this parameter or the URLRequest.url property 
		 * of the URLRequest object passed are null, Flash Player throws 
		 * a null pointer error.
		 */		
		public function load(request:URLRequest):void {
			if(!urlStream && parseFunc == parseIdle) {
				urlStream = new URLStream();
				urlStream.endian = Endian.LITTLE_ENDIAN;
				addEventHandlers();
				filesList = [];
				filesDict = new Dictionary();
				parseFunc = parseSignature;
				urlStream.load(request);
			}
		}
		
		/**
		 * Loads a ZIP archive from a ByteArray.
		 *
		 * @param bytes The ByteArray containing the ZIP archive
		 */
		public function loadBytes(bytes:ByteArray):void {
			if (!urlStream && parseFunc == parseIdle) {
				filesList = [];
				filesDict = new Dictionary();
				bytes.position = 0;
				bytes.endian = Endian.LITTLE_ENDIAN;
				parseFunc = parseSignature;
				if (parse(bytes)) {
					parseFunc = parseIdle;
					dispatchEvent(new Event(Event.COMPLETE));
				} else {
					dispatchEvent(new FZipErrorEvent(FZipErrorEvent.PARSE_ERROR, "EOF"));
				}
			}
		}

		/**
		 * Immediately closes the stream and cancels the download operation.
		 * Files contained in the ZIP archive being loaded stay accessible
		 * through the getFileAt() and getFileByName() methods.
		 */		
		public function close():void {
			if(urlStream) {
				parseFunc = parseIdle;
				removeEventHandlers();
				urlStream.close();
				urlStream = null;
			}
		}

		/**
		 * Serializes this zip archive into an IDataOutput stream (such as 
		 * ByteArray or FileStream) according to PKZIP APPNOTE.TXT
		 * 
		 * @param stream The stream to serialize the zip file into.
		 * @param includeAdler32 To decompress compressed files, FZip needs Adler32
		 * 		checksums to be injected into the zipped files. FZip will do that 
		 * 		automatically if includeAdler32 is set to true. Note that if the
		 * 		ZIP contains a lot of files, or big files, the calculation of the
		 * 		checksums may take a while.
		 */		
		public function serialize(stream:IDataOutput, includeAdler32:Boolean = false):void {
			if(stream != null && filesList.length > 0) {
				var endian:String = stream.endian;
				var ba:ByteArray = new ByteArray();
				stream.endian = ba.endian = Endian.LITTLE_ENDIAN;
				var offset:uint = 0;
				var files:uint = 0;
				for(var i:int = 0; i < filesList.length; i++) {
					var file:FZipFile = filesList[i] as FZipFile;
					if(file != null) {
						// first serialize the central directory item
						// into our temporary ByteArray
						file.serialize(ba, includeAdler32, true, offset);
						// then serialize the file itself into the stream
						// and update the offset
						offset += file.serialize(stream, includeAdler32);
						// keep track of how many files we have written
						files++;
					}
				}
				if(ba.length > 0) {
					// Write the central diectory items
					stream.writeBytes(ba);
				}
				// Write end of central directory:
				// Write signature
				stream.writeUnsignedInt(0x06054b50);
				// Write number of this disk (always 0)
				stream.writeShort(0);
				// Write number of this disk with the start of the central directory (always 0)
				stream.writeShort(0);
				// Write total number of entries on this disk
				stream.writeShort(files);
				// Write total number of entries
				stream.writeShort(files);
				// Write size
				stream.writeUnsignedInt(ba.length);
				// Write offset of start of central directory with respect to the starting disk number
				stream.writeUnsignedInt(offset);
				// Write zip file comment length (always 0)
				stream.writeShort(0);
				// Reset endian of stream
				stream.endian = endian;
			}
		}

		/**
		 * Gets the number of accessible files in the ZIP archive.
		 * 
		 * @return The number of files
		 */				
		public function getFileCount():uint {
			return filesList ? filesList.length : 0;
		}

		/**
		 * Retrieves a file contained in the ZIP archive, by index.
		 * 
		 * @param index The index of the file to retrieve
		 * @return A reference to a FZipFile object
		 */				
		public function getFileAt(index:uint):FZipFile {
			return filesList ? filesList[index] as FZipFile : null;
		}

		/**
		 * Retrieves a file contained in the ZIP archive, by filename.
		 * 
		 * @param name The filename of the file to retrieve
		 * @return A reference to a FZipFile object
		 */				
		public function getFileByName(name:String):FZipFile {
			return filesDict[name] ? filesDict[name] as FZipFile : null;
		}

		/**
		 * Adds a file to the ZIP archive.
		 * 
		 * @param name The filename
		 * @param content The ByteArray containing the uncompressed data (pass <code>null</code> to add a folder)
		 * @return A reference to the newly created FZipFile object
		 */				
		public function addFile(name:String, content:ByteArray = null):FZipFile {
			return addFileAt(filesList ? filesList.length : 0, name, content);
		}

		/**
		 * Adds a file from a String to the ZIP archive.
		 * 
		 * @param name The filename
		 * @param content The String
		 * @param charset The character set
		 * @return A reference to the newly created FZipFile object
		 */				
		public function addFileFromString(name:String, content:String, charset:String = "utf-8"):FZipFile {
			return addFileFromStringAt(filesList ? filesList.length : 0, name, content, charset);
		}

		/**
		 * Adds a file to the ZIP archive, at a specified index.
		 * 
		 * @param index The index
		 * @param name The filename
		 * @param content The ByteArray containing the uncompressed data (pass <code>null</code> to add a folder)
		 * @return A reference to the newly created FZipFile object
		 */				
		public function addFileAt(index:uint, name:String, content:ByteArray = null):FZipFile {
			if(filesList == null) {
				filesList = [];
			}
			if(filesDict == null) {
				filesDict = new Dictionary();
			} else if(filesDict[name]) {
				throw(new Error("File already exists: " + name + ". Please remove first."));
			}
			var file:FZipFile = new FZipFile();
			file.filename = name;
			file.content = content;
			if(index >= filesList.length) {
				filesList.push(file);
			} else {
				filesList.splice(index, 0, file);
			}
			filesDict[name] = file;
			return file;
		}

		/**
		 * Adds a file from a String to the ZIP archive, at a specified index.
		 * 
		 * @param index The index
		 * @param name The filename
		 * @param content The String
		 * @param charset The character set
		 * @return A reference to the newly created FZipFile object
		 */				
		public function addFileFromStringAt(index:uint, name:String, content:String, charset:String = "utf-8"):FZipFile {
			if(filesList == null) {
				filesList = [];
			}
			if(filesDict == null) {
				filesDict = new Dictionary();
			} else if(filesDict[name]) {
				throw(new Error("File already exists: " + name + ". Please remove first."));
			}
			var file:FZipFile = new FZipFile();
			file.filename = name;
			file.setContentAsString(content, charset);
			if(index >= filesList.length) {
				filesList.push(file);
			} else {
				filesList.splice(index, 0, file);
			}
			filesDict[name] = file;
			return file;
		}

		/**
		 * Removes a file at a specified index from the ZIP archive.
		 * 
		 * @param index The index
		 * @return A reference to the removed FZipFile object
		 */				
		public function removeFileAt(index:uint):FZipFile {
			if(filesList != null && filesDict != null && index < filesList.length) {
				var file:FZipFile = filesList[index] as FZipFile;
				if(file != null) {
					filesList.splice(index, 1);
					delete filesDict[file.filename];
					return file;
				}
			}
			return null;
		}

		/**
		 * @private
		 */		
		protected function parse(stream:IDataInput):Boolean {
			while (parseFunc(stream)){};
			return (parseFunc === parseIdle);
		}

		/**
		 * @private
		 */		
		private function parseIdle(stream:IDataInput):Boolean {
			return false;
		}
		
		/**
		 * @private
		 */		
		private function parseSignature(stream:IDataInput):Boolean {
			if(stream.bytesAvailable >= 4) {
				var sig:uint = stream.readUnsignedInt();
				switch(sig) {
					case 0x04034b50:
						parseFunc = parseLocalfile;
						currentFile = new FZipFile(charEncoding);
						break;
					case 0x02014b50:
					case 0x06054b50:
						parseFunc = parseIdle;
						break;
					default:
						throw(new Error("Unknown record signature."));
						break;
				}
				return true;
			}
			return false;
		}

		/**
		 * @private
		 */		
		private function parseLocalfile(stream:IDataInput):Boolean {
			if(currentFile.parse(stream)) {
				filesList.push(currentFile);
				if (currentFile.filename) {
					filesDict[currentFile.filename] = currentFile;
				}
				dispatchEvent(new FZipEvent(FZipEvent.FILE_LOADED, currentFile));
				currentFile = null;
				if (parseFunc != parseIdle) {
					parseFunc = parseSignature;
					return true;
				}
			}
			return false;
		}
		
		/**
		 * @private
		 */		
		protected function progressHandler(evt:Event):void {
			dispatchEvent(evt.clone());
			try {
				if(parse(urlStream)) {
					close();
					dispatchEvent(new Event(Event.COMPLETE));
				}
			} catch(e:Error) {
				close();
				if(hasEventListener(FZipErrorEvent.PARSE_ERROR)) {
					dispatchEvent(new FZipErrorEvent(FZipErrorEvent.PARSE_ERROR, e.message));
				} else {
					throw(e);
				}
			}
		}
		
		/**
		 * @private
		 */		
		protected function defaultHandler(evt:Event):void {
			dispatchEvent(evt.clone());
		}
		
		/**
		 * @private
		 */		
		protected function defaultErrorHandler(evt:Event):void {
			close();
			dispatchEvent(evt.clone());
		}
		
		/**
		 * @private
		 */		
		protected function addEventHandlers():void {
			urlStream.addEventListener(Event.COMPLETE, defaultHandler);
			urlStream.addEventListener(Event.OPEN, defaultHandler);
			urlStream.addEventListener(HTTPStatusEvent.HTTP_STATUS, defaultHandler);
			urlStream.addEventListener(IOErrorEvent.IO_ERROR, defaultErrorHandler);
			urlStream.addEventListener(SecurityErrorEvent.SECURITY_ERROR, defaultErrorHandler);
			urlStream.addEventListener(ProgressEvent.PROGRESS, progressHandler);
		}
		
		/**
		 * @private
		 */		
		protected function removeEventHandlers():void {
			urlStream.removeEventListener(Event.COMPLETE, defaultHandler);
			urlStream.removeEventListener(Event.OPEN, defaultHandler);
			urlStream.removeEventListener(HTTPStatusEvent.HTTP_STATUS, defaultHandler);
			urlStream.removeEventListener(IOErrorEvent.IO_ERROR, defaultErrorHandler);
			urlStream.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, defaultErrorHandler);
			urlStream.removeEventListener(ProgressEvent.PROGRESS, progressHandler);
		}
	}
}