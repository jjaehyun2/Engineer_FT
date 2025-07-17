package utils {
	import com.DebuggerUtils;
	import com.Math2D;
	
	import flash.geom.Point;
	
	import vyperlogix.shapes.DrawingHandle;

	public class ImageHelper {
		private static var expansion_counter:int = 0;
		
		private static const PROXIMITY:int = 5;

		public static const STAGE_SIZING:int = 1;
		public static const STAGE_PLACEMENT:int = 2;
		public static const STAGE_STOPPING:int = 3;
		
		public static var current_stage:int = ImageHelper.STAGE_SIZING;

		public static var static_stage:Boolean = false;
		
		public static var placement_deltas:Array = [];
		
		public static function reset_counter():void {
			ImageHelper.expansion_counter = 0;
		}
		
		public static function report_current_stage():String {
			return (ImageHelper.current_stage == ImageHelper.STAGE_SIZING) ? 'STAGE_SIZING' : 
				((ImageHelper.current_stage == ImageHelper.STAGE_PLACEMENT) ? 'STAGE_PLACEMENT' : 
					((ImageHelper.current_stage == ImageHelper.STAGE_STOPPING) ? 'STAGE_STOPPING' : 'UNKNOWN_STAGE'));
		}
		
		public static function are_all_expected_points_touching_borders(star:*,handle:DrawingHandle):Boolean {
			// How many outer points are there and are they all touching ?
			if (handle is DrawingHandle) {
				var i:String;
				var aPt:Point;
				var w:Number = star.width;
				var h:Number = star.height;
				var ww:Number = w-5;
				var hh:Number = h-5;
				var count:int = 0;
				for (i in handle.verticies) {
					aPt = handle.verticies[i];
					if ( (aPt.x >= ww) || (aPt.y >= hh) || (aPt.x <= 0) ) {
						count += 1;
					}
				}
				return (count != handle.points);
			}
			return false;
		}
		
		private static function draw_and_adjust(star:*):void {
			try {
				if (star.isAdjustable) {
					star.is_ignoring_drawing = true;
					star.draw_star();
					star.is_ignoring_drawing = false;
				}
			} catch (err:Error) {trace(DebuggerUtils.getFunctionName(err)+'.ERROR '+err.toString());}
		}
		
		public static function adjust_image(star:*,handle:DrawingHandle):void {
			var isDirty:Boolean = false;
			var wasValue:Number;
			if ( ( (!ImageHelper.static_stage) && (ImageHelper.current_stage >= ImageHelper.STAGE_SIZING) && (ImageHelper.current_stage <= ImageHelper.STAGE_PLACEMENT) ) || ( (ImageHelper.static_stage) && (ImageHelper.current_stage == ImageHelper.STAGE_SIZING) ) ) {
				trace(DebuggerUtils.getFunctionName(new Error())+'.1 --> handle.mostPt.x='+handle.mostPt.x+', star.container.width='+star.container.width+', handle.mostPt.y='+handle.mostPt.y+', star.container.height='+star.container.height);
				if ( (handle.mostPt.x < (star.container.width-5)) && (handle.mostPt.y < (star.container.height-5)) ) {
					wasValue = star.outerRadius;
					star.outerRadius += 0.5;
					star.innerRadius = star.innerOuterRatio * star.outerRadius;
					ImageHelper.expansion_counter += 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.2 (GROW) --> star.outerRadius (was)='+wasValue+', star.outerRadius (is)='+star.outerRadius+', ImageHelper.expansion_counter='+ImageHelper.expansion_counter);
					isDirty = (ImageHelper.expansion_counter != 0);
				} else if ( (handle.mostPt.x > (star.container.width+5)) || (handle.mostPt.y > (star.container.height-5)) ) {
					wasValue = star.outerRadius;
					star.outerRadius -= 0.5;
					star.innerRadius = star.innerOuterRatio * star.outerRadius;
					ImageHelper.expansion_counter -= 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.3 --> (SHRINK) star.outerRadius (was)='+wasValue+', star.outerRadius (is)='+star.outerRadius+', ImageHelper.expansion_counter='+ImageHelper.expansion_counter);
					isDirty = (ImageHelper.expansion_counter != 0);
				}
			}
			if ( (isDirty) || ( (ImageHelper.current_stage > ImageHelper.STAGE_SIZING) && (ImageHelper.current_stage <= ImageHelper.STAGE_PLACEMENT) ) ) {
				ImageHelper.placement_deltas.push(new Point(star.xPos,star.yPos));
				trace(DebuggerUtils.getFunctionName(new Error())+'.4 --> handle.leastPt.x='+handle.leastPt.x);
				if (handle.leastPt.x < 0) {
					wasValue = star.xPos;
					star.xPos += 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.5 --> star.xPos (was)='+wasValue+', star.xPos (is)='+star.xPos);
				} else if (handle.leastPt.x > 0) {
					wasValue = star.xPos;
					star.xPos -= 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.6 --> star.xPos (was)='+wasValue+', star.xPos (is)='+star.xPos);
				}
				trace(DebuggerUtils.getFunctionName(new Error())+'.7 --> handle.leastPt.y='+handle.leastPt.y);
				if (handle.leastPt.y < 0) {
					wasValue = star.yPos;
					star.yPos += 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.8 --> star.yPos (was)='+wasValue+', star.yPos (is)='+star.yPos);
				} else if (handle.leastPt.y < 0) {
					wasValue = star.yPos;
					star.yPos -= 1;
					trace(DebuggerUtils.getFunctionName(new Error())+'.9 --> star.yPos (was)='+wasValue+', star.yPos (is)='+star.yPos);
				}
				var originPt:Point = ImageHelper.placement_deltas.pop() as Point;
				var currentPt:Point = new Point(star.xPos,star.yPos);
				var dist:Number = Math2D.FindDistance(originPt,currentPt);
				trace(DebuggerUtils.getFunctionName(new Error())+'.9.1 --> originPte='+originPt.toString()+', currentPt='+currentPt.toString()+', dist='+dist.toPrecision(2));
				if (dist < 5) {
					ImageHelper.static_stage = true;
					ImageHelper.current_stage = ImageHelper.STAGE_STOPPING;
				}
				trace(DebuggerUtils.getFunctionName(new Error())+'.10 --> ImageHelper.current_stage='+ImageHelper.report_current_stage());
				if ( (true) && ( (Math.abs(handle.leastPt.y) <= 5) && ((Math.max(star.container.height,handle.mostPt.y) - Math.min(star.container.height,handle.mostPt.y)) <= 5) ) ) {
					if (!ImageHelper.static_stage) {
						ImageHelper.current_stage++;
					}
					if (ImageHelper.current_stage == ImageHelper.STAGE_STOPPING) {
						trace(DebuggerUtils.getFunctionName(new Error())+'.11 --> (STOPPING) !!!');
						isDirty = false;
					} else {
						trace(DebuggerUtils.getFunctionName(new Error())+'.12 --> (CONTINUE) !!!');
						isDirty = ImageHelper.are_all_expected_points_touching_borders(star,handle);
						if (isDirty) {
							if (handle.leastPt.x < 0) {
								wasValue = star.xPos;
								star.xPos += Math.abs(handle.leastPt.x/4);
								trace(DebuggerUtils.getFunctionName(new Error())+'.12a --> star.xPos (was)='+wasValue+', star.xPos (is)='+star.xPos);
							}
							//star.callLater(ImageHelper.draw_and_adjust,[star]);
						}
						isDirty = true;
					}
				} else {
					star.callLater(ImageHelper.draw_and_adjust,[star]);
					trace(DebuggerUtils.getFunctionName(new Error())+'.13 --> (DRAW_AND_ADJUST) !!!');
					isDirty = false;
				}
			} else {
				if (false) {
					isDirty = ImageHelper.are_all_expected_points_touching_borders(star,handle);
					trace(DebuggerUtils.getFunctionName(new Error())+'.14 --> (DETERMINE) isDirty='+isDirty);
					if (isDirty) {
						star.angle += 0.5
						trace(DebuggerUtils.getFunctionName(new Error())+'.15 --> (DRAW_AND_ADJUST) !!!');
						star.callLater(ImageHelper.draw_and_adjust,[star]);
					}
				}
				if (isDirty) {
					trace(DebuggerUtils.getFunctionName(new Error())+'.16 --> (STOPPING) !!!');
					isDirty = false;
				}
			}
		}
		
	}
}