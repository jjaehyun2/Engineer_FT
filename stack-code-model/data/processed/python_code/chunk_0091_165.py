/*

Haupt-Actionscript

*/

/*
Import von Standart Actionscript-Klassen 
*/
import flash.events.Event;
import flash.events.MouseEvent;
import fl.events.SliderEvent;

/*
EventListener
*/
fullscreen_btn.addEventListener(MouseEvent.CLICK, fullscreen);
//EventListener für Fullscreen-Button;
AnAusButton_btn.addEventListener(MouseEvent.CLICK, EinAus);
//EventListener für Ein/Aus-schalt-Button;

/*
Variable und Instanzen
*/
var shape: Shape = new Shape(); //Neue Instanz von der Shape-Klasse
var EinOderAus_boo: Boolean = false; //Boolean-Wert für Zustand
var c: int = 299792458;
var ablenkSpannung: Number = 0;
var teilchenV: Number;
var X_Wert: int;
var Y_Wert: int;
var X_HilfsWert: int;
var Y_HilfsWert: int;
var ablenkungVertikal: Number;
var ablenkungVertikalWeiter: Number;
var HilfsVariableL: Number = 0;
var HilfsVariableM: Number = 0;
var HilfsVariableS: Number = 0;
var kollisionsWert1: Number;
var kollisionsWert2: Number;
var kollisionsWert3: Number;
var kollisionsWert4: Number;
var kollisionsWert5: Number;
var kollisionsWert6: Number;
var kollisionsWert7: Number;
var kollisionsvariableX: int = 1093;
var kollisionsvariableX2: int = 770;

/*
Für den Startzustand jeweilige Texte,Movieclips,Buttons, Grafiken ausblenden
*/
kollisionTest1_mc.visible = false;
kollisionTest2_mc.visible = false;
kollisionTest3_mc.visible = false;

pfeil_Oben_mc.visible = false;
pfeil_Unten_mc.visible = false;
linie_Oben_mc.visible = false;
linie_Unten_mc.visible = false;

AblenkPlatteVertikal_ObenPLUS_mc.visible = false;
AblenkPlatteVertikal_ObenMINUS_mc.visible = false;
AblenkPlatteVertikal_UntenPLUS_mc.visible = false;
AblenkPlatteVertikal_UntenMINUS_mc.visible = false;
AblenkPlatteHorizontal_von_SeiteMINUS_mc.visible = false;
AblenkPlatteHorizontal_von_SeitePLUS_mc.visible = false;
AblenkPlatteVertikal_von_Oben_mc.visible = false;
AblenkPlatteVertikal_von_ObenMINUS_mc.visible = false;
AblenkPlatteVertikal_von_ObenPLUS_mc.visible = false;
AblenkPlatteVertikal_Oben2MINUS_mc.visible = false;
AblenkPlatteVertikal_Oben2PLUS_mc.visible = false;
AblenkPlatteVertikal_Oben2_mc.visible = false;
AblenkPlatteVertikal_Unten2MINUS_mc.visible = false;
AblenkPlatteVertikal_Unten2PLUS_mc.visible = false;
AblenkPlatteVertikal_Unten2_mc.visible = false;

