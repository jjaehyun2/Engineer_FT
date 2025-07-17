package com.adrienheisch.neuralnetwork 
{
	
	import flash.display.MovieClip;
	
	/**
	 * ...
	 * @author Adrien Heisch
	 */
	public class OutputNeuron extends NotInputNeuron 
	{
		
		public function OutputNeuron() 
		{
			super();
			
		}
		
		override protected function inputFormula(pIndex:int):Number 
		{
			return (1 / (1 + (Math.pow(Math.E, -inputLayer[pIndex].output)))) * weigths[pIndex];
		}
		
		override protected function setOutput(pInput:Number):void 
		{
			output = (pInput >= threshhold ? 1 : 0);
		}

	}
	
}