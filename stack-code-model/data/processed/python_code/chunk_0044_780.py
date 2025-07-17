/* --- START OF LICENSE AND COPYRIGHT BLURB ---

   This file is a part of the PUPIL project, see
   
     http://github.com/MIUNPsychology/PUPIL

   Copyright 2016 Department of Psychology, Mid Sweden University

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   --- END OF LICENSE AND COPYRIGHT BLURB --- */



package sfw.textformat
{
  import flash.display.*;
  import flash.events.*;
  import flash.text.*;

  import sfw.*;

  public class SFLabelTextFormat extends SFTextFormat
  {
    public function SFLabelTextFormat() 
    {
      super();
      
      font = "Arial";
      size = 14;
      color = SFComponent.COLOR_TEXT;
    }

    override public function getAssumedHeight():Number
    {
      return 20;
    }
    
    override public function getAssumedWidth():Number
    {
      return 8.04;
    }  
  }
}