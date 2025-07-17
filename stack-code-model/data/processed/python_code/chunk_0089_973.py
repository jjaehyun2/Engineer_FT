package kitaec.common
{
	public class Icon
	{
        // Controls
        [Embed(source='../assets/edit.png')]
        public static const ICON_EDIT:Class;
		[Embed(source='../assets/remove.png')]
		public static const ICON_REMOVE:Class;
        [Embed(source='../assets/add.png')]
        public static const ICON_ADD:Class;
        [Embed(source='../assets/delete.png')]
        public static const ICON_DELETE:Class;
        [Embed(source='../assets/back.png')]
        public static const ICON_ARROW_BACK:Class;
        [Embed(source='../assets/forward.png')]
        public static const ICON_ARROW_FORWARD:Class;

        // Notification
        [Embed(source='../assets/info.png')]
        public static const ICON_NOTIFY_INFO:Class;
        [Embed(source='../assets/warn.png')]
        public static const ICON_NOTIFY_WARN:Class;
        [Embed(source='../assets/error.png')]
        public static const ICON_NOTIFY_ERROR:Class;
	}
}