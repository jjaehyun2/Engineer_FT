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

package spine.attachments {
	import spine.Color;

	public dynamic class MeshAttachment extends VertexAttachment {
		public var uvs : Vector.<Number>;
		public var regionUVs : Vector.<Number>;
		public var triangles : Vector.<uint>;
		public var color : Color = new Color(1, 1, 1, 1);
		public var hullLength : int;
		private var _parentMesh : MeshAttachment;
		public var inheritDeform : Boolean;
		public var path : String;
		public var rendererObject : Object;
		public var regionU : Number;
		public var regionV : Number;
		public var regionU2 : Number;
		public var regionV2 : Number;
		public var regionRotate : Boolean;
		public var regionOffsetX : Number; // Pixels stripped from the bottom left, unrotated.
		public var regionOffsetY : Number;
		public var regionWidth : Number; // Unrotated, stripped size.
		public var regionHeight : Number;
		public var regionOriginalWidth : Number; // Unrotated, unstripped size.
		public var regionOriginalHeight : Number;		
		// Nonessential.
		public var edges : Vector.<int>;
		public var width : Number;
		public var height : Number;

		public function MeshAttachment(name : String) {
			super(name);
		}

		public function updateUVs() : void {			
			var i : int, n : int = regionUVs.length;
			var u: Number, v: Number, width: Number, height: Number;
			var textureWidth: Number, textureHeight: Number;
			if (!uvs || uvs.length != n) uvs = new Vector.<Number>(n, true);
			if (regionRotate) {
				textureHeight = regionWidth / (regionV2 - regionV);
				textureWidth = regionHeight / (regionU2 - regionU);
				u = regionU - (regionOriginalHeight - regionOffsetY - regionHeight) / textureWidth;
				v = regionV - (regionOriginalWidth - regionOffsetX - regionWidth) / textureHeight;
				width = regionOriginalHeight / textureWidth;
				height = regionOriginalWidth / textureHeight;
				for (i = 0; i < n; i += 2) {
					uvs[i] = u + regionUVs[int(i + 1)] * width;
					uvs[int(i + 1)] = v + height - regionUVs[i] * height;
				}
			} else {
				textureWidth = regionWidth / (regionU2 - regionU);
				textureHeight = regionHeight / (regionV2 - regionV);
				u = regionU - regionOffsetX / textureWidth;
				v = regionV - (regionOriginalHeight - regionOffsetY - regionHeight) / textureHeight;
				width = regionOriginalWidth / textureWidth;
				height = regionOriginalHeight / textureHeight;				
				for (i = 0; i < n; i += 2) {
					uvs[i] = u + regionUVs[i] * width;
					uvs[int(i + 1)] = v + regionUVs[int(i + 1)] * height;
				}
			}
		}

		override public function applyDeform(sourceAttachment : VertexAttachment) : Boolean {
			return this == sourceAttachment || (inheritDeform && _parentMesh == sourceAttachment);
		}

		public function get parentMesh() : MeshAttachment {
			return _parentMesh;
		}

		public function set parentMesh(parentMesh : MeshAttachment) : void {
			_parentMesh = parentMesh;
			if (parentMesh != null) {
				bones = parentMesh.bones;
				vertices = parentMesh.vertices;
				worldVerticesLength = parentMesh.worldVerticesLength;
				regionUVs = parentMesh.regionUVs;
				triangles = parentMesh.triangles;
				hullLength = parentMesh.hullLength;
				edges = parentMesh.edges;
				width = parentMesh.width;
				height = parentMesh.height;
			}
		}
	}
}