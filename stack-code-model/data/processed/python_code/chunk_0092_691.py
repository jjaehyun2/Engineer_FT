package citrus.objects.common 
{

	import citrus.objects.CitrusSprite;
	
	public class EmitterParticle extends CitrusSprite
	{
		public var velocityX:Number = 0;
		public var velocityY:Number = 0;
		public var birthTime:Number = 0;
		public var canRecycle:Boolean = true;
		
		public function EmitterParticle(params:Object = null) 
		{
			super(params);
			if (birthTime == 0)
				birthTime = new Date().time;
		}
	}

}