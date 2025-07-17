package devoron.components.decorators
{
	import flash.display.BitmapData;
	import flash.display.CapsStyle;
	import flash.display.DisplayObject;
	import flash.display.JointStyle;
	import flash.display.Sprite;
	import flash.geom.Rectangle;
	import org.aswing.ASColor;
	import org.aswing.Component;
	import org.aswing.geom.IntRectangle;
	import org.aswing.graphics.BitmapBrush;
	import org.aswing.graphics.Graphics2D;
	import org.aswing.graphics.Pen;
	import org.aswing.graphics.SolidBrush;
	import org.aswing.GroundDecorator;
	
	/**
	 * ColorDecorator
	 * @author Devoron
	 */
	public class ButtonGroupDecorator implements GroundDecorator
	{
		private var index:int;
		public var radius:Number;
		protected var topRightRadius:Number = -1;
		protected var bottomLeftRadius:Number = -1;
		protected var bottomRightRadius:Number = -1;
		public var color:ASColor;
		public var borderColor:ASColor;
		public var backgroundSprite:Sprite;
		public var comp:Component;
		public var graphics:Graphics2D;
		public var bounds:IntRectangle;
		public var rightGap:int;
		public var leftGap:int;
		public var topGap:int;
		public var bottomGap:int;
		public var image:BitmapData;
		protected var openingRect:Rectangle;
		protected var internalBorderColor:ASColor;
		
		public function ButtonGroupDecorator(color:ASColor, borderColor:ASColor = null, radius:Number = 0)
		{
			this.radius = radius;
			this.borderColor = borderColor ? borderColor : new ASColor(0, 0);
			this.color = color;
			backgroundSprite = new Sprite();
		}
		
		public function setOpeningRect(rectangle:Rectangle, internalBorderColor:ASColor = null):void
		{
			this.internalBorderColor = internalBorderColor;
			openingRect = rectangle;
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
		}
		
		public function setRadiuses(radius:Number, topRightRadius:Number = -1, bottomLeftRadius:Number = -1, bottomRightRadius:Number = -1):void
		{
			this.bottomRightRadius = bottomRightRadius;
			this.bottomLeftRadius = bottomLeftRadius;
			this.topRightRadius = topRightRadius;
			this.radius = radius;
		}
		
		/**
		 *[radius, topRightRadius, bottomLeftRadius, bottomRightRadius]
		 * @return [radius, topRightRadius, bottomLeftRadius, bottomRightRadius]
		 */
		public function getRadiuses():Array
		{
			return [radius, topRightRadius, bottomLeftRadius, bottomRightRadius];
		}
		
		public function setGaps(rightGap:int = 0, leftGap:int = 0, topGap:int = 0, bottomGap:int = 0):void
		{
			this.bottomGap = bottomGap;
			this.topGap = topGap;
			this.leftGap = leftGap;
			this.rightGap = rightGap;
		}
		
		/**
		 * [rightGap, leftGap, topGap, bottomGap]
		 * @return
		 */
		public function getGaps():Array
		{
			return [rightGap, leftGap, topGap, bottomGap];
		}
		
		public function clone():ButtonGroupDecorator
		{
			var decorator:ButtonGroupDecorator = new ButtonGroupDecorator(color, borderColor, radius);
			decorator.setGaps(rightGap, leftGap, topGap, bottomGap);
			if (image)
				decorator.setImage(image.clone());
			return decorator;
		}
		
		public function setImage(bd:BitmapData):void
		{
			image = bd;
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
		}
		
		public function getImage():BitmapData
		{
			return image;
		}
		
		public function set colorAlpha(value:Number):void {
			color = color.changeAlpha(value);
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
		}
		
		public function get colorAlpha():Number {
			return color.getAlpha();
			/*if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}*/
		}
		
		public function getColor():ASColor
		{
			return color;
		}
		
		public function setColor(value:ASColor):void
		{
			color = value;
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
		}
		
		public function getBorderColor():ASColor
		{
			return borderColor;
		}
		
		public function setBorderColor(value:ASColor):void
		{
			borderColor = value;
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
		}
		
		public function getInternalBorderColor():ASColor
		{
			return internalBorderColor;
		}
		
		public function getInternalRect():Rectangle
		{
			return openingRect;
		}
		
		public function setSelin(index:int):void {
			this.index = index;
			if (comp)
			{
				updateDecorator(comp, graphics, bounds);
					//c.updateUI();
			}
			
		}
		
		/* INTERFACE org.aswing.GroundDecorator */
		
		public function updateDecorator(c:Component, g:Graphics2D, b:IntRectangle):void
		{
			comp = c;
			graphics = g;
			bounds = b;
			backgroundSprite.graphics.clear();
			backgroundSprite.mouseChildren = true;
			backgroundSprite.mouseEnabled = false;
			var g2d:Graphics2D = new Graphics2D(backgroundSprite.graphics);
			
			if (!g2d)
			return;
			g.clear();
			//var shape:Shape = new Shape();
			//g.drawLine(new SolidBrush(new ASColor(0xFFFFFF, 0.44)), 0, 0, fullB.width, fullB.height);
			var pen:Pen = new Pen(new ASColor(0xFFFFFF, 0.14));
			//g.drawLine(pen, 0, 4, 54*10, 4);
			g.moveTo(0, 30);
			for (var i:int = 0; i < 11; i++)
			{
				//g.moveTo(i * 54 /*+ 2 * i*/ + 2, 4);
				g.drawLine(pen, i * 54 /*+ 2 * i*/ /*+ 4*/ /*+ 11*/, 4, i * 54  /*2 * i +*/ /*4 *//*+ 11*/,34);
					//g.drawLine(pen, 9 * 30+5, 0, tabBarBounds.width, tabBarBounds.height);
					//g.moveTo(9*30, tabBarBounds.height);
			}
			
			//g.drawLine(pen, 10 * 54-55, 4, 10 * 54-55,34);
			g.drawLine(pen, 10 * 54-55, 4, 10 * 54-55,34);
			//g.drawLine(pen, 11 * 54 /*+ 2 * i*/ /*+ 4*/ /*+ 11*/-22, 4, 11 * 54-2  /*2 * i +*/ /*4 *//*+ 11*/,34);
			//g.drawLine(pen, 0, 34, 54*10, 34);
			
			if(index>0){
			g.drawLine(pen, 0, 34, 54 * index, 34);
			
			g.drawLine(pen, 54 * (index+1)+1, 34, 54 * 10, 34); // +1px для скругления
			}
			
			return;
			
			
			if (image)
				g2d.beginFill(new BitmapBrush(image));
			else
				g2d.beginFill(new SolidBrush(color));
			
			if (radius != 0)
			{
				var trR:Number = topRightRadius == -1 ? radius : topRightRadius;
				var blR:Number = bottomLeftRadius == -1 ? radius : bottomLeftRadius;
				var brR:Number = bottomRightRadius == -1 ? radius : bottomRightRadius;
				
				if(borderColor){
				if(radius < 10)
				g2d.drawRoundRect(new Pen(borderColor, 0.25, true, "none", CapsStyle.ROUND, JointStyle.ROUND, 9), b.x + leftGap, b.y + topGap, b.width + rightGap, b.height + bottomGap, radius, trR, blR, brR-0.3);
				else
				g2d.drawCircle(new Pen(borderColor, 0), b.x + leftGap, b.y + topGap, /*b.width + rightGap, b.height + bottomGap,*/ radius);
				}
				
				if (openingRect)
					g2d.drawRectangle(new Pen((internalBorderColor || new ASColor(0, 0)), 0), openingRect.x, openingRect.y, openingRect.width, openingRect.height);
				
			}
			else
			{
				g2d.drawRectangle(new Pen(borderColor, 0), b.x + leftGap, b.y + topGap, b.width + rightGap, b.height + bottomGap);
				if (openingRect)
					g2d.drawRectangle(new Pen((internalBorderColor || new ASColor(0, 0)), 0), openingRect.x, openingRect.y, openingRect.width, openingRect.height);
			}
			
			g2d.endDraw();
			g2d.endFill();
		}
		
		public function getDisplay(c:Component):DisplayObject
		{
			return backgroundSprite;
		}
	
	}

}