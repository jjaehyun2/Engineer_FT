package screens.splash.gallery {
	import feathers.controls.DecelerationRate;
	import feathers.controls.List;
	import feathers.controls.ScrollBarDisplayMode;
	import feathers.themes.TopcoatLightMobileTheme;
	
	/**
	 * Extends MetalWorksMobileTheme to make some app-specific styling tweaks
	 */
	public class GalleryTheme extends TopcoatLightMobileTheme {
		public function GalleryTheme() {
			super();
		}
		
		override protected function initializeStyleProviders():void {
			super.initializeStyleProviders();
			this.getStyleProviderForClass(List).setFunctionForStyleName(GalleryMain.THUMBNAIL_LIST_NAME, this.setThumbnailListStyles);
		}
		
		protected function setThumbnailListStyles(list:List):void {
			//start with the default list styles. we could start from scratch,
			//if we wanted, but we're only making minor changes.
			super.setListStyles(list);
			
			//we're not displaying scroll bars
			list.scrollBarDisplayMode = ScrollBarDisplayMode.NONE;
			
			//make a swipe scroll a shorter distance
			list.decelerationRate = DecelerationRate.FAST;
		}
	}
}