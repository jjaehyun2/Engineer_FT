package we3d.loader 
{
	import flash.events.Event;
	import flash.utils.ByteArray;
	import flash.utils.Endian;
	
	import we3d.we3d;
	import we3d.material.Surface;
	import we3d.math.Vector3d;
	import we3d.mesh.Face;
	import we3d.mesh.UVCoord;
	import we3d.mesh.Vertex;
	import we3d.scene.SceneObject;
	import we3d.scene.SceneObjectMorph;
	import we3d.ui.Console;
	
	use namespace we3d;
	
	/**
	* Load MD2 files with animation. 
	*/ 
	public class MD2Loader extends SceneLoader 
	{
		public function MD2Loader () {}
		
		// [internal] Md2 file format has a bunch of header information
		// that is typically just read straight into a C-style struct, but
		// since this is not C =( we have to create variables for all of it.
		private var ident:int, version:int;
		private var skinwidth:int, skinheight:int;
		private var framesize:int;
		private var num_skins:int, num_vertices:int, num_st:int;
		private var num_tris:int, num_glcmds:int, num_frames:int;
		private var offset_skins:int, offset_st:int, offset_tris:int;
		private var offset_frames:int, offset_glcmds:int, offset_end:int;		
		
		public override function parseFile (data:ByteArray) :void 
		{
			super.init();
			
			currObject = new SceneObjectMorph();
			
			fileObjects.push(currObject);
			objectsByName[filename] = fileObjects[fileObjects.length-1];
			
			currSurface = new Surface();
			fileSurfaces.push(currSurface);
			surfacesByName[filename +".surface"] = fileSurfaces[fileSurfaces.length-1];
			
			var uvs:Vector.<UVCoord> = new Vector.<UVCoord>();
			var a:int;
			var b:int;
			var c:int; 
			var ta:int; 
			var tb:int; 
			var tc:int;
			
			var vertices:Vector.<Vertex> = currObject.points;
			var faces:Vector.<Face> = currObject.polygons
			var i:int;
			
			// Make sure to have this in Little Endian or you will hate you life.
			// At least I did the first time I did this for a while.
			data.endian = Endian.LITTLE_ENDIAN;
			
			// Read the header and make sure it is valid MD2 file
			readMd2Header(data);
			
			if (ident != 844121161 || version != 8)
				throw new Error("Error loading MD2 file (" + filepath + "): Not a valid MD2 file/bad version");
			
			// Vertice setup
			// 		Be sure to allocate memory for the vertices to the object
			//		These vertices will be updated each frame with the proper coordinates
			for (i = 0; i < num_vertices; i++) 
			{
				currObject.addPoint(0,0,0);
			}

			// UV coordinates
			//		Load them!
			data.position = offset_st;
			for (i = 0; i<num_st; i++) 
			{
				uvs.push(new UVCoord(data.readShort() / skinwidth, data.readShort() / skinheight ));
			}
			
			// Faces
			//		Creates the faces with the proper references to vertices
			//		NOTE: DO NOT change the order of the variable assignments here, 
			//			  or nothing will work.
			data.position = offset_tris;
			for (i = 0; i < num_tris; i++)
			{
				a = data.readUnsignedShort();
				b = data.readUnsignedShort();
				c = data.readUnsignedShort();
				ta = data.readUnsignedShort();
				tb = data.readUnsignedShort();
				tc = data.readUnsignedShort();
				
				var face:Face = currObject.addTriangle( currSurface, c,b,a, uvs[tc], uvs[tb], uvs[ta] );
			}
			
			// Frame animation data
			//		This part is a little funky.
			data.position = offset_frames;
			readFrames(data);
			
			SceneObjectMorph(currObject).setFrame(0);
			SceneObjectMorph(currObject).play();
			
			finishParse();
		}
		
		/**
		 * Reads in all the frames
		 */
		private function readFrames(data:ByteArray) :void 
		{
			var sx:Number, sy:Number, sz:Number;
			var tx:Number, ty:Number, tz:Number;
			var verts:Vector.<Vertex>;
			var frame_name:String;
			var i:int, j:int, char:int;
			var px:Number;	var py:Number;	var pz:Number;
			
			for (i = 0; i < num_frames; i++) {
				verts = new Vector.<Vertex>();
				
				sx = data.readFloat();
				sy = data.readFloat();
				sz = data.readFloat();
				
				tx = data.readFloat();
				ty = data.readFloat();
				tz = data.readFloat();
				
				frame_name = "";
				for (j = 0; j < 16; j++) {
					char = data.readUnsignedByte();
					if (char <= 32){
						data.position += 15-j;
						break;
					}else{
						
						if( (char >= 63 && char <= 126) || 
							(char >= 35 && char <= 59) || 
							char == 33 ) // !
								frame_name += String.fromCharCode(char);
					}
				}
				
				var vt:Vertex;
				// Note, the extra data.position++ in the for loop is there 
				// to skip over a byte that holds the "vertex normal index"
				for (j = 0; j < num_vertices; j++ /*, data.position++*/) {
					px = data.readUnsignedByte();
					py = data.readUnsignedByte();
					pz = data.readUnsignedByte();
					vt = new Vertex(
						((sx * px) + tx) * scaleX, 
						((sz * pz) + tz) * scaleY,
						((sy * py) + ty) * scaleZ);
					verts.push(vt);
					
					if( parseVertexNormals ) {
						MD2Normals.getNormalAt( data.readUnsignedByte(), normal );
						vt.normal = new Vector3d( -normal[0], -normal[1], -normal[2] );
					}else{
						data.position++;
					}
				}
				
				SceneObjectMorph(currObject).addMorph( frame_name, verts );
			}
		}
		private var normal:Vector.<Number> = new Vector.<Number>(3);
		public var parseVertexNormals:Boolean=true;
		
		/**
		 * Reads in all that MD2 Header data that is declared as private variables.
		 * I know its a lot, and it looks ugly, but only way to do it in Flash
		 */
		private function readMd2Header(data:ByteArray) :void 
		{
			ident = data.readInt();
			version = data.readInt();
			skinwidth = data.readInt();
			skinheight = data.readInt();
			framesize = data.readInt();
			num_skins = data.readInt();
			num_vertices = data.readInt();
			num_st = data.readInt();
			num_tris = data.readInt();
			num_glcmds = data.readInt();
			num_frames = data.readInt();
			offset_skins = data.readInt();
			offset_st = data.readInt();
			offset_tris = data.readInt();
			offset_frames = data.readInt();
			offset_glcmds = data.readInt();
			offset_end = data.readInt();
		}
		
		private function finishParse() :void 
		{
			dispatchEvent(new Event(Event.COMPLETE));
			clearMemory();
		}		
	}
}