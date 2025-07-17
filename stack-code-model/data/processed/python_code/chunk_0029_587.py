/**
 * User: booster
 * Date: 14/08/14
 * Time: 10:56
 */
package plugs {
import medkit.collection.List;

public interface IProvider {
    function get outputs():List

    function get name():String

    function requestPullData(outputConnection:Connection):*
}
}