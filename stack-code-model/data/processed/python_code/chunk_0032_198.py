package we3d.core.transform 
{
	import we3d.we3d;
	import we3d.animation.EnvelopeChannel;
	import we3d.animation.IChannel;
	import we3d.animation.PropertyAnimator;
	import we3d.math.Vector3d;

	use namespace we3d;
	
	/**
	* The AnimatedAll transform provides features from the 3.0 release
	*/
	public class AnimatedAll extends AnimatedHierarchy
	{
		public function AnimatedAll () {}
		
		/**	
		* Animate Properties relative to the transform (position, rotation, scale)
		* @param 	prop	relative path of the property
		* @return 	a new PropertyAnimator or the PropertyAnimator with the property if already registered
		*/
		public function animateProperty (prop:String, ec:IChannel=null) :PropertyAnimator {
			var d:int = prop.indexOf(".");
			
			if(d == -1) {
				if(this[prop] != null) {
					if(regPas[prop] != null) {
						return pas[regPas[prop]]; //property already animated
					}
					
					pas.push(new PropertyAnimator(this, prop, ec == null ? new EnvelopeChannel() : ec));
					regPas[prop] = pas.length-1;
				}
			}
			else{
				var a:Array = prop.split(".");
				var nm:* = regPas[a.join("_")];
				
				if(typeof(nm) == "number") {
					return pas[nm]; //property already animated
				}
				
				var t:* = this;
				var L:int = a.length-1;
				
				for(var i:int=0; i<L; i++) {
					t = t[a[i]];
				}
				
				if(t != null && a[a.length-1].length > 0) {
					pas.push(new PropertyAnimator(t, a[a.length-1], ec == null ? new EnvelopeChannel() : ec));
					regPas[a.join("_")] = pas.length-1;
				}
			}
			
			return pas[pas.length-1];
		}
		
		/**	
		* deletes a registered PropertyAnimator
		* @param 	prop 	relative path to the property
		*/
		public function clearPropertyAnimator (prop:String) :void {
			
			var d:int = prop.indexOf(".");
			var nm:*;
			var name:String;
			
			if(d == -1) {
				nm = regPas[prop];
				name = prop;
			}
			else{
				var a:Array = prop.split(".");
				name = a.join("_");
				nm = regPas[name];
			}
			
			if(nm != undefined) {
				
				pas.splice(nm, 1);
				delete regPas[name];
				
				for(var i:String in regPas) {
					if(regPas[i]>nm) regPas[i]--;
				}
			}
		}
		
		/** 
		* Returns the position at a frame <br/>
		* @return 	the position as a new Vector
		*/
		public function getPositionAt (f:Number) :Vector3d {
				return new Vector3d(	pas[regPas.x] == null ? x : pas[regPas.x].env.getValue(f), 
									pas[regPas.y] == null ? y : pas[regPas.y].env.getValue(f), 
									pas[regPas.z] == null ? z : pas[regPas.z].env.getValue(f));
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getPositionXAt (f:Number) :Number {
				return pas[regPas.x] == null ? x : pas[regPas.x].env.getValue(f);
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getPositionYAt (f:Number) :Number {
			return pas[regPas.y] == null ? y : pas[regPas.y].env.getValue(f);
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getPositionZAt (f:Number) :Number {
			return  pas[regPas.z] == null ? z : pas[regPas.z].env.getValue(f);
		}
		
		/** 
		* Sets the position of the Object3d at a frame <br/>
		* @param	x	the location on the x Axis or null to ignore keyframing
		* @param	y	the location on the y Axis or null to ignore keyframing
		* @param	z	the location on the z axis or null to ignore keyframing
		* @param	f	frame for x, y and z.
		* @param 	testFrame	if true, the method only creates keyframes if required
		*/
		public function setPositionAt (ax:*, ay:*, az:*, f:Number, testFrame:Boolean=false) :void {
			var env:IChannel;
			if(ax != null) {
				if(!testFrame || getPositionXAt(f) != ax) {
					if(typeof(regPas.x) == "number") {
						pas[regPas.x].env.storeFrame(f, ax);
					}else{
						env = animateProperty("x").env;
						env.storeFrame(f, ax);
					}
				}
			}
			if(ay != null) {
				if(!testFrame || getPositionYAt(f) != ay) {
					if(typeof(regPas.y) == "number") {
						pas[regPas.y].env.storeFrame(f, ay);
					}else{
						env = animateProperty("y").env;
						env.storeFrame(f, ay);
					}
				}
			}
			if(az != null) {
				if(!testFrame || getPositionZAt(f) != az) {
					if(typeof(regPas.z) == "number") {
						pas[regPas.z].env.storeFrame(f, az);
					}else{
						env = animateProperty("z").env;
						env.storeFrame(f, az);
					}
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setPositionXAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getPositionXAt(f) != v) {
				if(typeof(regPas.x) == "number") {
					pas[regPas.x].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("x").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setPositionYAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getPositionYAt(f) != v) {
				if(typeof(regPas.y) == "number") {
					pas[regPas.y].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("y").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setPositionZAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getPositionZAt(f) != v) {
				if(typeof(regPas.z) == "number") {
					pas[regPas.z].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("z").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/**
		* Moves the Object3d on a frame  <br/>
		* @param	x	offset on the x Axis or null to ignore keyframing
		* @param	y	offset on the y Axis or null to ignore keyframing
		* @param	z	offset on the z Axis or null to ignore keyframing
		* @param	f	a keyframe for all position envelope channels (x, y and z)
		*/
		public function moveAt (ax:*, ay:*, az:*, f:Number) :void {
			var env:IChannel;
			if(ax != null) {
				if(typeof(regPas.x) == "number") {
					pas[regPas.x].env.storeFrame(f, ax + pas[regPas.x].env.getValue(f));
				}else{
					env = animateProperty("x").env;
					env.storeFrame(f, ax + x);
				}
			}
			if(ay != null) {
				if(typeof(regPas.y) == "number") {
					pas[regPas.y].env.storeFrame(f, ay + pas[regPas.y].env.getValue(f));
				}else{
					env = animateProperty("y").env;
					env.storeFrame(f, ay + y);
				}
			}
			if(az != null) {
				if(typeof(regPas.z) == "number") {
					pas[regPas.z].env.storeFrame(f, az + pas[regPas.z].env.getValue(f));
				}else{
					env = animateProperty("z").env;
					env.storeFrame(f, az + z);
				}
			}
		}
		
		/** 
		* Returns the rotation at a frame <br/>
		* @param	f		the frame number
		* @return 	the rotation of the Object as a new Vector
		*/
		public function getRotationAt (f:Number) :Vector3d {
				return new Vector3d(	pas[regPas.rotationX] == null ? rotationX  : pas[regPas.rotationX].env.getValue(f), 
									pas[regPas.rotationY] == null ? rotationY  : pas[regPas.rotationY].env.getValue(f), 
									pas[regPas.rotationZ] == null ? rotationZ  : pas[regPas.rotationZ].env.getValue(f));
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getRotationXAt (f:Number) :Number {
			return pas[regPas.rotationX] == null ? rotationX  : pas[regPas.rotationX].env.getValue(f);
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getRotationYAt (f:Number) :Number {
			return pas[regPas.rotationY] == null ? rotationY  : pas[regPas.rotationY].env.getValue(f);
		}
		
		/**
		* @param	f
		* @return
		*/
		public function getRotationZAt (f:Number) :Number {
			return pas[regPas.rotationZ] == null ? rotationZ  : pas[regPas.rotationZ].env.getValue(f);
		}
		
		/** 
		* Sets the rotation of the Object3d <br/> 
		* @param	x	the rotation on the x Axis in radian or null to ignore keyframing
		* @param	y	the rotation on the y Axis in radian or null to ignore keyframing
		* @param	z	the rotation on the z axis in radian or null to ignore keyframing
		* @param	f	frame for x, y and z.
		* @param	testFrame	if true, the method only creates keyframes if required
		*/
		public function setRotationAt (ax:*, ay:*, az:*, f:Number, testFrame:Boolean=false) :void {
			var env:IChannel;
			if(ax != null) {
				if(!testFrame || getRotationXAt(f) != ax) {
					if(typeof(regPas.rotationX) == "number") {
						pas[regPas.rotationX].env.storeFrame(f, ax);
					}else{
						env = animateProperty("rotationX").env;
						env.storeFrame(f, ax);
					}
				}
			}
			
			if(ay != null) {
				if(!testFrame || getRotationYAt(f) != ay) {
					if(typeof(regPas.rotationY) == "number") {
						pas[regPas.rotationY].env.storeFrame(f, ay);
					}else{
						env = animateProperty("rotationY").env;
						env.storeFrame(f, ay);
					}
				}
			}
			
			if(az != null) {
				if(!testFrame || getRotationZAt(f) != az) {
					if(typeof(regPas.rotationZ) == "number") {
						pas[regPas.rotationZ].env.storeFrame(f, az);
					}else{
						env = animateProperty("rotationZ").env;
						env.storeFrame(f, az);
					}
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setRotationXAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getRotationXAt(f) != v) {
				if(typeof(regPas.rotationX) == "number") {
					pas[regPas.rotationX].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("rotationX").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setRotationYAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getRotationYAt(f) != v) {
				if(typeof(regPas.rotationY) == "number") {
					pas[regPas.rotationY].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("rotationY").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/**
		* @param	v
		* @param	f
		* @param	testFrame
		*/
		public function setRotationZAt (v:Number, f:Number, testFrame:Boolean=false) :void {
			if(!testFrame || getRotationZAt(f) != v) {
				if(typeof(regPas.rotationZ) == "number") {
					pas[regPas.rotationZ].env.storeFrame(f, v);
				}else{
					var env:IChannel = animateProperty("rotationZ").env;
					env.storeFrame(f, v);
				}
			}
		}
		
		/** 
		* Rotates the Object3d by offset <br/>
		* @param	x	the rotation offset on the x Axis in radian or null to ignore keyframing
		* @param	y	the rotation offset on the y Axis in radian or null to ignore keyframing
		* @param	z	the rotation offset on the z axis in radian or null to ignore keyframing
		* @param	f	frame for x, y and z.
		*/
		public function rotateAt (ax:*, ay:*, az:*, f:Number) :void {
			var env:IChannel;
			if(ax != null) {
				if(typeof(regPas.rotationX) == "number") {
					pas[regPas.rotationX].env.storeFrame(f, ax + pas[regPas.rotationX].env.getValue(f));
				}else{
					env = animateProperty("rotationX").env;
					env.storeFrame(f, ax + rotationX);
				}
			}
			
			if(ay != null) {
				if(typeof(regPas.rotationY) == "number") {
					pas[regPas.rotationY].env.storeFrame(f, ay + pas[regPas.rotationY].env.getValue(f));
				}else{
					env = animateProperty("rotationY").env;
					env.storeFrame(f, ay + rotationY);
				}
			}
			
			if(az != null) {
				if(typeof(regPas.rotationZ) == "number") {
					pas[regPas.rotationZ].env.storeFrame(f, az + pas[regPas.rotationZ].env.getValue(f));
				}else{
					env = animateProperty("rotationZ").env;
					env.storeFrame(f, az + rotationZ);
				}
			}
		}
	
		/**
		* Clear the position channels and set the values to default values from the arguments or to 0 if undefined
		* @param	dpos 		default position
		* @param	clearEc 	delete envelope channels or clear their timelines
		*/
		public function clearPositionChannels (dpos:*, clearEc:Boolean) :void {
			if(pas["x"] != null) {
				if(clearEc) {
					clearPropertyAnimator("x");
					if(dpos.x != undefined) {
						x = dpos.x;
					}else{
						x = 0;
					}
				}else{
					pas["x"].env.clearFrames();
					if(dpos.x != undefined)
						pas["x"].env.storeFrame(1, dpos.x);
				}
			}
			
			if(pas["y"] != null) {
				if(clearEc) {
					clearPropertyAnimator("y");
					if(dpos.y != undefined) {
						y = dpos.y;
					}else{
						y = 0;
					}
				}else{
					pas["y"].env.clearFrames();
					if(dpos.y != undefined)
						pas["y"].env.storeFrame(1, dpos.y);
				}
			}
			
			
			if(pas["z"] != null) {
				if(clearEc) {
					clearPropertyAnimator("z");
					if(dpos.z != undefined) {
						z = dpos.z;
					}else{
						z = 0;
					}
				}else{
					pas["z"].env.clearFrames();
					if(dpos.z != undefined)
						pas["z"].env.storeFrame(1, dpos.z);
				}
			}
		}
		
		/**
		* Clear the rotation channels and set the values to default values from the arguments or to 0 if undefined
		* @param	dpos 		default position
		* @param	clearEc 	delete envelope channels or clear their timelines
		*/
		public function clearRotationChannels (dpos:*, clearEc:Boolean) :void {
			if(pas["rotationX"] != null) {
				if(clearEc) {
					clearPropertyAnimator("rotationX");
					if(dpos.x != undefined) {
						rotationX = dpos.x;
					}else{
						rotationX = 0;
					}
				}else{
					pas["rotationX"].env.clearFrames();
					if(dpos.x != undefined)
						pas["rotationX"].env.storeFrame(1, dpos.x);
				}
			}
			
			if(pas["rotationY"] != null) {
				if(clearEc) {
					clearPropertyAnimator("rotationY");
					if(dpos.y != undefined) {
						rotationY = dpos.y;
					}else{
						rotationY = 0;
					}
				}else{
					pas["rotationY"].env.clearFrames();
					if(dpos.y != undefined)
						pas["rotationY"].env.storeFrame(1, dpos.y);
				}
			}
			
			
			if(pas["rotationZ"] != null) {
				if(clearEc) {
					clearPropertyAnimator("rotationZ");
					if(dpos.z != undefined) {
						rotationZ = dpos.z;
					}else{
						rotationZ = 0;
					}
				}else{
					pas["rotationZ"].env.clearFrames();
					if(dpos.z != undefined)
						pas["rotationZ"].env.storeFrame(1, dpos.z);
				}
			}
		}
	
	}
}