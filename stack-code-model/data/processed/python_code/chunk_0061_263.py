package {
	import flash.display.*;
	import flash.events.*;
	import flash.utils.*;
	import flash.media.*;
	import flash.net.*;
	//import flash.time.*;
	public class keyedit extends Sprite {

		//var s:Sound = new Sound();
		public function edit(keysign:int,keysigncontainer) {

			//keysigncontainer=new Sprite();
			/*
			
			-------------------上面還沒寫
			4:E大調/C#小調
			3:A大調/F#小調
			2:D大調/b小調
			1:F大調/e小調
			0:C大調/a小調
			*/
			//var keysign:int=4;

			var ClassRef2:Class;
			if (keysign>0) {
				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss:MovieClip = new ClassRef2();

				keysigncontainer.addChild(ss);
				ss.x=62;
				ss.y=84;

				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss1:MovieClip = new ClassRef2();
				keysigncontainer.addChild(ss1);
				ss1.x=62;
				ss1.y=216;

				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss2:MovieClip = new ClassRef2();
				keysigncontainer.addChild(ss2);
				ss2.x=62;
				ss2.y=348;

				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss3:MovieClip = new ClassRef2();
				keysigncontainer.addChild(ss3);
				ss3.x=62;
				ss3.y=168;

				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss4:MovieClip = new ClassRef2();
				keysigncontainer.addChild(ss4);
				ss4.x=62;
				ss4.y=168+132;

				ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
				var ss5:MovieClip = new ClassRef2();
				keysigncontainer.addChild(ss5);
				ss5.x=62;
				ss5.y=168+132+132;

				if (keysign>1) {
					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa);
					sa.x=69;
					sa.y=93;

					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa1:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa1);
					sa1.x=69;
					sa1.y=93+132;

					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa2:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa2);
					sa2.x=69;
					sa2.y=93+132+132;

					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa3:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa3);
					sa3.x=69;
					sa3.y=177;


					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa4:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa4);
					sa4.x=69;
					sa4.y=177+132;

					ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
					var sa5:MovieClip = new ClassRef2();
					keysigncontainer.addChild(sa5);
					sa5.x=69;
					sa5.y=177+132+132;

					if (keysign>2) {
						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb);
						sb.x=78;
						sb.y=81;

						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb1:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb1);
						sb1.x=78;
						sb1.y=81+132;

						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb2:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb2);
						sb2.x=78;
						sb2.y=81+132+132;

						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb3:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb3);
						sb3.x=78;
						sb3.y=165;

						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb4:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb4);
						sb4.x=78;
						sb4.y=165+132;


						ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
						var sb5:MovieClip = new ClassRef2();
						keysigncontainer.addChild(sb5);
						sb5.x=78;
						sb5.y=165+132+132;
						if (keysign>3) {
							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc);
							sc.x=86;
							sc.y=90;

							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc1:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc1);
							sc1.x=86;
							sc1.y=90+132;

							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc2:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc2);
							sc2.x=86;
							sc2.y=90+132+132;

							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc3:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc3);
							sc3.x=86;
							sc3.y=174;

							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc4:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc4);
							sc4.x=86;
							sc4.y=174+132;


							ClassRef2 = getDefinitionByName(("Sharp1")) as Class;
							var sc5:MovieClip = new ClassRef2();
							keysigncontainer.addChild(sc5);
							sc5.x=86;
							sc5.y=174+132+132;
						}
					}
				}
			} else if (keysign<0) {
				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss = new ClassRef2();

				keysigncontainer.addChild(ss);
				ss.x=62;
				ss.y=95;

				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss1 = new ClassRef2();
				keysigncontainer.addChild(ss1);
				ss1.x=62;
				ss1.y=95+132;

				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss2 = new ClassRef2();
				keysigncontainer.addChild(ss2);
				ss2.x=62;
				ss2.y=95+132+132;

				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss3= new ClassRef2();
				keysigncontainer.addChild(ss3);
				ss3.x=62;
				ss3.y=179;

				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss4= new ClassRef2();
				keysigncontainer.addChild(ss4);
				ss4.x=62;
				ss4.y=179+132;

				ClassRef2 = getDefinitionByName(("Flat1")) as Class;
				ss5= new ClassRef2();
				keysigncontainer.addChild(ss5);
				ss5.x=62;
				ss5.y=179+132+132;
				if (keysign<-1) {
					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa= new ClassRef2();
					keysigncontainer.addChild(sa);
					sa.x=69;
					sa.y=86;

					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa1= new ClassRef2();
					keysigncontainer.addChild(sa1);
					sa1.x=69;
					sa1.y=86+132;

					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa2 = new ClassRef2();
					keysigncontainer.addChild(sa2);
					sa2.x=69;
					sa2.y=86+132+132;

					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa3= new ClassRef2();
					keysigncontainer.addChild(sa3);
					sa3.x=69;
					sa3.y=170;


					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa4= new ClassRef2();
					keysigncontainer.addChild(sa4);
					sa4.x=69;
					sa4.y=170+132;

					ClassRef2 = getDefinitionByName(("Flat1")) as Class;
					sa5= new ClassRef2();
					keysigncontainer.addChild(sa5);
					sa5.x=69;
					sa5.y=170+132+132;
					if (keysign<-2) {
						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb= new ClassRef2();
						keysigncontainer.addChild(sb);
						sb.x=78;
						sb.y=98;

						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb1 = new ClassRef2();
						keysigncontainer.addChild(sb1);
						sb1.x=78;
						sb1.y=98+132;

						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb2= new ClassRef2();
						keysigncontainer.addChild(sb2);
						sb2.x=78;
						sb2.y=98+132+132;

						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb3= new ClassRef2();
						keysigncontainer.addChild(sb3);
						sb3.x=78;
						sb3.y=183;

						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb4= new ClassRef2();
						keysigncontainer.addChild(sb4);
						sb4.x=78;
						sb4.y=183+132;


						ClassRef2 = getDefinitionByName(("Flat1")) as Class;
						sb5= new ClassRef2();
						keysigncontainer.addChild(sb5);
						sb5.x=78;
						sb5.y=183+132+132;
						if (keysign<-3) {
							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc= new ClassRef2();
							keysigncontainer.addChild(sc);
							sc.x=86;
							sc.y=89;

							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc1= new ClassRef2();
							keysigncontainer.addChild(sc1);
							sc1.x=86;
							sc1.y=89+132;

							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc2= new ClassRef2();
							keysigncontainer.addChild(sc2);
							sc2.x=86;
							sc2.y=89+132+132;

							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc3= new ClassRef2();
							keysigncontainer.addChild(sc3);
							sc3.x=86;
							sc3.y=173;

							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc4= new ClassRef2();
							keysigncontainer.addChild(sc4);
							sc4.x=86;
							sc4.y=173+132;


							ClassRef2 = getDefinitionByName(("Flat1")) as Class;
							sc5= new ClassRef2();
							keysigncontainer.addChild(sc5);
							sc5.x=86;
							sc5.y=173+132+132;
							if (keysign<-4) {
								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd);
								sd.x=89;
								sd.y=102;

								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd1:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd1);
								sd1.x=89;
								sd1.y=102+132;

								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd2:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd2);
								sd2.x=89;
								sd2.y=102+132+132;

								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd3:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd3);
								sd3.x=89;
								sd3.y=102+132+132+132;

								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd4:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd4);
								sd4.x=89;
								sd4.y=102+132+132+132;


								ClassRef2 = getDefinitionByName(("Flat1")) as Class;
								var sd5:MovieClip= new ClassRef2();
								keysigncontainer.addChild(sd5);
								sd5.x=86;
								sd5.y=173+132+132;
							}
						}
					}
				}
			}
		}
	}
}