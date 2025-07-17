package org.openPyro.effects
{
	import flash.display.DisplayObject;
	
	/**
	 * The EffectDescriptor class is an object that can be passed 
	 * to an Effect class to execute.Unlike Flex's effects which can 
	 * only operate on UIComponents and are therefore tied to
	 * them, OpenPyro effects are executed based on EffectDescriptors, 
	 * so are decoupled from the framework.
	 */ 
	
	public class EffectDescriptor
	{
		public var target:DisplayObject;
		public var duration:Number;
		public var properties:Object
		public var beforeStart:Function;
		public var onComplete:Function;
		public var onCancel:Function;
		public var transition:String = "linear";
		
		public function EffectDescriptor(target:DisplayObject = null, 
										duration:Number = NaN, 
										properties:Object = null,
										beforeStart:Function = null,
										onComplete:Function = null)
		{
			this.target = target;
			this.duration = duration;
			this.properties = properties;
			this.beforeStart = beforeStart;
			this.onComplete = onComplete;
		}
		
		public function setProperty(pty:String, value:*):void{
			if(!properties){
				properties = {};
			}
			properties[pty] = value;
		}

	}
}