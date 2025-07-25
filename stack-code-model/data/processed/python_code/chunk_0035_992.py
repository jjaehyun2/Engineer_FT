/*
* Copyright 2007-2012 the original author or authors.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/
package org.as3commons.zip {
	import flash.events.*;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Loader;
	import flash.utils.ByteArray;

	/**
	 * Dispatched when all pending files have been processed.
	 *
	 * @eventType flash.events.Event.COMPLETE
	 */
	[Event(name="complete", type="flash.events.Event")]

	/**
	 * <p>ZipLibrary works with a Zip instance to load files as
	 * usable instances, like a DisplayObject or BitmapData. Each file
	 * from a loaded zip is processed based on their file extensions.
	 * More than one Zip instance can be supplied, and if it is
	 * currently loading files, then ZipLibrary will wait for incoming
	 * files before it completes.</p>
	 *
	 * <p>Flash's built-in Loader class is used to convert formats, so the
	 * only formats currently supported are ones that Loader supports.
	 * As of this writing they are SWF, JPEG, GIF, and PNG.</p>
	 *
	 * <p>The following example loads an external zip file, outputs the
	 * width and height of an image and then loads a sound from a SWF file.</p>
	 *
	 * <pre>
	 * package {
	 * 	import flash.events.*;
	 * 	import flash.display.BitmapData;
	 * 	import org.as3commons.zip.Zip;
	 * 	import org.as3commons.org.ZipLibrary;
	 *
	 * 	public class Example {
	 * 		private var lib:ZipLibrary;
	 *
	 * 		public function Example(url:String) {
	 * 			lib = new ZipLibrary();
	 * 			lib.formatAsBitmapData(".gif");
	 * 			lib.formatAsBitmapData(".jpg");
	 * 			lib.formatAsBitmapData(".png");
	 * 			lib.formatAsDisplayObject(".swf");
	 * 			lib.addEventListener(Event.COMPLETE,onLoad);
	 *
	 * 			var zip:Zip = new Zip();
	 * 			zip.load(url);
	 * 			lib.addZip(zip);
	 * 		}
	 * 		private function onLoad(evt:Event) {
	 * 			var image:BitmapData = lib.getBitmapData("test.png");
	 * 			trace("Size: " + image.width + "x" + image.height);
	 *
	 * 			var importedSound:Class = lib.getDefinition("data.swf", "SoundClass") as Class;
	 * 			var snd:Sound = new importedSound() as Sound;
	 * 		}
	 * 	}
	 * }</pre>
	 *
	 * @see http://livedocs.macromedia.com/flex/201/langref/flash/display/Loader.html
	 *
	 * @author Claus Wahlers
	 * @author Max Herkender
	 */
	public class ZipLibrary extends EventDispatcher implements IZipLibrary {
		static private const FORMAT_BITMAPDATA:uint = (1 << 0);
		static private const FORMAT_DISPLAYOBJECT:uint = (1 << 1);

		private var pendingFiles:Array = [];
		private var pendingZips:Array = [];
		private var currentState:uint = 0;
		private var currentFilename:String;
		private var currentZip:Zip;
		private var currentLoader:Loader;

		private var bitmapDataFormat:RegExp = /[]/;
		private var displayObjectFormat:RegExp = /[]/;
		private var bitmapDataList:Object = {};
		private var displayObjectList:Object = {};

		/**
		 * Constructor
		 */
		public function ZipLibrary() {
			super();
		}

		/**
		 * Use this method to add an Zip instance to the processing queue.
		 * If the Zip instance specified is not active (currently receiving files)
		 * when it is processed than only the files already loaded will be processed.
		 *
		 * @param zip An Zip instance to process
		 */
		public function addZip(zip:IZip):void {
			pendingZips.unshift(zip);
			processNext();
		}

		/**
		 * Used to indicate a file extension that triggers formatting to BitmapData.
		 *
		 * @param ext A file extension (".jpg", ".png", etc)
		 */
		public function formatAsBitmapData(ext:String):void {
			bitmapDataFormat = addExtension(bitmapDataFormat, ext);
		}

		/**
		 * Used to indicate a file extension that triggers formatting to DisplayObject.
		 *
		 * @param ext A file extension (".swf", ".png", etc)
		 */
		public function formatAsDisplayObject(ext:String):void {
			displayObjectFormat = addExtension(displayObjectFormat, ext);
		}

		/**
		 * @private
		 */
		private function addExtension(original:RegExp, ext:String):RegExp {
			return new RegExp(ext.replace(/[^A-Za-z0-9]/, "\\$&") + "$|" + original.source);
		}

		/**
		 * Request a file that has been formatted as BitmapData.
		 * A ReferenceError is thrown if the file does not exist as a
		 * BitmapData.
		 *
		 * @param filename The filename of the BitmapData instance.
		 */
		public function getBitmapData(filename:String):BitmapData {
			if (!bitmapDataList[filename] is BitmapData) {
				throw new Error("File \"" + filename + "\" was not found as a BitmapData");
			}
			return bitmapDataList[filename] as BitmapData;
		}

		/**
		 * Request a file that has been formatted as a DisplayObject.
		 * A ReferenceError is thrown if the file does not exist as a
		 * DisplayObject.
		 *
		 * @param filename The filename of the DisplayObject instance.
		 */
		public function getDisplayObject(filename:String):DisplayObject {
			if (!displayObjectList.hasOwnProperty(filename)) {
				throw new ReferenceError("File \"" + filename + "\" was not found as a DisplayObject");
			}
			return displayObjectList[filename] as DisplayObject;
		}

		/**
		 * Retrieve a definition (like a class) from a SWF file that has
		 * been formatted as a DisplayObject.
		 * A ReferenceError is thrown if the file does not exist as a
		 * DisplayObject, or the definition does not exist.
		 *
		 * @param filename The filename of the DisplayObject instance.
		 */
		public function getDefinition(filename:String, definition:String):Object {
			if (!displayObjectList.hasOwnProperty(filename)) {
				throw new ReferenceError("File \"" + filename + "\" was not found as a DisplayObject, ");
			}
			var disp:DisplayObject = displayObjectList[filename] as DisplayObject;
			try {
				return disp.loaderInfo.applicationDomain.getDefinition(definition);
			} catch (e:ReferenceError) {
				throw new ReferenceError("Definition \"" + definition + "\" in file \"" + filename + "\" could not be retrieved: " + e.message);
			}
			return null;
		}

		/**
		 * @private
		 */
		private function processNext(evt:Event=null):void {
			while (currentState === 0) {
				if (pendingFiles.length > 0) {
					var nextFile:ZipFile = pendingFiles.pop();
					if (bitmapDataFormat.test(nextFile.filename)) {
						currentState |= FORMAT_BITMAPDATA;
					}
					if (displayObjectFormat.test(nextFile.filename)) {
						currentState |= FORMAT_DISPLAYOBJECT;
					}
					if ((currentState & (FORMAT_BITMAPDATA | FORMAT_DISPLAYOBJECT)) !== 0) {
						currentFilename = nextFile.filename;
						currentLoader = new Loader();
						currentLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, loaderCompleteHandler);
						currentLoader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, loaderCompleteHandler);
						var content:ByteArray = nextFile.content;
						content.position = 0;
						currentLoader.loadBytes(content);
						break;
					}
				} else if (currentZip == null) {
					if (pendingZips.length > 0) {
						currentZip = pendingZips.pop();
						var i:uint = currentZip.getFileCount();
						while (i > 0) {
							pendingFiles.push(currentZip.getFileAt(--i));
						}
						if (currentZip.active) {
							currentZip.addEventListener(Event.COMPLETE, zipCompleteHandler);
							currentZip.addEventListener(ZipEvent.FILE_LOADED, fileCompleteHandler);
							currentZip.addEventListener(ZipErrorEvent.PARSE_ERROR, zipCompleteHandler);
							break;
						} else {
							currentZip = null;
						}
					} else {
						dispatchEvent(new Event(Event.COMPLETE));
						break;
					}
				} else {
					break;
				}
			}
		}

		/**
		 * @private
		 */
		private function loaderCompleteHandler(evt:Event):void {
			if ((currentState & FORMAT_BITMAPDATA) === FORMAT_BITMAPDATA) {
				if (currentLoader.content is Bitmap && (currentLoader.content as Bitmap).bitmapData is BitmapData) {
					var bitmapData:BitmapData = (currentLoader.content as Bitmap).bitmapData;
					bitmapDataList[currentFilename] = bitmapData.clone();
						//trace(currentFilename+" -> BitmapData ("+bitmapData.width+"x"+bitmapData.height+")");
				} else if (currentLoader.content is DisplayObject) {
					var width:uint = uint(currentLoader.content.width);
					var height:uint = uint(currentLoader.content.height);
					if (width && height) {
						var bitmapData2:BitmapData = new BitmapData(width, height, true, 0x00000000);
						bitmapData2.draw(currentLoader);
						bitmapDataList[currentFilename] = bitmapData2;
							//trace(currentFilename+" -> BitmapData ("+bitmapData2.width+"x"+bitmapData2.height+")");
					} else {
						trace("File \"" + currentFilename + "\" could not be converted to BitmapData");
					}
				} else {
					trace("File \"" + currentFilename + "\" could not be converted to BitmapData");
				}
			}
			if ((currentState & FORMAT_DISPLAYOBJECT) === FORMAT_DISPLAYOBJECT) {
				if (currentLoader.content is DisplayObject) {
					//trace(currentFilename+" -> DisplayObject");
					displayObjectList[currentFilename] = currentLoader.content;
				} else {
					currentLoader.unload();
					trace("File \"" + currentFilename + "\" could not be loaded as a DisplayObject");
				}
			} else {
				currentLoader.unload();
			}
			currentLoader = null;
			currentFilename = "";
			currentState &= ~(FORMAT_BITMAPDATA | FORMAT_DISPLAYOBJECT);
			processNext();
		}

		/**
		 * @private
		 */
		private function fileCompleteHandler(evt:ZipEvent):void {
			pendingFiles.unshift(evt.file);
			processNext();
		}

		/**
		 * @private
		 */
		private function zipCompleteHandler(evt:Event):void {
			currentZip.removeEventListener(Event.COMPLETE, zipCompleteHandler);
			currentZip.removeEventListener(ZipEvent.FILE_LOADED, fileCompleteHandler);
			currentZip.removeEventListener(ZipErrorEvent.PARSE_ERROR, zipCompleteHandler);
			currentZip = null;
			processNext();
		}
	}
}