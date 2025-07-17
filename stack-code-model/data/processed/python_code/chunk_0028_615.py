package rb.framework.data{
    import rb.framework.events.DependencyPropertyChangeEvent;

    [Event(name="change", type="rb.framework.events.DependencyPropertyChangeEvent")]
	/**
	 *带有数据变化事件通知 对象
	 * @author Gao.D.X
	 * 
	 */	
    public class DependencyObject extends DispatcherObject {

        protected var prop:Dict;
		public var hasSet:Boolean = false;

        public function DependencyObject(){
            
            this.prop = new Dict();
            
        }
		/**
		 *取得数据
		 * @param name
		 * @param value
		 * @return 
		 * 
		 */
        protected function GET(key:String, value:Object=null):*{
            
            if (this.prop.containsKey(key)){
                
                return (this.prop.get(key));
            };
            
            return (value);
        }
		/**
		 *设置数据 
		 * @param key
		 * @param value
		 * @return 
		 * 
		 */
        protected function SET(key:String, value:Object):Boolean{
            if(!this.hasSet) this.hasSet = true;
			
            var oldValue:Object = this.prop.get(key);
            
            var _isChange:Boolean = this.prop.set(key, value);
            
            if (_isChange){
                
                this.dispatchEvent(new DependencyPropertyChangeEvent(key, oldValue, value));
            };
            
            return (_isChange);
        }


    }

    
    
    
    
}//package rb.framework.data