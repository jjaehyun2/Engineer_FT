package rb.framework.data{
    
	/**
	 *链表。 
	 * @author Gao.D.X
	 * 
	 */
    public class CollectionEnumerator {

        protected var itemsList:Array;
        protected var cursor:int;

        public function CollectionEnumerator(list:Array){
            
            this.itemsList = list;
            
            this.reset();
            
        }

        public function get current():Object{
            
            return (this.itemsList[this.cursor]);
        }

        public function get isEnd():Boolean{
            
            if (this.itemsList == null){
                return (true);
            };
            
            if (this.itemsList.length == 0){
                return (true);
            };
            
            if (this.cursor >= this.itemsList.length){
                return (true);
            };
            
            return (false);
        }

        public function moveNext():void{
            
            this.cursor++;
            
        }

        public function reset():void{
            
            this.cursor = 0;
            
        }


    }

    
    
    
    
}//package rb.framework.data