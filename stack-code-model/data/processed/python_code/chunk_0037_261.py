package com.illuzor.engine3d.net {
	
	import alternativa.engine3d.loaders.Parser3DS;
	import alternativa.engine3d.loaders.ParserA3D;
	import alternativa.engine3d.loaders.ParserCollada;
	import alternativa.engine3d.materials.TextureMaterial;
	import alternativa.engine3d.objects.Mesh;
	import alternativa.engine3d.resources.BitmapTextureResource;
	import com.illuzor.engine3d.notifications.NotificationManager;
	import com.illuzor.engine3d.notifications.WindowType;
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.display.Loader;
	import flash.events.Event;
	import flash.events.IOErrorEvent;
	import flash.events.ProgressEvent;
	import flash.events.SecurityErrorEvent;
	import flash.net.URLLoader;
	import flash.net.URLLoaderDataFormat;
	import flash.net.URLRequest;
	
	/**
	 * Функции для загрузки внешних данных:
	 *  - Загрузка модели и текстуры;
	 *  - Загрузка xml файла.
	 * 
	 * @author illuzor  //  illuzor@gmail.com  //  illuzor.com
	 */
	
	public class DataLoader {
		/** @private путь для загрузки текстуры. Если "null", путь пустой */
		static private var textureURL:String;
		/** @private загрузчик текстуры*/
		static private var textureLoader:Loader;
		/** @private трёхмерная модель из внешнего файла */
		static private var mesh:Mesh;
		/** @private ссылка функцию для приёма модели */
		static private var sendModel:Function;
		/** @private ссылка функцию для приёма xml */
		static private var sendXML:Function;
		static private var typeOfModel:String;
		/**
		 * Функция для загрузки модели
		 * 
		 * @param	getter ссылка функцию для приёма модели
		 * @param	modelPath путь для загрузки файла модели
		 * @param	texturePath путь для загрузки текстуры. Если "null", путь пустой
		 */
		static public function LoadModel(getter:Function, modelType:String, modelPath:String, texturePath:String = "null"):void {
			sendModel = getter;
			textureURL = texturePath;
			typeOfModel = modelType;
			
			NotificationManager.addLoaderWindow(WindowType.LOADING_MODEL);
			
			var modelLoader:URLLoader = new URLLoader();
			modelLoader.dataFormat = URLLoaderDataFormat.BINARY;
			modelLoader.load(new URLRequest(modelPath));
			modelLoader.addEventListener(Event.COMPLETE, modelLoaded);
			modelLoader.addEventListener(ProgressEvent.PROGRESS, modelLoadingProgress);
		}
		/**
		 * @private Процесс загрузки текстуры. Обновление окна.
		 * 
		 * @param	e событие прогресса загрузки модели
		 */
		static private function modelLoadingProgress(e:ProgressEvent):void {
			NotificationManager.updateLoaderWindow(WindowType.LOADING_MODEL, e.bytesLoaded/e.bytesTotal);
		}
		/**
		 * @private выполняется после загрузки модели.
		 * Если есть текстура, грузим её, если нет, отдаём модель.
		 * 
		 * @param	e событие окончания загрузки модели
		 */
		static private function modelLoaded(e:Event):void {
			e.target.removeEventListener(Event.COMPLETE, modelLoaded);
			e.target.removeEventListener(ProgressEvent.PROGRESS, modelLoadingProgress);
			
			
			switch (typeOfModel) {
				case "3ds":;
					var parser3ds:Parser3DS = new Parser3DS();
					parser3ds.parse((e.target as URLLoader).data); // парсим загруженный файл

					mesh = parser3ds.objects[0] as Mesh; // вытаскиваем модель из парсера
					parser3ds = null;
				break;
				
				case "a3d":
					var parserA3d:ParserA3D = new ParserA3D();
					parserA3d.parse((e.target as URLLoader).data);
					
					trace(parserA3d.objects)
					
					mesh = parserA3d.objects[6] as Mesh; // вытаскиваем модель из парсера
					parserA3d = null;
				break;
				
				case "dae":
					var parserDae:ParserCollada = new ParserCollada();
					parserDae.parse(new XML(e.target.data));
					
					mesh = parserDae.objects[0] as Mesh; // вытаскиваем модель из парсера
					parserDae = null;
				break;
				default:
			}
			/*if (typeOfModel == "3ds") {
				
			} else if ()*/
			
			
			
			if (textureURL != "null") {
				loadTexture();
			} else {
				sendModel(mesh);
				NotificationManager.removeLoaderWindow();
			}
			
		}
		/**
		 * @private загрузка текстуры
		 */
		static private function loadTexture():void {
			NotificationManager.addLoaderWindow(WindowType.LOADING_TEXTURE);
			
			textureLoader = new Loader();
			textureLoader.load(new URLRequest(textureURL));
			textureLoader.contentLoaderInfo.addEventListener(Event.COMPLETE, textureLoaded);
			textureLoader.contentLoaderInfo.addEventListener(ProgressEvent.PROGRESS, textureLoadingProgress);
		}
		/**
		 * @private Процесс загрузки текстуры. Обновление окна.
		 * 
		 * @param	e событие прогресса загрузки текстуры
		 */
		static private function textureLoadingProgress(e:ProgressEvent):void {
			NotificationManager.updateLoaderWindow(WindowType.LOADING_TEXTURE, e.bytesLoaded/e.bytesTotal);
		}
		/**
		 * @private текстура загружена. Отдаём модель
		 * 
		 * @param	e событие окончания загрузки текстуры.
		 */
		static private function textureLoaded(e:Event):void {
			textureLoader.contentLoaderInfo.removeEventListener(Event.COMPLETE, textureLoaded);
			textureLoader.contentLoaderInfo.removeEventListener(ProgressEvent.PROGRESS, textureLoadingProgress);
			var bitmapData:BitmapData = (e.target.content as Bitmap).bitmapData;
			mesh.setMaterialToAllSurfaces(new TextureMaterial(new BitmapTextureResource(bitmapData)));
			sendModel(mesh);
			NotificationManager.removeLoaderWindow();
		}
		/**
		 * Загрузка xml
		 * 
		 * @param	path путь к xml
		 * @param	successFunction функция получения xml. В параметр передаётся xml
		 */
		static public function loadXML(path:String, successFunction:Function):void {
			sendXML = successFunction;
			
			var xmlLoader:URLLoader = new URLLoader();
			xmlLoader.load(new URLRequest(path));
			xmlLoader.addEventListener(Event.COMPLETE, xmlLoaded);
			xmlLoader.addEventListener(IOErrorEvent.IO_ERROR, ioLoadingError);
			xmlLoader.addEventListener(SecurityErrorEvent.SECURITY_ERROR, securityLoadingError);
		}
		/**
		 * @private xml загружен корректно, отдаём его
		 * 
		 * @param	e событие окончания загрузки xml файла
		 */
		static private function xmlLoaded(e:Event):void { //  xml загружен корректно
			e.target.removeEventListener(Event.COMPLETE, xmlLoaded);
			e.target.removeEventListener(IOErrorEvent.IO_ERROR, ioLoadingError);
			e.target.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, securityLoadingError);
			sendXML(new XML(e.target.data));
		}
		/**
		 * @private ошибка ввода-вывода загрузки xml
		 * 
		 * @param	e событие ошибки ввода-вывода
		 */
		static private function ioLoadingError(e:IOErrorEvent):void { // не удалось загрузить xml
			e.target.removeEventListener(Event.COMPLETE, xmlLoaded);
			e.target.removeEventListener(IOErrorEvent.IO_ERROR, ioLoadingError);
			e.target.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, securityLoadingError);
			trace("XML Loading IO Error")
		}
		/**
		 * @private ошибка безопасности загрузки xml
		 * 
		 * @param	e событие ошибки безопасности
		 */
		static private function securityLoadingError(e:SecurityErrorEvent):void {
			e.target.removeEventListener(Event.COMPLETE, xmlLoaded);
			e.target.removeEventListener(IOErrorEvent.IO_ERROR, ioLoadingError);
			e.target.removeEventListener(SecurityErrorEvent.SECURITY_ERROR, securityLoadingError);
			trace("XML Loading security Error")
		}
		
	}
}