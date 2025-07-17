package org.aswing.dnd
{
	import org.aswing.values.ASColor;
	import starling.display.DisplayObject;
	import starling.display.MovieClip;
	import starling.display.Sprite;
	
	/*
	   Copyright aswing.org, see the LICENCE.txt.
	 */
	
	import flash.display.Bitmap;
	import flash.display.BitmapData;
	import flash.geom.Matrix;
	import flash.text.TextField;
	import org.aswing.Component;
	import org.aswing.dnd.DraggingImage;
	import org.aswing.JLabel;
	//import org.aswing.ElementCreater;
	import org.aswing.graphics.Pen;
	import org.aswing.JList;
	
	/**
	 * @author iiley
	 */
	public class ListDragImage implements DraggingImage
	{
		private var list:JList;
		private var textField:TextField;
		private var width:Number;
		private var height:Number;
		private var target:MovieClip;
		private var number:Number;
		private var x:Number;
		private var y:Number;
		
		private var image:Bitmap;
		
		public function ListDragImage(list:JList, offsetY:Number, selectedIndices:Array)
		{
			
			/*height = list.getCellFactory().getCellHeight();
			   if (height == 0)
			   {
			   height = 18;
			   }
			   width = list.getInsets().getInsideSize(list.getSize()).width - 10;
			   number = list.getSelectedIndices().length;
			   x = 0;
			   y = offsetY;
			
			   for (var i:int = firstIndex; i <= lastIndex; i++)
			   {
			   ib = (getCellByIndex(i).getCellComponent()).getBounds(this);
			   if (mp.y < ib.y + ib.height)
			   {
			   offsetY = ib.y;
			   break;
			   }
			   }
			 */
			//trace(" offsetY " + offsetY);
			
			var com:Component;
			var cellBd:BitmapData;
			//var cellBds:Vector.<BitmapData> = new Vector.<BitmapData>();
			/*for each (var selId:uint in selectedIndices)
			   {
			   com = (list.getCellByIndex(selId)).getCellComponent();
			   cellBd = new BitmapData(com.getWidth(), com.getHeight(), true, 0x0);
			   //var m:Matrix = new Matrix(0,0,0,0,0,
			   cellBd.draw(com, null, null, null, null, true);
			   cellBds.push(cellBd);
			 }*/
			
			var summHeigth:uint = 0;
			var maxWidth:uint = 0;
			var selId:uint = 0;
			for each (selId in selectedIndices)
			{
				com = (list.getCellByIndex(selId)).getCellComponent();
				summHeigth += com.getHeight();
				
				maxWidth = maxWidth < com.getWidth() ? com.getWidth() : maxWidth;
			}
			
			var mat:Matrix = new Matrix();
			var imageBd:BitmapData = new BitmapData(maxWidth, summHeigth, true, 0x0);
			trace("maxWidh " + maxWidth + " summ " + summHeigth);
			var tx:uint = 0;
			var ty:uint = 0;
			selId = 0;
			for each (selId in selectedIndices)
			{
				com = (list.getCellByIndex(selId)).getCellComponent();
				imageBd.draw(com, mat);
				//tx += com.getWidth();
				ty += com.getHeight();
				mat.translate(0, ty);
			}
			
			image = new Bitmap(imageBd, "auto", true);
			image.y += offsetY;
		
		}
		
		public function setCanvas(target:MovieClip):void
		{
			this.target = target;
			//textField.removeTextField();
			//textField = ElementCreater.getInstance().createTF(target, "n_of_draging_text");
		}
		
		public function switchToAcceptImage():void
		{
			//target.clear();
			//drawItems(new Graphics(target), true);
		}
		
		public function switchToRejectImage():void
		{
			//target.clear();
			//drawItems(new Graphics(target), false);
		}
		
		/* INTERFACE devoron.aswing3d.dnd.DraggingImage */
		
		public function getDisplay():DisplayObject
		{
			/*var r:Sprite = new Sprite();
			   r.graphics.beginFill(0x000000);
			   r.graphics.drawRect(0, 0, 100, 100);
			   r.graphics.endFill();
			
			 return r;*/
			return image;
		}
	
	/*private function drawItems(g:Graphics, allow:Boolean):void
	   {
	   var w:Number = width;
	   var h:Number = height;
	   var r:Number = Math.min(w, h) - 2;
	
	   if (!allow)
	   {
	   g.drawLine(new Pen(ASColor.RED, 2), x + 1, y + 1, x + 1 + r, y + 1 + r);
	   g.drawLine(new Pen(ASColor.RED, 2), x + 1 + r, y + 1, x + 1, y + 1 + r);
	   }
	   textField.visible = false;
	   if (number > 1)
	   {
	   if (number > 2)
	   {
	   g.drawRectangle(new Pen(ASColor.GRAY), x + 4, y + 4, w - 3, h - 2);
	   textField.visible = true;
	   textField.x = x + width + 2;
	   textField.y = y;
	   textField.text = (number + "");
	   }
	   g.drawRectangle(new Pen(ASColor.GRAY), x + 2, y + 2, w - 1, h - 1);
	   }
	   g.drawRectangle(new Pen(ASColor.GRAY), x, y, w, h);
	 }*/
	}
}