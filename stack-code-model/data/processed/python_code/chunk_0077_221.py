package services.events.items.management
{
	import services.cairngorm.BaseEvent;
	import services.vo.items.HotelItemVO;

	public class SaveSystemArticleEvent extends BaseEvent
	{
		// ----------------------------------------------------------- //
		//                          VARIABLES                          //
		// ----------------------------------------------------------- //
		/**
		 *  This property contain item.
		 *  
		 *  @default new HotelItemVO()
		 *  
		 *  @see services.vo.backend.HotelItemVO
		 */
		private var _item:HotelItemVO = new HotelItemVO();
		/**
		 *  This property contain id of sub group for which transaction will be
		 *  saved.
		 */
		private var _sysGroupId:Number;
		/**
		 *  This property contain id of transaction for which article will be
		 *  saved.
		 */
		private var _sysTransactionId:Number;
		/**
		 *  This property contain index of transaction into list of transaction
		 *  who have saved article.
		 */
		private var _transactionIndex:int;
		/**
		 *  This property contain index of article into the list of articles for
		 *  transaction who have saved article.
		 */
		private var _articleIndex:int;
		/**
		 *  This property is <code>true</code> if adding article is new.
		 *  
		 *  @default false
		 */
		private var _isNewArticle:Boolean = false;
		
		// ----------------------------------------------------------- //
		//                    METHODS AND FUNCTIONS                    //
		// ----------------------------------------------------------- //
		/**
		 *  SaveSystemArticleEvent. Constructor.
		 *  
		 *  @param type:String is the type of the event, accessible
		 *         as Event.type.
		 */
		public function SaveSystemArticleEvent(type:String)
		{
			super(type);
		}
		
		// ----------------------------------------------------------- //
		//                      GETTER AND SETTER                      //
		// ----------------------------------------------------------- //
		/**
		 *  Saving item.
		 */
		public function get item():HotelItemVO
		{
			return _item;
		}
		/**
		 *  @private
		 */
		public function set item(value:HotelItemVO):void
		{
			_item = value;
		}
		
		/**
		 *  Id of sub group for which transaction will be saved.
		 */
		public function get sysGroupId():Number
		{
			return _sysGroupId;
		}
		/**
		 *  @private
		 */
		public function set sysGroupId(value:Number):void
		{
			_sysGroupId = value;
		}
		
		/**
		 *  Id of transaction for which article will be saved.
		 */
		public function get sysTransactionId():Number
		{
			return _sysTransactionId;
		}
		/**
		 *  @private
		 */
		public function set sysTransactionId(value:Number):void
		{
			_sysTransactionId = value;
		}
		
		/**
		 *  The index of transaction into list of transaction who have
		 *  saved article.
		 */
		public function get transactionIndex():int
		{
			return _transactionIndex;
		}
		/**
		 *  @private
		 */
		public function set transactionIndex(value:int):void
		{
			_transactionIndex = value;
		}
		
		/**
		 *  The index of article into the list of articles for transaction
		 *  who have saved article.
		 */
		public function get articleIndex():int
		{
			return _articleIndex;
		}
		/**
		 *  @private
		 */
		public function set articleIndex(value:int):void
		{
			_articleIndex = value;
		}
		
		/**
		 *  The state of adding article.
		 */
		public function get isNewArticle():Boolean
		{
			return _isNewArticle;
		}
		/**
		 *  @private
		 */
		public function set isNewArticle(value:Boolean):void
		{
			_isNewArticle = value;
		}
	}
}