package com.marioretana.checkersgame {
	/**
	 * Holds information about the game resources and rules that is used for multiple purposes.
	 * @author Mario Retana <maretanar@gmail.com>
	 */
	public class GlobalConfiguration {
		
		/**
		 * The width of the game tiles in pixels.
		 */
		public static const TILE_WIDTH:int = 32;
		/**
		 * The height of the game tiles in pixels.
		 */
		public static const TILE_HEIGHT:int = 32;
		/**
		 * The width of the game stage in pixels.
		 */
		public static const STAGE_WIDTH:int = 320;
		/**
		 * The height of the game stage in pixels.
		 */
		public static const STAGE_HEIGHT:int = 320;
		/**
		 * The alpha value of a chip when it is moved by a user.
		 */
		public static const CHIP_USER_MOVED_ALPHA:Number = 0.7;
		/**
		 * Minimum X value in stage coordinates that a chip that is in play can have.
		 */
		public static const LEFT_BORDER:Number = 32;
		/**
		 * Maximum X value in stage coordinates that a chip that is in play can have.
		 */
		public static const RIGHT_BORDER:Number = 288;
		/**
		 * Minimum Y value in stage coordinates that a chip that is in play can have.
		 */
		public static const TOP_BORDER:Number = 32;
		/**
		 * Maximum Y value in stage coordinates that a chip that is in play can have.
		 */
		public static const BOTTOM_BORDER:Number = 288;
				
	}
}