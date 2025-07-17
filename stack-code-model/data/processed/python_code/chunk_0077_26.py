package rb.framework.mvc.strategies{
	/**
	 *策略规则 
	 * @author Gao.D.X
	 * 
	 */	
    public class StrategyRules {

        public static const PARENT_TO_CHILD:uint = 1;
        public static const CHILD_TO_PARENT:uint = 1 << 1;
        public static const TO_OTHER_CONTEXT:uint = 1 << 2;
        public static const MODEL_TO_MODEL:uint = 1 << 3;
        public static const MODEL_TO_VIEW:uint = 1 << 4;
        public static const MODEL_TO_CONTROLLER:uint = 1 << 5;
        public static const VIEW_TO_MODEL:uint = 1 << 6;
        public static const VIEW_TO_VIEW:uint = 1 << 7;
        public static const VIEW_TO_CONTROLLER:uint = 1 << 8;
        public static const CONTROLLER_TO_MODEL:uint = 1 << 9;
        public static const CONTROLLER_TO_VIEW:uint = 1 << 10;
        public static const CONTROLLER_TO_CONTROLLER:uint = 1 << 11;
		

     

        public function StrategyRules(){
        }

        public static function get ALL():uint{
             
            return PARENT_TO_CHILD | CHILD_TO_PARENT | TO_OTHER_CONTEXT | MODEL_TO_MODEL | MODEL_TO_VIEW | MODEL_TO_CONTROLLER | VIEW_TO_MODEL | VIEW_TO_VIEW | VIEW_TO_CONTROLLER | CONTROLLER_TO_MODEL | CONTROLLER_TO_VIEW | CONTROLLER_TO_CONTROLLER;
        }

        public static function get DEFAULT():uint{ 
            return PARENT_TO_CHILD | CHILD_TO_PARENT | TO_OTHER_CONTEXT | MODEL_TO_MODEL | MODEL_TO_CONTROLLER | VIEW_TO_VIEW | VIEW_TO_CONTROLLER | CONTROLLER_TO_MODEL | CONTROLLER_TO_VIEW | CONTROLLER_TO_CONTROLLER;
        }


    }

    
    
    
    
}//package rb.framework.mvc.strategies