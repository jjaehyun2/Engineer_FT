package flair.logging
{
	import flash.utils.getQualifiedClassName;

	/**
	 * @author SamYStudiO ( contact@samystudio.net )
	 */
	public class AHandler implements IHandler
	{
		/**
		 * @private
		 */
		protected var _level : Level = Level.ALL;

		/**
		 * @inheritDoc
		 */
		public function get level() : Level
		{
			return _level;
		}

		public function set level( level : Level ) : void
		{
			_level = level || ( Level.ALL );
		}

		/**
		 * @private
		 */
		protected var _formatter : IFormatter = new SimpleFormatter();

		/**
		 * @inheritDoc
		 */
		public function get formatter() : IFormatter
		{
			return _formatter;
		}

		public function set formatter( formatter : IFormatter ) : void
		{
			_formatter = formatter || new SimpleFormatter();
		}

		/**
		 *
		 */
		public function AHandler()
		{
			if( getQualifiedClassName( this ) == "flair.targets::AHandler" )
				throw new Error( this + " Abstract class cannot be instantiated" );
		}

		/**
		 * @inheritDoc
		 */
		public function publish( message : LogRecord ) : void
		{

		}

		/**
		 * @inheritDoc
		 */
		public function isLoggable( record : LogRecord ) : Boolean
		{
			return record.level.value >= _level.value;
		}
	}
}