//----------------------------------------------------------------------------------------------------
// class for SID Simulator
//  Copyright (c) 2008 keim All rights reserved.
//  Distributed under BSD-style license (see org.si.license.txt).
//----------------------------------------------------------------------------------------------------


package org.si.sion.sequencer.simulator {
    import org.si.sion.module.SiOPMTable;
    
    
    /** MOS Tech 8580 SID chip simulator */
    public class SiMMLSimulatorSID extends SiMMLSimulatorBase
    {
        function SiMMLSimulatorSID()
        {
            super(MT_SID, 3, new SiMMLSimulatorVoiceSet(11));
            
            var i:int, toneVoiceSet:SiMMLSimulatorVoiceSet;
            
            // default voice set
            for (i=0; i<8; i++) {
                this._defaultVoiceSet.voices[i] = new SiMMLSimulatorVoice(SiOPMTable.PG_PULSE+i, SiOPMTable.PT_PSG);
            }
            this._defaultVoiceSet.voices[8]  = new SiMMLSimulatorVoice(SiOPMTable.PG_TRIANGLE,    SiOPMTable.PT_PSG);
            this._defaultVoiceSet.voices[9]  = new SiMMLSimulatorVoice(SiOPMTable.PG_SAW_UP,      SiOPMTable.PT_PSG);
            this._defaultVoiceSet.voices[10] = new SiMMLSimulatorVoice(SiOPMTable.PG_NOISE_PULSE, SiOPMTable.PT_OPM_NOISE);
            this._defaultVoiceSet.initVoiceIndex = 1;
            
            // voice set for channel 1,2
            toneVoiceSet = new SiMMLSimulatorVoiceSet(8);
            toneVoiceSet.initVoiceIndex = 4;
            for (i=0; i<8; i++) {
                toneVoiceSet.voices[i] = new SiMMLSimulatorVoice(SiOPMTable.PG_PULSE+i*2, SiOPMTable.PT_PSG);
            }
            this._channelVoiceSet[0] = toneVoiceSet;
            this._channelVoiceSet[1] = toneVoiceSet;
            
            // voice set for channel 3
            toneVoiceSet = new SiMMLSimulatorVoiceSet(1);
            toneVoiceSet.initVoiceIndex = 0;
            toneVoiceSet.voices[0] = new SiMMLSimulatorVoice(SiOPMTable.PG_CUSTOM, SiOPMTable.PT_PSG);
            this._channelVoiceSet[2] = toneVoiceSet;

            // voice set for channel 4
            toneVoiceSet = new SiMMLSimulatorVoiceSet(2);
            toneVoiceSet.initVoiceIndex = 0;
            toneVoiceSet.voices[0] = new SiMMLSimulatorVoice(SiOPMTable.PG_NOISE_PULSE,    SiOPMTable.PT_GB_NOISE);
            toneVoiceSet.voices[1] = new SiMMLSimulatorVoice(SiOPMTable.PG_NOISE_GB_SHORT, SiOPMTable.PT_GB_NOISE);
            this._channelVoiceSet[3] = toneVoiceSet;
        }
    }
}