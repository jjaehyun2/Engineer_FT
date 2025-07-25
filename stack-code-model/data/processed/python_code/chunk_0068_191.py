package org.mangui.osmf.plugins {
    import org.osmf.media.MediaElement;
    import org.mangui.HLS.HLS;
    import org.mangui.HLS.HLSEvent;
    import org.mangui.HLS.HLSAudioTrack;
    import org.mangui.HLS.utils.*;
    import org.osmf.traits.AlternativeAudioTrait;
    import org.osmf.events.AlternativeAudioEvent;
    import org.osmf.net.StreamingItem;
    import org.osmf.utils.OSMFStrings;

    public class HLSAlternativeAudioTrait extends AlternativeAudioTrait {
        private var _hls : HLS;
        private var _media : MediaElement;
        private var _audioTrackList : Vector.<HLSAudioTrack>;
        private var _numAlternativeAudioStreams : int;
        private var _transitionInProgress : Boolean = false;
        private var _activeTransitionIndex : int = DEFAULT_TRANSITION_INDEX;
        private var _lastTransitionIndex : int = INVALID_TRANSITION_INDEX;

        public function HLSAlternativeAudioTrait(hls : HLS, media : MediaElement) {
            super(0);
            _numAlternativeAudioStreams = 0;
            _hls = hls;
            _media = media;
            _hls.addEventListener(HLSEvent.AUDIO_TRACK_CHANGE, _audioTrackChangedHandler);
            _hls.addEventListener(HLSEvent.AUDIO_TRACKS_LIST_CHANGE, _audioTrackListChangedHandler);
        }

        override public function get numAlternativeAudioStreams() : int {
            Log.debug("HLSAlternativeAudioTrait:numAlternativeAudioStreams:" + _numAlternativeAudioStreams);
            return _numAlternativeAudioStreams;
        }

        override public function getItemForIndex(index : int) : StreamingItem {
            Log.debug("HLSDynamicStreamTrait:getItemForIndex(" + index + ")");
            if (index <= INVALID_TRANSITION_INDEX || index >= numAlternativeAudioStreams) {
                throw new RangeError(OSMFStrings.getString(OSMFStrings.ALTERNATIVEAUDIO_INVALID_INDEX));
            }

            if (index == DEFAULT_TRANSITION_INDEX) {
                return null;
            }
            var name : String = _audioTrackList[index + 1].title;
            var streamItem : StreamingItem = new StreamingItem("AUDIO", name);
            streamItem.info.label = name;
            return streamItem;
        }

        override protected function endSwitching(index : int) : void {
            Log.debug("HLSDynamicStreamTrait:endSwitching(" + index + ")");
            if (switching) {
                executeSwitching(_indexToSwitchTo);
            }
            super.endSwitching(index);
        }

        protected function executeSwitching(indexToSwitchTo : int) : void {
            Log.debug("HLSDynamicStreamTrait:executeSwitching(" + indexToSwitchTo + ")");
            if (_lastTransitionIndex != indexToSwitchTo) {
                _activeTransitionIndex = indexToSwitchTo;
                _transitionInProgress = true;
                _hls.audioTrack = indexToSwitchTo + 1;
            }
        }

        private function _audioTrackChangedHandler(event : HLSEvent) : void {
            Log.debug("HLSDynamicStreamTrait:_audioTrackChangedHandler");
            _transitionInProgress = false;
            setSwitching(false, _lastTransitionIndex);
        }

        private function _audioTrackListChangedHandler(event : HLSEvent) : void {
            Log.debug("HLSDynamicStreamTrait:_audioTrackListChangedHandler");
            _audioTrackList = _hls.audioTracks;
            if (_audioTrackList.length > 0) {
                // try to change default Audio Track Title for GrindPlayer ...
                if (_audioTrackList[0].title.indexOf("TS/") == -1) {
                    Log.debug("default audio track title:" + _audioTrackList[0].title);
                    _media.resource.addMetadataValue("defaultAudioLabel", _audioTrackList[0].title);
                }
            }
            _numAlternativeAudioStreams = _audioTrackList.length - 1;
            if (_numAlternativeAudioStreams > 0) {
                dispatchEvent(new AlternativeAudioEvent(AlternativeAudioEvent.NUM_ALTERNATIVE_AUDIO_STREAMS_CHANGE, false, false, false));
            }
        }
    }
}