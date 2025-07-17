/**
 * User: booster
 * Date: 15/08/14
 * Time: 10:15
 */
package plugs.error {

public class PullingDataNotSupportedError extends Error {
    public function PullingDataNotSupportedError(message:* = "pulling data model is not supported", id:* = 0) {
        super(message, id);
    }
}
}