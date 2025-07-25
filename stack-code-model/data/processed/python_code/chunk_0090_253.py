////////////////////////////////////////////////////////////////////////////////
//
//  Licensed to the Apache Software Foundation (ASF) under one or more
//  contributor license agreements.  See the NOTICE file distributed with
//  this work for additional information regarding copyright ownership.
//  The ASF licenses this file to You under the Apache License, Version 2.0
//  (the "License"); you may not use this file except in compliance with
//  the License.  You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
//  Unless required by applicable law or agreed to in writing, software
//  distributed under the License is distributed on an "AS IS" BASIS,
//  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//  See the License for the specific language governing permissions and
//  limitations under the License.
//
////////////////////////////////////////////////////////////////////////////////

package
{

/**
 *  @private
 *  This class is used to link additional classes into framework.swc
 *  beyond those that are found by dependecy analysis starting
 *  from the classes specified in manifest.xml.
 *  For example, Button does not have a reference to ButtonSkin,
 *  but ButtonSkin needs to be in framework.swc along with Button.
 */
internal class MxClasses
{
	// Maintain alphabetical order
	import mx.controls.Alert; Alert;
	import mx.controls.videoClasses.CuePointManager; CuePointManager;
	import mx.effects.easing.Cubic; Cubic;
	import mx.effects.easing.Linear; Linear;
	import mx.effects.easing.Quadratic; Quadratic;
	import mx.effects.easing.Quartic; Quartic;
	import mx.effects.easing.Quintic; Quintic;
	import mx.effects.easing.Sine; Sine;

	import mx.modules.Module; Module;
	import mx.modules.ModuleLoader; ModuleLoader;
	import mx.skins.halo.AccordionHeaderSkin; AccordionHeaderSkin;
	import mx.skins.halo.ActivatorSkin; ActivatorSkin;
	import mx.skins.halo.ApplicationBackground; ApplicationBackground;
	import mx.skins.halo.ButtonBarButtonSkin; ButtonBarButtonSkin;
	import mx.skins.halo.ButtonSkin; ButtonSkin;
	import mx.skins.halo.CheckBoxIcon; CheckBoxIcon;
	import mx.skins.halo.ColorPickerSkin; ColorPickerSkin;
	import mx.skins.halo.ComboBoxArrowSkin; ComboBoxArrowSkin;
	import mx.skins.halo.DataGridColumnResizeSkin; DataGridColumnResizeSkin;
	import mx.skins.halo.DataGridHeaderBackgroundSkin; DataGridHeaderBackgroundSkin;
	import mx.skins.halo.DataGridHeaderSeparator; DataGridHeaderSeparator;
	import mx.skins.halo.DataGridSortArrow; DataGridSortArrow;
	import mx.skins.halo.DateChooserIndicator; DateChooserIndicator;
	import mx.skins.halo.DateChooserMonthArrowSkin; DateChooserMonthArrowSkin;
	import mx.skins.halo.DateChooserYearArrowSkin; DateChooserYearArrowSkin;
	import mx.skins.halo.HaloBorder; HaloBorder;
	import mx.skins.halo.HaloColors; HaloColors;
	import mx.skins.halo.SliderHighlightSkin; SliderHighlightSkin;
	import mx.skins.halo.SliderThumbSkin; SliderThumbSkin;
	import mx.skins.halo.SliderTrackSkin; SliderTrackSkin;
	import mx.skins.halo.LinkButtonSkin; LinkButtonSkin;
	import mx.skins.halo.LinkSeparator; LinkSeparator;
	import mx.skins.halo.ListDropIndicator; ListDropIndicator;
	import mx.skins.halo.MenuBarBackgroundSkin; MenuBarBackgroundSkin;
	import mx.skins.halo.NumericStepperDownSkin; NumericStepperDownSkin;
	import mx.skins.halo.NumericStepperUpSkin; NumericStepperUpSkin;
	import mx.skins.halo.PanelSkin; PanelSkin;
	import mx.skins.halo.PopUpButtonSkin; PopUpButtonSkin;
	import mx.skins.halo.PopUpIcon; PopUpIcon;
	import mx.skins.halo.PopUpMenuIcon; PopUpMenuIcon;
	import mx.skins.halo.ProgressBarSkin; ProgressBarSkin;
	import mx.skins.halo.ProgressIndeterminateSkin; ProgressIndeterminateSkin;
	import mx.skins.halo.ProgressMaskSkin; ProgressMaskSkin;
	import mx.skins.halo.ProgressTrackSkin; ProgressTrackSkin;
	import mx.skins.halo.RadioButtonIcon; RadioButtonIcon;
	import mx.skins.halo.ScrollArrowSkin; ScrollArrowSkin;
	import mx.skins.halo.ScrollThumbSkin; ScrollThumbSkin;
	import mx.skins.halo.ScrollTrackSkin; ScrollTrackSkin;
	import mx.skins.halo.TabSkin; TabSkin;
	import mx.skins.halo.TitleBackground; TitleBackground;
	import mx.skins.halo.WindowBackground; WindowBackground;

}

}