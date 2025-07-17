/*
 * Copyright 2010 the original author or authors.
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

package org.spicefactory.parsley.core.builder {
import org.spicefactory.parsley.core.processor.DestroyPhase;
import org.spicefactory.parsley.core.processor.InitPhase;

/**
 * Builder for applying configuration to a single property processor.
 * 
 * @author Jens Halm
 */
public interface PropertyProcessorBuilder {
	
	
	/**
	 * Specify the phase the processor should be invoked in during initialization.
	 * The default is <code>InitPhase.preInit()</code>.
	 * 
	 * @param phase the phase the processor should be invoked in during initialization
	 * @return this builder instance for method chaining
	 */
	function initIn (phase: InitPhase) : PropertyProcessorBuilder;
	
	/**
	 * Specify the phase the processor should be invoked in when the target instance
	 * gets removed from the Context.
	 * The default is <code>DestroyPhase.postDestroy()</code>.
	 * 
	 * @param phase the phase the processor should be invoked in when the target instance
	 * gets removed from the Context
	 * @return this builder instance for method chaining
	 */
	function destroyIn (phase: DestroyPhase) : PropertyProcessorBuilder;
	
	/**
	 * Indicates that the processor must read from the property.
	 * 
	 * @return this builder instance for method chaining
	 */
	function mustRead () : PropertyProcessorBuilder;
	
	/**
	 * Indicates that the processor must write to the property.
	 * 
	 * @return this builder instance for method chaining
	 */
	function mustWrite () : PropertyProcessorBuilder;
	
	/**
	 * Specifies the required type of the property configured by this processor.
	 * 
	 * @param type the required type of the property configured by this processor
	 * @return this builder instance for method chaining
	 */
	function expectType (type: Class) : PropertyProcessorBuilder;
	
	
}
}