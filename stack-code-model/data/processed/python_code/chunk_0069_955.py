package rb.framework.data.binding{
    import rb.framework.errors.SingletonError;
    import rb.framework.data.DependencyObject;
	/**
	 *绑定类 范例
	 * <br/>
	 * <br/>	Binding.bind(someDepencyObject, this, {
       <br/>         	rolename:"rolename",
       <br/>         	headImageUrl:"headImageUrl",
       <br/>         	sex:"sex",
       <br/>         	coins:"coins",vip:"vip"
       <br/>     }, BindingMode.ONE_WAY); 
	 * @author Gao.D.X
	 * 
	 */
    public class Binding {

        private static var _instance:Binding;

        protected var _methods:Array;
 

        public function Binding(){
            if (_instance != null){
                throw (new SingletonError(this));
            };
            
            _instance = this;
            
            this.init();
            
        }

        private static function get instance():Binding{
            
            if (_instance == null){
                _instance = new (Binding)();
            };
            
            return (_instance);
        }

        public static function bind(source:DependencyObject, target:Object, map:Object, mode:uint, ... _args):Boolean{
            _args.splice(0, 0, source, target, map, mode);
            
            return (instance.bind.apply(_instance, _args));
        }

        public static function unbind(source:DependencyObject, target:Object):void{
            
            instance.unbind(source, target);
            
        }

        public static function unbindFromSource(source:DependencyObject):void{
            instance.unbindFromSource(source);
            
        }

        public static function unbindFromTarget(target:Object):void{
            instance.unbindFromTarget(target);
            
        }

        public static function clear():void{
            
            instance.clear();
            
        }

        public static function get methods():Array{
            
            return (instance._methods);
        }


        protected function init():void{
            
            this._methods = new Array();
            
            this._methods.push(new DataPropertyBinding());
            
        }

        public function bind(source:DependencyObject, target:Object, map:Object, mode:uint, ... _args):Boolean{
            var method:IBindingMethod;
            var result:Boolean;
            
            _args.splice(0, 0, source, target, map, mode);
            
            for each (method in this._methods) {
                
                if (method.bind.apply(method, _args)){
                    
                    result = true;
                    
                    break;
                };
            };
            
            return (result);
        }

        public function unbind(source:DependencyObject, target:Object):void{
            var method:IBindingMethod;
            for each (method in this._methods) {
                
                method.unbind(source, target);
            };
            
        }

        public function unbindFromSource(source:DependencyObject):void{
            var method:IBindingMethod;
            
            for each (method in this._methods) {
                
                method.unbindFromSource(source);
            };
            
        }

        public function unbindFromTarget(target:Object):void{
            var method:IBindingMethod;
            
            for each (method in this._methods) {
                
                method.unbindFromTarget(target);
            };
            
        }

        public function clear():void{
            var method:IBindingMethod;
            for each (method in this._methods) {
                
                method.clear();
            };
            
        }


    }

    
    
    
    
}//package rb.framework.data.binding