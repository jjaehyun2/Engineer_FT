package com.adrienheisch.neuralnetwork 
{
	
	import flash.display.MovieClip;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class Neuron extends MovieClip 
	{

		public static var list: Vector.<Neuron> = new Vector.<Neuron>();
		
		public var network: NeuralNetwork;
		public var output: Number = 0;
		
		public function Neuron() 
		{
			super();
			
			stop();
			
			list.push(this);
		}
		
		public function refresh(): void {
			if (output) gotoAndStop(2);
			else gotoAndStop(1);
		}
		
		public function destroy(): void {
			list.splice(list.indexOf(this), 1);
			if (parent != null) parent.removeChild(this);
		}

	}
	
}