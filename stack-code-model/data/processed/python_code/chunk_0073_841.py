package danmaq.mmga.components
{

	import danmaq.mmga.state.CStateInitialize;
	import danmaq.nineball.core.component.context.CContext;
	
	import flash.events.Event;
	
	import spark.components.Group;
	
	/**
	 * アプリケーションのメイン ロジック クラス。
	 * 
	 * @author Mc(danmaq)
	 */
	public final class CMMGAMain extends Group
	{
		
		//* constants ──────────────────────────────-*
		
		/** 状態による制御AI。 */
		private static var _context:CContext;

		//* constructor & destructor ───────────────────────*
		
		/**
		 * コンストラクタ。
		 */
		public function CMMGAMain()
		{
			if(_context == null)
			{
				_context = new CContext(CStateInitialize.instance, this);
				addEventListener(Event.ENTER_FRAME, _context.updateFromEvent);
			}
		}

		//* class properties ───────────────────────────*
		
		/**
		 * 状態による制御AIを取得します。
		 *
		 * @return 状態による制御AI。
		 */
		public static function get context():CContext
		{
			return _context;
		}
	}
}