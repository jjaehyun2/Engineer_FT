package com.IndieGo.soal {

	import flash.display.MovieClip;
	import flash.events.MouseEvent;
	import com.IndieGo.utils.Transforms;

	public class topList extends MovieClip {

		private var Trans:Transforms;
		public var TX:Object;

		public function topList(): void {

			stop();

			Trans = new Transforms( stage );
			Trans.place( this, ( stage.stageWidth + width ), y, true );
			
		}

		public function toLeft(): void {
			
			Trans.animPlace( this, -width, y, true, 1 );
			
		}

		public function toRight(): void {
			
			Trans.animPlace( this, ( stage.stageWidth + width ), y, true, 1 );
			
		}

		public function toShow(): void {
			
			Trans.animPlace( this, ( stage.stageWidth / 2 ), y, true, 1 );

		}

	}

}