Koordinatenlinien2_mc.visible = false;
Text2_txt.visible = false;
Schirm2_mc.visible = false;
Roehre2_mc.visible = false;
Draehte2_mc.visible = false;
GluewendelUNDWehneltzylinder2_mc.visible = false;
VertikalZ_mc.visible = false;
AblenkPlatteVertikal_Oben2_mc.visible = false;
AblenkPlatteHorizontal1_mc.visible = false;
kondensatorHorizontal_mc.visible = false;
AblenkPlatteHorizontal2_mc.visible = false;
AblenkPlatteVertikal_Unten2_mc.visible = false;
ZwischenEbene_mc.visible = false;
SchirmPunkt_mc.visible = false;
schirm_linie_senkrecht_mc.visible = false;
schirm_linie_waagerecht_mc.visible = false;
schirm_mc.visible = false;
Text3_txt.visible = false;
koordinaten_pfeil_Y_mc.visible = false;
koordinaten_Y_txt.visible = false;
koordinaten_pfeil_Z_mc.visible = false;
koordinaten_Z_txt.visible = false;
y_Ablenkung_vom_schirm_txt.visible = false;
z_Ablenkung_vom_schirm_txt.visible = false;
punkt_speichern_btn.visible = false;
clear_btn.visible = false;
ZwischenEbene2_mc.visible = false;
Anleitung_txt.visible = false;
Kathodenstrahlroere_txt.visible = false;
Simulation_txt.visible = false;
HintergrundWeiß _Anleitung_mc.visible = false;
Hintergrund_Anleitung_mc.visible = false;
X_btn.visible = false;
anleitungtext_txt.visible = false;
Simulationtext_txt.visible = false;
Kathodetext_txt.visible = false;

infopoint1_mc.visible = false;
infopoint2_mc.visible = false;
infopoint3_mc.visible = false;
infopoint4_mc.visible = false;
infopoint6_mc.visible = false;
infopoint7_mc.visible = false;
infopoint8_mc.visible = false;
infopoint9_mc.visible = false;
infopoint10_mc.visible = false;
infopoint11_mc.visible = false;
infopoint12_mc.visible = false;
infofenster1_mc.visible = false;
infofenster2_mc.visible = false;
infofenster3_mc.visible = false;
infofenster4_mc.visible = false;
infofenster5_mc.visible = false;
infofenster6_mc.visible = false;
infofenster7_mc.visible = false;
infofenster9_mc.visible = false;
infofenster10_mc.visible = false;
infofenster11_mc.visible = false;
infofenster12_mc.visible = false;

GluewendelUNDWehneltzylinder2_mc.stop();
GluewendelUNDWehneltzylinder_mc.stop();

hor_txt.alpha = 0.3;
k2_sliderUk_mc.enabled = false;
k2_sliderUk_txt.alpha = 0.3;
k2_sliderD_mc.enabled = false;
k2_sliderD_txt.alpha = 0.3;
k2_sliderL_mc.enabled = false;
k2_sliderL_txt.alpha = 0.3;


