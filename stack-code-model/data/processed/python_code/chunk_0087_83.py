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

package org.puremvc.as3.multicore.utilities.fabrication.patterns.command.routing.test {
    import org.puremvc.as3.multicore.interfaces.ICommand;
    import org.puremvc.as3.multicore.interfaces.INotification;
    import org.puremvc.as3.multicore.patterns.observer.Notification;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IRouter;
    import org.puremvc.as3.multicore.utilities.fabrication.interfaces.IRouterMessage;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.SimpleFabricationCommand;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.routing.*;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.command.test.AbstractFabricationCommandTest;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.observer.RouterNotification;
    import org.puremvc.as3.multicore.utilities.fabrication.patterns.observer.TransportNotification;
    import org.puremvc.as3.multicore.utilities.fabrication.routing.mock.RouterMock;
    import org.puremvc.as3.multicore.utilities.fabrication.vo.ModuleAddress;

    /**
     * @author Darshan Sawardekar
     */
    public class RouteNotificationCommandTest extends AbstractFabricationCommandTest {

        public var router:RouterMock;


        [Test]
        public function routeNotificationCommandHasValidType():void
        {
            assertType(RouteNotificationCommand, command);
            assertType(SimpleFabricationCommand, command);
        }

        [Test]
        public function routeNotificationCommandPicksUpDefaultRouteFromFabricationIfDestinationIsNotSpecified():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo(null);

            fabrication.mock.property("defaultRoute").returns("R/R0/INPUT").once;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertEquals("R/R0/INPUT", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandUsesStaticAllRouteIfNoDestinationIsProvidedAndNoDefaultDestinationWasAlsoNotPresent():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo(null);

            fabrication.mock.property("defaultRoute").returns(null).once;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertEquals("*", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }


        [Test]
        public function routeNotificationCommandDoesNotSuffixInputPipeNameToAllRoute():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("*");

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertNotContained(ModuleAddress.INPUT_SUFFIX, message.getTo());
                        assertEquals("*", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandDoesNotSuffixInputPipeNameIfInputPipeNameIsAlreadySpecified():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("D/D0/INPUT");

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertEquals("D/D0/INPUT", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandDoesNotSuffixInputPipeNameIfInstanceDestinationToAllIsPresent():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("D/*");

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertNotContained(ModuleAddress.INPUT_SUFFIX, message.getTo());
                        assertEquals("D/*", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routNotificationCommandDoesNotSuffixInputPipeNameIfDestinationIsAModuleGroup():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("myGroup");

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        return message.getTo() == "myGroup";
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandAddsInputSuffixIfInputSuffixIsNotSpecifiedOnModuleAddressWithClassAndInstanceName():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("D/D0");

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertContained(ModuleAddress.INPUT_SUFFIX, message.getTo());
                        assertEquals("D/D0/INPUT", message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotficationCommandUsesInputPipeFromModuleAddressObjectIfPresent():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            var moduleAddress:ModuleAddress = new ModuleAddress("R", "R0");
            transport.setTo(moduleAddress);

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertContained(ModuleAddress.INPUT_SUFFIX, message.getTo());
                        assertEquals(moduleAddress.getInputName(), message.getTo());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandSetsValidMessageFromSourceAddress():void
        {
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getFrom());
                        assertType(String, message.getFrom());
                        assertEquals("Z/Z1/OUTPUT", message.getFrom());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandSavesTransportNotificationOnTheRouterMessage():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;

            fabrication.mock.property("defaultRoute").returns(null).never;
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        assertNotNull(message.getTo());
                        assertType(String, message.getTo());
                        assertEquals(transport, message.getNotification());
                        return true;
                    }
                    ).once;

            executeCommand();

            verifyMock(fabrication.mock);
            verifyMock(router.mock);
        }

        [Test]
        public function routeNotificationCommandAddsModuleGroupSuffixToPlainInstanceInGroupRoute():void
        {
            var transport:TransportNotification = notification.getBody() as TransportNotification;
            transport.setTo("X/#");

            fabrication.mock.property("defaultRoute").returns(null).never;
            fabrication.mock.property("moduleGroup").returns("myGroup").atLeast(1);
            router.mock.method("route").withArgs(
                    function(message:IRouterMessage):Boolean
                    {
                        return message.getTo() == "X/#myGroup";
                    }
                    ).once;

            executeCommand();

            verifyMock(router.mock);
            verifyMock(fabrication.mock);
        }

        [Before]
        override public function setUp():void
        {
            router = new RouterMock();
            super.setUp();

            facade.mock.method("getFabrication").withNoArgs.returns(fabrication).atLeast(1);
            fabrication.mock.property("moduleAddress").returns(new ModuleAddress("Z", "Z1")).atLeast(1);
            fabrication.mock.property("router").returns(router);
            fabrication.mock.property("router").withArgs(IRouter);
        }

        override public function createCommand():ICommand
        {
            return new RouteNotificationCommand();
        }

        override public function createNotification():INotification
        {
            var transport:TransportNotification = new TransportNotification(
                    "changeNote", "changeBody", "changeType", "*"
                    );

            return new Notification(RouterNotification.SEND_MESSAGE_VIA_ROUTER, transport);
        }

    }
}