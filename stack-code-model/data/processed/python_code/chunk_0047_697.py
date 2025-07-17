package com.github.mortido.sqcity.resources
{
    import com.github.mortido.sqcity.GameState;
    import com.github.mortido.sqcity.configuration.ImageInfo;

    import flash.display.Bitmap;
    import flash.display.BitmapData;
    import flash.display.Loader;
    import flash.display.LoaderInfo;
    import flash.events.Event;
    import flash.events.IOErrorEvent;
    import flash.net.URLRequest;
    import flash.utils.Dictionary;

    public class CachedResourceManager implements IGameResourceManager
    {
        private const URL_KEY:String = "url";
        private const RETRY_KEY:String = "retry";

        private var pendingQueue:Dictionary = new Dictionary();
        private var activeLoaders:Dictionary = new Dictionary();
        private var cache:Dictionary = new Dictionary();

        public function createImageSprite(id:String):BitmapWrapper
        {
            var ii:ImageInfo = GameState.instance.config.imageInfos[id];

            if (ii == null)
            {
                throw new Error("Can't create image with id: \"" + id + "\".")
            }

            // Check cache.
            var cached:Boolean = cache[ii.url] != null;
            var bitmap:Bitmap = cached ? new Bitmap(BitmapData(cache[ii.url])) : new Assets.StubImage();

            // Set reference point.
            bitmap.x = -ii.referenceX;
            bitmap.y = -ii.referenceY;

            if (cached)
            {
                return new BitmapWrapper(bitmap);
            }

            // If already downloading - add to queue.
            var queue:Vector.<Bitmap> = pendingQueue[ii.url] as Vector.<Bitmap>;
            if (queue == null)
            {
                // Or start new downloading.
                queue = new Vector.<Bitmap>();
                pendingQueue[ii.url] = queue;
                var loader:Loader = LoaderPool.instance.checkout();
                var loadInfo:Object = {};
                loadInfo[URL_KEY] = ii.url;
                loadInfo[RETRY_KEY] = 0;
                activeLoaders[loader] = loadInfo;
                loader.contentLoaderInfo.addEventListener(Event.COMPLETE, completeLoadHandler);
                loader.contentLoaderInfo.addEventListener(IOErrorEvent.IO_ERROR, errorLoadHandler);
                loader.load(new URLRequest(ii.url));
            }

            queue.push(bitmap);
            return new BitmapWrapper(bitmap);
        }

        private function completeLoadHandler(event:Event):void
        {
            var loaderInfo:LoaderInfo = LoaderInfo(event.target);
            var url:String = activeLoaders[loaderInfo.loader][URL_KEY];
            var bd:BitmapData = Bitmap(loaderInfo.content).bitmapData;
            var queue:Vector.<Bitmap> = pendingQueue[url] as Vector.<Bitmap>;
            for (var i:int = 0; i < queue.length; i++)
            {
                queue[i].bitmapData = bd;
            }
            cache[url] = bd;
            pendingQueue[url] = null;
            delete pendingQueue[url];
            activeLoaders[loaderInfo.loader] = null;
            delete activeLoaders[loaderInfo.loader];
            LoaderPool.instance.checkin(loaderInfo.loader);
        }

        private function errorLoadHandler(event:Event):void
        {
            var loaderInfo:LoaderInfo = LoaderInfo(event.target);
            var url:String = activeLoaders[loaderInfo.loader][URL_KEY];
            var retry:int = activeLoaders[loaderInfo.loader][RETRY_KEY];
            if (retry < 3)
            {
                retry += 1;
                trace("Can't load image by url: " + url + ". Retry attempt #" + retry);
                activeLoaders[loaderInfo.loader][RETRY_KEY] = retry;
                loaderInfo.loader.load(new URLRequest(url));
                return;
            }

            trace("Image by url: " + url + " wasn't loaded.");

            // Don't clean pending queue - will retry again if some element will request this image.
            activeLoaders[loaderInfo.loader] = null;
            delete activeLoaders[loaderInfo.loader];
            LoaderPool.instance.checkin(loaderInfo.loader);
        }
    }
}