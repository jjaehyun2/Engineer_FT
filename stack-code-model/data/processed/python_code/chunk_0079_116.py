package rb.framework.data{

    public class NodeEnumerator {

        protected var sourceNode:Node;
        protected var currentNode:Node;

        public function NodeEnumerator(node:Node){
            
            this.sourceNode = node;
            
            this.reset();
            
        }

        public function get current():Object{
            
            return (this.currentNode);
        }

        public function get isEnd():Boolean{
            
            return this.currentNode == null;
        }

        public function moveNext():void{
            
            if (this.currentNode == null){
                return;
            };
            
            if (this.currentNode.firstChild != null){
                
                this.currentNode = this.currentNode.firstChild;
                
                return;
            };
            
            if (this.currentNode.next != null){
                
                this.currentNode = this.currentNode.next;
                
                return;
            };
            
            if (this.currentNode.parent != null && this.currentNode.parent != this.sourceNode){
                
                if (this.currentNode.parent.next != null){
                    
                    this.currentNode = this.currentNode.parent.next;
                    
                    return;
                };
            };
            
            this.currentNode = null;
            
        }

        public function reset():void{
            
            this.currentNode = this.sourceNode;
            
        }


    }

    
    
    
    
}//package rb.framework.data