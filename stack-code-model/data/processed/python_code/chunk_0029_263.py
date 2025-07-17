package LayaAir3D_Camera {
	import common.CameraMoveScript;
	import laya.d3.core.BaseCamera;
	import laya.d3.core.Camera;
	import laya.d3.core.Sprite3D;
	import laya.d3.core.light.DirectionLight;
	import laya.d3.core.material.BaseMaterial;
	import laya.d3.core.material.SkyBoxMaterial;
	import laya.d3.core.scene.Scene3D;
	import laya.d3.math.Vector3;
	import laya.d3.math.Vector4;
	import laya.d3.math.Viewport;
	import laya.d3.resource.models.SkyBox;
	import laya.d3.resource.models.SkyRenderer;
	import laya.display.Stage;
	import laya.utils.Handler;
	import laya.utils.Stat;
	
	/**
	 * ...
	 * @author ...
	 */
	public class MultiCamera {
		private var _translate:Vector3 = new Vector3(0, 0, 1.5);
		
		public function MultiCamera() {
			//初始化引擎
			Laya3D.init(0, 0);
			Laya.stage.scaleMode = Stage.SCALE_FULL;
			Laya.stage.screenMode = Stage.SCREEN_NONE;
			//显示性能面板
			Stat.show();
			
			//创建场景
			var scene:Scene3D = Laya.stage.addChild(new Scene3D()) as Scene3D;
			
			//创建相机
			var camera1:Camera = scene.addChild(new Camera(0, 0.1, 100)) as Camera;
			//设置相机清除颜色
			camera1.clearColor = new Vector4(0.3, 0.3, 0.3, 1.0);
			camera1.transform.translate(_translate);
			//设置裁剪空间的视口
			camera1.normalizedViewport = new Viewport(0, 0, 0.5, 1.0);
			
			//创建相机
			var camera2:Camera = scene.addChild(new Camera(0, 0.1, 100)) as Camera;
			camera2.clearColor = new Vector4(0.0, 0.0, 1.0, 1.0);
			_translate.setValue(0, 0, 1.5);
			camera2.transform.translate(_translate);
			camera2.normalizedViewport = new Viewport(0.5, 0.0, 0.5, 0.5);
			//相机添加视角控制组件(脚本)
			camera2.addComponent(CameraMoveScript);
			//设置相机清除标志，使用天空
			camera2.clearFlag = BaseCamera.CLEARFLAG_SKY;
			BaseMaterial.load("res/threeDimen/skyBox/skyBox2/skyBox2.lmat", Handler.create(this, function(mat:SkyBoxMaterial):void {
				var skyRenderer:SkyRenderer = camera2.skyRenderer;
				skyRenderer.mesh = SkyBox.instance;
				skyRenderer.material = mat;
			}));
			
			//添加平行光
			var directionLight:DirectionLight = scene.addChild(new DirectionLight()) as DirectionLight;
			
			//加载资源
			Sprite3D.load("res/threeDimen/skinModel/LayaMonkey/LayaMonkey.lh", Handler.create(this, function(sp:Sprite3D):void {
				var layaMonkey:Sprite3D = scene.addChild(sp) as Sprite3D;
			}))
		
		}
	
	}

}