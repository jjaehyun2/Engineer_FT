package com.audioengine.format.pcm
{
	import flash.utils.ByteArray;

	/**
	 * @author Andre Michelle
	 */
	public class PCM16BitStereo44Khz extends PCMStrategy
		implements IPCMIOStrategy
	{
		public function PCM16BitStereo44Khz( compressionType: Object = null )
		{
			super( compressionType, 44100.0, 2, 16 );
		}
		
		public function read32BitStereo44KHz( data: ByteArray, dataOffset: Number, target : ByteArray, length : Number, startPosition : Number ) : void
		{
			data.position = dataOffset + ( startPosition << 2 );
			
			for ( var i : int = 0; i < length; i ++ )
			{
				target.writeFloat( data.readShort() * 3.051850947600e-05 ); // DIV 0x7FFF
				target.writeFloat( data.readShort() * 3.051850947600e-05 ); // DIV 0x7FFF
			}
		}
		
		public function write32BitStereo44KHz( data : ByteArray, target: ByteArray, numSamples : uint ) : void
		{
			for ( var i : int = 0 ; i < numSamples ; ++i )
			{
				const left : Number = data.readFloat() * _gain;
				
				if( left > 1.0 )
					target.writeShort( 0x7FFF );
				else
				if( left < -1.0 )
					target.writeShort( -0x7FFF );
				else
					target.writeShort( left * 0x7FFF );

				const right : Number = data.readFloat() * _gain;
				
				if( right > 1.0 )
					target.writeShort( 0x7FFF );
				else
				if( right < -1.0 )
					target.writeShort( -0x7FFF );
				else
					target.writeShort( right * 0x7FFF );
			}
		}
	}
}