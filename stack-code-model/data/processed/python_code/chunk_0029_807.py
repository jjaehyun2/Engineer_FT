/**
 * Copyright (C) 2008 Darshan Sawardekar.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
 
package org.puremvc.as3.multicore.utilities.fabrication.patterns.command.undoable.test {
    import org.puremvc.as3.multicore.interfaces.ICommand;
    import org.puremvc.as3.multicore.interfaces.INotification;
    import org.puremvc.as3.multicore.patterns.observer.Notification;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.SimpleFabricationCommand;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.test.AbstractFabricationCommandTest;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.undoable.*;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.observer.FabricationNotification;

    /**
	 * @author Darshan Sawardekar
	 */
	public class FabricationUndoCommandTest extends AbstractFabricationCommandTest {

        [Test]
		public function fabricationUndoCommandHasValidType():void {
			assertType(FabricationUndoCommand, command);
			assertType(SimpleFabricationCommand, command);
		}

        [Test]
		public function fabricationUndoCommandInvokesUndoOnFacadeWithNoArgsWhenStepsAreNotSpecified():void {
			facade.mock.method("undo").withArgs(1).once;

			executeCommand();

			verifyMock(facade.mock);
		}

        [Test]
		public function fabricationUndoCommandInvokesUndoOnFacadeWithSpecifiedStepsWhenStepsAreSpecified():void {
			notification.setBody(5);
			facade.mock.method("undo").withArgs(5).once;
			executeCommand();
			verifyMock(facade.mock);
		}

		override public function createCommand():ICommand {
			return new FabricationUndoCommand();
		}
		
		override public function createNotification():INotification {
			return new Notification(FabricationNotification.UNDO);
		}
		

		
	}
}