package blackbird.protocol.api {
	import scriptor.additional.api.IDisposable;

	/**
	 * @author Aziz Zainutdin (hello at scriptor.me)
	 */
	public interface IKeepAliveTimer extends IDisposable {
		function start() : void;

		function stop() : void;

		function resetFailureTimer() : void;
	}
}