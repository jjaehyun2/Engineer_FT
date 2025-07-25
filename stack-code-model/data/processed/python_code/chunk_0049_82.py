/*
 * Copyright 2002-2009 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.springbyexample.web.flex.controller {

import com.adobe.cairngorm.control.FrontController;

import org.springbyexample.web.flex.controller.command.PersonDeleteCommand;
import org.springbyexample.web.flex.controller.command.PersonSearchCommand;
import org.springbyexample.web.flex.event.PersonDeleteEvent;
import org.springbyexample.web.flex.event.PersonSearchEvent;
        

/**
 * <p>Person controller.</p>
 * 
 * @author David Winterfeldt
 */     
public class PersonController extends FrontController {

    /**
     * Constructor
     */
    public function PersonController() {
        super();
        
        addCommand(PersonSearchEvent.EVENT_ID, PersonSearchCommand);
        addCommand(PersonDeleteEvent.EVENT_ID, PersonDeleteCommand);
    }

}

}