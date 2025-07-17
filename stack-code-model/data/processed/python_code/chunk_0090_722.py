package com.vini123.component.system
{
	import com.vini123.component.text.Label;
	import com.vini123.implement.IDestroy;
	
	import flash.display.CapsStyle;
	import flash.display.JointStyle;
	import flash.display.LineScaleMode;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.events.Event;
	import flash.system.System;
	import flash.utils.getTimer;
	
	public class FPSMonitor extends Sprite implements IDestroy
	{
		private var fpsWidth:int;
		private var fpsHeight:int;
		private var padding:int;
		
		private var fpsLabel:Label;
		private var memoryLabel:Label;
		private var fpsShape:Shape;
		private var memoryShape:Shape;
		
		private var fpsTime:int;
		
		private var curCount:int;
		private var curFps:Number;
		
		private var fpsColor:int = 0xff0000;
		private var memoryColor:int = 0xEE4DED;
		private const SHAPE_X_PADDING:int = 3;
		private const MAX_MEMORY:int = 1024 * 1024;
		
		private var fpsmDataList:Vector.<FPSMData>;
		
		/**
		 * 该项目正常的内存大小 （第一个公开的自定义属性，总共两个）
		 *  单位是M，默认是100M
		 */		
		public var wantMemory:int = 100;
		
		/**
		 * 监控频率 , 默认值是30（第二个公开的自定义属性，总共两个） 
		 */		
		public var frequency:int = 30;
			
		/**
		 * 
		 * @param fw 监控的宽度
		 * @param fh 监控的高度
		 * @param fp 文字距离左边，顶部的距离，默认是5px
		 *  默认是开启监控。start开启，stop结束，destroy卸载
		 * 
		 */		
		public function FPSMonitor(fw:int , fh:int , fp:int = 5)
		{
			fpsWidth = fw;
			fpsHeight = fh;
			padding = fp;
			
			visible = mouseChildren = false;
			addEventListener(Event.ADDED_TO_STAGE , addToStageHandler);
		}
		
		private function addToStageHandler(e:Event):void
		{
			removeEventListener(Event.ADDED_TO_STAGE , addToStageHandler);
			
			fpsLabel =  new Label("" , "微软雅黑" , 12 , fpsColor);
			addChild(fpsLabel);
			
			memoryLabel = new Label("" , "微软雅黑" , 12 , memoryColor);
			addChild(memoryLabel);
			
			fpsShape = new Shape();
			addChild(fpsShape);
			
			memoryShape = new Shape();
			addChild(memoryShape);
			
			fpsmDataList = new Vector.<FPSMData>();
			
			fps = stage.frameRate;
			memory = System.totalMemory;
			
			layout();
			
			start();
		}
		
		/**
		 * 启动FPS侦听渲染 
		 *  默认启动
		 */		
		public function start():void
		{
			if(!hasEventListener(Event.ENTER_FRAME))
			{
				addEventListener(Event.ENTER_FRAME , enterHandler);
			}
			
			fpsTime = getTimer();
		}
		
		/**
		 * 停止FPS侦听渲染 
		 * 
		 */		
		public function stop():void
		{
			if(hasEventListener(Event.ENTER_FRAME))
			{
				removeEventListener(Event.ENTER_FRAME , enterHandler);
			}
		}
		
		private function enterHandler(e:Event):void
		{
			curCount ++;
			memory = System.totalMemory;
			if(curCount >= frequency)
			{
				curCount = 0;
				curFps = (1000 * frequency/(getTimer() - fpsTime));
				fps = curFps;
				fpsTime = getTimer();
				
				fpsmDataList.push(new FPSMData(curFps , System.totalMemory));
				draw();
			}
		}
		
		private function layout():void
		{
			fpsLabel.x = memoryLabel.x = padding;
			memoryLabel.y = fpsLabel.y + fpsLabel.height;
		}
		
		private function set fps(value:Number):void
		{
			fpsLabel.text = "FPS: "  + value.toFixed(2);
		}
		
		private function set memory(value:uint):void
		{
			memoryLabel.text = "MEMORY: " + transformBytesToString(value);
		}
		
		private function transformBytesToString(value:uint):String  
		{ 
			var byteStr:String = "";  
			if (value < 1024) 
			{
				byteStr = String(value) + "b";  
			}  
			else if (value < 10240) 
			{  
				byteStr = Number(value / 1024).toFixed(2) + "kb"; 
			} 
			else if (value < 102400)  
			{  
				byteStr = Number(value / 1024).toFixed(1) + "kb";  
			} 
			else if (value < 1048576)    
			{ 
				byteStr = Math.round(value / 1024) + "kb";  
			}  
			else if (value < 10485760) 
			{ 
				byteStr = Number(value / 1048576).toFixed(2) + "mb"; 
			} 
			else if (value < 104857600) 
			{ 
				byteStr = Number(value / 1048576).toFixed(1) + "mb";  
			}  
			else
			{  
				byteStr = Math.round(value / 1048576) + "mb";  
			} 
			return byteStr;  
		} 
		
		private function draw():void
		{
			var maxLen:int = Math.round(fpsWidth/SHAPE_X_PADDING);
			if(fpsmDataList.length > maxLen)
			{
				fpsmDataList.shift();
			}
			var listLen:int = fpsmDataList.length;
			if(!listLen)return;
			
			var tempList:Vector.<FPSMData> = fpsmDataList.concat();
			var fpsmData:FPSMData = tempList.pop();
			fpsShape.graphics.clear();
			fpsShape.graphics.lineStyle(1 , fpsColor , 1 , true , LineScaleMode.NORMAL , CapsStyle.ROUND , JointStyle.ROUND , 3)
			fpsShape.graphics.moveTo(fpsWidth , fpsmData.fps * (fpsHeight/(2 * stage.frameRate)));
			
			memoryShape.graphics.clear();
			memoryShape.graphics.lineStyle(1 , memoryColor , 1 , true , LineScaleMode.NORMAL , CapsStyle.ROUND , JointStyle.ROUND , 3)
			memoryShape.graphics.moveTo(fpsWidth , fpsHeight - fpsmData.memory * (wantMemory/(fpsHeight * MAX_MEMORY)));
			
			while(tempList.length)
			{
				fpsmData = tempList.pop();
				var posX:int = fpsWidth - (listLen - tempList.length) * SHAPE_X_PADDING;
				var posY:int = int(fpsmData.fps * (fpsHeight/(2 * stage.frameRate)));
				fpsShape.graphics.lineTo(posX , posY);
				posY = fpsHeight - int(fpsmData.memory * (wantMemory/(fpsHeight * MAX_MEMORY)));
				memoryShape.graphics.lineTo(posX , posY);
			}
		}
		
		override public function get width():Number
		{
			return fpsWidth;
		}
		
		override public function get height():Number
		{
			return fpsHeight;
		}
		/**
		 * 销毁 
		 * 
		 */		
		public function destroy():void
		{
			stop();
			removeChildren();
			if(fpsLabel)
			{
				fpsLabel.destroy();
				fpsLabel = null;
			}
			
			if(memoryLabel)
			{
				memoryLabel.destroy();
				memoryLabel = null;
			}
			
			if(fpsShape)
			{
				fpsShape.graphics.clear();
				fpsShape = null;
			}
			
			if(memoryShape)
			{
				memoryShape.graphics.clear();
				memoryShape = null;
			}
		}
	}
}

class FPSMData
{
	public var fps:int;
	public var memory:int;
	
	public function FPSMData(fps:Number , memory:Number):void
	{	
		this.fps = int(fps);
		this.memory = int(memory);
	}
}