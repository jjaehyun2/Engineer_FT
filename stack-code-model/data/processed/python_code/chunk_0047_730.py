//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.v2.extensions.commandMap.support
{
	import org.robotlegs.v2.extensions.commandMap.api.ICommandMapping;
	import org.robotlegs.v2.extensions.commandMap.api.ICommandTrigger;

	public class NullCommandTrigger implements ICommandTrigger
	{
		public function NullCommandTrigger()
		{
		}

		public function addMapping(mapping:ICommandMapping):void
		{
		}

		public function removeMapping(mapping:ICommandMapping):void
		{
		}
	}
}