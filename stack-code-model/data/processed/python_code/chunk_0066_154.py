package  TowerOfHanoi
{
	import gfw.graphic.GraphicsResource;
	import flash.display.*;
	import flash.geom.*;
	import mx.core.*;

	public final class Resources
	{
		[Embed(source="assets/sprites/BtArrowLeft.png")]
		public static var BtArrowLeft:Class;
		public static var BtArrowLeftGraphics:GraphicsResource = new GraphicsResource(new BtArrowLeft());// , 4, -1, new Rectangle(0, 0, 80, 30));
		[Embed(source="assets/sprites/BtArrowUp.png")]
		public static var BtArrowUp:Class;
		public static var BtArrowUpGraphics:GraphicsResource = new GraphicsResource(new BtArrowUp());
		[Embed(source="assets/sprites/BtArrowRight.png")]
		public static var BtArrowRight:Class;
		public static var BtArrowRightGraphics:GraphicsResource = new GraphicsResource(new BtArrowRight());
		[Embed(source="assets/sprites/BtArrowDown.png")]
		public static var BtArrowDown:Class;
		public static var BtArrowDownGraphics:GraphicsResource = new GraphicsResource(new BtArrowDown());
		[Embed(source="assets/sprites/BtRestart.png")]
		public static var BtRestart:Class;
		public static var BtRestartGraphics:GraphicsResource = new GraphicsResource(new BtRestart());
		////// Sounds /////
		[Embed(source="assets/sounds/hit1.mp3")]
		public static var hit1Sound:Class;
		public static var hit1FX:SoundAsset = new hit1Sound() as SoundAsset;
		[Embed(source="assets/sounds/bump.mp3")]
		public static var bumpSound:Class;
		public static var bumpFX:SoundAsset = new bumpSound() as SoundAsset;
	}

}