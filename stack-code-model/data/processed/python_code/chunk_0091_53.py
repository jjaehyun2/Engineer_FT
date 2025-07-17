package {
	
	import flash.display.MovieClip;
	import flash.geom.Point;
	import flash.geom.Rectangle;
	
	public class Triangle extends TerrainObject {
		
		public function Triangle() {
			// constructor code
			super();
		}
		
		override public function narrowCheckPoint(p:Point):Boolean {
			if (narrowRect.containsPoint(p)) {
				var m:Number = narrowRect.height / narrowRect.width;
				var distX:Number;
				var overSlope:Boolean;
				if (rotation == 0) {
					distX = p.x - narrowRect.left;
					overSlope = true;
				} else if (rotation == -90) {
					m *= -1;
					distX = p.x - narrowRect.right;
					overSlope = true;
				} else if (rotation == 180) {
					distX = p.x - narrowRect.left;
					overSlope = false;
				} else if (rotation == 90) {
					m *= -1;
					distX = p.x - narrowRect.right;
					overSlope = false;
				} else {
					trace("ERROR! Incorrect rotation !");
					return false;
				}
				var distY:Number = m * distX +  narrowRect.top;
				if ((overSlope && p.y >= distY) || (!overSlope && p.y <= distY)) {
					return true;
				}
			}
			return false;
		}
		
		override public function narrowCheck(body:Body):void {
			var projectedLoc:Point = new Point(body.x, body.y).add(body.velocity);
			var proj_Point:Point;
			var distAxis:Number;
			var distHit:Number;
			if (rotation == 0) {
				
				if (body.velocity.x > 0) { //right arm hit
					wallCheck(Util.RIGHT, body, projectedLoc);
				} else if (body.velocity.x < 0) { //left arm hit
					proj_Point = new Point(body.hitBox_X.left, body.hitBox_X.bottom).add(projectedLoc);
					distAxis = proj_Point.y - narrowRect.top;
					
					if (distAxis <= narrowRect.height && distAxis >= 0 && body.x + body.hitBox_X.left >= narrowRect.left) {
						distHit = (distAxis) * (narrowRect.width / narrowRect.height) + narrowRect.left;
						if (proj_Point.x < distHit) {
							body.x = distHit + body.hitBox_X.width / 2;
							body.checkBounce(true);
							body.checkBounceSlope(true);
							body.leftHit = true;
						}
					}
					
				}
				
				if (body.velocity.y >= 0) { //Foot hit
					
					proj_Point = new Point(body.hitBox_Y.left, body.hitBox_Y.bottom).add(projectedLoc);
					distAxis = proj_Point.x - narrowRect.right;
					
					if (distAxis >= -narrowRect.width && distAxis <= 0 && body.y + body.hitBox_Y.bottom <= narrowRect.bottom) {
						distHit = ((narrowRect.height / narrowRect.width) * distAxis) + narrowRect.bottom;
						if (proj_Point.y > distHit) {
							body.y = distHit - body.hitBox_Y.height / 2;
							body.checkBounce(false);
							body.checkBounceSlope(true);
							body.botHit = true;
						}
					}
					
				} else if (body.velocity.y < 0) { //Head hit
					wallCheck(Util.UP, body, projectedLoc);
				}
				
			} else if (rotation == -90) {
				
				if (body.velocity.x >= 0) { //right arm hit
					
					proj_Point = body.hitBox_X.bottomRight.add(projectedLoc);
					distAxis = narrowRect.bottom - proj_Point.y;
					if (distAxis <= narrowRect.height && distAxis >= 0 && body.x + body.hitBox_X.right <= narrowRect.right) {
						distHit = (distAxis) * (narrowRect.width / narrowRect.height) + narrowRect.left;
						if (proj_Point.x > distHit) {
							body.x = distHit - body.hitBox_X.width / 2;
							body.checkBounce(true);
							body.checkBounceSlope(false);
							body.rightHit = true;
						}
					}
				} else if (body.velocity.x < 0) { //left arm hit
					wallCheck(Util.LEFT, body, projectedLoc);
					
				}
				
				if (body.velocity.y >= 0) { //Foot hit
					proj_Point = body.hitBox_Y.bottomRight.add(projectedLoc);
					distAxis = narrowRect.left - proj_Point.x;
					
					if (distAxis >= -narrowRect.width && distAxis <= 0 && body.y + body.hitBox_Y.bottom <= narrowRect.bottom) {
						distHit = ((narrowRect.height / narrowRect.width) * distAxis) + narrowRect.bottom;
						if (proj_Point.y > distHit) {
							body.y = distHit - body.hitBox_Y.height / 2;
							body.checkBounce(false);
							body.checkBounceSlope(false);
							body.botHit = true;
						}
					}
					
				} else if (body.velocity.y < 0) { //Head hit
					wallCheck(Util.UP, body, projectedLoc);
				}
				
			} else if (rotation == 180) {
				if (body.velocity.x > 0) { //right arm hit
					proj_Point = new Point(body.hitBox_X.right, body.hitBox_X.top).add(projectedLoc);
					distAxis = proj_Point.y - narrowRect.top;
					if (distAxis <= narrowRect.height && distAxis >= 0 && body.x + body.hitBox_X.right <= narrowRect.right) {
						distHit = (distAxis) * (narrowRect.width / narrowRect.height) + narrowRect.left;
						if (proj_Point.x > distHit) {
							body.x = distHit - body.hitBox_X.width / 2;
							body.checkBounce(true);
							body.rightHit = true;
						}
					}
				} else if (body.velocity.x < 0) { //left arm hit
					
					wallCheck(Util.LEFT, body, projectedLoc);
					
				}
				
				if (body.velocity.y > 0) { //Foot hit
					wallCheck(Util.DOWN, body, projectedLoc);
					
				} else if (body.velocity.y < 0) { //Head hit
					proj_Point = new Point(body.hitBox_Y.right, body.hitBox_Y.top).add(projectedLoc);
					distAxis = proj_Point.x - narrowRect.left;
					
					if (distAxis <= narrowRect.width && distAxis >= 0 && body.y + body.hitBox_Y.top >= narrowRect.top) {
						distHit = ((narrowRect.height / narrowRect.width) * distAxis) + narrowRect.top;
						if (proj_Point.y < distHit) {
							body.y = distHit + body.hitBox_Y.height / 2;
							body.checkBounce(false);
							body.topHit = true;
						}
					}
				}
				
			} else if (rotation == 90) {
				if (body.velocity.y > 0) { //Foot hit
					wallCheck(Util.DOWN, body, projectedLoc);
					
				} else if (body.velocity.y < 0) { //Head hit
					proj_Point = body.hitBox_Y.topLeft.add(projectedLoc);
					distAxis = narrowRect.right - proj_Point.x;
					
					if (distAxis <= narrowRect.width && distAxis >= 0 && body.y + body.hitBox_Y.top >= narrowRect.top) {
						
						distHit = ((narrowRect.height / narrowRect.width) * distAxis) + narrowRect.top;
						
						if (proj_Point.y < distHit) {
							body.y = distHit + body.hitBox_Y.height / 2;
							body.checkBounce(false);
							body.topHit = true;
						}
					}
				}
				
				if (body.velocity.x > 0) { //right arm hit
					wallCheck(Util.RIGHT, body, projectedLoc);
				} else if (body.velocity.x < 0) { //left arm hit
					proj_Point = body.hitBox_X.topLeft.add(projectedLoc);
					distAxis = narrowRect.bottom - proj_Point.y;
					if (distAxis <= narrowRect.height && distAxis >= 0 && body.x + body.hitBox_X.left >= narrowRect.left) {
						distHit = (distAxis) * (narrowRect.width / narrowRect.height) + narrowRect.left;
						if (proj_Point.x < distHit) {
							body.x = distHit + body.hitBox_X.width / 2;
							body.checkBounce(true);
							body.leftHit = true;
							
						}
					}
					
				}
			}
		
		}
	
	}
}