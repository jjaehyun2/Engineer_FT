package com.does.lotte.object.character {
	import com.does.lotte.global.User;

	import flash.display.Bitmap;
	import flash.display.Sprite;
	import flash.events.Event;

	/**
	 * @author chaesumin
	 */
	public class CharacterProfile extends Sprite {
		public function CharacterProfile() {
			addEventListener(Event.ADDED_TO_STAGE, initAddStage);
			addEventListener(Event.REMOVED_FROM_STAGE, initRemoveStage);
			init();
		}

		private function initAddStage(event : Event) : void {
			removeEventListener(Event.ADDED_TO_STAGE, initAddStage);
			start();
		}

		private function initRemoveStage(event : Event) : void {
			removeEventListener(Event.REMOVED_FROM_STAGE, initRemoveStage);
		}

		private function init() : void {
			var bitmap : Bitmap = User.getUserProfile();
			if (bitmap) {
				addChild(bitmap);
			}
		}

		private function start() : void {
		}
	}
}