/*

Slider-Actionscript

*/


import fl.events.SliderEvent; //SliderEvent-Klasse

/*
EventListener
*/
sliderUa_mc.addEventListener(SliderEvent.THUMB_DRAG, Ua_Slide);
k1_sliderUk_mc.addEventListener(SliderEvent.THUMB_DRAG, k1_Uk_Slide);
k1_sliderD_mc.addEventListener(SliderEvent.THUMB_DRAG, k1_D_Slide);
k1_sliderL_mc.addEventListener(SliderEvent.THUMB_DRAG, k1_L_Slide);
k2_sliderUk_mc.addEventListener(SliderEvent.THUMB_DRAG, k2_Uk_Slide);
k2_sliderD_mc.addEventListener(SliderEvent.THUMB_DRAG, k2_D_Slide);
k2_sliderL_mc.addEventListener(SliderEvent.THUMB_DRAG, k2_L_Slide);

/*
Sliderwerte bestimmen
*/
sliderUa_mc.maximum = 100;
sliderUa_mc.minimum = 1;
sliderUa_mc.snapInterval = 1;
sliderUa_mc.value = 50;
k1_sliderUk_mc.maximum = 20;
k1_sliderUk_mc.minimum = -20;
k1_sliderUk_mc.snapInterval = 0.1;
k1_sliderUk_mc.value = 0;
k1_sliderD_mc.maximum = 130;
k1_sliderD_mc.minimum = 1;
k1_sliderD_mc.snapInterval = 1;
k1_sliderD_mc.value = 50;
k1_sliderL_mc.maximum = 130;
k1_sliderL_mc.minimum = 1;
k1_sliderL_mc.snapInterval = 1;
k1_sliderL_mc.value = 85;
k2_sliderUk_mc.maximum = 20;
k2_sliderUk_mc.minimum = -20;
k2_sliderUk_mc.snapInterval = 0.1;
k2_sliderUk_mc.value = 0;
k2_sliderD_mc.maximum = 130;
k2_sliderD_mc.minimum = 1;
k2_sliderD_mc.snapInterval = 1;
k2_sliderD_mc.value = 50;
k2_sliderL_mc.maximum = 100;
k2_sliderL_mc.minimum = 1;
k2_sliderL_mc.snapInterval = 1;
k2_sliderL_mc.value = 85;

