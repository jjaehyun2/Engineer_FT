package kabam.rotmg.stage3D.graphic3D {
import kabam.rotmg.stage3D.proxies.Context3DProxy;
import kabam.rotmg.stage3D.proxies.Program3DProxy;
import kabam.rotmg.stage3D.shaders.FragmentShader;
import kabam.rotmg.stage3D.shaders.FragmentShaderRepeat;
import kabam.rotmg.stage3D.shaders.VertextShader;

public class Program3DFactory {

    public static const TYPE_REPEAT_ON:Boolean = true;

    public static const TYPE_REPEAT_OFF:Boolean = false;

    private static var instance:Program3DFactory;

    public static function getInstance():Program3DFactory {
        if (instance == null) {
            instance = new Program3DFactory("yoThisIsInternal");
        }
        return instance;
    }

    public function Program3DFactory(_arg_1:String = "") {
        super();
        if (_arg_1 != "yoThisIsInternal") {
            throw new Error("Program3DFactory is a singleton. Use Program3DFactory.getInstance()");
        }
    }
    private var repeatProgram:Program3DProxy;
    private var noRepeatProgram:Program3DProxy;

    public function dispose():void {
        if (this.repeatProgram) {
            this.repeatProgram.getProgram3D().dispose();
        }
        if (this.noRepeatProgram) {
            this.noRepeatProgram.getProgram3D().dispose();
        }
        instance = null;
    }

    public function getProgram(_arg_1:Context3DProxy, _arg_2:Boolean):Program3DProxy {
        var _local3:* = null;
        var _local4:* = _arg_2;
        switch (_local4) {
            case true:
                if (this.repeatProgram == null) {
                    this.repeatProgram = _arg_1.createProgram();
                    this.repeatProgram.upload(new VertextShader().getVertexProgram(), new FragmentShaderRepeat().getVertexProgram());
                }
                _local3 = this.repeatProgram;
                break;
            case false:
                if (this.noRepeatProgram == null) {
                    this.noRepeatProgram = _arg_1.createProgram();
                    this.noRepeatProgram.upload(new VertextShader().getVertexProgram(), new FragmentShader().getVertexProgram());
                }
                _local3 = this.noRepeatProgram;
                break;
            default:
                if (this.repeatProgram == null) {
                    this.repeatProgram = _arg_1.createProgram();
                    this.repeatProgram.upload(new VertextShader().getVertexProgram(), new FragmentShaderRepeat().getVertexProgram());
                }
                _local3 = this.repeatProgram;
        }
        return _local3;
    }
}
}