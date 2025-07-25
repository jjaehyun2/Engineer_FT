/******************************************************************************
 * Spine Runtimes License Agreement
 * Last updated May 1, 2019. Replaces all prior versions.
 *
 * Copyright (c) 2013-2019, Esoteric Software LLC
 *
 * Integration of the Spine Runtimes into software or otherwise creating
 * derivative works of the Spine Runtimes is permitted under the terms and
 * conditions of Section 2 of the Spine Editor License Agreement:
 * http://esotericsoftware.com/spine-editor-license
 *
 * Otherwise, it is permitted to integrate the Spine Runtimes into software
 * or otherwise create derivative works of the Spine Runtimes (collectively,
 * "Products"), provided that each user of the Products must obtain their own
 * Spine Editor license and redistribution of the Products in any form must
 * include this license and copyright notice.
 *
 * THIS SOFTWARE IS PROVIDED BY ESOTERIC SOFTWARE LLC "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN
 * NO EVENT SHALL ESOTERIC SOFTWARE LLC BE LIABLE FOR ANY DIRECT, INDIRECT,
 * INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES, BUSINESS
 * INTERRUPTION, OR LOSS OF USE, DATA, OR PROFITS) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *****************************************************************************/

package spine.animation {
	import spine.MathUtils;
	import spine.Event;
	import spine.Skeleton;

	/** Base class for frames that use an interpolation bezier curve. */
	public class CurveTimeline implements Timeline {
		static private const LINEAR : Number = 0;
		static private const STEPPED : Number = 1;
		static private const BEZIER : Number = 2;
		static private const BEZIER_SIZE : int = 10 * 2 - 1;
		private var curves : Vector.<Number>; // type, x, y, ...

		public function CurveTimeline(frameCount : int) {
			curves = new Vector.<Number>((frameCount - 1) * BEZIER_SIZE, true);
		}

		public function apply(skeleton : Skeleton, lastTime : Number, time : Number, firedEvents : Vector.<Event>, alpha : Number, blend : MixBlend, direction : MixDirection) : void {
		}

		public function getPropertyId() : int {
			return 0;
		}

		public function get frameCount() : int {
			return curves.length / BEZIER_SIZE + 1;
		}

		public function setLinear(frameIndex : int) : void {
			curves[int(frameIndex * BEZIER_SIZE)] = LINEAR;
		}

		public function setStepped(frameIndex : int) : void {
			curves[int(frameIndex * BEZIER_SIZE)] = STEPPED;
		}

		/** Sets the control handle positions for an interpolation bezier curve used to transition from this keyframe to the next.
		 * cx1 and cx2 are from 0 to 1, representing the percent of time between the two keyframes. cy1 and cy2 are the percent of
		 * the difference between the keyframe's values. */
		public function setCurve(frameIndex : int, cx1 : Number, cy1 : Number, cx2 : Number, cy2 : Number) : void {
			var tmpx : Number = (-cx1 * 2 + cx2) * 0.03, tmpy : Number = (-cy1 * 2 + cy2) * 0.03;
			var dddfx : Number = ((cx1 - cx2) * 3 + 1) * 0.006, dddfy : Number = ((cy1 - cy2) * 3 + 1) * 0.006;
			var ddfx : Number = tmpx * 2 + dddfx, ddfy : Number = tmpy * 2 + dddfy;
			var dfx : Number = cx1 * 0.3 + tmpx + dddfx * 0.16666667, dfy : Number = cy1 * 0.3 + tmpy + dddfy * 0.16666667;

			var i : int = frameIndex * BEZIER_SIZE;
			var curves : Vector.<Number> = this.curves;
			curves[int(i++)] = BEZIER;

			var x : Number = dfx, y : Number = dfy;
			for (var n : int = i + BEZIER_SIZE - 1; i < n; i += 2) {
				curves[i] = x;
				curves[int(i + 1)] = y;
				dfx += ddfx;
				dfy += ddfy;
				ddfx += dddfx;
				ddfy += dddfy;
				x += dfx;
				y += dfy;
			}
		}

		public function getCurvePercent(frameIndex : int, percent : Number) : Number {
			percent = MathUtils.clamp(percent, 0, 1);
			var curves : Vector.<Number> = this.curves;
			var i : int = frameIndex * BEZIER_SIZE;
			var type : Number = curves[i];
			if (type == LINEAR) return percent;
			if (type == STEPPED) return 0;
			i++;
			var x : Number = 0;
			for (var start : int = i, n : int = i + BEZIER_SIZE - 1; i < n; i += 2) {
				x = curves[i];
				if (x >= percent) {
					var prevX : Number, prevY : Number;
					if (i == start) {
						prevX = 0;
						prevY = 0;
					} else {
						prevX = curves[int(i - 2)];
						prevY = curves[int(i - 1)];
					}
					return prevY + (curves[int(i + 1)] - prevY) * (percent - prevX) / (x - prevX);
				}
			}
			var y : Number = curves[int(i - 1)];
			return y + (1 - y) * (percent - x) / (1 - x); // Last point is 1,1.
		}
	}
}