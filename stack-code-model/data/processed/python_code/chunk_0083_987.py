package devoron.data.core.serializer
{
	
	/**
	 * Serializer
	 * @author Devoron
	 */
	public class Serializer implements ICompositeSerializer
	{
		
		public function Serializer()
		{
			//set
		}
		
		/* INTERFACE devoron.data.core.serializer.ISerializer */
		
		public function serialize(any:*, ...args):String
		{
			throw new Error("No function body in Serializer.as");
			return null;
		}
		
		/* INTERFACE devoron.data.core.serializer.ICompositeSerializer */
		
		public function setSerializerShema(serializerShema:ISerializerShema):void 
		{
			
		}
	
	}

}