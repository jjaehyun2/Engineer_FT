package
{
  import flash.display.CapsStyle;
  import flash.display.DisplayObject;
  import flash.display.GraphicsPath;
  import flash.display.GraphicsSolidFill;
  import flash.display.GraphicsStroke;
  import flash.display.IGraphicsData;
  import flash.display.JointStyle;
  import flash.display.LineScaleMode;
  import flash.display.Sprite;
  import flash.events.ContextMenuEvent;
  import flash.events.Event;
  import flash.events.KeyboardEvent;
  import flash.events.MouseEvent;
  import flash.events.TextEvent;
  import flash.external.ExternalInterface;
  import flash.geom.Rectangle;
  import flash.net.FileFilter;
  import flash.net.FileReference;
  import flash.net.navigateToURL;
  import flash.net.sendToURL;
  import flash.net.URLLoader;
  import flash.net.URLRequest;
  import flash.net.URLRequestHeader;
  import flash.net.URLRequestMethod;
  import flash.net.URLVariables;
  import flash.text.Font;
  import flash.text.TextField;
  import flash.text.TextFieldType;
  import flash.text.TextFormat;
  import flash.text.TextFormatAlign;
  import flash.ui.ContextMenu;
  import flash.ui.Keyboard;
  import flash.ui.Mouse;
  import flash.ui.MouseCursor;
  import flash.utils.ByteArray;
  import flash.utils.Dictionary;
  import flash.utils.Endian;
  import flash.utils.setTimeout;

  import co.uk.mikestead.net.URLFileVariable;
  import co.uk.mikestead.net.URLRequestBuilder;

  import com.adobe.serialization.json.JSON;
  import com.hurlant.util.Base64;

  import ui.TinyButton;
  import ui.TinySlider;

  /**
   * SfxrApp
   *
   * Copyright 2009 Thomas Vian
   *
   * Licensed under the Apache License, Version 2.0 (the "License");
   * you may not use this file except in compliance with the License.
   * You may obtain a copy of the License at
   *
   *   http://www.apache.org/licenses/LICENSE-2.0
   *
   * Unless required by applicable law or agreed to in writing, software
   * distributed under the License is distributed on an "AS IS" BASIS,
   * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   * See the License for the specific language governing permissions and
   * limitations under the License.
   *
   * @author Thomas Vian
   */
  [SWF(width='640', height='480', frameRate='25')]
  public class SfxrApp extends Sprite
  {
    //--------------------------------------------------------------------------
    //
    //  Properties
    //
    //--------------------------------------------------------------------------
    [Embed(source = "assets/amiga4ever.ttf", fontName = "Amiga4Ever", mimeType = "application/x-font", embedAsCFF = "false")]
    private var Amiga4Ever:Class;            // Pixel font, original was in a tga file

    private var _synth:SfxrSynth;            // synthesizer instance

    private var _propLookup:Dictionary;      // Look up for property names using a slider key
    private var _sliderLookup:Object;        // Look up for sliders using a property name key
    private var _waveformLookup:Array;       // Look up for waveform buttons
    private var _squareLookup:Array;         // Look up for sliders controlling a square wave property

    private var _back:TinyButton;            // Button to skip back a sound
    private var _forward:TinyButton;         // Button to skip forward a sound
    private var _history:Vector.<SfxrSynth>; // List of generated settings
    private var _historyPos:int;             // Current history position

    private var _copyPaste:TextField;        // Input TextField for the settings

    private var _fileRef:FileReference;      // File reference for loading in sfs file

    private var _sfxrRect:Rectangle;         // Click rectangle for LD website link
    private var _volumeRect:Rectangle;       // Click rectangle for resetting volume

    private var embeddedMode:Boolean = false;// True if this is embedded in a larger editor and save should spit out json
    private var publishButton:TinyButton;    // Button to publish to web
    private var status:TextField;            // Text status indicator

    //--------------------------------------------------------------------------
    //
    //  Constructor
    //
    //--------------------------------------------------------------------------

    /**
     * Waits until on the stage before init
     */
    public function SfxrApp()
    {
      if (stage)   init();
      else     addEventListener(Event.ADDED_TO_STAGE, init);
    }

    //--------------------------------------------------------------------------
    //
    //  Init Method
    //
    //--------------------------------------------------------------------------

    /**
     * Initialises the synthesizer and draws the interface
     * @param  e  Added to stage event
     */
    private function init(e:Event = null):void
    {
      var flashvars:Object = this.root.loaderInfo.parameters;
      embeddedMode = flashvars.embeddedMode;

      removeEventListener(Event.ADDED_TO_STAGE, init);

      _synth = new SfxrSynth();
      SfxrGenerator.randomize(_synth);

      _propLookup = new Dictionary();
      _sliderLookup = {};
      _waveformLookup = [];
      _squareLookup = [];

      _history = new Vector.<SfxrSynth>();
      _history.push(_synth);

      drawGraphics();
      drawButtons();
      drawSliders();
      drawCopyPaste();

      var settingsData:String;

      if (flashvars.soundData) {
        settingsData = flashvars.soundData;
      } else {
        // Try external interface
        settingsData = ExternalInterface.call("loadSettingsFile");
      }

      if (settingsData) {
        setSettingsFile(Base64.decodeToByteArray(settingsData));
      }

      updateSliders();
      updateButtons();
      updateCopyPaste();

      ExternalInterface.addCallback("getSaveData", function():String {
        var baseFilePath:String = flashvars.baseFilePath;

        return JSON.encode({
          files: [{
            path: baseFilePath + ".sfs",
            contents_base64: Base64.encodeByteArray(getSettingsFile())
          }, {
            path: baseFilePath + ".wav",
            contents_base64: Base64.encodeByteArray(_synth.getWavFile())
          }]
        });
      });
    }

    //--------------------------------------------------------------------------
    //
    //  Keyboard Methods
    //
    //--------------------------------------------------------------------------

    //--------------------------------------------------------------------------
    //
    //  Button Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Adds the buttons to the stage
     */
    private function drawButtons():void
    {
      // Generator
      addButton("PICKUP/COIN",   clickPickupCoin,  4, 32);
      addButton("LASER/SHOOT",   clickLaserShoot,  4, 62);
      addButton("EXPLOSION",     clickExplosion,   4, 92);
      addButton("POWERUP",       clickPowerup,     4, 122);
      addButton("HIT/HURT",      clickHitHurt,     4, 152);
      addButton("JUMP",          clickJump,        4, 182);
      addButton("BLIP/SELECT",   clickBlipSelect,  4, 212);
      addButton("MUTATE",        clickMutate,      4, 324);
      addButton("RANDOMIZE",     clickRandomize,   4, 354, 2);

      // History
      _back =   addButton("BACK",       clickBack,      4, 384);
      _forward =   addButton("FORWARD", clickForward,   4, 414);
      _back.enabled = false;
      _forward.enabled = false;

      // Waveform
      addButton("SQUAREWAVE", clickSquarewave,   130, 28, 1, true);
      addButton("SAWTOOTH",   clickSawtooth,     250, 28, 1, true);
      addButton("SINEWAVE",   clickSinewave,     370, 28, 1, true);
      addButton("NOISE",      clickNoise,        490, 28, 1, true);

      addButton("PLAY SOUND",   clickPlaySound,   490, 228);
      status = addLabel("", 492, 356, 0);

      if(embeddedMode) {
        addButton("SAVE AS",   clickSaveSoundAs,   490, 318);
        addButton("SAVE",      clickEmbeddedSave,  490, 378, 3);
      } else {
        addButton("LOAD SOUND",   clickLoadSound,   490, 288);
        addButton("SAVE SOUND",   clickSaveSound,   490, 318);

        publishButton =
          addButton("PUBLISH .WAV", clickPostWav,     490, 378, 3);
      }

      addButton("44100 HZ",     clickSampleRate,  490, 408);
      addButton("16-BIT",       clickBitDepth,    490, 438);
    }

    /**
     * Adds a single button
     * @param  label      Text to display on the button
     * @param  onClick      Callback function called when the button is clicked
     * @param  x        X position of the button
     * @param  y        Y position of the button
     * @param  border      Thickness of the border in pixels
     * @param  selectable    If the button is selectable
     * @param  selected    If the button starts as selected
     */
    private function addButton(label:String, onClick:Function, x:Number, y:Number, border:Number = 1, selectable:Boolean = false):TinyButton
    {
      var button:TinyButton = new TinyButton(onClick, label, border, selectable);
      button.x = x;
      button.y = y;
      addChild(button);

      if(selectable) _waveformLookup.push(button);

      return button;
    }

    /**
     * Updates the buttons to reflect the synthesizer
     */
    private function updateButtons():void
    {
      selectedSwitch(_waveformLookup[_synth.waveType]);
    }

    //--------------------------------------------------------------------------
    //
    //  Generator Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Sets the synthesizer to generate a pickup/coin sound and previews it
     * @param  button  Button pressed
     */
    private function clickPickupCoin(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generatePickupCoin(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate a laser/shoot sound and previews it
     * @param  button  Button pressed
     */
    private function clickLaserShoot(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generateLaserShoot(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate an explosion sound and previews it
     * @param  button  Button pressed
     */
    private function clickExplosion(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generateExplosion(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate a powerup sound and previews it
     * @param  button  Button pressed
     */
    private function clickPowerup(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generatePowerup(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate a hit/hurt sound and previews it
     * @param  button  Button pressed
     */
    private function clickHitHurt(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generateHitHurt(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate a jump sound and previews it
     * @param  button  Button pressed
     */
    private function clickJump(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generateJump(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to generate a blip/select sound and previews it
     * @param  button  Button pressed
     */
    private function clickBlipSelect(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.generateBlipSelect(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to mutate the sound and preview it
     * @param  button  Button pressed
     */
    private function clickMutate(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.mutate(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    /**
     * Sets the synthesizer to randomize the sound and preview it
     * @param  button  Button pressed
     */
    private function clickRandomize(button:TinyButton):void
    {
      addToHistory();
      SfxrGenerator.randomize(_synth);
      updateSliders();
      updateButtons();
      updateCopyPaste();
      _synth.play();
    }

    //--------------------------------------------------------------------------
    //
    //  History Methods
    //
    //--------------------------------------------------------------------------

    /**
     * When the back button is clicked, moves back through the history
     * @param  button  TinyButton clicked
     */
    private function clickBack(button:TinyButton):void
    {
      _historyPos--;
      if(_historyPos == 0)           _back.enabled = false;
      if(_historyPos < _history.length - 1)   _forward.enabled = true;

      _synth.stop();
      _synth = _history[_historyPos];

      updateSliders();
      updateButtons();
      updateCopyPaste();

      _synth.play();
    }

    /**
     * When the forward button is clicked, moves forward through the history
     * @param  button  TinyButton clicked
     */
    private function clickForward(button:TinyButton):void
    {
      _historyPos++;
      if(_historyPos > 0)           _back.enabled = true;
      if(_historyPos == _history.length - 1)   _forward.enabled = false;

      _synth.stop();
      _synth = _history[_historyPos];

      updateSliders();
      updateButtons();
      updateCopyPaste();

      _synth.play();
    }

    /**
     * Adds a new sound effect to the history.
     * Called just before a new sound effect is generated.
     */
    private function addToHistory():void
    {
      _historyPos++;
      _synth = _synth.clone();
      _history = _history.slice(0, _historyPos);
      _history.push(_synth);

      _back.enabled = true;
      _forward.enabled = false;
    }

    //--------------------------------------------------------------------------
    //
    //  Waveform Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Selects the squarewave waveform type
     * @param  button  Button pressed
     */
    private function clickSquarewave(button:TinyButton):void
    {
      _synth.waveType = 0;
      _synth.deleteCache();
      selectedSwitch(button);
      updateCopyPaste();
    }

    /**
     * Selects the sawtooth waveform type
     * @param  button  Button pressed
     */
    private function clickSawtooth(button:TinyButton):void
    {
      _synth.waveType = 1;
      _synth.deleteCache();
      selectedSwitch(button);
      updateCopyPaste();
    }

    /**
     * Selects the sinewave waveform type
     * @param  button  Button pressed
     */
    private function clickSinewave(button:TinyButton):void
    {
      _synth.waveType = 2;
      _synth.deleteCache();
      selectedSwitch(button);
      updateCopyPaste();
    }

    /**
     * Selects the noise waveform type
     * @param  button  Button pressed
     */
    private function clickNoise(button:TinyButton):void
    {
      _synth.waveType = 3;
      _synth.deleteCache();
      selectedSwitch(button);
      updateCopyPaste();
    }

    /**
     * Unselects all the waveform buttons and selects the one passed in
     * @param  select  Selects this button
     */
    private function selectedSwitch(select:TinyButton):void
    {
      for(var i:uint = 0, l:uint = _waveformLookup.length; i < l; i++)
      {
        if(_waveformLookup[i] != select) _waveformLookup[i].selected = false;
      }

      if(!select.selected) select.selected = true;

      for(i = 0; i < 2; i++)
      {
        _squareLookup[i].dimLabel = _synth.waveType != 0;
      }
    }

    //--------------------------------------------------------------------------
    //
    //  Play/Save/Export Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Previews the sound
     * @param  button  Button pressed
     */
    private function clickPlaySound(button:TinyButton):void
    {
      _synth.play();
    }

    /**
     * Opens a browse window to load a sound setting file
     * @param  button  Button pressed
     */
    private function clickLoadSound(button:TinyButton):void
    {
      _fileRef = new FileReference();
      _fileRef.addEventListener(Event.SELECT, onSelectSettings);
      _fileRef.browse([new FileFilter("SFX Sample Files (*.sfs)", "*.sfs")]);
    }

    /**
     * When the user selects a file, begins loading it
     * @param  e  Select event
     */
    private function onSelectSettings(e:Event):void
    {
      _fileRef.cancel();

      _fileRef.removeEventListener(Event.SELECT, onSelectSettings);
      _fileRef.addEventListener(Event.COMPLETE, onLoadSettings);
      _fileRef.load();
    }

    /**
     * Once loaded, passes the file to the synthesizer to parse
     * @param  e  Complete event
     */
    private function onLoadSettings(e:Event):void
    {
      _fileRef.removeEventListener(Event.COMPLETE, onLoadSettings);

      addToHistory();
      setSettingsFile(_fileRef.data);
      updateSliders();
      updateButtons();
      updateCopyPaste();

      _fileRef = null;
    }
                
    /**
     * Posts the settings and wav to the server
     * @param  button  Button pressed
     */
    private function clickPostWav(button:TinyButton):void
    {
      status.text = "SAVING...";
      publishButton.enabled = false;

      // TODO: Gather title and description data

      var variables:URLVariables = new URLVariables();

      // Send along the flashvars
      var params:Object = this.root.loaderInfo.parameters;
      for(var key:String in params) {
        variables[key] = params[key];
      }

      variables["sound[wav]"] = new URLFileVariable(_synth.getWavFile(), "sfx.wav", "audio/x-wav");
      variables["sound[sfs]"] = new URLFileVariable(getSettingsFile(), "sfx.sfs");

      var request:URLRequest = new URLRequestBuilder(variables).build();
      request.url = "/sounds/";

      //  Handlers
      var loader:URLLoader = new URLLoader();
      loader.addEventListener(Event.COMPLETE, on_complete);

      // Send request
      loader.load(request);
      function on_complete(e : Event):void{
        status.text = "SAVED!";
        publishButton.enabled = true;
      }
    }

    /**
     * Saves out a sound settings file
     * @param  button  Button pressed
     */
    private function clickSaveSound(button:TinyButton):void
    {
      var file:ByteArray = getSettingsFile();

      new FileReference().save(file, "sfx.sfs");
    }

    /**
     * Embedded Mode, should fire 'save' action to external editor
     * @param  button  Button pressed
     */
    private function clickEmbeddedSave(button:TinyButton):void
    {
      ExternalInterface.call("save");
    }

    /**
     * Embedded Mode, should fire 'save as' action to external editor
     * @param  button  Button pressed
     */
    private function clickSaveSoundAs(button:TinyButton):void
    {
      // TODO: Fire save as external event
    }

    /**
     * Exports the sound as a .wav file
     * @param  button  Button pressed
     */
    private function clickExportWav(button:TinyButton):void
    {
      var file:ByteArray = _synth.getWavFile();

      new FileReference().save(file, "sfx.wav");
    }

    /**
     * Switches the sample rate between 44100Hz and 22050Hz
     * @param  button  Button pressed
     */
    private function clickSampleRate(button:TinyButton):void
    {
      if(_synth.sampleRate == 44100)   _synth.sampleRate = 22050;
      else               _synth.sampleRate = 44100;

      button.label = _synth.sampleRate + " HZ";
    }

    /**
     * Switches the bit depth between 16-bit and 8-bit
     * @param  button  Button pressed
     */
    private function clickBitDepth(button:TinyButton):void
    {
      if(_synth.bitDepth == 16)   _synth.bitDepth = 8;
      else             _synth.bitDepth = 16;

      button.label = _synth.bitDepth + "-BIT";
    }

    //--------------------------------------------------------------------------
    //
    //  Settings File Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Writes the current parameters to a ByteArray and returns it
     * Compatible with the original Sfxr files
     * @return  ByteArray of settings data
     */
    public function getSettingsFile():ByteArray
    {
      var file:ByteArray = new ByteArray();
      file.endian = Endian.LITTLE_ENDIAN;

      file.writeInt(102);
      file.writeInt(_synth.waveType);
      file.writeFloat(_synth.masterVolume);

      file.writeFloat(_synth.startFrequency);
      file.writeFloat(_synth.minFrequency);
      file.writeFloat(_synth.slide);
      file.writeFloat(_synth.deltaSlide);
      file.writeFloat(_synth.squareDuty);
      file.writeFloat(_synth.dutySweep);

      file.writeFloat(_synth.vibratoDepth);
      file.writeFloat(_synth.vibratoSpeed);
      file.writeFloat(0);

      file.writeFloat(_synth.attackTime);
      file.writeFloat(_synth.sustainTime);
      file.writeFloat(_synth.decayTime);
      file.writeFloat(_synth.sustainPunch);

      file.writeBoolean(false);
      file.writeFloat(_synth.lpFilterResonance);
      file.writeFloat(_synth.lpFilterCutoff);
      file.writeFloat(_synth.lpFilterCutoffSweep);
      file.writeFloat(_synth.hpFilterCutoff);
      file.writeFloat(_synth.hpFilterCutoffSweep);

      file.writeFloat(_synth.phaserOffset);
      file.writeFloat(_synth.phaserSweep);

      file.writeFloat(_synth.repeatSpeed);

      file.writeFloat(_synth.changeSpeed);
      file.writeFloat(_synth.changeAmount);

      return file;
    }

    /**
     * Reads parameters from a ByteArray file
     * Compatible with the original Sfxr files
     * @param  file  ByteArray of settings data
     */
    public function setSettingsFile(file:ByteArray):void
    {
      _synth.deleteCache();
      file.position = 0;
      file.endian = Endian.LITTLE_ENDIAN;

      var version:int = file.readInt();

      if(version != 100 && version != 101 && version != 102) return;

      _synth.waveType = file.readInt();
      _synth.masterVolume = (version == 102) ? file.readFloat() : 0.5;

      _synth.startFrequency = file.readFloat();
      _synth.minFrequency = file.readFloat();
      _synth.slide = file.readFloat();
      _synth.deltaSlide = (version >= 101) ? file.readFloat() : 0.0;

      _synth.squareDuty = file.readFloat();
      _synth.dutySweep = file.readFloat();

      _synth.vibratoDepth = file.readFloat();
      _synth.vibratoSpeed = file.readFloat();
      var unusedVibratoDelay:Number = file.readFloat();

      _synth.attackTime = file.readFloat();
      _synth.sustainTime = file.readFloat();
      _synth.decayTime = file.readFloat();
      _synth.sustainPunch = file.readFloat();

      var unusedFilterOn:Boolean = file.readBoolean();
      _synth.lpFilterResonance = file.readFloat();
      _synth.lpFilterCutoff = file.readFloat();
      _synth.lpFilterCutoffSweep = file.readFloat();
      _synth.hpFilterCutoff = file.readFloat();
      _synth.hpFilterCutoffSweep = file.readFloat();

      _synth.phaserOffset = file.readFloat();
      _synth.phaserSweep = file.readFloat();

      _synth.repeatSpeed = file.readFloat();

      _synth.changeSpeed = (version >= 101) ? file.readFloat() : 0.0;
      _synth.changeAmount = (version >= 101) ? file.readFloat() : 0.0;

      _synth.validate();
    }

    //--------------------------------------------------------------------------
    //
    //  Slider Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Adds the sliders to the stage
     */
    private function drawSliders():void
    {
      addSlider("ATTACK TIME",            "attackTime",          350, 70);
      addSlider("SUSTAIN TIME",           "sustainTime",         350, 88);
      addSlider("SUSTAIN PUNCH",          "sustainPunch",        350, 106);
      addSlider("DECAY TIME",             "decayTime",           350, 124);
      addSlider("START FREQUENCY",        "startFrequency",      350, 142);
      addSlider("MIN FREQUENCY",          "minFrequency",        350, 160);
      addSlider("SLIDE",                  "slide",               350, 178, true);
      addSlider("DELTA SLIDE",            "deltaSlide",          350, 196, true);
      addSlider("VIBRATO DEPTH",          "vibratoDepth",        350, 214);
      addSlider("VIBRATO SPEED",          "vibratoSpeed",        350, 232);
      addSlider("CHANGE AMOUNT",          "changeAmount",        350, 250, true);
      addSlider("CHANGE SPEED",           "changeSpeed",         350, 268);
      addSlider("SQUARE DUTY",            "squareDuty",          350, 286, false, true);
      addSlider("DUTY SWEEP",             "dutySweep",           350, 304, true, true);
      addSlider("REPEAT SPEED",           "repeatSpeed",         350, 322);
      addSlider("PHASER OFFSET",          "phaserOffset",        350, 340, true);
      addSlider("PHASER SWEEP",           "phaserSweep",         350, 358, true);
      addSlider("LP FILTER CUTOFF",       "lpFilterCutoff",      350, 376);
      addSlider("LP FILTER CUTOFF SWEEP", "lpFilterCutoffSweep", 350, 394, true);
      addSlider("LP FILTER RESONANCE",    "lpFilterResonance",   350, 412);
      addSlider("HP FILTER CUTOFF",       "hpFilterCutoff",      350, 430);
      addSlider("HP FILTER CUTOFF SWEEP", "hpFilterCutoffSweep", 350, 448, true);
      addSlider("",                       "masterVolume",        492, 208);
    }

    /**
     * Adds a single slider
     * @param  label      Text label to display next to the slider
     * @param  property    Property name to link with the slider
     * @param  x        X position of slider
     * @param  y        Y Position of slider
     * @param  plusMinus    If the slider ranges from -1 to 1 (true) or 0 to 1 (false)
     * @param  square      If the slider is linked to the square duty properties
     */
    private function addSlider(label:String, property:String, x:Number, y:Number, plusMinus:Boolean = false, square:Boolean = false):TinySlider
    {
      var slider:TinySlider = new TinySlider(onSliderChange, label, plusMinus);
      slider.x = x;
      slider.y = y;
      addChild(slider);

      _propLookup[slider] = property;
      _sliderLookup[property] = slider;

      if (square) _squareLookup.push(slider);

      return slider;
    }

    /**
     * Updates the property on the synthesizer to the slider's value
     * @param  slider
     */
    private function onSliderChange(slider:TinySlider):void
    {
      _synth[_propLookup[slider]] = slider.value;

      _synth.deleteCache();

      updateCopyPaste();
    }

    /**
     * Updates the sliders to reflect the synthesizer
     */
    private function updateSliders():void
    {
      for(var prop:String in _sliderLookup)
      {
        _sliderLookup[prop].value = _synth[prop];
      }
    }

    //--------------------------------------------------------------------------
    //
    //  Copy Paste Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Adds a TextField over the whole app.
     * Allows for right-click copy/paste, as well as ctrl-c/ctrl-v
     */
    private function drawCopyPaste():void
    {
      _copyPaste = new TextField();
      _copyPaste.addEventListener(TextEvent.TEXT_INPUT, updateFromCopyPaste);
      _copyPaste.addEventListener(KeyboardEvent.KEY_DOWN, updateCopyPaste);
      _copyPaste.addEventListener(KeyboardEvent.KEY_UP, updateCopyPaste);
      _copyPaste.defaultTextFormat = new TextFormat("Amiga4Ever", 8, 0);
      _copyPaste.wordWrap = false;
      _copyPaste.multiline = false;
      _copyPaste.type = TextFieldType.INPUT;
      _copyPaste.embedFonts = true;
      _copyPaste.width = 640;
      _copyPaste.height = 580;
      _copyPaste.x = 0;
      _copyPaste.y = -20;
      addChild(_copyPaste);

      _copyPaste.contextMenu = new ContextMenu();
      _copyPaste.contextMenu.addEventListener(ContextMenuEvent.MENU_SELECT, updateCopyPaste);

      Mouse.cursor = MouseCursor.ARROW;
    }

    /**
     * Updates the contents of the textfield to a representation of the settings
     * @param  e  Optional event
     */
    private function updateCopyPaste(e:Event = null):void
    {
      _copyPaste.text = _synth.getSettingsString();

      _copyPaste.setSelection(0, _copyPaste.text.length);
      stage.focus = _copyPaste;
    }

    /**
     * When the textfield is pasted into, and the new info parses, updates the settings
     * @param  e  Text input event
     */
    private function updateFromCopyPaste(e:TextEvent):void
    {
      if (e.text.split(",").length == 24) addToHistory();

      if (!_synth.setSettingsString(e.text))
      {
        _copyPaste.setSelection(0, _copyPaste.text.length);
        stage.focus = _copyPaste;

        _copyPaste.text = _synth.getSettingsString();
      }

      _copyPaste.setSelection(0, _copyPaste.text.length);
      stage.focus = _copyPaste;

      updateSliders();
      updateButtons();
    }

    //--------------------------------------------------------------------------
    //
    //  Graphics Methods
    //
    //--------------------------------------------------------------------------

    /**
     * Draws the extra labels, frames and lines to the stage
     */
    private function drawGraphics():void
    {
      var lines:Vector.<IGraphicsData> = new Vector.<IGraphicsData>();
      lines.push(new GraphicsStroke(2, false, LineScaleMode.NORMAL, CapsStyle.NONE, JointStyle.MITER, 3, new GraphicsSolidFill(0)));
      lines.push(new GraphicsPath(Vector.<int>([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2,2]),
                    Vector.<Number>([  114,0,     114,480,
                              160,66,    460,66,
                              160,138,  460,138,
                              160,246,  460,246,
                              160,282,  460,282,
                              160,318,  460,318,
                              160,336,  460,336,
                              160,372,  460,372,
                              160, 462,  460, 462,
                              590,212, 618,212, 618,388, 590,388])));
      lines.push(new GraphicsStroke(1, false, LineScaleMode.NORMAL, CapsStyle.NONE, JointStyle.MITER, 3, new GraphicsSolidFill(0)));
      lines.push(new GraphicsPath(Vector.<int>([1,2,1,2,1,2,1,2]),
                    Vector.<Number>([  160, 65,   160, 463,
                              460, 65,  460, 463])));

      graphics.drawGraphicsData(lines);

      graphics.lineStyle(2, 0xFF0000, 1, true, LineScaleMode.NORMAL, CapsStyle.SQUARE, JointStyle.MITER);
      graphics.drawRect(549.5, 207.5, 43, 10);

      addLabel("CLICK ON LABELS", 484, 68, 0x877569, 500);
      addLabel("TO RESET SLIDERS", 480, 82, 0x877569, 500);

      addLabel("COPY/PASTE SETTINGS", 470, 108, 0x877569, 500);
      addLabel("TO SHARE SOUNDS", 484, 122, 0x877569, 500);

      addLabel("BASED ON SFXR BY", 480, 148, 0x877569, 500);
      addLabel("TOMAS PETTERSSON", 480, 162, 0x877569, 500);

      addLabel("VOLUME", 516, 192, 0);

      addLabel("GENERATOR", 6, 8, 0x504030);
      addLabel("MANUAL SETTINGS", 122, 8, 0x504030);

      _sfxrRect = new Rectangle(480, 115, 100, 30);
      _volumeRect = new Rectangle(516, 192, 200, 15);

      stage.addEventListener(MouseEvent.MOUSE_DOWN, onClick);
    }

    /**
     * Handles clicking either
     * @param  e  Click event
     */
    private function onClick(e:MouseEvent):void
    {
      if (_sfxrRect.contains(stage.mouseX, stage.mouseY)) navigateToURL(new URLRequest("http://www.ludumdare.com/compo/2007/12/13/sfxr-sound-effects-for-all/"));
      if (_volumeRect.contains(stage.mouseX, stage.mouseY)) _sliderLookup["masterVolume"].value = 0.5;
    }

    /**
     * Adds a label
     * @param  label    Text to display
     * @param  x      X position of the label
     * @param  y      Y position of the label
     * @param  colour    Colour of the text
     */
    private function addLabel(label:String, x:Number, y:Number, colour:uint, width:Number = 200):TextField
    {
      var txt:TextField = new TextField();
      txt.defaultTextFormat = new TextFormat("Amiga4Ever", 8, colour);
      txt.selectable = false;
      txt.embedFonts = true;
      txt.text = label;
      txt.width = width;
      txt.height = 15;
      txt.x = x;
      txt.y = y;
      addChild(txt);

      return txt;
    }
  }
}