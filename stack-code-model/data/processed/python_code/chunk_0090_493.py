package devoron.components.multicontainers.timeline.components
{
	import devoron.studio.modificators.timeline.TimelineLabel;
	import devoron.studio.modificators.timeline.Track;
	import flash.display.BitmapData;
	import flash.display.DisplayObject;
	import flash.display.Graphics;
	import flash.display.Sprite;
	import flash.geom.Rectangle;
	import org.aswing.ASColor;
	import org.aswing.Component;
	import org.aswing.decorators.ColorDecorator;
	import org.aswing.ext.Form;
	import org.aswing.geom.IntRectangle;
	import org.aswing.graphics.BitmapBrush;
	import org.aswing.graphics.Graphics2D;
	import org.aswing.graphics.Pen;
	import org.aswing.graphics.SolidBrush;
	import org.aswing.GroundDecorator;
	import org.aswing.JList;
	
	/**
	 * TimelineSliderBackgroundDecorator
	 * @author Devoron
	 */
	public class TimelineSliderBackgroundDecorator extends ColorDecorator
	{
		private var labelsColor:ASColor;
		private var tracks:Array;
		private var tracksForm:JList;
		private var sp:Sprite;
		
		public function TimelineSliderBackgroundDecorator(color:ASColor, labelsColor:ASColor, borderColor:ASColor = null, radius:Number = 0)
		{
			super(color, borderColor, radius);
			this.labelsColor = labelsColor;
			
			sp = new Sprite();
			sp.y = 2;
		}
		
		public function update():void
		{
			// отрисовать карту timeline
			
			gtrace("b.width / 1880 " + bounds.width);
			var scale:Number = bounds.width / 1880;
			
			// draw labels
			var graphics:Graphics = sp.graphics;
			graphics.clear();
			
			for each (var track:Track in tracks)
			{
				//gtrace(track.getBounds(tracksForm));
				var labels:Array = track.getLabels();
				for each (var label:TimelineLabel in labels)
				{
					var labelBounds:Rectangle = label.getBounds(tracksForm);
					//labelBounds.
					//gtrace(labelBounds);
					//g2d.beginFill(new SolidBrush(labelsColor));
					//g2d.drawRectangle(new Pen(new ASColor(0,0), 0), labelBounds.x*scale, labelBounds.y*0.01/*scale*/, labelBounds.width*scale, 1/*labelBounds.height*scale*/);
					//g2d.endFill();
					//graphics.beginFill(0xFFFFFF, 0.4);
					
					graphics.lineStyle(1, 0xFFFFFF, 0.4);
					//graphics.drawRect(labelBounds.x, labelBounds.y, labelBounds.width, labelBounds.height);
					graphics.moveTo(labelBounds.x, labelBounds.y);
					graphics.lineTo(labelBounds.right, labelBounds.y);
					graphics.endFill();
				}
			}
			
			sp.width = bounds.width;
			sp.height = bounds.height;
			sp.height -= 4;
			
			if (!(sp in backgroundSprite))
			{
				backgroundSprite.addChild(sp);
			}
		
			//updateDecorator(comp, graphics, bounds);
		}
		
		/* INTERFACE org.aswing.GroundDecorator */
		
		public override function updateDecorator(c:Component, g:Graphics2D, b:IntRectangle):void
		{
			comp = c;
			graphics = g;
			bounds = b;
			gtrace("bounds " + bounds);
			backgroundSprite.graphics.clear();
			backgroundSprite.mouseChildren = true;
			backgroundSprite.mouseEnabled = false;
			
			var g2d:Graphics2D = new Graphics2D(backgroundSprite.graphics);
			
			// draw bg color on image
			if (image)
				g2d.beginFill(new BitmapBrush(image));
			else
				g2d.beginFill(new SolidBrush(color));
			
			if (radius != 0)
			{
				var trR:Number = topRightRadius == -1 ? radius : topRightRadius;
				var blR:Number = bottomLeftRadius == -1 ? radius : bottomLeftRadius;
				var brR:Number = bottomRightRadius == -1 ? radius : bottomRightRadius;
				g2d.drawRoundRect(new Pen(borderColor, 0), b.x + leftGap, b.y + topGap, b.width + rightGap, b.height + bottomGap, radius, trR, blR, brR);
				
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
		
		public function setTracks(tracks:Array):void
		{
			this.tracks = tracks;
		
		}
		
		public function setTracksForm(tracksForm:JList):void
		{
			this.tracksForm = tracksForm;
		}
	
	}

}