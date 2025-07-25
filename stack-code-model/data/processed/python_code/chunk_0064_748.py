package com.splunk.controls
{

	import flash.display.DisplayObject;

	public final class Cursors
	{

		// Private Static Properties

		private static var _cursorMove:DisplayObject;
		private static var _cursorResizeN:DisplayObject;
		private static var _cursorResizeNE:DisplayObject;
		private static var _cursorResizeE:DisplayObject;
		private static var _cursorResizeSE:DisplayObject;
		private static var _cursorResizeS:DisplayObject;
		private static var _cursorResizeSW:DisplayObject;
		private static var _cursorResizeW:DisplayObject;
		private static var _cursorResizeNW:DisplayObject;

		// Public Static Getters/Setters

		public static function get MOVE() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorMove;
			if (!cursor)
			{
				cursor = Cursors._cursorMove = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,2,2,0,0,0,0,2,1,2,0,0,0,0,2,2,0,0,0,0,
					0,0,0,2,1,2,0,0,0,0,2,1,2,0,0,0,0,2,1,2,0,0,0,
					0,0,2,1,1,2,0,0,0,0,2,1,2,0,0,0,0,2,1,1,2,0,0,
					0,2,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,0,
					2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
					0,2,1,1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1,1,1,2,0,
					0,0,2,1,1,2,0,0,0,0,2,1,2,0,0,0,0,2,1,1,2,0,0,
					0,0,0,2,1,2,0,0,0,0,2,1,2,0,0,0,0,2,1,2,0,0,0,
					0,0,0,0,2,2,0,0,0,0,2,1,2,0,0,0,0,2,2,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_N() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeN;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeN = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_NE() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeNE;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeNE = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,2,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,2,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_E() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeE;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeE = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,
					0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,
					0,0,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,
					0,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,0,
					2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
					0,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,0,
					0,0,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,
					0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,
					0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_SE() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeSE;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeSE = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,2,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,2,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_S() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeS;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeS = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,2,2,2,1,2,2,2,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_SW() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeSW;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeSW = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,2,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,2,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_W() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeW;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeW = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,
					0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,
					0,0,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,
					0,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,0,
					2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,
					0,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,0,
					0,0,2,1,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,
					0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,
					0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

		public static function get RESIZE_NW() : DisplayObject
		{
			var cursor:DisplayObject = Cursors._cursorResizeNW;
			if (!cursor)
			{
				cursor = Cursors._cursorResizeNW = CursorUtils.createBitmapCursor([
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,1,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,1,2,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,2,2,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,0,0,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,0,2,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,2,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
					0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
					], [0x00000000,0xFFFFFFFF,0xFF000000], 11, 11);
			}
			return cursor;
		}

	}

}