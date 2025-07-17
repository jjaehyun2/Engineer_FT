package {
	import flash.display.*;
	import flash.events.*;
	import flash.utils.*;
	import flash.media.*;
	import flash.net.*;
	//import flash.time.*;
	public class playm {
		public var xx:int;
		public var yy:int;
		public var cc:int;
		public var corotating:int;//1 or 0;
		public var a_x:int;
		public var a_y:int;
		public var a_tempo:String;
		public var a_pitch:int;
		public var test:musical;
		var my_sound:Sound=new Sound();
		var my_channel:SoundChannel;
		var pitch:musical;
		//var s:Sound = new Sound();
		public function voice(keysign:int,speed:int,pitch:musical,delay:int,ppause:int) {
			// my_sound.addEventListener(Event.COMPLETE,loader_complete);




			var sharpflat:String="";
			//my_sound.soundTransform=transform;
			if (ppause!=0) {
				//if (pitch.sharpflat!="Nature") {
					if (pitch.sharpflat=="Sharp") {
						if (((pitch.a_pitch-2)%7==0) || ((pitch.a_pitch-6)%7==0)) {
							pitch.a_pitch=pitch.a_pitch+1;
						} else {
							sharpflat="a";
						}
					} else if (pitch.sharpflat=="Flat") {
						if (((pitch.a_pitch)%7==0) || ((pitch.a_pitch-3)%7==0)) {
							pitch.a_pitch=pitch.a_pitch-1;
						} else {
							sharpflat="b";
						}
					}
					if (keysign>0) {
						if ((pitch.a_pitch-3)%7==0) {
							sharpflat="a";
						}
						if (keysign>1) {
							if ((pitch.a_pitch)%7==0) {
								sharpflat="a";
							}
							if (keysign>2) {
								if ((pitch.a_pitch-4)%7==0) {
									sharpflat="a";
								}
								if (keysign>3) {
									if ((pitch.a_pitch-1)%7==0) {
										sharpflat="a";
									}
									if (keysign>4) {
										if ((pitch.a_pitch-5)%7==0) {
											sharpflat="a";
										}
										if (keysign>5) {
											if ((pitch.a_pitch-2)%7==0) {
												pitch.a_pitch=pitch.a_pitch+1;
											}
											if (keysign>6) {
												if ((pitch.a_pitch-6)%7==0) {
													pitch.a_pitch=pitch.a_pitch+1;
												}
											}
										}
									}
								}
							}
						}
					}
					else if (keysign<0){
						if ((pitch.a_pitch-6)%7==0) {
							sharpflat="b";
						}
						if (keysign<-1){
							if ((pitch.a_pitch-2)%7==0) {
							sharpflat="b";
							}
							if (keysign<-2){
								if ((pitch.a_pitch-5)%7==0) {
									sharpflat="b";
								}
								if (keysign<-3){
									if ((pitch.a_pitch-1)%7==0) {
									sharpflat="b";
									}
									if (keysign<-4){
										if ((pitch.a_pitch-4)%7==0) {
											sharpflat="b";
										}
									}
								}
							}
						}
					}
					//if (pitch.a_tempo!="Crotchetrest"){
						if (pitch.sharpflat!="Nature") {
							my_sound.load(new URLRequest(pitch.a_pitch+ sharpflat +".mp3"));
							trace("play:"+pitch.a_pitch+ sharpflat +".mp3");
							my_channel=my_sound.play(0);
						}else{
							my_sound.load(new URLRequest(pitch.a_pitch +".mp3"));
							trace("play:"+pitch.a_pitch+ sharpflat +".mp3");
							my_channel=my_sound.play(0);
						}	
					//}
					var myTimer2:Timer = new Timer((60/speed)*1000*sign(pitch)/4+((60/speed)*1000*sign(pitch)/5), 1);
					myTimer2.addEventListener("timer", call_delay);
					myTimer2.start();
					
				//}
			}
		}

		function call_delay(event:TimerEvent) {
			my_channel.stop();
		}

		function tempo(namex:String) {
			if (namex=="Crotchet" || namex=="Crotchetrest") {
				return 4;
			} else if (namex=="Minim" || namex=="Minimrest") {
				return 8;
			} else if (namex=="Quaver" || namex=="Quaverrest") {
				return 2;
			} else if (namex=="Semiquaver") {
				return 1;
			} else if (namex=="Semibreve" || namex=="Semibreverest") {
				return 16;
			}
		}
		function sign(musicalarray:musical) {
			if (musicalarray.sign=="dot_plus1") {
				return tempo(musicalarray.a_tempo) * 1.5;
			} else {
				return tempo(musicalarray.a_tempo);
			}
		}
	}
}