/*
Linienfunktion: Zeichnung von der Instanz 'shape'
*/
function bewegung() {
	shape.graphics.clear();
	//vorherige Zeichnung löschen;
	X_Wert = 490;
	Y_Wert = 348.25;
	HilfsVariableL = 0.000;
	HilfsVariableM = 0.000;

	if (EinOderAus_boo == true) {
		/*
		Kollisionen ausrechnen
		*/
		kollisionsWert1 = 0.5 * ((teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2))) * Math.pow(kondensatorVertikal_mc.width / 1000, 2) * 1000;
		if (kollisionsWert1 > (kondensatorVertikal_mc.height / 2) || kollisionsWert1 < -(kondensatorVertikal_mc.height / 2)) {
			kollisionTest1_mc.visible = true;
		} else {
			kollisionTest1_mc.visible = false;
		}
		kollisionsWert2 = 0.5 * ((teilchen_Ladung * k2_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorHorizontal_mc.height / 1000) * Math.pow(teilchenV, 2))) * Math.pow(kondensatorHorizontal_mc.width / 1000, 2) * 1000;
		if (kollisionsWert2 >= (kondensatorHorizontal_mc.height / 2) && kollisionTest1_mc.visible == false || kollisionsWert2 <= -(kondensatorHorizontal_mc.height / 2) && kollisionTest1_mc.visible == false) {
			if (kollisionTest1_mc.visible == false && kollisionTest3_mc.visible == false) {
				kollisionTest2_mc.visible = true;
			}
		} else {
			kollisionTest2_mc.visible = false;
		}
		kollisionsWert3 = kollisionsWert1 + ((teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * (kondensatorVertikal_mc.width / 1000) * ((771.15 - 450 - kondensatorVertikal_mc.width) / 1000) * 1000);
		if (kollisionsWert3 < (-95.6) && kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false || kollisionsWert3 > 95.6 && kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false) {
			kollisionTest3_mc.visible = true;
		} else {
			kollisionTest3_mc.visible = false;
		}
		kollisionsWert4 = kollisionsWert1 + ((teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * (kondensatorVertikal_mc.width / 1000) * ((993 - 450 - kondensatorVertikal_mc.width) / 1000) * 1000);
		kollisionsWert5 = kollisionsWert2 + ((teilchen_Ladung * k2_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorHorizontal_mc.height / 1000) * Math.pow(teilchenV, 2)) * (kondensatorHorizontal_mc.width / 1000) * ((993 - 670 - kondensatorHorizontal_mc.width) / 1000) * 1000);

		/*
		Zeichnung bei Oberansicht
		*/
		if (Text2_txt.visible == true && Text3_txt.visible == false) {
			kollisionsvariableX = 1093;
			while (X_Wert < 550) //bis x=550
			{
				X_HilfsWert = X_Wert + 1;
				Y_HilfsWert = Y_Wert;
				shape.graphics.lineStyle(1, 0x000000);
				shape.graphics.moveTo(X_Wert, Y_Wert);
				shape.graphics.lineTo(X_HilfsWert, Y_Wert);
				X_Wert = X_HilfsWert;
			}
			if (kollisionTest1_mc.visible == false) {
				X_Wert = 550 + VertikalZ_mc.width; //1. Feld "überspringen"
				while (X_Wert < kollisionsvariableX2) //bis x=770
				{
					X_HilfsWert = X_Wert + 1;
					Y_HilfsWert = Y_Wert;
					shape.graphics.lineStyle(1, 0x000000);
					shape.graphics.moveTo(X_Wert, Y_Wert);
					shape.graphics.lineTo(X_HilfsWert, Y_Wert);
					X_Wert = X_HilfsWert;
				}

				while (X_Wert >= 770 && X_Wert < (770 + kondensatorHorizontal_mc.width) && Y_Wert <= (kondensatorHorizontal_mc.y + kondensatorHorizontal_mc.height) && Y_HilfsWert > AblenkPlatteHorizontal1_mc.y + 5 && Y_HilfsWert < AblenkPlatteHorizontal2_mc.y) //bis x=770+Feld
				{
					HilfsVariableL = Math.round((HilfsVariableL + 0.001) * 1000) / 1000;
					ablenkungVertikal = 0.5 * ((teilchen_Ladung * k2_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorHorizontal_mc.height / 1000) * Math.pow(teilchenV, 2))) * Math.pow(HilfsVariableL, 2) * 1000;
					X_HilfsWert = X_Wert + 1;
					shape.graphics.lineStyle(1, 0x000000);
					shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal);
					shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal);
					X_Wert = X_HilfsWert;
					Y_HilfsWert = Y_Wert + ablenkungVertikal;
				}
				if (kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false) {
					while (X_Wert >= (770 + kondensatorHorizontal_mc.width) && X_Wert < 871.15 && Y_HilfsWert > 252.75 && Y_HilfsWert < 443.95) //bis x=871.15
					{
						HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
						ablenkungVertikalWeiter = (teilchen_Ladung * k2_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorHorizontal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
						X_HilfsWert = X_Wert + 1;
						shape.graphics.lineStyle(1, 0x000000);
						shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
						shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
						X_Wert = X_HilfsWert;
						Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;
					}



					while (X_Wert >= 871.15 && X_Wert < kollisionsvariableX) //bis x=1093
					{
						HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
						ablenkungVertikalWeiter = (teilchen_Ladung * k2_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorHorizontal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
						X_HilfsWert = X_Wert + 1;
						kollisionsWert6 = (126.80 / 221.80) * ((HilfsVariableM - (871.15 - (770 + kondensatorHorizontal_mc.width)) / 1000) * 1000) + 95.6;
						kollisionsWert7 = (126.80 / -221.80) * ((HilfsVariableM - (871.15 - (770 + kondensatorHorizontal_mc.width)) / 1000) * 1000) - 95.6;
						if (ablenkungVertikal + ablenkungVertikalWeiter < kollisionsWert6 && ablenkungVertikal + ablenkungVertikalWeiter > kollisionsWert7) {
							shape.graphics.lineStyle(1, 0x000000);
							shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							kollisionTest3_mc.visible = false;
						} else {
							kollisionsvariableX = X_HilfsWert;
							kollisionTest3_mc.visible = true;
						}
						X_Wert = X_HilfsWert;
						Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;

						if (kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false) {
							ablenkung_txt.text = "z = " + String(Math.round(ablenkungVertikal + ablenkungVertikalWeiter)) + " mm"; //Ablenkung schreiben
						}
					}
				}
			}
		}

		/*
		Zeichnung bei Seitenansicht
		*/
		else if (Text2_txt.visible == false && Text3_txt.visible == false) {
			if (kollisionsvariableX < 1093) {
				kollisionTest3_mc.visible = true;
			} else {
				kollisionTest3_mc.visible = false;
			}
			while (X_Wert < 550) //bis x=550
			{
				X_HilfsWert = X_Wert + 1;
				Y_HilfsWert = Y_Wert;
				shape.graphics.lineStyle(1, 0x000000);
				shape.graphics.moveTo(X_Wert, Y_Wert);
				shape.graphics.lineTo(X_HilfsWert, Y_Wert);
				X_Wert = X_HilfsWert;
			}
			while (X_Wert >= 550 && X_Wert < (550 + kondensatorVertikal_mc.width) && Y_Wert < (kondensatorVertikal_mc.y + kondensatorVertikal_mc.height) && Y_HilfsWert > AblenkPlatteVertikal1_mc.y + 5 && Y_HilfsWert < AblenkPlatteVertikal2_mc.y) //bis x=550+Feld
			{
				HilfsVariableL = Math.round((HilfsVariableL + 0.001) * 1000) / 1000;
				ablenkungVertikal = 0.5 * ((teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2))) * Math.pow(HilfsVariableL, 2) * 1000;
				X_HilfsWert = X_Wert + 1;
				shape.graphics.lineStyle(1, 0x000000);
				shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal);
				shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal);
				X_Wert = X_HilfsWert;
				Y_HilfsWert = Y_Wert + ablenkungVertikal;
			}
			if (kollisionTest1_mc.visible == false) {
				kollisionsvariableX2 = 770;
				while (X_Wert >= (550 + kondensatorVertikal_mc.width) && X_Wert < 770 && Y_HilfsWert > 252.75 && Y_HilfsWert < 443.95) //bis x=770
				{
					HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
					ablenkungVertikalWeiter = (teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
					X_HilfsWert = X_Wert + 1;
					shape.graphics.lineStyle(1, 0x000000);
					shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
					shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
					X_Wert = X_HilfsWert;
					Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;
				}

				if (Y_HilfsWert < 252.75 || Y_HilfsWert > 443.95) {
					kollisionsvariableX2 = X_HilfsWert;
					kollisionTest3_mc.visible = true;
				}
				if (kollisionTest2_mc.visible == false) {
					if (X_Wert >= (550 + kondensatorVertikal_mc.width) && X_Wert < 871.15) {
						HilfsVariableS = HilfsVariableM;
						HilfsVariableS = Math.round((HilfsVariableS + 0.001) * 1000) / 1000;
						ablenkungVertikalWeiter = (teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableS * 1000;
						X_Wert = kondensatorHorizontal_von_Seite_mc.x + kondensatorHorizontal_von_Seite_mc.width; //2. Feld "überspringen"
						HilfsVariableM = Math.round((HilfsVariableM + (kondensatorHorizontal_von_Seite_mc.width / 1000)) * 1000) / 1000;
					}

					while (X_Wert >= (550 + kondensatorVertikal_mc.width) && X_Wert < 871.15 && Y_HilfsWert > 252.75 && Y_HilfsWert < 443.95) //bis x=871.15
					{
						HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
						ablenkungVertikalWeiter = (teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
						X_HilfsWert = X_Wert + 1;
						shape.graphics.lineStyle(1, 0x000000);
						shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
						shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
						X_Wert = X_HilfsWert;
						Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;
						if (Y_HilfsWert < 252.75 || Y_HilfsWert > 443.95) {
							kollisionTest3_mc.visible = true;
						}
					}
					if (kollisionTest3_mc.visible == true) {
						while (X_Wert >= 871.15 && X_Wert < kollisionsvariableX) //bis Kollision mit Röhre
						{
							HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
							ablenkungVertikalWeiter = (teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
							X_HilfsWert = X_Wert + 1;
							shape.graphics.lineStyle(1, 0x000000);
							shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							X_Wert = X_HilfsWert;
							Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;
							if (kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false) {
								ablenkung_txt.text = "y = " + String(Math.round(ablenkungVertikal + ablenkungVertikalWeiter)) + " mm"; //SchirmPunkt_mc.y=347+Math.round(ablenkungVertikal + ablenkungVertikalWeiter);
							}
						}
					} else {
						while (X_Wert >= 871.15 && X_Wert < kollisionsvariableX) //bis x=1093 (ende)
						{
							HilfsVariableM = Math.round((HilfsVariableM + 0.001) * 1000) / 1000;
							ablenkungVertikalWeiter = (teilchen_Ladung * k1_sliderUk_mc.value * 1000) / (((1 / Math.sqrt(1 - (Math.pow(teilchenV, 2) / Math.pow(c, 2)))) * teilchen_Masse) * (kondensatorVertikal_mc.height / 1000) * Math.pow(teilchenV, 2)) * HilfsVariableL * HilfsVariableM * 1000;
							X_HilfsWert = X_Wert + 1;
							shape.graphics.lineStyle(1, 0x000000);
							shape.graphics.moveTo(X_Wert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							shape.graphics.lineTo(X_HilfsWert, Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter);
							X_Wert = X_HilfsWert;
							Y_HilfsWert = Y_Wert + ablenkungVertikal + ablenkungVertikalWeiter;
							if (kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false) {
								ablenkung_txt.text = "y = " + String(Math.round(ablenkungVertikal + ablenkungVertikalWeiter)) + " mm";
							}
						}
					}
				}
			}
		}

		/*
		Schirmkoordinaten berechnen
		*/
		if (kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false && kollisionsWert4 < 220 && kollisionsWert4 > (-220) && kollisionsWert5 < 220 && kollisionsWert5 > (-220)) {
			if (Text3_txt.visible == true) {
				SchirmPunkt_mc.visible = true;
			}
			SchirmPunkt_mc.y = 347 + kollisionsWert4;
			SchirmPunkt_mc.x = 747 - kollisionsWert5;
			y_Ablenkung_vom_schirm_txt.text = "y = " + String(Math.round(kollisionsWert4)) + " mm";
			z_Ablenkung_vom_schirm_txt.text = "z = " + String(Math.round(kollisionsWert5)) + " mm";
		} else {
			SchirmPunkt_mc.visible = false;
		}
	}


	addChild(shape); // Zeichnung anzeigen

	/*
	Wertpfeile anpassen
	*/
	if (kollisionTest1_mc.visible == false && kollisionTest2_mc.visible == false && kollisionTest3_mc.visible == false) {
		if (Text2_txt.visible == true) {
			if (ablenkungVertikal + ablenkungVertikalWeiter <= -20) {
				linie_Unten_mc.visible = false;
				pfeil_Unten_mc.visible = false;
				linie_Oben_mc.visible = true;
				pfeil_Oben_mc.visible = true;
				linie_Oben_mc.height = -(ablenkungVertikal + ablenkungVertikalWeiter) - 3;
				linie_Oben_mc.y = 348.25 - 3 - linie_Oben_mc.height;
				pfeil_Oben_mc.y = linie_Oben_mc.y;
			} else if (ablenkungVertikal + ablenkungVertikalWeiter >= 20) {
				linie_Unten_mc.visible = true;
				pfeil_Unten_mc.visible = true;
				linie_Oben_mc.visible = false;
				pfeil_Oben_mc.visible = false;
				linie_Unten_mc.height = ablenkungVertikal + ablenkungVertikalWeiter - 3;
				linie_Unten_mc.y = 348.25 + 3;
				pfeil_Unten_mc.y = linie_Unten_mc.y + linie_Unten_mc.height - pfeil_Unten_mc.height;
			} else {
				linie_Unten_mc.visible = false;
				pfeil_Unten_mc.visible = false;
				linie_Oben_mc.visible = false;
				pfeil_Oben_mc.visible = false;
			}
		} else {
			if (ablenkungVertikal + ablenkungVertikalWeiter <= -20) {
				linie_Unten_mc.visible = false;
				pfeil_Unten_mc.visible = false;
				linie_Oben_mc.visible = true;
				pfeil_Oben_mc.visible = true;
				linie_Oben_mc.height = -(ablenkungVertikal + ablenkungVertikalWeiter) - 3;
				linie_Oben_mc.y = 348.25 - 3 - linie_Oben_mc.height;
				pfeil_Oben_mc.y = linie_Oben_mc.y;
			} else if (ablenkungVertikal + ablenkungVertikalWeiter >= 20) {
				linie_Unten_mc.visible = true;
				pfeil_Unten_mc.visible = true;
				linie_Oben_mc.visible = false;
				pfeil_Oben_mc.visible = false;
				linie_Unten_mc.height = ablenkungVertikal + ablenkungVertikalWeiter - 3;
				linie_Unten_mc.y = 348.25 + 3;
				pfeil_Unten_mc.y = linie_Unten_mc.y + linie_Unten_mc.height - pfeil_Unten_mc.height;
			} else {
				linie_Unten_mc.visible = false;
				pfeil_Unten_mc.visible = false;
				linie_Oben_mc.visible = false;
				pfeil_Oben_mc.visible = false;
			}
		}
	} else {
		linie_Unten_mc.visible = false;
		pfeil_Unten_mc.visible = false;
		linie_Oben_mc.visible = false;
		pfeil_Oben_mc.visible = false;
		ablenkung_txt.text = "y = - - -";
	}
}

/*
Berechnung der Geschwindigkeit
*/
function BerechnungV() {
	teilchenV = c * Math.sqrt(1 - (1 / (1 + (Math.abs(teilchen_Ladung) * (sliderUa_mc.value * 1000)) / (teilchen_Masse * Math.pow(c, 2)))));
	sliderV_txt.text = "-> V = " + String(Math.round(teilchenV)) + " m/s"; //trace(teilchenV);
}

/*
Einschalten/Auschalten
*/
function EinAus(einaus: MouseEvent) {
	if (EinOderAus_boo == false) {
		EinOderAus_boo = true;
	} else if (EinOderAus_boo == true) {
		SchirmPunkt_mc.visible = false;
		EinOderAus_boo = false;
		kollisionTest1_mc.visible = false;
		kollisionTest2_mc.visible = false;
		kollisionTest3_mc.visible = false;
		ablenkung_txt.text = "y = - - -";
	}
	BerechnungV();
	bewegung();
}

/*
Fullscreen ein- oder ausschalten*/
function fullscreen(fullscreening: MouseEvent) {
	if (stage.displayState == StageDisplayState.NORMAL) {
		stage.displayState = StageDisplayState.FULL_SCREEN;
	} else if (stage.displayState == StageDisplayState.FULL_SCREEN) {
		stage.displayState = StageDisplayState.NORMAL;
	}
}