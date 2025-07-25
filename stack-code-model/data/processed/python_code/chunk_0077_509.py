package we3d.renderer.wireframe 
{
	import flash.display.BitmapData;
	
	import we3d.we3d;
	import we3d.core.Camera3d;
	import we3d.core.Object3d;
	import we3d.core.culling.BoxCulling;
	import we3d.material.FlatAttributes;
	import we3d.material.Surface;
	import we3d.math.Matrix3d;
	import we3d.math.Vector3d;
	import we3d.mesh.Face;
	import we3d.mesh.Vertex;
	import we3d.rasterizer.Rasterizer;
	import we3d.renderer.IRenderer;
	import we3d.renderer.RenderSession;
	import we3d.scene.SceneObject;

	use namespace we3d;
	
	/**
	* Orthographic wireframe renderer with line clipping in 2d
	*/
	public class WFClipRect implements IRenderer 
	{
		public function WFClipRect () {}
		
		public function clipLine (p1x:Number, p1y:Number, p2x:Number, p2y:Number, p1:Vector3d, p2:Vector3d, w:int, h:int) :int {
			p1.x = p1x;
			p1.y = p1y;
			p2.x = p2x;
			p2.y = p2y;
			
			var b_clip:int = 0;
			var slope:Number
			
			// Top
			var a:Boolean = p1.y >= 0;
			var b:Boolean = p2.y >= 0;
		
			if (!a && !b) {
				return -1;	
			}else if( a != b ){
				b_clip++;
				slope = (p2.y - p1.y) / (p2.x - p1.x);
				if( a ) {
					p2.x = -p1.y / slope+p1.x;
					p2.y = 0;
				}else {
					p1.x = -p2.y / slope+p2.x;
					p1.y = 0;	
				}
			}
			
			// Bottom
			a = p1.y <= h;
			b = p2.y <= h;
			if(!a && !b) {
				return -1 ;
			}else if( a != b  )  {
				b_clip += 10;
				slope = (p2.y - p1.y) / (p2.x - p1.x);
				if( a ) {
					p2.x = ((h-p1.y) / slope)+p1.x;
					p2.y = h;
				}else {
					p1.x = ((h-p2.y) / slope)+p2.x;
					p1.y = h;	
				}
			}
			
			// Left
			a = p1.x >= 0;
			b = p2.x >= 0;
			if(!a && !b) {
				return -1 ;
			}else if( a != b ){
				b_clip += 100;
				slope = (p2.y - p1.y) / (p2.x - p1.x);
				if(a) {
					p2.x = 0;
					p2.y = -p1.x * slope+p1.y;
				}else{
					p1.x = 0;
					p1.y = -p2.x * slope+p2.y;
				}
			}
			
			//Right
			a = p1.x <= w;
			b = p2.x <= w;
			if (!a && !b) {
				return -1 ;
			}else if( a != b ){
				b_clip += 1000;
				slope = (p2.y - p1.y) / (p2.x - p1.x);
				if(a) {
					p2.x = w;
					p2.y = ((w-p1.x) * slope)+p1.y;
				}else{
					p1.x = w;
					p1.y = ((w-p2.x) * slope)+p2.y;
				}
			}
			
			return b_clip;
		}
		
		public function draw (session:RenderSession) :void {
			
			var v:Camera3d = session.camera;
			var objectList:Vector.<Object3d>  = session.scene.objectList;
			var f:Number = session.currentFrame;
			var cw:int = v._width;
			var ch:int = v._height;
			var sf:Surface;
			var atb:FlatAttributes;
			var o:SceneObject;
			var p:Face;
			var j:int;
			var L:int;
			var r:Vector.<Face>;
			
			var objs:int = objectList.length;
			var acp2d:Vector3d = new Vector3d();
			var bcp2d:Vector3d = new Vector3d();
			var $p:Vector.<Vertex>;
			var l:int;
			var g:Vertex;
			var h:Vertex;
			var cgv:Matrix3d = new Matrix3d();
			var x:Number; var y:Number; var z:Number;
			var vtxs:Vector.<Vertex>;
			var k:int;
			var vtxa:Vertex;
			var vtxb:Vertex;
			var gv:Matrix3d;
			var ofc:int;
			var x0:Number; var y0:Number;
			var pt0:Vertex;	var pt1:Vertex;	var pt2:Vertex;
			var pL:int;
			var scale:Number= v.orthoScale;
			var vt:Number = v.t;
			var vs:Number = v.s;
			var vw:Number = v.width;
			var vh:Number = v.height;
			var sl:Rasterizer = new Rasterizer();
			var bmpd:BitmapData = session.bmp;
			
			var linecol:int;
			var boxCulling:BoxCulling;
			var pculled:int;
			var culled:Boolean;
			
			for(var i:int=0; i<objs; i++) {
				
				o = SceneObject(objectList[i]);
				
				o.initFrame(session);
				
				cgv = o.camMatrix;
				o.culled = false;
				
				if(o.objectCuller is BoxCulling) 
				{
					boxCulling = BoxCulling(o.objectCuller);
					pculled = 0;
						
					// translate all points of bounding box
					for(j=0; j<8; j++) {
						vtxa = boxCulling.points[j];
						vtxa.wx = cgv.a*vtxa.x + cgv.e*vtxa.y + cgv.i*vtxa.z + cgv.m;
						vtxa.wy = cgv.b*vtxa.x + cgv.f*vtxa.y + cgv.j*vtxa.z + cgv.n;
						vtxa.wz = cgv.c*vtxa.x + cgv.g*vtxa.y + cgv.k*vtxa.z + cgv.o //+ v._nearClipping;
						vtxa.sx = vt + vtxa.wx/scale * vt;
						vtxa.sy = vs - vtxa.wy/scale * vs;
					}
					
					// Cull Top
					culled = true;
					for(j=0; j<8; j++) {
						vtxa = boxCulling.points[j];
						if(vtxa.sy > 0) {
							culled = false;
							break;
						}
					}
					if(culled) {
						o.culled = true;
						continue;
					}
					
					// Cull Left
					culled = true;
					for(j=0; j<8; j++) {
						vtxa = boxCulling.points[j];
						if(vtxa.sx > 0) {
							culled = false;
							break;
						}
					}
					if(culled) {
						o.culled = true;
						continue;
					}
					
					// Cull Bottom
					culled = true;
					for(j=0; j<8; j++) {
						vtxa = boxCulling.points[j];
						if(vtxa.sy < vh) {
							culled = false;
							break;
						}
					}
					if(culled) {
						o.culled = true;
						continue;
					}
					
					// Cull Right
					culled = true;
					for(j=0; j<8; j++) {
						vtxa = boxCulling.points[j];
						if(vtxa.sx < vw) {
							culled = false;
							break;
						}
					}
					if(culled) {
						o.culled = true;
						continue;
					}
				}
				
				if(o.initMesh(session)) continue;
				
				r = o.polygons;
				L = r.length;
				
				ofc = o.frameCounter;
				gv = o.transform.gv;
				
				for(j=0; j<L; j++) {
					
					p = r[j];
					pL = p.vLen;
					if(pL < 2) continue;
					
					vtxb = p.normal;
					vtxb.wz = gv.c * vtxb.x + gv.g * vtxb.y + gv.k * vtxb.z;
					vtxb.wy = gv.b * vtxb.x + gv.f * vtxb.y + gv.j * vtxb.z;
					vtxb.wx = gv.a * vtxb.x + gv.e * vtxb.y + gv.i * vtxb.z;
										
					vtxs = p.vtxs;
					
					for(k=0; k<pL; k++) {
						vtxb = vtxs[k];
						if(vtxb.frameCounter1 != ofc) {
							vtxb.wz = cgv.c * vtxb.x + cgv.g * vtxb.y + cgv.k * vtxb.z + cgv.o;
							vtxb.wy = cgv.b * vtxb.x + cgv.f * vtxb.y + cgv.j * vtxb.z + cgv.n;
							vtxb.wx = cgv.a * vtxb.x + cgv.e * vtxb.y + cgv.i * vtxb.z + cgv.m //+ v._nearClipping;
							vtxb.sx = vt + vtxb.wx/scale * vt;
							vtxb.sy = vs - vtxb.wy/scale * vs;
							
							if( vtxb.sx < 0 || vtxb.sy < 0 || vtxb.sx > vw || vtxb.sy > vh ) continue;
							vtxb.frameCounter2 = ofc;
						}
						
					}
					
					sf = p.surface;
					atb = FlatAttributes(sf.attributes);
					linecol = atb._color32;
					
					pt0 = p.a;
					pt1 = p.b;
					
					if(pL == 2) {
						if(clipLine(pt0.sx, pt0.sy, pt1.sx, pt1.sy, acp2d, bcp2d, cw, ch) >= 0) {
							p.frameCounter = ofc;
							sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
						}
					}
					else{
						
						pt2 = p.c;
						x0 = pt0.sx;
						y0 = pt0.sy;
						
						if(pL == 3) {
							if(clipLine(x0, y0, pt1.sx, pt1.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
							if(clipLine(pt1.sx, pt1.sy, pt2.sx, pt2.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
							if(clipLine(pt2.sx, pt2.sy, x0, y0, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
						}
						else if(pL == 4) {
							if(clipLine(x0, y0, pt1.sx, pt1.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
							if(clipLine(pt1.sx, pt1.sy, pt2.sx, pt2.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
							g = p.vtxs[3];
							if(clipLine(pt2.sx, pt2.sy, g.sx, g.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
							if(clipLine(g.sx, g.sy, x0, y0, acp2d, bcp2d, cw, ch) >= 0){
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
						}
						else{
							
							$p = p.vtxs;
							l = pL;
							
							while(--l > 0) {
								g = $p[l];
								h = $p[l-1];
								if(clipLine(g.sx, g.sy, h.sx, h.sy, acp2d, bcp2d, cw, ch) >= 0) {
									sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
									p.frameCounter = ofc;
								}
							}
							
							g = $p[0];
							h = $p[pL-1];
							if(clipLine(g.sx, g.sy, h.sx, h.sy, acp2d, bcp2d, cw, ch) >= 0) {
								sl.drawLine (acp2d.x, acp2d.y, bcp2d.x, bcp2d.y, linecol, bmpd);
								p.frameCounter = ofc;
							}
						}
					}
				}
			}
			
			bmpd.unlock();
		}
		
	}
}