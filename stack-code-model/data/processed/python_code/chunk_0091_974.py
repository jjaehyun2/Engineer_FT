package rb.framework.data.binding{
    import rb.framework.data.DependencyObject;
    import rb.framework.events.DependencyPropertyChangeEvent;
    import rb.framework.utils.ObjectUtils;

    public class DataPropertyBinding {

        protected var list:Array;

        public function DataPropertyBinding(){
            this.init();
            
        }

        protected function init():void{
            
            this.list = new Array();
            
        }

        protected function contain(relationship:BindingRelationship):Boolean{
            var r:BindingRelationship;
            
            for each (r in this.list) {
                
                if (r.source == relationship.source && r.target == relationship.target){
                    
                    return (true);
                };
            };
            
            return (false);
        }

        protected function add(relationship:BindingRelationship):Boolean{
            if (relationship.mode == BindingMode.ONE_TIME){
                return (false);
            };
            
            if (this.contain(relationship)){
                return (false);
            };
            
            if (relationship.mode == BindingMode.ONE_WAY || relationship.mode == BindingMode.TWO_WAY){
                
                relationship.source.addEventListener(DependencyPropertyChangeEvent.CHANGE, this.onObjectPropertyChange);
            };
            
            if (relationship.mode == BindingMode.TWO_WAY){
                
                (relationship.target as DependencyObject).addEventListener(DependencyPropertyChangeEvent.CHANGE, this.onObjectPropertyChange);
            };
            
            this.list.push(relationship);
            
            return (true);
        }

        protected function onObjectPropertyChange(e:DependencyPropertyChangeEvent):void{
            var r:BindingRelationship;
            
            for each (r in this.list) {
                
                if (r.mode == BindingMode.ONE_WAY){
                    
                    //unresolved if
                    //  @36 ifne @100
                    //  e.currentTarget
                    //  r.source
					if( r.source != e.currentTarget){
						continue;
					}

                };
                
                if (r.mode == BindingMode.TWO_WAY){
                    
                    //unresolved if
                    //  @63 iftrue @100
                    if( r.source != e.currentTarget&&e.target != e.currentTarget){
						continue;
					}

                };
                
				if (r.source === e.currentTarget){
					
					ObjectUtils.copyValues(r.source, r.target, r.map);
				} else {
					
					if (e.target === e.currentTarget){
						
						ObjectUtils.copyValues(r.source, r.target, r.map, true);
					};
				};
            };
            
        }

        protected function remove(source:DependencyObject, target:Object):void{
            var r:BindingRelationship;
            var needRemoveSource:Boolean = true;
            
            var needRemoveTarget:Boolean = true;
            
            for each (r in this.list) {
                
                if (r.source == source){
                    
                    needRemoveSource = false;
                };
                
                if (r.target == target && r.mode == BindingMode.TWO_WAY){
                    
                    needRemoveTarget = false;
                };
                
                if (needRemoveSource == false && needRemoveTarget == false) break;
            };
            
            if (needRemoveSource){
               if(source) source.removeEventListener(DependencyPropertyChangeEvent.CHANGE, this.onObjectPropertyChange);
            };
            
            if (needRemoveTarget && target is DependencyObject){
                (target as DependencyObject).removeEventListener(DependencyPropertyChangeEvent.CHANGE, this.onObjectPropertyChange);
            };
            
        }

        public function bind(source:DependencyObject, target:Object, map:Object, mode:uint, ... _args):Boolean{
			if(!map)
			{
				map=ObjectUtils.getMapList(source);
			}
			if(source == null ||(target == null || map == null))
			{
				return (false);
			}
//            if(source == null ||(target == null || map == null){
//				
//                return (false);
//            };
            
            var relationship:BindingRelationship = new BindingRelationship();
            
            relationship.source = source;
            
            relationship.target = target;
            
            relationship.map = map;
            
            relationship.mode = mode;
            
            relationship.args = _args;
            
            var result:Boolean = this.add(relationship);
            
            ObjectUtils.copyValues(source, target, map);
            
            return (result);
        }

        public function unbind(source:DependencyObject, target:Object):void{
            var relationship:BindingRelationship;
            var i:int = (this.list.length - 1);
            while (i >= 0) {
                
                
                relationship = this.list[i];
                
                if ((relationship.source == source && relationship.target == target)){
                    
                    this.list.splice(i, 1);
                };
                
                i--;
            };
            
            this.remove(source, target);
            
        }

        public function unbindFromSource(source:DependencyObject):void{
            var relationship:BindingRelationship;
            
            var i:int = (this.list.length - 1);
            while (i >= 0) {
                
                
                relationship = this.list[i];
                
                if (source == relationship.source){
                    
                    this.list.splice(i, 1);
                };
                
                i--;
            };
            
            this.remove(source, null);
            
        }

        public function unbindFromTarget(target:Object):void{
            var relationship:BindingRelationship;
            
            var i:int = (this.list.length - 1);
            while (i >= 0) {
                
                
                relationship = this.list[i];
                
                if (target == relationship.target){
                    
                    this.list.splice(i, 1);
                };
                
                i--;
            };
            
            this.remove(null, target);
            
        }

        public function clear():void{
            var r:BindingRelationship;
            var o:DependencyObject;
            var removeList:Array = new Array();
            
            for each (r in this.list) {
                
                if (removeList.indexOf(r.source) < 0){
                    removeList.push(r.source);
                };
                
                if (r.mode == BindingMode.TWO_WAY){
                    
                    if (removeList.indexOf(r.target) < 0){
                        removeList.push(r.target);
                    };
                };
            };
            
            for each (o in removeList) {
                
                o.removeEventListener(DependencyPropertyChangeEvent.CHANGE, this.onObjectPropertyChange);
            };
            
            this.list.splice(0, this.list.length);
            
        }


    }

    
    
    
    
}//package rb.framework.data.binding