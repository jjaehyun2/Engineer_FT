//
// Flump - Copyright 2013 Flump Authors

package flump.display {

import deng.fzip.FZip;
import deng.fzip.FZipErrorEvent;
import deng.fzip.FZipEvent;
import deng.fzip.FZipFile;

import flash.display.BitmapData;
import flash.events.Event;
import flash.events.IOErrorEvent;
import flash.events.ProgressEvent;
import flash.geom.Point;
import flash.geom.Rectangle;
import flash.net.URLRequest;
import flash.utils.ByteArray;
import flash.utils.Dictionary;

import flump.executor.Executor;
import flump.executor.Future;
import flump.executor.FutureTask;
import flump.mold.AtlasMold;
import flump.mold.AtlasTextureMold;
import flump.mold.LibraryMold;
import flump.mold.MovieMold;
import flump.mold.TextureGroupMold;

import starling.core.Starling;
import starling.textures.Texture;

internal class Loader {
    public function Loader (toLoad :Object, libLoader :LibraryLoader) {
        _scaleFactor = (libLoader.scaleFactor > 0 ? libLoader.scaleFactor :
            Starling.contentScaleFactor);
        _libLoader = libLoader;
        _toLoad = toLoad;
    }

    public function load (future :FutureTask) :void {
        _future = future;

        _zip.addEventListener(Event.COMPLETE, _future.monitoredCallback(onZipLoadingComplete));
        _zip.addEventListener(IOErrorEvent.IO_ERROR, _future.fail);
        _zip.addEventListener(FZipErrorEvent.PARSE_ERROR, _future.fail);
        _zip.addEventListener(FZipEvent.FILE_LOADED, _future.monitoredCallback(onFileLoaded));
        _zip.addEventListener(ProgressEvent.PROGRESS, _future.monitoredCallback(onProgress));

        if (_toLoad is String) _zip.load(new URLRequest(String(_toLoad)));
        else _zip.loadBytes(ByteArray(_toLoad));
    }

    protected function onProgress (e :ProgressEvent) :void {
        _libLoader.urlLoadProgressed.emit(e);
    }

    protected function onFileLoaded (e :FZipEvent) :void {
        const loaded :FZipFile = _zip.removeFileAt(_zip.getFileCount() - 1);
        const name :String = loaded.filename;
        if (name == LibraryLoader.LIBRARY_LOCATION) {
            const jsonString :String = loaded.content.readUTFBytes(loaded.content.length);
            _lib = LibraryMold.fromJSON(JSON.parse(jsonString), _libLoader.scaleTexturesToOrigin);
            _libLoader.libraryMoldLoaded.emit(_lib);
        } else if (name.indexOf(PNG, name.length - PNG.length) != -1) {
            _atlasBytes[name] = loaded.content;
        } else if (name.indexOf(JPG, name.length - JPG.length) != -1) {
            _atlasBytes[name] = loaded.content;
        } else if (name.indexOf(ATF, name.length - ATF.length) != -1) {
            _atlasBytes[name] = loaded.content;
            _libLoader.atfAtlasLoaded.emit({name: name, bytes: loaded.content});
        } else if (name == LibraryLoader.VERSION_LOCATION) {
            const zipVersion :String = loaded.content.readUTFBytes(loaded.content.length);
            if (zipVersion != LibraryLoader.VERSION) {
                throw new Error("Zip is version " + zipVersion + " but the code needs " +
                    LibraryLoader.VERSION);
            }
            _versionChecked = true;
        } else if (name == LibraryLoader.MD5_LOCATION ) { // Nothing to verify
        } else {
            _libLoader.fileLoaded.emit({name: name, bytes: loaded.content});
        }
    }

    protected function onZipLoadingComplete (..._) :void {
        _zip = null;
        if (_lib == null) throw new Error(LibraryLoader.LIBRARY_LOCATION + " missing from zip");
        if (!_versionChecked) throw new Error(LibraryLoader.VERSION_LOCATION + " missing from zip");
        _bitmapLoaders.terminated.connect(_future.monitoredCallback(onBitmapLoadingComplete));

        // Determine the scale factor we want to use
        var textureGroup :TextureGroupMold = _lib.bestTextureGroupForScaleFactor(_scaleFactor);
        if (textureGroup != null) {
            for (var ii :int = 0; ii < textureGroup.atlases.length; ++ii) {
                loadAtlas(textureGroup, ii)
            }
        }
        // free up extra atlas bytes immediately
        for (var leftover :String in _atlasBytes) {
            if (_atlasBytes.hasOwnProperty(leftover)) {
                ByteArray(_atlasBytes[leftover]).clear();
                delete (_atlasBytes[leftover]);
            }
        }
        _bitmapLoaders.shutdown();
    }

    protected function loadAtlas (textureGroup :TextureGroupMold, atlasIndex :int) :void {
        var atlas :AtlasMold = textureGroup.atlases[atlasIndex];
        const bytes :ByteArray = _atlasBytes[atlas.file];
        delete _atlasBytes[atlas.file];
        if (bytes == null) {
            throw new Error("Expected an atlas '" + atlas.file + "', but it wasn't in the zip");
        }

        bytes.position = 0; // reset the read head
        var scale :Number = atlas.scaleFactor * (_libLoader.scaleTexturesToOrigin ? _lib.baseScale : 1);
        if (_lib.textureFormat == "atf") {
            // we do not dipose of the ByteArray so that Starling will handle a context loss.
            baseTextureLoaded(Texture.fromAtfData(bytes, scale, _libLoader.generateMipMaps), atlas);
        } else {
            var atlasFuture :Future = _bitmapLoaders.submit(
                function (onSuccess :Function, onFailure :Function) :void {
                    // Executor's onSuccess and onFailure are varargs functions, which our
                    // function may not handle correctly if it changes its behavior based on the
                    // number of receiving arguments. So we un-vararg-ify them here, which is
                    // kinda crappy!
                    var unaryOnSuccess :Function = function (result :*) :void { onSuccess(result); };
                    var unaryOnFailure :Function = function (err :*) :void { onFailure(err); };
                    _libLoader.delegate.loadAtlasBitmap(atlas, atlasIndex, bytes, unaryOnSuccess, unaryOnFailure);
                });
            atlasFuture.failed.connect(onBitmapLoadingFailed);
            atlasFuture.succeeded.connect(function (bitmapData :BitmapData) :void {
                _libLoader.pngAtlasLoaded.emit({atlas: atlas, image: bitmapData});
                var tex :Texture = _libLoader.delegate.createTextureFromBitmap(
                    atlas, bitmapData, scale, _libLoader.generateMipMaps);
                baseTextureLoaded(tex, atlas);
                // We dispose of the ByteArray, but not the BitmapData,
                // so that Starling will handle a context loss.
                bytes.clear();
            });
        }
    }

    protected function baseTextureLoaded (baseTexture :Texture, atlas :AtlasMold) :void {
        _baseTextures.push(baseTexture);

        _libLoader.delegate.consumingAtlasMold(atlas);
        var scale :Number = atlas.scaleFactor * (_libLoader.scaleTexturesToOrigin ? _lib.baseScale : 1);
        for each (var atlasTexture :AtlasTextureMold in atlas.textures) {
            var bounds :Rectangle = atlasTexture.bounds;
            var offset :Point = atlasTexture.origin;

            // Starling expects subtexture bounds to be unscaled
            if (scale != 1) {
                bounds = bounds.clone();
                bounds.x /= scale;
                bounds.y /= scale;
                bounds.width /= scale;
                bounds.height /= scale;

                offset = offset.clone();
                offset.x /= scale;
                offset.y /= scale;
            }

            _creators[atlasTexture.symbol] = _libLoader.delegate.createImageCreator(
                atlasTexture,
                Texture.fromTexture(baseTexture, bounds),
                offset,
                atlasTexture.symbol);
        }
    }

    protected function onBitmapLoadingComplete (..._) :void {
        for each (var movie :MovieMold in _lib.movies) {
            movie.fillLabels();
            _creators[movie.id] = _libLoader.delegate.createMovieCreator(
                movie, _lib.frameRate);
        }
        _future.succeed(new LibraryImpl(_baseTextures, _creators, _lib.isNamespaced, _lib.baseScale));
    }

    protected function onBitmapLoadingFailed (e :*) :void {
        if (_future.isComplete) return;
        _future.fail(e);
        _bitmapLoaders.shutdownNow();
    }

    protected var _toLoad :Object;
    protected var _scaleFactor :Number;
    protected var _libLoader :LibraryLoader;
    protected var _future :FutureTask;
    protected var _versionChecked :Boolean;

    protected var _zip :FZip = new FZip();
    protected var _lib :LibraryMold;

    protected const _baseTextures :Vector.<Texture> = new <Texture>[];
    protected const _creators :Dictionary = new Dictionary();//<name, ImageCreator/MovieCreator>
    protected const _atlasBytes :Dictionary = new Dictionary();//<String name, ByteArray>
    protected const _bitmapLoaders :Executor = new Executor(1);

    protected static const JPG :String = ".jpg";
    protected static const PNG :String = ".png";
    protected static const ATF :String = ".atf";
}
}