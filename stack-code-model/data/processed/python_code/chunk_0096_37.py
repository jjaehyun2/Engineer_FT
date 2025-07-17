/*

Teilchenauswahl-Actionscript

*/

import flash.events.Event; //Event-Klasse

/*
Variable und Konstanten
*/
var elektron_Ladung: Number = 1.6022 * Math.pow(10, -19);
var elektron_Masse: Number = 9.10939 * Math.pow(10, -31);
var proton_Ladung: Number = -1.6022 * Math.pow(10, -19);
var proton_Masse: Number = 1.67262 * Math.pow(10, -27);
var alphaTeilchen_Ladung: Number = 2 * (-1.6022 * Math.pow(10, -19));
var alphaTeilchen_Masse: Number = 6.6442 * Math.pow(10, -27);
var teilchen_Ladung: Number = elektron_Ladung;
var teilchen_Masse: Number = elektron_Masse;

/*
Teilchen Auswahl
*/
teilchenAuswahl_cb.addEventListener(Event.CHANGE, teilchenAuswahl);

function teilchenAuswahl(teilchenAusgewaehlt: Event) {
	if (teilchenAuswahl_cb.value == "ElektronenData") {
		if (infomodusAn == true) {
			infopoint11_mc.visible = false;
			infopoint12_mc.visible = false;
			infopoint1_mc.visible = true;
		}
		teilchen_Ladung = elektron_Ladung;
		teilchen_Masse = elektron_Masse;
		GluewendelUNDWehneltzylinder2_mc.gotoAndStop(1);
		GluewendelUNDWehneltzylinder_mc.gotoAndStop(1);

		sliderUa_mc.maximum = 100;
		sliderUa_mc.minimum = 1;
		sliderUa_mc.snapInterval = 1;
		sliderUa_mc.value = 50;
		sliderUa_txt.text = "Ua = 50 kV";
		sliderV_txt.text = "-> V = 89500905 m/s";
		k1_sliderUk_txt.text = "Uk = 0 kV";
		k1_sliderD_txt.text = "d = 50 mm";
		k1_sliderL_txt.text = "l = 85 mm";
		k2_sliderUk_txt.text = "Uk = 0 kV";
		k2_sliderD_txt.text = "d = 50 mm";
		k2_sliderL_txt.text = "l = 85 mm";

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
	} else if (teilchenAuswahl_cb.value == "ProtonenData") {
		if (infomodusAn == true) {
			infopoint11_mc.visible = true;
			infopoint12_mc.visible = false;
			infopoint1_mc.visible = false;
		}
		teilchen_Ladung = proton_Ladung;
		teilchen_Masse = proton_Masse;
		GluewendelUNDWehneltzylinder2_mc.gotoAndStop(2);
		GluewendelUNDWehneltzylinder_mc.gotoAndStop(2);

		sliderUa_mc.maximum = 100;
		sliderUa_mc.minimum = 1;
		sliderUa_mc.snapInterval = 1;
		sliderUa_mc.value = 50;
		sliderUa_txt.text = "Ua = 50 kV";
		sliderV_txt.text = "-> V = 2188432 m/s";
		k1_sliderUk_txt.text = "Uk = 0 kV";
		k1_sliderD_txt.text = "d = 50 mm";
		k1_sliderL_txt.text = "l = 85 mm";
		k2_sliderUk_txt.text = "Uk = 0 kV";
		k2_sliderD_txt.text = "d = 50 mm";
		k2_sliderL_txt.text = "l = 85 mm";

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
	} else if (teilchenAuswahl_cb.value == "alphaTeilchenData") {

		if (infomodusAn == true) {
			infopoint11_mc.visible = false;
			infopoint12_mc.visible = true;
			infopoint1_mc.visible = false;
		}
		teilchen_Ladung = alphaTeilchen_Ladung;
		teilchen_Masse = alphaTeilchen_Masse;
		GluewendelUNDWehneltzylinder2_mc.gotoAndStop(3);
		GluewendelUNDWehneltzylinder_mc.gotoAndStop(3);

		sliderUa_mc.maximum = 100;
		sliderUa_mc.minimum = 1;
		sliderUa_mc.snapInterval = 1;
		sliderUa_mc.value = 50;
		sliderUa_txt.text = "Ua = 50 kV";
		sliderV_txt.text = "-> V = 1552856 m/s";
		k1_sliderUk_txt.text = "Uk = 0 kV";
		k1_sliderD_txt.text = "d = 50 mm";
		k1_sliderL_txt.text = "l = 85 mm";
		k2_sliderUk_txt.text = "Uk = 0 kV";
		k2_sliderD_txt.text = "d = 50 mm";
		k2_sliderL_txt.text = "l = 85 mm";

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
	}
	BerechnungV();
	bewegung();
}