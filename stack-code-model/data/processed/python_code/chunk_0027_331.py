package LayaAir3D_Physics3D {
	import laya.d3.core.Camera;
	import laya.d3.core.MeshSprite3D;
	import laya.d3.core.Sprite3D;
	import laya.d3.core.Transform3D;
	import laya.d3.core.light.DirectionLight;
	import laya.d3.core.material.BlinnPhongMaterial;
	import laya.d3.core.scene.Scene3D;
	import laya.d3.math.Vector3;
	import laya.d3.math.Vector4;
	import laya.d3.math.Matrix4x4;
	import laya.d3.physics.PhysicsCollider;
	import laya.d3.physics.Rigidbody3D;
	import laya.d3.physics.shape.BoxColliderShape;
	import laya.d3.physics.shape.CapsuleColliderShape;
	import laya.d3.physics.shape.SphereColliderShape;
	import laya.d3.resource.models.PrimitiveMesh;
	import laya.display.Stage;
	import laya.events.KeyBoardManager;
	import laya.utils.Handler;
	import laya.utils.Stat;
	import laya.resource.Texture2D;
	
	public class PhysicsWorld_Kinematic {
		
		private var scene:Scene3D;
		private var camera:Camera;
		private var kinematicSphere:Sprite3D;
		private var translateW:Vector3 = new Vector3(0, 0, -0.2);
		private var translateS:Vector3 = new Vector3(0, 0, 0.2);
		private var translateA:Vector3 = new Vector3(-0.2, 0, 0);
		private var translateD:Vector3 = new Vector3(0.2, 0, 0);
		private var translateQ:Vector3 = new Vector3(-0.01, 0, 0);
		private var translateE:Vector3 = new Vector3(0.01, 0, 0);
		
		private var mat1:BlinnPhongMaterial;
		private var mat3:BlinnPhongMaterial;
		
		public function PhysicsWorld_Kinematic() {
			Laya3D.init(0, 0, null);
			Laya.stage.scaleMode = Stage.SCALE_FULL;
			Laya.stage.screenMode = Stage.SCREEN_NONE;
			Stat.show();
			scene = Laya.stage.addChild(new Scene3D()) as Scene3D;
			
			camera = scene.addChild(new Camera(0, 0.1, 100)) as Camera;
			camera.transform.translate(new Vector3(0, 8, 20));
			camera.transform.rotate(new Vector3(-30, 0, 0), true, false);
			camera.clearColor = null;
			
			var directionLight:DirectionLight = scene.addChild(new DirectionLight()) as DirectionLight;
			directionLight.color = new Vector3(1, 1, 1);
			//设置平行光的方向
			var mat:Matrix4x4 = directionLight.transform.worldMatrix;
			mat.setForward(new Vector3(-1.0, -1.0, 1.0));
			directionLight.transform.worldMatrix=mat;
			
			mat1 = new BlinnPhongMaterial();
			mat3 = new BlinnPhongMaterial();
			//加载纹理资源
			Texture2D.load("res/threeDimen/Physics/rocks.jpg", Handler.create(this, function(tex:Texture2D):void {
				mat1.albedoTexture = tex;
			}));
			
			Texture2D.load("res/threeDimen/Physics/wood.jpg", Handler.create(this, function(tex:Texture2D):void {
				mat3.albedoTexture = tex;
			}));
			
			var plane:MeshSprite3D = scene.addChild(new MeshSprite3D(PrimitiveMesh.createPlane(20, 20, 10, 10))) as MeshSprite3D;
			var planeMat:BlinnPhongMaterial = new BlinnPhongMaterial();
			Texture2D.load("res/threeDimen/Physics/wood.jpg", Handler.create(this, function(tex:Texture2D):void {
				planeMat.albedoTexture = tex;
			}));
			planeMat.tilingOffset = new Vector4(2, 2, 0, 0);
			plane.meshRenderer.material = planeMat;
			
			var rigidBody:PhysicsCollider = plane.addComponent(PhysicsCollider) as PhysicsCollider;
			var boxShape:BoxColliderShape = new BoxColliderShape(20, 0, 20);
			rigidBody.colliderShape = boxShape;
			
			for (var i:int = 0; i < 60; i++) {
				addBox();
				addCapsule();
			}
			
			addKinematicSphere();
		}
		
		public function addKinematicSphere():void {
			var mat2:BlinnPhongMaterial = new BlinnPhongMaterial();
			Texture2D.load("res/threeDimen/Physics/plywood.jpg", Handler.create(this, function(tex:Texture2D):void {
				mat2.albedoTexture = tex;
			}));
			var albedoColor:Vector4 = mat2.albedoColor;
			albedoColor.setValue(1.0, 0.0, 0.0, 1.0);
			mat2.albedoColor = albedoColor;
			
			var radius:Number = 0.8;
			var sphere:MeshSprite3D = scene.addChild(new MeshSprite3D(PrimitiveMesh.createSphere(radius))) as MeshSprite3D;
			sphere.meshRenderer.material = mat2;
			var pos:Vector3 = sphere.transform.position;
			pos.setValue(0, 0.8, 0);
			sphere.transform.position = pos;
			//创建刚体碰撞器
			var rigidBody:Rigidbody3D = sphere.addComponent(Rigidbody3D);
			//创建球型碰撞器
			var sphereShape:SphereColliderShape = new SphereColliderShape(radius);
			//设置刚体碰撞器的形状为球型
			rigidBody.colliderShape = sphereShape;
			//设置刚体为Kinematic，仅可通过transform属性移动物体
			rigidBody.isKinematic = true;
			//rigidBody.detectCollisions = false;
			
			kinematicSphere = sphere;
			Laya.timer.frameLoop(1, this, onKeyDown);
		}
		
		private function onKeyDown():void {
			KeyBoardManager.hasKeyDown(87) && kinematicSphere.transform.translate(translateW);//W
			KeyBoardManager.hasKeyDown(83) && kinematicSphere.transform.translate(translateS);//S
			KeyBoardManager.hasKeyDown(65) && kinematicSphere.transform.translate(translateA);//A
			KeyBoardManager.hasKeyDown(68) && kinematicSphere.transform.translate(translateD);//D
			KeyBoardManager.hasKeyDown(81) && kinematicSphere.transform.translate(translateQ);//Q
			KeyBoardManager.hasKeyDown(69) && kinematicSphere.transform.translate(translateE);//E
		}
		
		public function addBox():void {
			var sX:int = Math.random() * 0.75 + 0.25;
			var sY:int = Math.random() * 0.75 + 0.25;
			var sZ:int = Math.random() * 0.75 + 0.25;
			var box:MeshSprite3D = scene.addChild(new MeshSprite3D(PrimitiveMesh.createBox(sX, sY, sZ))) as MeshSprite3D;
			box.meshRenderer.material = mat1;
			var transform:Transform3D = box.transform;
			var pos:Vector3 = transform.position;
			pos.setValue(Math.random() * 4 - 2, 2, Math.random() * 4 - 2);
			transform.position = pos;
			var rotationEuler:Vector3 = transform.rotationEuler;
			rotationEuler.setValue(Math.random() * 360, Math.random() * 360, Math.random() * 360);
			transform.rotationEuler = rotationEuler;
			
			var rigidBody:Rigidbody3D = box.addComponent(Rigidbody3D);
			var boxShape:BoxColliderShape = new BoxColliderShape(sX, sY, sZ);
			rigidBody.colliderShape = boxShape;
			rigidBody.mass = 10;
		}
		
		public function addCapsule():void {
			var raidius:int = Math.random() * 0.2 + 0.2;
			var height:int = Math.random() * 0.5 + 0.8;
			var capsule:MeshSprite3D = scene.addChild(new MeshSprite3D(PrimitiveMesh.createCapsule(raidius, height))) as MeshSprite3D;
			capsule.meshRenderer.material = mat3;
			var transform:Transform3D = capsule.transform;
			var pos:Vector3 = transform.position;
			pos.setValue(Math.random() * 4 - 2, 2, Math.random() * 4 - 2);
			transform.position = pos;
			var rotationEuler:Vector3 = transform.rotationEuler;
			rotationEuler.setValue(Math.random() * 360, Math.random() * 360, Math.random() * 360);
			transform.rotationEuler = rotationEuler;
			
			var rigidBody:Rigidbody3D = capsule.addComponent(Rigidbody3D);
			var sphereShape:CapsuleColliderShape = new CapsuleColliderShape(raidius, height);
			rigidBody.colliderShape = sphereShape;
			rigidBody.mass = 10;
		}
	}
}