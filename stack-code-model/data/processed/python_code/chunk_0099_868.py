package RiddleStrip 
{
	import gfw.graphic.GraphicsResource;
	import gfw.core.GameObject;
	/**
	 * ...
	 * @author jk
	 */
	public class Picture extends GameObject
	{
		
		public function Picture() 
		{
			
		}
		public function SetGraphic(gr: GraphicsResource):void {
			this.m_Graphic = gr;
			this.width = this.m_Graphic.drawRect.width;
			this.height = this.m_Graphic.drawRect.height;
		}
		
	}

}