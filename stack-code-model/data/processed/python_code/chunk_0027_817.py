package framework.core.utils
{
	import flash.net.SharedObject;
	
	import services.vo.frontend.UserProfileVO;
	
	import h2olib.helpers.SharedObjectHelper;

    /**
     * The SharedObjectHelperUtils class is used for ..
     *
     * @author Anton Kirzyk / Ramada
     * @version $Revision 1.0 $ $Date: 2009/09/19
     */
	public class UtilsSharedObject extends SharedObjectHelper
	{
		public function UtilsSharedObject()
		{
			super();
		}
		
        /**
         * Loads login data from shared object
         *
         * @return LoginDataObject
         */
        public static function loadLoggedInUserVO(defaultLogin:String, defaultPassword:String = ""):UserProfileVO {
            var result:UserProfileVO;
            var so:SharedObject = SharedObject.getLocal("loginInfo");

            result = new UserProfileVO();
            if (so.size > 0) 
            {
                result.sUserLogin = so.data["login"];
               // result.sUserPassword = so.data["password"];
                //result.rememberPassword = so.data["rememberPassword"];
            }
            else
            {
                result.sUserLogin = defaultLogin;
                result.sUserPassword = defaultPassword;	
            }
            
            return result;
        }

        public static function saveLoggedInUserVO(value:UserProfileVO):void {
            if (!value) return;

            var so:SharedObject = SharedObject.getLocal("loginInfo");
            so.data["login"] = value.sUserLogin;
           // so.data["password"] = value.sUserPassword;
            //so.data["password"] = (value.rememberPassword ? value.passwordForSave : "");
            //so.data["rememberPassword"] = value.rememberPassword;
            so.flush();            
            // load user shared object
            userSharedObject = SharedObject.getLocal("loginInfo");
        }
		
		
	}
}