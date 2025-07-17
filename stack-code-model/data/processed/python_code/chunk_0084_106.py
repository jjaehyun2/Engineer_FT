package com.qcenzo.apps.album.effects
{
	public class Tile extends Effect
	{
		public function Tile()
		{
		}
		
		override protected function initCameraStat():void
		{ 
			_cmrStat.appendTranslation(0, 0, -1);
		}
		
		override protected function generateMesh(numQuads:int):void
		{
			var c:int = Math.sqrt(numQuads);
			var dy:Number = 2 / c;
			var dx:Number = _asp * dy;
			var x0:Number;
			var y0:Number;
			var z0:Number = 0; 
			var w0:Number;
			for (var i:int = 0; i < numQuads; i++)
			{
				x0 = -_asp + (i % c) * dx;
				y0 = 1 - int(i / c) * dy;
				w0 = i / numQuads;
				
				_vx[_nvx++] = x0;
				_vx[_nvx++] = y0;
				_vx[_nvx++] = z0;
				_vx[_nvx++] = w0;
				_vx[_nvx++] = x0 + dx;
				_vx[_nvx++] = y0;
				_vx[_nvx++] = z0;
				_vx[_nvx++] = w0;
				_vx[_nvx++] = x0;
				_vx[_nvx++] = y0 - dy;
				_vx[_nvx++] = z0;
				_vx[_nvx++] = w0;
				_vx[_nvx++] = x0 + dx;
				_vx[_nvx++] = y0 - dy;
				_vx[_nvx++] = z0;
				_vx[_nvx++] = w0;
			}
		}
	}
}