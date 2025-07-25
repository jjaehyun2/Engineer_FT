/*
include "../includes/License.as.inc";
 */

package temple.core.errors 
{
	import temple.core.debug.log.Log;

	/**
	 * Error thrown when a method argument is invalid.
	 * The TempleArgumentError will automatic Log the error message.
	 * 
	 * @author Thijs Broerse
	 */
	public class TempleArgumentError extends ArgumentError implements ITempleError
	{
		private var _sender:Object;
		
		/**
		 * Creates a new TempleArgumentError
		 * @param sender The object that gererated the error. If the Error is gererated in a static function, use the
		 *  toString function of the class
		 * @param message The error message
		 * @param id The id of the error
		 */
		public function TempleArgumentError(sender:Object, message:*, id:* = 0)
		{
			_sender = sender;
			super(message, id);
			
			var stack:String = getStackTrace();
			if (stack)
			{
				Log.error(stack + " id:" + id, String(sender));
			}
			else
			{
				Log.error("TempleArgumentError: '" + message + "' id:" + id, String(sender));
			}
		}
		
		/**
		 * @inheritDoc
		 */
		public function get sender():Object
		{
			return _sender;
		}
	}
}