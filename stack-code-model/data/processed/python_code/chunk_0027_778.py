package integration.commandPooling.testObj.controller {
import integration.commandPooling.CommandPoolingTests;
import integration.commandPooling.testObj.CommPoolingDependencyProxy;

import mvcexpress.mvc.PooledCommand;

/**
 * CLASS COMMENT
 * @author Raimundas Banevicius (http://mvcexpress.org/)
 */
public class CommPoolingLockedFailCommand extends PooledCommand {

	static public var test:String = "aoeuaoeu";

	static public var executedProxyNames:String = "";

	[Inject]
	public var dependency:CommPoolingDependencyProxy;

	public function CommPoolingLockedFailCommand() {
		super();
	}

	public function execute(blank:Object):void {
		lock();
		CommPoolingLockedFailCommand.executedProxyNames += dependency.proxyName;
		sendMessage(CommandPoolingTests.EXECUTE_REMOVED_DEPENDENCY_COMMAND, CommPoolingDependencyProxy);
		unlock();
	}

}
}