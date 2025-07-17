/**
 * Created with IntelliJ IDEA.
 * User: mobitile
 * Date: 10/17/13
 * Time: 7:25 PM
 * To change this template use File | Settings | File Templates.
 */
package skein.rest.core
{
import skein.rest.core.coding.DefaultCoding;
import skein.rest.core.coding.JSONCoding;
import skein.rest.core.coding.MultipartFormCoding;
import skein.rest.core.coding.WWWFormCoding;

public class Encoder
{
    public static function forType(contentType:String):Function
    {
        switch (contentType)
        {
            case "application/json" :
                return JSONCoding.encode;
                break;

            case "application/x-www-form-urlencoded" :
                return WWWFormCoding.encode;
                break;

            case "multipart/form-data":
                return MultipartFormCoding.encode;
                break;

            default :
                return DefaultCoding.encode;
                break;
        }
    }

}
}