//------------------------------------------------------------------------------
//  Copyright (c) 2011 the original author or authors. All Rights Reserved. 
// 
//  NOTICE: You are permitted to use, modify, and distribute this file 
//  in accordance with the terms of the license agreement accompanying it. 
//------------------------------------------------------------------------------

package org.robotlegs.v2.extensions.hooks
{
	import org.robotlegs.v2.core.utilities.pushValuesToClassVector;

	public class GuardsAndHooksConfig implements IGuardsAndHooksConfig
	{

		protected var _guards:Vector.<Class> = new Vector.<Class>();

		public function get guards():Vector.<Class>
		{
			return _guards;
		}

		protected var _hooks:Vector.<Class> = new Vector.<Class>();

		public function get hooks():Vector.<Class>
		{
			return _hooks;
		}

		public function GuardsAndHooksConfig()
		{

		}

		public function withGuards(... guardClasses):IGuardsAndHooksConfig
		{
			pushValuesToClassVector(guardClasses, _guards);
			return this;
		}

		public function withHooks(... hookClasses):IGuardsAndHooksConfig
		{
			pushValuesToClassVector(hookClasses, _hooks);
			return this;
		}
	}
}