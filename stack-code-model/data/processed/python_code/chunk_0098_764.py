package rb.framework.mvc{ 
 
    import laya.display.Node;
    import laya.display.Sprite;
    import laya.utils.Dictionary;
	
	
//	

	/**
	 * AbstractLayer 虚化层大多数Controller与View均继承于此
	 * <br/>
	 * 子类主要继承扩展onInit，onAdd，onRemove
	 * @author Gao.D.X
	 * 
	 * 
	 */	
    public class AbstractLayer {

        protected var _type:uint;
        protected var _context:GameContext;
        protected var _handlers:Dictionary;
        protected var _actived:Boolean;
		protected var UIs:Array=new Array();
        public function AbstractLayer() { 
            this.init();
            
        }
		/**
		 *设置上下文 
		 * @param value
		 * 
		 */		
        internal function setContext(value:GameContext):void{
            this._context = value;
            
        }
		/**
		 *设置类型，主要为 
		 * LayerTypes.NONE 0
		 * LayerTypes.MODEL 1
		 * LayerTypes.CONTROLLER 2
		 * LayerTypes.VIEW 3
		 * 
		 * @param value
		 * @see rb.framework.mvc.core.LayerTypes
		 * 
		 */		
        public function setType(value:uint):void{
            this._type = value;
            
        }
		/**
		 * 结构体内呼叫初始化
		 */
        final protected function init():void{
            this._handlers = new Dictionary();
            
            this.onInit();
            
        }
		/**
		 * 结构化时初始化函数继承
		 */
        protected function onInit():void{
        }
		/**
		 * 当被加入Context时进行调用
		 * @see rb.framework.mvc.Context.addLayer();
		 */
        public function onAdd():void{
        }
		/**
		 * 当被剔除Context时进行调用
		 * @see rb.framework.mvc.Context.removeLayer();
		 */
        public function onRemove():void {
			//Debug.log("remove::" + getQualifiedClassName(this));
			this.clearHandlers();
			if(UIs.length>0){
				for(var i:int=0;i<UIs.length;i++){
					UIs[i].removeSelf();
				}
				UIs=[];
			}
        }
		protected function addUI(gui:Node):void{
			//UIs.push(QuickUtils.AddPopBack(Main.ui));
			QuickUtils.AddCenter(gui as Sprite,Main.ui);
			UIs.push(gui);
			
		}
		/**
		 * 接受通知策略中注册的handler函数执行
		 * @param	msg
		 * @see rb.framework.mvc.strategies.notifyHandle()
		 */
        final public function execute(msg:Message):void{

//            if (this._handlers.indexOf(msg.name)==-1){
//                return;
//            };
            
            var handler:Function = this._handlers.get(msg.name);

            if (handler)handler.call(this, msg);
            
        }
		/**
		 * 通过上下文进行内部消息通知
		 * @param	name 消息名字
		 * @param	type 消息方式：主要区分是直接还是序列队伍模式
		 * @param	... _args
		 * @return
		 */
        public function notify(name:String, type:String, ... _args):Message
		{
            var msg:Message = new Message(name, type, this, _args);
			
			
            if (this.context != null){
                this.context.notify(msg);
            };
            
            return (msg);
        }

        protected function addHandler(name:String, handler:Function):void{
             
            
            if (this._handlers.indexOf(name)>=0){
                return;
            }
            
            this._handlers.set(name, handler);
			GameContext.addHandler(name,this);
            
        }

        protected function removeHandler(name:String, handler:Function):void{
             
            
            if (this._handlers.indexOf(name)<0){
                return;
            }
            
            this._handlers.remove(name);
			GameContext.removeHandler(name,this);
        }

        public function clearHandlers():void{
            
            
            
            this._handlers.clear();
            
        }

        public function get type():uint{
            
            
            
            return (this._type);
        }

        public function get context():GameContext
		{
            return (this._context);
        }

        public function get actived():Boolean{
            
            
            
            return (this._actived);
        }

        public function set actived(value:Boolean):void{
            
            
            
            
            this._actived = value;
            
        }


    }

    
    
    
    
}//package rb.framework.mvc