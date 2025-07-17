package rb.framework.data{
	public class Enum {
		
		public function Enum(){
			
			
		}
		
		public static function set(source:uint, value:uint, containValue:Boolean=true):uint{
			
			
			
			
			
			
			if (containValue){
				
				return ((source | value));
			};
			
			if (contain(source, value)){
				
				return ((source ^ value));
			};
			
			return (source);
		}
		
		public static function contain(source:uint, value:uint):Boolean{
			
			
			
			
			
			return (source & value) == value;
		}
		  
		
		
	}
	
	
	
	
	
}//package hs.framework.reflection