/*
Slider betätigen
*/
function Ua_Slide(UaGeslidet: SliderEvent) {
	sliderUa_txt.text = "Ua = " + sliderUa_mc.value + " kV";
	BerechnungV();
	bewegung();
}
function k1_Uk_Slide(k1_UkGeslidet: SliderEvent) {
	k1_sliderUk_txt.text = "Uk = " + k1_sliderUk_mc.value + " kV";
	if (k1_sliderUk_mc.value > 0) {
		AblenkPlatteVertikal_Oben_mc.visible = false;
		AblenkPlatteVertikal_Unten_mc.visible = false;
		AblenkPlatteVertikal_ObenPLUS_mc.visible = false;
		AblenkPlatteVertikal_ObenMINUS_mc.visible = true;
		AblenkPlatteVertikal_UntenPLUS_mc.visible = true;
		AblenkPlatteVertikal_UntenMINUS_mc.visible = false;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_von_ObenMINUS_mc.visible = true;
			AblenkPlatteVertikal_von_ObenPLUS_mc.visible = false;
			AblenkPlatteVertikal_von_Oben_mc.visible = false;
		}
	} else if (k1_sliderUk_mc.value == 0) {
		AblenkPlatteVertikal_Oben_mc.visible = true;
		AblenkPlatteVertikal_Unten_mc.visible = true;
		AblenkPlatteVertikal_ObenPLUS_mc.visible = false;
		AblenkPlatteVertikal_ObenMINUS_mc.visible = false;
		AblenkPlatteVertikal_UntenPLUS_mc.visible = false;
		AblenkPlatteVertikal_UntenMINUS_mc.visible = false;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_von_ObenMINUS_mc.visible = false;
			AblenkPlatteVertikal_von_ObenPLUS_mc.visible = false;
			AblenkPlatteVertikal_von_Oben_mc.visible = true;
		}
	} else if (k1_sliderUk_mc.value < 0) {
		AblenkPlatteVertikal_Oben_mc.visible = false;
		AblenkPlatteVertikal_Unten_mc.visible = false;
		AblenkPlatteVertikal_ObenPLUS_mc.visible = true;
		AblenkPlatteVertikal_ObenMINUS_mc.visible = false;
		AblenkPlatteVertikal_UntenPLUS_mc.visible = false;
		AblenkPlatteVertikal_UntenMINUS_mc.visible = true;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_von_ObenMINUS_mc.visible = false;
			AblenkPlatteVertikal_von_ObenPLUS_mc.visible = true;
			AblenkPlatteVertikal_von_Oben_mc.visible = false;
		}
	}
	ablenkSpannung = k1_sliderUk_mc.value * 1000;
	bewegung();
}
function k1_D_Slide(k1_DGeslidet: SliderEvent) {
	k1_sliderD_txt.text = "d = " + k1_sliderD_mc.value + " mm";
	kondensatorVertikal_mc.height = k1_sliderD_mc.value;
	kondensatorVertikal_mc.y = (323.25 + (25 - kondensatorVertikal_mc.height / 2));
	AblenkPlatteVertikal1_mc.y = kondensatorVertikal_mc.y - 5;
	AblenkPlatteVertikal2_mc.y = kondensatorVertikal_mc.y + kondensatorVertikal_mc.height;
	AblenkPlatteVertikal_Oben_mc.y = AblenkPlatteVertikal1_mc.y - 27.25;
	AblenkPlatteVertikal_Unten_mc.y = AblenkPlatteVertikal2_mc.y + 5;
	AblenkPlatteVertikal_ObenPLUS_mc.y = AblenkPlatteVertikal1_mc.y - 27.25;
	AblenkPlatteVertikal_UntenPLUS_mc.y = AblenkPlatteVertikal2_mc.y + 5;
	AblenkPlatteVertikal_ObenMINUS_mc.y = AblenkPlatteVertikal1_mc.y - 27.25;
	AblenkPlatteVertikal_UntenMINUS_mc.y = AblenkPlatteVertikal2_mc.y + 5;
	bewegung();
}
function k1_L_Slide(k1_LGeslidet: SliderEvent) {
	k1_sliderL_txt.text = "l = " + k1_sliderL_mc.value + " mm";
	kondensatorVertikal_mc.width = k1_sliderL_mc.value;
	VertikalZ_mc.width = k1_sliderL_mc.value;
	AblenkPlatteVertikal_von_ObenMINUS_mc.x = 550 - 19.5 + (VertikalZ_mc.width / 2);
	AblenkPlatteVertikal_von_ObenPLUS_mc.x = 550 - 19.5 + (VertikalZ_mc.width / 2);
	AblenkPlatteVertikal_von_Oben_mc.x = 550 - 19.5 + (VertikalZ_mc.width / 2);
	AblenkPlatteVertikal1_mc.width = kondensatorVertikal_mc.width;
	AblenkPlatteVertikal2_mc.width = kondensatorVertikal_mc.width;
	AblenkPlatteVertikal_Oben_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_Oben_mc.width / 2);
	AblenkPlatteVertikal_Unten_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_Unten_mc.width / 2);
	AblenkPlatteVertikal_ObenPLUS_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_ObenPLUS_mc.width / 2);
	AblenkPlatteVertikal_UntenPLUS_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_UntenPLUS_mc.width / 2);
	AblenkPlatteVertikal_ObenMINUS_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_ObenMINUS_mc.width / 2);
	AblenkPlatteVertikal_UntenMINUS_mc.x = kondensatorVertikal_mc.x + (kondensatorVertikal_mc.width / 2) - (AblenkPlatteVertikal_UntenMINUS_mc.width / 2); //VertikalZ_mc.width=
	bewegung();
}
function k2_Uk_Slide(k2_UkGeslidet: SliderEvent) {
	k2_sliderUk_txt.text = "Uk = " + k2_sliderUk_mc.value + " kV";
	if (k2_sliderUk_mc.value < 0) {
		AblenkPlatteHorizontal_von_SeiteMINUS_mc.visible = false;
		AblenkPlatteHorizontal_von_SeitePLUS_mc.visible = true;
		AblenkPlatteHorizontal_von_Seite_mc.visible = false;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_Oben2MINUS_mc.visible = false;
			AblenkPlatteVertikal_Oben2PLUS_mc.visible = true;
			AblenkPlatteVertikal_Oben2_mc.visible = false;
			AblenkPlatteVertikal_Unten2MINUS_mc.visible = true;
			AblenkPlatteVertikal_Unten2PLUS_mc.visible = false;
			AblenkPlatteVertikal_Unten2_mc.visible = false;
		}
	} else if (k2_sliderUk_mc.value == 0) {
		AblenkPlatteHorizontal_von_SeiteMINUS_mc.visible = false;
		AblenkPlatteHorizontal_von_SeitePLUS_mc.visible = false;
		AblenkPlatteHorizontal_von_Seite_mc.visible = true;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_Oben2MINUS_mc.visible = false;
			AblenkPlatteVertikal_Oben2PLUS_mc.visible = false;
			AblenkPlatteVertikal_Oben2_mc.visible = true;
			AblenkPlatteVertikal_Unten2MINUS_mc.visible = false;
			AblenkPlatteVertikal_Unten2PLUS_mc.visible = false;
			AblenkPlatteVertikal_Unten2_mc.visible = true;
		}
	} else if (k2_sliderUk_mc.value > 0) {
		AblenkPlatteHorizontal_von_SeiteMINUS_mc.visible = true;
		AblenkPlatteHorizontal_von_SeitePLUS_mc.visible = false;
		AblenkPlatteHorizontal_von_Seite_mc.visible = false;
		if (Koordinatenlinien2_mc.visible == true) {
			AblenkPlatteVertikal_Oben2MINUS_mc.visible = true;
			AblenkPlatteVertikal_Oben2PLUS_mc.visible = false;
			AblenkPlatteVertikal_Oben2_mc.visible = false;
			AblenkPlatteVertikal_Unten2MINUS_mc.visible = false;
			AblenkPlatteVertikal_Unten2PLUS_mc.visible = true;
			AblenkPlatteVertikal_Unten2_mc.visible = false;
		}
	}
	ablenkSpannung = k2_sliderUk_mc.value * 1000;
	bewegung();
}
function k2_D_Slide(k2_DGeslidet: SliderEvent) {
	k2_sliderD_txt.text = "d = " + k2_sliderD_mc.value + " mm";
	kondensatorHorizontal_mc.height = k2_sliderD_mc.value;
	kondensatorHorizontal_mc.y = (323.25 + (25 - kondensatorHorizontal_mc.height / 2));
	AblenkPlatteHorizontal1_mc.y = kondensatorHorizontal_mc.y - 5;
	AblenkPlatteHorizontal2_mc.y = kondensatorHorizontal_mc.y + kondensatorHorizontal_mc.height;
	AblenkPlatteVertikal_Oben2_mc.y = AblenkPlatteHorizontal1_mc.y - 27.25;
	AblenkPlatteVertikal_Unten2_mc.y = AblenkPlatteHorizontal2_mc.y + 5;
	AblenkPlatteVertikal_Oben2MINUS_mc.y = AblenkPlatteHorizontal1_mc.y - 27.25;
	AblenkPlatteVertikal_Unten2MINUS_mc.y = AblenkPlatteHorizontal2_mc.y + 5;
	AblenkPlatteVertikal_Oben2PLUS_mc.y = AblenkPlatteHorizontal1_mc.y - 27.25;
	AblenkPlatteVertikal_Unten2PLUS_mc.y = AblenkPlatteHorizontal2_mc.y + 5;
	bewegung();
}
function k2_L_Slide(k2_LGeslidet: SliderEvent) {
	k2_sliderL_txt.text = "l = " + k2_sliderL_mc.value + " mm";
	kondensatorHorizontal_mc.width = k2_sliderL_mc.value;
	kondensatorHorizontal_von_Seite_mc.width = k2_sliderL_mc.value;
	AblenkPlatteHorizontal_von_SeiteMINUS_mc.x = 770 - 19.5 + (kondensatorHorizontal_von_Seite_mc.width / 2);
	AblenkPlatteHorizontal_von_SeitePLUS_mc.x = 770 - 19.5 + (kondensatorHorizontal_von_Seite_mc.width / 2);
	AblenkPlatteHorizontal_von_Seite_mc.x = 770 - 19.5 + (kondensatorHorizontal_von_Seite_mc.width / 2);
	AblenkPlatteHorizontal1_mc.width = kondensatorHorizontal_mc.width;
	AblenkPlatteHorizontal2_mc.width = kondensatorHorizontal_mc.width;
	AblenkPlatteVertikal_Oben2_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Oben2_mc.width / 2);
	AblenkPlatteVertikal_Unten2_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Unten2_mc.width / 2);
	AblenkPlatteVertikal_Oben2MINUS_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Oben2_mc.width / 2);
	AblenkPlatteVertikal_Unten2MINUS_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Unten2_mc.width / 2);
	AblenkPlatteVertikal_Oben2PLUS_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Oben2_mc.width / 2);
	AblenkPlatteVertikal_Unten2PLUS_mc.x = kondensatorHorizontal_mc.x + (kondensatorHorizontal_mc.width / 2) - (AblenkPlatteVertikal_Unten2_mc.width / 2);
	kondensatorHorizontal_von_Seite_mc.width = kondensatorHorizontal_mc.width;
	AblenkPlatteHorizontal_von_SeiteMINUS_mc.x = kondensatorHorizontal_von_Seite_mc.x + (kondensatorHorizontal_von_Seite_mc.width / 2) - AblenkPlatteHorizontal_von_SeiteMINUS_mc.width;
	AblenkPlatteHorizontal_von_SeitePLUS_mc.x = kondensatorHorizontal_von_Seite_mc.x + (kondensatorHorizontal_von_Seite_mc.width / 2) - AblenkPlatteHorizontal_von_SeitePLUS_mc.width;
	AblenkPlatteHorizontal_von_Seite_mc.x = kondensatorHorizontal_von_Seite_mc.x + (kondensatorHorizontal_von_Seite_mc.width / 2) - AblenkPlatteHorizontal_von_Seite_mc.width;


	bewegung();
}