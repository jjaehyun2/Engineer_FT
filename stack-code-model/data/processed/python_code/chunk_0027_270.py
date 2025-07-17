/**
 * Created by ricardo_neves at bytesfromouterspace.com on 28/02/2015.
 */
package com.bytesfromouterspace.stockbrokers.controller {

    import com.bytesfromouterspace.stockbrokers.model.SoundRandomGeneratorModel;

    import flash.events.Event;
    import flash.events.IOErrorEvent;
    import flash.events.SampleDataEvent;
    import flash.media.ID3Info;

    import flash.media.Sound;

    import flash.media.SoundChannel;
    import flash.media.SoundMixer;
    import flash.net.URLRequest;
    import flash.utils.ByteArray;
    import flash.utils.Timer;

    public class SoundRandomGeneratorController {

        protected var _model:SoundRandomGeneratorModel;
        protected var _sound:Sound;
        protected var _channel:SoundChannel;
        protected var _soundData:ByteArray;

        public function SoundRandomGeneratorController(model:SoundRandomGeneratorModel) {
            this._model = model;
        }

        public function start():void {
            if(_model.soundPath != null) {
                _soundData = new ByteArray();
                _sound = new Sound();
                _sound.addEventListener(Event.ID3, onSoundID3);
                _sound.addEventListener(IOErrorEvent.IO_ERROR, onSoundError);
                _sound.addEventListener(Event.COMPLETE, onSoundComplete);
                _sound.addEventListener(SampleDataEvent.SAMPLE_DATA, onSoundSample);
                _sound.load(new URLRequest(_model.soundPath));
                trace("Sound started");
            } else {
                trace("No SOund");
            }
        }

        private function onSoundSample(event:SampleDataEvent):void {
            trace(event);
        }

        private function onSoundComplete(event:Event):void {
            trace(event);
            _model.numSamples = Math.floor ((_sound.length/1000)*44100);
            _sound.extract(_soundData, _model.numSamples);

            _soundData.position = 0;

            /*var max:Number = Number.MIN_VALUE;
            var min:Number = Number.MAX_VALUE;
            var val:Number = 0;
            var ns:Number = 0;
            var avg:Number = 0;
            while(_soundData.bytesAvailable > 0){
                val = _soundData.readFloat();
                if(val != 0) {
                    val *= 100;
                    if(Math.abs(val) > 1) {
                        val /= val;
                    }
                    if (val < min) {
                        min = val;
                    }
                    if (val > max) {
                        max = val;
                    }
                    ns++;
                    avg += val;
                }
            }
            trace("Min:", min, "Max:", max, "Samples:", ns, "AVG:", avg / ns);*/
            _model.soundData = _soundData;
            //_sound.play();
            trace(_soundData.bytesAvailable, _soundData.position, _soundData.length);
        }

        private function onSoundError(event:IOErrorEvent):void {
            trace(event);
        }

        private function onSoundID3(event:Event):void {
            var id3:ID3Info = _sound.id3;
            trace(event, _sound.length);
        }

        public function process():void {
            if(_channel) {
                trace(_channel.position, _channel.leftPeak, _channel.rightPeak);

            }
        }


        public function generate():void {
            _model.generateAudioRandom();
        }
    }
}