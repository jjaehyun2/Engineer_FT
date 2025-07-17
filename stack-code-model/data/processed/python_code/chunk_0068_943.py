/**
 * Created by newkrok on 02/06/16.
 */
package net.fpp.pandastory.config
{
	import net.fpp.pandastory.vo.ImportParserConfigVO;
	import net.fpp.pandastory.parser.EnemyPathDataVOVectorParser;
	import net.fpp.pandastory.parser.LibraryElementDataVOVectorParser;
	import net.fpp.pandastory.parser.PolygonBackgroundVOVectorParser;
	import net.fpp.pandastory.parser.RectangleBackgroundVOVectorParser;
	import net.fpp.pandastory.vo.EnemyPathDataVO;
	import net.fpp.pandastory.vo.LibraryElementDataVO;
	import net.fpp.pandastory.vo.PolygonBackgroundVO;
	import net.fpp.pandastory.vo.RectangleBackgroundVO;

	public class ImportParserConfig
	{
		private const _rule:Vector.<ImportParserConfigVO> = new <ImportParserConfigVO>[
			new ImportParserConfigVO( new Vector.<PolygonBackgroundVO>, PolygonBackgroundVOVectorParser ),
			new ImportParserConfigVO( new Vector.<RectangleBackgroundVO>, RectangleBackgroundVOVectorParser ),
			new ImportParserConfigVO( new Vector.<EnemyPathDataVO>, EnemyPathDataVOVectorParser ),
			new ImportParserConfigVO( new Vector.<LibraryElementDataVO>, LibraryElementDataVOVectorParser )
		];

		public function get config():Object
		{
			return this._rule;
		}
	}
}