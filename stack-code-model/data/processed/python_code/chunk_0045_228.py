package vyperlogix.shapes {
	import com.GUID;
	import com.VectorUtils;
	
	import flash.geom.Point;

	public class DrawingHandle extends Object {
		public var id:String;
		public var callback:Function;
		public var verticies:Array = [];
		public var lineSegments:Array = [];

		public var leastPt:Point;
		public var mostPt:Point;
		
		public static const PRECISION:int = 5;
		
		private static var _schema_:Array = [
			[1,2], // Between Segment 2 and 3 is the upper arm.
			[3,4], // Between Segment 4 and 5 is the left arm.
			[5,6], // Between Segment 6 and 7 is the lower left arm.
			[7,8], // Between Segment 8 and 9 is the lower right arm.
			[9,0] // Between Segment 10 and 1 is the right arm.
		];
		
		public function DrawingHandle() {
			super();
			this.id = GUID.create();
			this.leastPt = new Point(2^31,2^31);
			this.mostPt = new Point(-(2^31),-(2^31));
		}

		public function init_verticies():void {
			while (this.verticies.length > 0) {
				this.verticies.pop();
			}
		}
		
		public function get segment_schema():Array {
			return DrawingHandle._schema_;
		}
		
		public function get segments_for_schema():Array {
			var aSeg:Array;
			var segments:Array = [];
			for (var i:int = 0; i < this.segment_schema.length; i++) {
				aSeg = this.segment_schema[i];
				segments.push([this.lineSegments[aSeg[0]],this.lineSegments[aSeg[aSeg.length-1]]]);
			}
			return segments;
		}

		private function gather_lineSegments():void {
			var i:String;
			var aPtFrom:Point;
			var aPtTo:Point;
			var iFrom:int;
			var iTo:int;
			var iMax:int = this.verticies.length - 1;
			for (i in this.verticies) {
				iFrom = int(i);
				iTo = (iFrom == iMax) ? 0 : iFrom + 1;
				aPtFrom = this.verticies[iFrom];
				aPtTo = this.verticies[iTo];
				if ( (aPtFrom.x != aPtTo.x) && (aPtFrom.y != aPtTo.y) ) {
					this.lineSegments.push({'label':'Segment '+(int(i)+1),'points':{'from':aPtFrom,'to':aPtTo}});
				}
			}
		}
		
		public function issue_callback(pt:*):void {
			var aPt:Point;
			if (this.callback is Function) {
				try {
					if (pt != null) {
						aPt = VectorUtils.precision_to(pt,DrawingHandle.PRECISION);
						this.verticies.push(aPt);
					} else {
						this.verticies = this.verticies;
						this.leastPt = new Point(2^31,2^31);
						this.mostPt = new Point(-(2^31),-(2^31));
						var i:String;
						for (i in this.verticies) {
							aPt = this.verticies[i];
							if (aPt.x < this.leastPt.x) {
								this.leastPt.x = aPt.x;
							}
							if (aPt.y < this.leastPt.y) {
								this.leastPt.y = aPt.y;
							}
							if (aPt.x > this.mostPt.x) {
								this.mostPt.x = aPt.x;
							}
							if (aPt.y > this.mostPt.y) {
								this.mostPt.y = aPt.y;
							}
						}
						this.gather_lineSegments();
					}
					this.callback(this,pt);
				} catch (err:Error) {
					trace('DrawingHandle.issue_callback().Error '+err.toString()+'\n'+err.getStackTrace());
				}
			}
		}
	}
}