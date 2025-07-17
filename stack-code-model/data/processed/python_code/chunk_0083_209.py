package devoron.components.filechooser.workerspectrum
{
	import flash.display.BitmapData;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.events.TimerEvent;
	import flash.media.Sound;
	import flash.system.MessageChannel;
	import flash.system.Worker;
	import flash.utils.ByteArray;
	import flash.utils.CompressionAlgorithm;
	import flash.utils.Timer;
	
	/**
	 * WorkerSpectrum.
	 * @author Devoron
	 */
	public class WorkerSpectrum extends Sprite
	{
		
		/** @private Канал связи "из фоновового воркера в основной" */
		private var backToMain:MessageChannel;
		/** @private Канал связи "из основного воркера в фоновый" */
		private var mainToBack:MessageChannel;
		private var bytes:ByteArray;
		private var sound:Sound;
		
		//private var objectsAndPaths:
		
		public function WorkerSpectrum()
		{
			super();
			
			// создаём каналы связи по тем же самым ключам, что и классе Main
			backToMain = Worker.current.getSharedProperty("backToMainChannel");
			mainToBack = Worker.current.getSharedProperty("mainToBackChannel");
			
			//добавить слушатель на получение данных из основного воркера
			mainToBack.addEventListener(Event.CHANNEL_MESSAGE, mainWorkerAudioDataHandler);
		}
		
		private var path:String;
		
		/**
		 * Обработчик получения команды на вычисление спектра.
		 * @param	e
		 */
		private function mainWorkerAudioDataHandler(e:Event):void
		{
			var result:* = mainToBack.receive();
			path = String(result);
			bytes = Worker.current.getSharedProperty("bytes");
			
			if (bytes)
			{
				sound = new Sound();
				//sound.addEventListener(Event.COMPLETE, onSoundComplete);
				sound.loadCompressedDataFromByteArray(bytes, bytes.length);
				createImage(bytes);
			}
		}
		
		private function onSoundComplete(e:Event):void
		{
			
			//backToMain.send("в рот мне ноги");
			createImage(bytes);
		}
		
		private function createImage(bytes:ByteArray):void
		{
			var bd:BitmapData = new BitmapData(197, 100);
			bd.lock();
			var length:Number = bytes.length;
			
			sound.extract(bytes, length, 0);
			
			var w:uint = 197;
			var h:uint = 100;
			
			var inc:Number = w / (length / 200);
			var n:Number = 0;
			bytes.position = 0;
			var i:int = 0;
			var xpos:Number = 0;
			
			var spectrum:Sprite = new Sprite();
			var g:Graphics = spectrum.graphics;
			g.lineStyle(1, 0xFF0000, 1);
			//g.lineStyle(1, 0xFFFFFF, .1);
			g.moveTo(0, h * .5);
			
			//spectrumGraphics.
			
			var pos:uint = 0;
			var l:uint = bytes.length;
			var halfH:Number = h * .5;
			
			while (pos < l)
			{
				bytes.position = pos;
				n = (bytes.readFloat() + bytes.readFloat()) * .5;
				
				g.lineTo(xpos, halfH + halfH * n);
				
				//bd.fillRect(new Rectangle(xpos, halfH + halfH * n, 1, 1), 0x000000);
				
				xpos += inc;
				pos += 1600;
			}
			
			bytes.position = 0;
			
			bd.unlock();
			
			/*	var sp:Sprite = new Sprite();
			   sp.graphics.beginFill(0x008080);
			   sp.graphics.drawRect(0, 0, 197, 100);
			 sp.graphics.endFill();*/
			
			bd.draw(spectrum);
			
			var ba:ByteArray = new ByteArray();
			bd.copyPixelsToByteArray(bd.rect, ba);
			
			backToMain.send(path);
			backToMain.send(ba);
			//onDecode(bd);
		}
	
	}

}