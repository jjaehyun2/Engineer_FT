/******************************************************************************
 * Spine Runtimes License Agreement
 * Last updated January 1, 2020. Replaces all prior versions.
 *
 * Copyright (c) 2013-2020, Esoteric Software LLC
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
 * THE SPINE RUNTIMES ARE PROVIDED BY ESOTERIC SOFTWARE LLC "AS IS" AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL ESOTERIC SOFTWARE LLC BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES,
 * BUSINESS INTERRUPTION, OR LOSS OF USE, DATA, OR PROFITS) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 * THE SPINE RUNTIMES, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *****************************************************************************/

package spine {
	public class IkConstraint implements Updatable {
		internal var _data : IkConstraintData;
		public var bones : Vector.<Bone>;
		public var target : Bone;
		public var bendDirection : int;
		public var compress: Boolean;
		public var stretch: Boolean;
		public var mix : Number;
		public var softness : Number = 0;
		public var active : Boolean;

		public function IkConstraint(data : IkConstraintData, skeleton : Skeleton) {
			if (data == null) throw new ArgumentError("data cannot be null.");
			if (skeleton == null) throw new ArgumentError("skeleton cannot be null.");
			_data = data;
			mix = data.mix;
			softness = data.softness;
			bendDirection = data.bendDirection;
			compress = data.compress;
			stretch = data.stretch;

			bones = new Vector.<Bone>();
			for each (var boneData : BoneData in data.bones)
				bones[bones.length] = skeleton.findBone(boneData.name);
			target = skeleton.findBone(data.target._name);
		}

		public function isActive() : Boolean {
			return active;
		}

		public function apply() : void {
			update();
		}

		public function update() : void {
			switch (bones.length) {
				case 1:
					apply1(bones[0], target.worldX, target.worldY, compress, stretch, _data.uniform, mix);
					break;
				case 2:
					apply2(bones[0], bones[1], target.worldX, target.worldY, bendDirection, stretch, softness, mix);
					break;
			}
		}

		public function get data() : IkConstraintData {
			return _data;
		}

		public function toString() : String {
			return _data.name;
		}

		/** Adjusts the bone rotation so the tip is as close to the target position as possible. The target is specified in the world
		 * coordinate system. */
		static public function apply1(bone : Bone, targetX : Number, targetY : Number, compress: Boolean, stretch : Boolean, uniform: Boolean, alpha : Number) : void {
			if (!bone.appliedValid) bone.updateAppliedTransform();
			var p : Bone = bone.parent;

			var pa : Number = p.a, pb : Number = p.b, pc : Number = p.c, pd : Number = p.d;
			var rotationIK : Number = -bone.ashearX - bone.arotation, tx : Number = 0, ty : Number = 0;
			switch(bone.data.transformMode) {
				case TransformMode.onlyTranslation:
					tx = targetX - bone.worldX;
					ty = targetY - bone.worldY;
					break;
				case TransformMode.noRotationOrReflection:
					var s : Number = Math.abs(pa * pd - pb * pc) / (pa * pa + pc * pc);
					var sa : Number = pa / bone.skeleton.scaleX;
					var sc : Number = pc / bone.skeleton.scaleY;
					pb = -sc * s * bone.skeleton.scaleX;
					pd = sa * s * bone.skeleton.scaleY;
					rotationIK += Math.atan2(sc, sa) * MathUtils.radDeg;
					// Fall through.
				default:
					var x : Number = targetX - p.worldX, y : Number = targetY - p.worldY;
					var d : Number = pa * pd - pb * pc;
					tx = (x * pd - y * pb) / d - bone.ax;
					ty = (y * pa - x * pc) / d - bone.ay;
			}

			rotationIK += Math.atan2(ty, tx) * MathUtils.radDeg;
			if (bone.ascaleX < 0) rotationIK += 180;
			if (rotationIK > 180)
				rotationIK -= 360;
			else if (rotationIK < -180) rotationIK += 360;
			var sx : Number = bone.ascaleX;
			var sy : Number = bone.ascaleY;
			if (compress || stretch) {
				switch (bone.data.transformMode) {
					case TransformMode.noScale:
					case TransformMode.noScaleOrReflection:
						tx = targetX - bone.worldX;
						ty = targetY - bone.worldY;
				}
				var b : Number = bone.data.length * sx, dd : Number = Math.sqrt(tx * tx + ty * ty);
				if ((compress && dd < b) || (stretch && dd > b) && b > 0.0001) {
					var s : Number = (dd / b - 1) * alpha + 1;
					sx *= s;
					if (uniform) sy *= s;
				}
			}
			bone.updateWorldTransformWith(bone.ax, bone.ay, bone.arotation + rotationIK * alpha, sx, sy, bone.ashearX, bone.ashearY);
		}

		/** Adjusts the parent and child bone rotations so the tip of the child is as close to the target position as possible. The
		 * target is specified in the world coordinate system.
		 * @param child Any descendant bone of the parent. */
		static public function apply2(parent : Bone, child : Bone, targetX : Number, targetY : Number, bendDir : int, stretch : Boolean, softness: Number, alpha : Number) : void {
			if (alpha == 0) {
				child.updateWorldTransform();
				return;
			}
			if (!parent.appliedValid) parent.updateAppliedTransform();
			if (!child.appliedValid) child.updateAppliedTransform();
			var px : Number = parent.ax, py : Number = parent.ay, psx : Number = parent.ascaleX, sx : Number = psx, psy : Number = parent.ascaleY, csx : Number = child.ascaleX;
			var os1 : int, os2 : int, s2 : int;
			if (psx < 0) {
				psx = -psx;
				os1 = 180;
				s2 = -1;
			} else {
				os1 = 0;
				s2 = 1;
			}
			if (psy < 0) {
				psy = -psy;
				s2 = -s2;
			}
			if (csx < 0) {
				csx = -csx;
				os2 = 180;
			} else
				os2 = 0;
			var cx : Number = child.ax, cy : Number, cwx : Number, cwy : Number, a : Number = parent.a, b : Number = parent.b, c : Number = parent.c, d : Number = parent.d;
			var u : Boolean = Math.abs(psx - psy) <= 0.0001;
			if (!u) {
				cy = 0;
				cwx = a * cx + parent.worldX;
				cwy = c * cx + parent.worldY;
			} else {
				cy = child.ay;
				cwx = a * cx + b * cy + parent.worldX;
				cwy = c * cx + d * cy + parent.worldY;
			}
			var pp : Bone = parent.parent;
			a = pp.a;
			b = pp.b;
			c = pp.c;
			d = pp.d;
			var id : Number = 1 / (a * d - b * c), x : Number = cwx - pp.worldX, y : Number = cwy - pp.worldY;
			var dx : Number = (x * d - y * b) * id - px, dy : Number = (y * a - x * c) * id - py;
			var l1 : Number = Math.sqrt(dx * dx + dy * dy), l2 : Number = child.data.length * csx, a1 : Number, a2 : Number;
			if (l1 < 0.0001) {
				apply1(parent, targetX, targetY, false, stretch, false, alpha);
				child.updateWorldTransformWith(cx, cy, 0, child.ascaleX, child.ascaleY, child.ashearX, child.ashearY);
				return;
			}
			x = targetX - pp.worldX;
			y = targetY - pp.worldY;
			var tx : Number = (x * d - y * b) * id - px, ty : Number = (y * a - x * c) * id - py;
			var dd : Number = tx * tx + ty * ty;
			if (softness != 0) {
				softness *= psx * (csx + 1) / 2;
				var td : Number = Math.sqrt(dd), sd : Number = td - l1 - l2 * psx + softness;
				if (sd > 0) {
					var p : Number = Math.min(1, sd / (softness * 2)) - 1;
					p = (sd - softness * (1 - p * p)) / td;
					tx -= p * tx;
					ty -= p * ty;
					dd = tx * tx + ty * ty;
				}
			}
			outer:
			if (u) {
				l2 *= psx;
				var cos : Number = (dd - l1 * l1 - l2 * l2) / (2 * l1 * l2);
				if (cos < -1)
					cos = -1;
				else if (cos > 1) {
					cos = 1;
					if (stretch) sx *= (Math.sqrt(dd) / (l1 + l2) - 1) * alpha + 1;
				}
				a2 = Math.acos(cos) * bendDir;
				a = l1 + l2 * cos;
				b = l2 * Math.sin(a2);
				a1 = Math.atan2(ty * a - tx * b, tx * a + ty * b);
			} else {
				a = psx * l2;
				b = psy * l2;
				var aa : Number = a * a, bb : Number = b * b, ta : Number = Math.atan2(ty, tx);
				c = bb * l1 * l1 + aa * dd - aa * bb;
				var c1 : Number = -2 * bb * l1, c2 : Number = bb - aa;
				d = c1 * c1 - 4 * c2 * c;
				if (d >= 0) {
					var q : Number = Math.sqrt(d);
					if (c1 < 0) q = -q;
					q = -(c1 + q) / 2;
					var r0 : Number = q / c2, r1 : Number = c / q;
					var r : Number = Math.abs(r0) < Math.abs(r1) ? r0 : r1;
					if (r * r <= dd) {
						y = Math.sqrt(dd - r * r) * bendDir;
						a1 = ta - Math.atan2(y, r);
						a2 = Math.atan2(y / psy, (r - l1) / psx);
						break outer;
					}
				}
				var minAngle : Number = Math.PI, minX : Number = l1 - a, minDist : Number = minX * minX, minY : Number = 0;
				var maxAngle : Number = 0, maxX : Number = l1 + a, maxDist : Number = maxX * maxX, maxY : Number = 0;
				c = -a * l1 / (aa - bb);
				if (c >= -1 && c <= 1) {
					c = Math.acos(c);
					x = a * Math.cos(c) + l1;
					y = b * Math.sin(c);
					d = x * x + y * y;
					if (d < minDist) {
						minAngle = c;
						minDist = d;
						minX = x;
						minY = y;
					}
					if (d > maxDist) {
						maxAngle = c;
						maxDist = d;
						maxX = x;
						maxY = y;
					}
				}
				if (dd <= (minDist + maxDist) / 2) {
					a1 = ta - Math.atan2(minY * bendDir, minX);
					a2 = minAngle * bendDir;
				} else {
					a1 = ta - Math.atan2(maxY * bendDir, maxX);
					a2 = maxAngle * bendDir;
				}
			}
			var os : Number = Math.atan2(cy, cx) * s2;
			var rotation : Number = parent.arotation;
			a1 = (a1 - os) * MathUtils.radDeg + os1 - rotation;
			if (a1 > 180)
				a1 -= 360;
			else if (a1 < -180) a1 += 360;
			parent.updateWorldTransformWith(px, py, rotation + a1 * alpha, sx, parent.ascaleY, 0, 0);
			rotation = child.arotation;
			a2 = ((a2 + os) * MathUtils.radDeg - child.ashearX) * s2 + os2 - rotation;
			if (a2 > 180)
				a2 -= 360;
			else if (a2 < -180) a2 += 360;
			child.updateWorldTransformWith(cx, cy, rotation + a2 * alpha, child.ascaleX, child.ascaleY, child.ashearX, child.ashearY);
		}
	}
}