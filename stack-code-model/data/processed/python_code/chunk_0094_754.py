package rb.framework.data{
    import rb.framework.core.*;

    public class HeapEnumerator {

        protected var heap:Heap;
        protected var bakupList:Array;
        protected var bakupCompareFunction:Function;

        public function HeapEnumerator(list:Array, compareFunction:Function){
            this.bakupList = list;
            
            this.bakupCompareFunction = compareFunction;
            
            this.reset();
            
        }

        public function get current():Object{
            
            return (this.heap.top);
        }

        public function get isEnd():Boolean{
            
            return ((this.heap == null)) || ((this.heap.count == 0));
        }

        public function moveNext():void{
            
            this.heap.remove();
            
        }

        public function reset():void{
            
            this.heap = new Heap(this.bakupCompareFunction, this.bakupList);
            
        }


    }

    
    
    
    
}//package rb.framework.data