package {

	import flash.errors.*;
	import flash.system.*;
	import flash.filters.*;
	import flash.text.*;
	import flash.display.*;
	import flash.events.*;
	import flash.utils.*;
	import flash.media.*;
	import flash.net.*;
	import flash.ui.*;
	import flash.external.*;


	public class guestplay extends Sprite {
		public var url = ExternalInterface.call("function(){return document.location.href;}");
		public var tempurl=decodeURI(url).split("?");
		public var tempvalue=tempurl[1];///?songname=star2468&userid=admin
		public var tempvalue2=tempvalue.split("&");
		
		public var songnametemp=tempvalue2[0].split("=");
		public var songname=songnametemp[1];
		
		public var useridtemp=tempvalue2[1].split("=");
		public var userid=useridtemp[1];
		
		public var speed:int=120;//速度
		public var containericon:Array=new Array(10);//要弄一個陣列把畫面所有音符元件放入
		public var containericonlow:Array=new Array(10);//要弄一個陣列把畫面所有音符元件放入
		public var ClassRef:Class;
		//public var mus:Array=new Array(10);
		public var playmus:Array=new Array(2000);
		public var playmuslow:Array=new Array(2000);

		public var playmusicon:Array=new Array(2000);
		public var playmusiconlow:Array=new Array(2000);

		public var container:Sprite=new Sprite();
		public var container2:Sprite=new Sprite();
		public var keysigncontainer:Sprite=new Sprite();
		public var selectcontainer:Sprite=new Sprite();
		public var mus:Array=new Array(10);
		public var muslow:Array=new Array(10);


		public var x1:int=0;
		public var y1:int=0;
		public var count:int=-1;//高音譜全部第幾個音
		public var countlow:int=-1;//高音譜全部第幾個音

		//======讀取音樂用
		public var page:int=0;//第幾頁
		public var line:int=0;//第幾行
		public var linecount:int=0;//列上第幾個

		public var linelow:int=0;//第幾行
		public var linelowcount:int=0;//列上第幾個
		//======

		//======目前編曲到的位置
		public var editpage:int=0;//編曲到第幾頁
		public var editline:int=0;//編曲到第幾行
		public var editlinecount:int=0;//編曲到列上第幾個

		//======目前編曲到的位置
		public var section:int=16;//一個小節內最高容量
		public var tempsection:int=0;//目前小節儲存數

		public var sectionlow:int=16;//一個小節內最高容量
		public var tempsectionlow:int=0;//目前小節儲存數

		public var section1st:int=66;//第一小節起始數
		public var section2nd:int=208;//第二小節起始數
		public var section3rd:int=351;//第三小節起始數
		public var section4th:int=494;//第四小節起始數
		public var sectionarray:Array=new Array(66,208,351,494);//

		public var sectionstep:int=0;
		public var sectionlowstep:int=0;
		public var pagecounthigh:Array=new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1);
		public var pagecountlow:Array=new Array(-1,-1,-1,-1,-1,-1,-1,-1,-1,-1);
		public var sa_linecount:Array=new Array(10);//高音譜每頁每行個數
		public var sb_linecount:Array=new Array(10);//低音譜每頁每行
		public var sharpflat_log:Array=new Array();
		public var keysign=0;
		

		public function guestplay() {
		
			//Semibreve.addEventListener(MouseEvent.MOUSE_DOWN,Note_Plus);
			//Minim.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Crotchet.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Quaver.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Semiquaver.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Sharp.addEventListener(MouseEvent.MOUSE_DOWN, Sharp_Flat);
			//Flat.addEventListener(MouseEvent.MOUSE_DOWN, Sharp_Flat);
			//Semibreverest.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Minimrest.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Crotchetrest.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Quaverrest.addEventListener(MouseEvent.MOUSE_DOWN, Note_Plus);
			//Nature.addEventListener(MouseEvent.MOUSE_DOWN, Dot_Plus);
			//dot_plus.addEventListener(MouseEvent.MOUSE_DOWN, Dot_Plus);
			
			C.addEventListener(MouseEvent.MOUSE_DOWN,CFunction);
			G.addEventListener(MouseEvent.MOUSE_DOWN,GFunction);
			D.addEventListener(MouseEvent.MOUSE_DOWN,DFunction);
			A.addEventListener(MouseEvent.MOUSE_DOWN,AFunction);
			E.addEventListener(MouseEvent.MOUSE_DOWN,EFunction);
			
			F.addEventListener(MouseEvent.MOUSE_DOWN,FFunction);
			F_flat.addEventListener(MouseEvent.MOUSE_DOWN,F_flatFunction);
			E_flat.addEventListener(MouseEvent.MOUSE_DOWN,E_flatFunction);
			A_flat.addEventListener(MouseEvent.MOUSE_DOWN,A_flatFunction);
			D_flat.addEventListener(MouseEvent.MOUSE_DOWN,D_flatFunction);
			
			include "keybottom.as";
		

			function Remark(event:MouseEvent):void {
				event.currentTarget.gotoAndPlay(2);
			}

			function RemarkOUT(event:MouseEvent):void {
				event.currentTarget.gotoAndPlay(1);
			}
			var keychange:keyedit=new keyedit();
			keychange.edit(keysign,keysigncontainer);
					speedtest.text=String(speed);
			speedtest.addEventListener(KeyboardEvent.KEY_DOWN, textInputHandler);
			function textInputHandler(e:KeyboardEvent){
				trace("tt:"+e.keyCode);
				if (e.keyCode==13){
					speed=Number(speedtest.text);
					trace("speed:"+speed);
				}
			}
					
			底圖.addEventListener(MouseEvent.MOUSE_DOWN, StartSelect);
			stage.addEventListener(MouseEvent.MOUSE_UP, EndSelect);
			//Deletebtn.addEventListener(MouseEvent.CLICK,DeleteHandler);
			//Slur.addEventListener(MouseEvent.MOUSE_DOWN,slur);
			//Eightva.addEventListener(MouseEvent.MOUSE_DOWN,Eva);
			//Cancelbtn.addEventListener(MouseEvent.CLICK,CancelbtnHandler);

			Play_btn.addEventListener(MouseEvent.ROLL_OVER,Remark);
			Play_btn.addEventListener(MouseEvent.ROLL_OUT,RemarkOUT);
			Play_btn.addEventListener(MouseEvent.MOUSE_DOWN,playmusic);
			Pause_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			Pause_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			Pause_btn.addEventListener(MouseEvent.MOUSE_DOWN,pausemusic);
			//New_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//New_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Picture_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Picture_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Music_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Music_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Import_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Import_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Export_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Export_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Text_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Text_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//Videos_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//Videos_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			//CleanAll_btn.addEventListener(MouseEvent.ROLL_OVER, Remark);
			//CleanAll_btn.addEventListener(MouseEvent.ROLL_OUT, RemarkOUT);
			Forward_btn.addEventListener(MouseEvent.MOUSE_DOWN,npage);
			Reverse_btn.addEventListener(MouseEvent.MOUSE_DOWN,lpage);

			for (var i=0; i<10; i++) {//10面
				mus[i]=new Array(5);
				containericon[i]=new Array(5);
				for (var j=0; j<5; j++) {
					mus[i][j]=new Array(500);
					containericon[i][j]=new Array(500);
					for (var k=0; k<500; k++) {
						mus[i][j][k]=new Array(5);
						containericon[i][j][k]=new Array(5);
					}
				}
			}

			for (i=0; i<2000; i++) {
				playmus[i]=new musical();

			}

			for (i=0; i<2000; i++) {
				playmuslow[i]=new musical();
			}

			/*
			for(var a=0; a<10; a++) 
			{
			var page:Array = mus[a];
			for (var b=0; b<5; b++) 
			{
			var line = page[b];
			}
			}
			
			for each(var page in mus)
			{
			for each(var line in page)
			}*/

			for (var a=0; a<10; a++) {
				for (var b=0; b<5; b++) {
					for (var c=0; c<500; c++) {
						for (var d=0; d<5; d++) {
							mus[a][b][c][d]=new musical();
						}
					}
				}
			}
			for (i=0; i<10; i++) {//10面
				muslow[i]=new Array(5);
				containericonlow[i]=new Array(5);
				for (j=0; j<5; j++) {
					muslow[i][j]=new Array(500);
					containericonlow[i][j]=new Array(500);
					for (k=0; k<500; k++) {
						muslow[i][j][k]=new Array(5);
						containericonlow[i][j][k]=new Array(5);
					}
				}
			}

			for (a=0; a<10; a++) {
				for (b=0; b<5; b++) {
					for (c=0; c<500; c++) {
						for (d=0; d<5; d++) {
							muslow[a][b][c][d]=new musical();
						}
					}
				}
			}
			for (i=0; i<10; i++) {//10面
				sa_linecount[i]=new Array(3);
				sb_linecount[i]=new Array(3);
			}
			for (a=0; a<10; a++) {
				for (b=0; b<5; b++) {
					sa_linecount[a][b]=-1;
					sb_linecount[a][b]=-1;
				}
			}
			loadvar();
			selectinit();
			//init(page);
			
			//sendvar();
			
		}
		include "guestconnectread.as"
		//include "sendvar.as"
		//目前各頁個數 之後要把個數都儲存起來


		//var sharpflat_log:Array=new Array();

		include "selectt.as"

		public var select;

		//trace("container:"+container);
		public function init(page:int):void {
			var keychange:keyedit=new keyedit();
			keychange.edit(keysign,keysigncontainer);
			speedtest.text=String(speed);
			titlename.text=songname;
		
		roundObject=null;
		include "slurinit.as"
		EvaLine=null;
		include "eightinit.as"
		
			for (var nn:int=0; nn<10; nn++) {
				for (var bb:int=0; bb<3; bb++) {
					for (var vv:int=0; vv<32; vv++) {
						for (var cor:int=0; cor<5; cor++) {
							if (containericon[nn][bb][vv][cor]!=null) {
								containericon[nn][bb][vv][cor].mouseEnabled=true;
							}

							if (containericonlow[nn][bb][vv][cor]!=null) {
								containericonlow[nn][bb][vv][cor].mouseEnabled=true;
							}
						}
					}
				}
			}
			trace("gg"+page);
			addChild(keysigncontainer);
			addChild(selectcontainer);
			addChild(container2);
			addChild(container);
			container.mouseEnabled=false;
			var test:int=section1st;
			sectionstep=0;//這樣每次重劃才會被清空
			tempsection=0;//
			line=0;
			linecount=0;
			//a=new Array();

			for (var e=1; e<=6; e++) {
				for (var r=1; r<=4; r++) {
					//取得畫面上的線
					var up:MovieClip=this["up"+e+r];
					var down:MovieClip=this["down"+e+r];

					//線消失
					up.visible=false;
					down.visible=false;

				}
			}
			var iconsign;
			var line8=false;//畫線flag
			for (var i=0; i<=pagecounthigh[page]; i++) {
				//var test:int=section1st;
				iconsign=1;
				trace(mus[page][line][linecount][0].a_tempo,mus[page][line][linecount][0].xx,linecount,sectionstep,mus[page][line][linecount][0].a_pitch);
				if ((mus[page][line][linecount][0].a_tempo) != null) {
					//trace("123");
					ClassRef = getDefinitionByName((mus[page][line][linecount][0].a_tempo+"1")) as Class;
					var yy:MovieClip = new ClassRef();
					container.addChild(yy);
					//stage.addChild(yy);



					if (mus[page][line][linecount][0].sharpflat=="Sharp") {
						iconsign=2;
					} else if (mus[page][line][linecount][0].sharpflat=="Flat") {
						iconsign=3;
					} else if (mus[page][line][linecount][0].sharpflat=="Nature") {
						iconsign=4;
					}
					if (mus[page][line][linecount][0].sign=="dot_plus1") {
						iconsign=iconsign+10;
					}
					if (yy.y>51&&yy.y<93||yy.y>198&&yy.y<225||yy.y>330&&yy.y<357) {
						iconsign=iconsign+5;
					}
					yy.gotoAndStop(iconsign);
					//yy.mouseEnabled=false;
					//a.push(yy);
					setColor(yy,0,0,0);
					//a[i]=yy;


					//yy[0].gotoAndStop(5);
					//yy.addEventListener(MouseEvent.click,StopDrag);
					yy.y=mus[page][line][linecount][0].yy;
					containericon[page][line][linecount][0]=yy;

					if (yy.y>57.3&&yy.y<129.3) {
						linejudge=1;
						upper=81.3;
						lower=105.3;
					}
					if (yy.y>135.3&&yy.y<198.3) {
						linejudge=2;
						upper=159.3;
						lower=183.3;
					}
					if (yy.y>198.3&&yy.y<261.3) {
						linejudge=3;
						upper=213.3;
						lower=237.3;
					}
					if (yy.y>267.3&&yy.y<330.3) {
						linejudge=4;
						upper=291.3;
						lower=315.3;
					}
					if (yy.y>330.3&&yy.y<393.3) {
						linejudge=5;
						upper=345.3;
						lower=369.3;
					}
					if (yy.y>399.3&&yy.y<471.3) {
						linejudge=6;
						upper=423.3;
						lower=447.3;
					}

					//yy.gotoAndStop(2);
					//yy.x=test;
					//test=test+35;
					if ((tempsection+sign(mus[page][line][linecount][0]))<=section) {
						if (tempo(mus[page][line][linecount][0].a_tempo)==16) {
							test=test+30;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==8) {
							test=test+47;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==4) {
							test=test+28;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==2) {
							test=test+16;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==1) {
							test=test+8;
						}

						tempsection=tempsection+sign(mus[page][line][linecount][0]);


						line8=false;
					} else {
						line8=true;
						//休止符測試
						if (tempsection<section) {
							determine(stage.mouseX,stage.mouseY);

							var sleepsection=(section-tempsection)/4-1;
							if (sleepsection<0) {
								sleepsection=3;
							}
							trace("剩餘空間"+sleepsign[sleepsection]);
							/*sa_linecount[page][line]++;
							move_next(linecount-1,sa_linecount[page][line],0);
							
							
							
							mus[page][line][linecount][0].xx=mus[page][line][linecount-2][0].xx+30;
							mus[page][line][linecount][0].yy=mus[page][line][linecount-2][0].yy;
							mus[page][line][linecount][0].cc=pagecounthigh[page];
							mus[page][line][linecount][0].a_tempo=sleepsign[sleepsection];
							mus[page][line][linecount][0].a_pitch=5;
							
							init(page);*/
							ClassRef = getDefinitionByName((sleepsign[sleepsection]+"1")) as Class;
							var cc:MovieClip = new ClassRef();
							container.addChild(cc);
							cc.y=mus[page][line][linecount-1][0].yy;
							cc.x=mus[page][line][linecount-1][0].xx+20;


						}

						sectionstep++;
						tempsection=0;
						test=sectionarray[sectionstep];

						if (tempo(mus[page][line][linecount][0].a_tempo)==16) {
							test=test+30;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==8) {
							test=test+47;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==4) {
							test=test+28;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==2) {
							test=test+16;
						} else if (tempo(mus[page][line][linecount][0].a_tempo)==1) {
							test=test+8;
						}

						tempsection=tempsection+sign(mus[page][line][linecount][0]);
						//配置後超過範圍的音符要移到下一行 這部份還沒寫
					}
					trace("放置後"+test);
					mus[page][line][linecount][0].xx=test;
					//顯示合旋
					for (var corotating:int=1; corotating<5; corotating++) {
						if ((mus[page][line][linecount][corotating].a_tempo) != null) {
							ClassRef = getDefinitionByName((mus[page][line][linecount][corotating].a_tempo+"1")) as Class;
							var _corotating:MovieClip = new ClassRef();
							container.addChild(_corotating);
							_corotating.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);
							_corotating.x=test;
							_corotating.y=mus[page][line][linecount][corotating].yy;
							containericon[page][line][linecount][corotating]=_corotating;
							iconsign=1;

							if (mus[page][line][linecount][corotating].sharpflat=="Sharp") {
								iconsign=2;
							} else if (mus[page][line][linecount][corotating].sharpflat=="Flat") {
								iconsign=3;
							} else if (mus[page][line][linecount][corotating].sharpflat=="Nature") {
								iconsign=4;
							}
							if (mus[page][line][linecount][corotating].sign=="dot_plus1") {
								iconsign=iconsign+10;
							}
							if (_corotating.y>51&&_corotating.y<93||_corotating.y>198&&_corotating.y<225||_corotating.y>330&&_corotating.y<357) {
								//_corotating.gotoAndStop(6);
								iconsign=iconsign+5;
							}

							//和弦倒轉以及計算
							if (_corotating.y>57.3&&_corotating.y<129.3) {
								linejudge=1;
								upper=81.3;
								lower=105.3;
							}
							if (_corotating.y>135.3&&_corotating.y<198.3) {
								linejudge=2;
								upper=159.3;
								lower=183.3;
							}
							if (_corotating.y>198.3&&_corotating.y<261.3) {
								linejudge=3;
								upper=213.3;
								lower=237.3;
							}
							if (_corotating.y>267.3&&_corotating.y<330.3) {
								linejudge=4;
								upper=291.3;
								lower=315.3;
							}
							if (_corotating.y>330.3&&_corotating.y<393.3) {
								linejudge=5;
								upper=345.3;
								lower=369.3;
							}
							if (_corotating.y>399.3&&_corotating.y<471.3) {
								linejudge=6;
								upper=423.3;
								lower=447.3;
							}

							var d=0;
							var lineY=0;
							//和弦內加線
							if (_corotating.y-upper<0&&_corotating.y-lower<0) {
								d=(upper-_corotating.y)/6;
								lineY=upper-6;
								for (var pp:int=1; pp<=d; pp++) {
									trace("lineY="+lineY);

									var noteline:MovieClip=new Line;
									keysigncontainer.addChild(noteline);
									noteline.x=_corotating.x-7;
									noteline.y=lineY;

									lineY=lineY-6;

								}
								trace("d="+d);

							}
							_corotating.gotoAndStop(iconsign);

						}
					}
					//顯示合旋

					yy.x=test;

					////////主音加上線
					d=0;
					lineY=0;

					if (yy.y-upper<0&&yy.y-lower<0) {
						d=(upper-yy.y)/6;
						lineY=upper-6;
						for (pp=1; pp<=d; pp++) {
							trace("lineY="+lineY);

							noteline=new Line  ;
							keysigncontainer.addChild(noteline);
							noteline.x=yy.x-7;
							noteline.y=lineY;

							lineY=lineY-6;

						}
						trace("d="+d);

					}
					d=0;
					lineY=0;

					if (yy.y-upper>0&&yy.y-lower>0) {
						d=(yy.y-lower)/6;
						lineY=lower+6;
						for (pp=1; pp<=d; pp++) {
							trace("lineY="+lineY);

							noteline=new Line  ;
							keysigncontainer.addChild(noteline);
							noteline.x=yy.x-7;
							noteline.y=lineY;

							lineY=lineY+6;

						}
						trace("d="+d);

					}

					//////////////




					if ((linecount>0) && (line8==false)) {//八分音符畫線
						if ((mus[page][line][linecount-1][0].a_tempo=="Quaver") && (mus[page][line][linecount][0].a_tempo=="Quaver")) {
							var roundObject2:Line = new Line();
							roundObject2.mouseEnabled=false;
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(mus[page][line][linecount-1][0].xx+3,mus[page][line][linecount-1][0].yy-18);
							roundObject2.graphics.lineTo(mus[page][line][linecount][0].xx+3,mus[page][line][linecount][0].yy-18);
							container.addChild(roundObject2);

							containericon[page][line][linecount][0].gotoAndStop(containericon[page][line][linecount][0].currentFrame+30);

							if ((containericon[page][line][linecount-1][0].currentFrame+30)<50) {
								containericon[page][line][linecount - 1][0].gotoAndStop(containericon[page][line][linecount-1][0].currentFrame+30);
							}
							//*
							//trace("testtt:"+containericon[page][line][linecount-1][0].currentFrame);
							//var temp8=Number(containericon[page][line][linecount-1][0].currentFrame+30);
							//containericon[page][line][linecount-1][0].gotoAndStop(temp8);
							//trace("testtt:"+temp8);
							//*/
							//containericon[page][line][linecount-1][0].gotoAndStop(containericon[page][line][linecount-1][0].currentFrame-19);
							//trace("Frame:"+containericon[page][line][linecount-1][0].currentFrame,"Frame2:"+containericon[page][line][linecount][0].currentFrame);


						} else if ((mus[page][line][linecount-1][0].a_tempo=="Semiquaver") && (mus[page][line][linecount][0].a_tempo=="Semiquaver")) {
							roundObject2 = new Line();
							roundObject2.mouseEnabled=false;
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(mus[page][line][linecount-1][0].xx+3,mus[page][line][linecount-1][0].yy-18);
							roundObject2.graphics.lineTo(mus[page][line][linecount][0].xx+3,mus[page][line][linecount][0].yy-18);
							container.addChild(roundObject2);
							containericon[page][line][linecount][0].gotoAndStop(containericon[page][line][linecount][0].currentFrame+30);


							if ((containericon[page][line][linecount-1][0].currentFrame+30)<50) {
								containericon[page][line][linecount - 1][0].gotoAndStop(containericon[page][line][linecount-1][0].currentFrame+30);
							}
							roundObject2 = new Line();
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(mus[page][line][linecount-1][0].xx+3,mus[page][line][linecount-1][0].yy-12);
							roundObject2.graphics.lineTo(mus[page][line][linecount][0].xx+3,mus[page][line][linecount][0].yy-12);
							container.addChild(roundObject2);
						}
					}
					yy.addEventListener(MouseEvent.MOUSE_UP,StartDrag);
					yy.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);

					linecount++;
					//目前
					if ((sectionstep==3) && ((tempsection+sign(mus[page][line][linecount][0]))>section) || (mus[page][line][linecount][0].a_tempo==null)) {
						line++;
						sectionstep=0;
						tempsection=0;
						linecount=0;
						test=section1st;

						if (line==3) {
							break;
						}
					}

				} else {
					line++;
					sectionstep=0;
					tempsection=0;
					linecount=0;
					test=section1st;

					if (line==3) {
						break;
					}
				}

			}
			//在做擠到後面





			//

			sectionlowstep=0;//這樣每次重劃才會被清空
			tempsectionlow=0;//
			linelow=0;
			linelowcount=0;

			for (e=1; e<=6; e++) {
				for (r=1; r<=4; r++) {
					//取得畫面上的線
					up=this["up"+e+r];
					down=this["down"+e+r];

					//線消失
					up.visible=false;
					down.visible=false;

				}
			}
			line8=false;
			var testlow:int=section1st;
			for (i=0; i<=pagecountlow[page]; i++) {
				iconsign=1;
				trace(muslow[page][linelow][linelowcount][0].a_tempo,muslow[page][linelow][linelowcount][0].xx,linelowcount,sectionlowstep,tempsectionlow);
				if ((muslow[page][linelow][linelowcount][0].a_tempo) != null) {

					ClassRef = getDefinitionByName((muslow[page][linelow][linelowcount][0].a_tempo+"1")) as Class;
					var gg:MovieClip = new ClassRef();
					container.addChild(gg);
					gg.y=muslow[page][linelow][linelowcount][0].yy;


					if (muslow[page][linelow][linelowcount][0].sharpflat=="Sharp") {
						iconsign=2;
					} else if (muslow[page][linelow][linelowcount][0].sharpflat=="Flat") {
						iconsign=3;
					} else if (muslow[page][linelow][linelowcount][0].sharpflat=="Nature") {
						iconsign=4;
					}
					if (muslow[page][linelow][linelowcount][0].sign=="dot_plus1") {
						iconsign=iconsign+10;
					}
					if (gg.y>51&&gg.y<93||gg.y>198&&gg.y<225||gg.y>330&&gg.y<357) {
						iconsign=iconsign+5;
					}
					gg.gotoAndStop(iconsign);

					containericonlow[page][linelow][linelowcount][0]=gg;
					setColor(gg,0,0,0);

					if (gg.y>57.3&&gg.y<129.3) {
						linejudge=1;
						upper=81.3;
						lower=105.3;
					}
					if (gg.y>135.3&&gg.y<198.3) {
						linejudge=2;
						upper=159.3;
						lower=183.3;
					}
					if (gg.y>198.3&&gg.y<261.3) {
						linejudge=3;
						upper=213.3;
						lower=237.3;
					}
					if (gg.y>267.3&&gg.y<330.3) {
						linejudge=4;
						upper=291.3;
						lower=315.3;
					}
					if (gg.y>330.3&&gg.y<393.3) {
						linejudge=5;
						upper=345.3;
						lower=369.3;
					}
					if (gg.y>399.3&&gg.y<471.3) {
						linejudge=6;
						upper=423.3;
						lower=447.3;
					}
					//yy.x=testlow;
					//testlow=testlow+35;
					if ((tempsectionlow+sign(muslow[page][linelow][linelowcount][0]))<=section) {
						if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==16) {
							testlow=testlow+30;//71
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==8) {
							testlow=testlow+47;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==4) {
							testlow=testlow+28;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==2) {
							testlow=testlow+16;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==1) {
							testlow=testlow+8;
						}

						tempsectionlow=tempsectionlow+sign(muslow[page][linelow][linelowcount][0]);
						line8=false;
					} else {
						line8=true;
						//休止符測試
						if (tempsectionlow<section) {
							ClassRef = getDefinitionByName(("Crotchetrest1")) as Class;
							var dd:MovieClip = new ClassRef();
							container.addChild(dd);
							dd.y=muslow[page][linelow][linelowcount-1][0].yy;
							dd.x=muslow[page][linelow][linelowcount-1][0].xx+40;
						}


						sectionlowstep++;
						tempsectionlow=0;
						testlow=sectionarray[sectionlowstep];

						if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==16) {
							testlow=testlow+30;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==8) {
							testlow=testlow+47;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==4) {
							testlow=testlow+28;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==2) {
							testlow=testlow+16;
						} else if (tempo(muslow[page][linelow][linelowcount][0].a_tempo)==1) {
							testlow=testlow+8;
						}

						tempsectionlow=tempsectionlow+sign(mus[page][linelow][linelowcount][0]);
						//配置後超過範圍的音符要移到下一行 這部份還沒寫
					}
					trace("放置後"+testlow);
					muslow[page][linelow][linelowcount][0].xx=testlow;

					for (corotating=1; corotating<5; corotating++) {
						if ((muslow[page][linelow][linelowcount][corotating].a_tempo) != null) {
							ClassRef = getDefinitionByName((muslow[page][linelow][linelowcount][corotating].a_tempo+"1")) as Class;
							var _corotating2:MovieClip = new ClassRef();
							container.addChild(_corotating2);
							_corotating2.x=testlow;
							_corotating2.y=muslow[page][linelow][linelowcount][corotating].yy;
							containericonlow[page][linelow][linelowcount][corotating]=_corotating2;
							iconsign=1;

							if (muslow[page][linelow][linelowcount][corotating].sharpflat=="Sharp") {
								iconsign=2;
							} else if (muslow[page][linelow][linelowcount][corotating].sharpflat=="Flat") {
								iconsign=3;
							} else if (muslow[page][linelow][linelowcount][corotating].sharpflat=="Nature") {
								iconsign=4;
							}
							if (muslow[page][linelow][linelowcount][corotating].sign=="dot_plus1") {
								iconsign=iconsign+10;
							}
							if (_corotating2.y>51&&_corotating2.y<93||_corotating2.y>198&&_corotating2.y<225||_corotating2.y>330&&_corotating2.y<357) {
								iconsign=iconsign+5;
							}

							//和弦倒轉以及計算
							if (_corotating2.y>57.3&&_corotating2.y<129.3) {
								linejudge=1;
								upper=81.3;
								lower=105.3;
							}
							if (_corotating2.y>135.3&&_corotating2.y<198.3) {
								linejudge=2;
								upper=159.3;
								lower=183.3;
							}
							if (_corotating2.y>198.3&&_corotating2.y<261.3) {
								linejudge=3;
								upper=213.3;
								lower=237.3;
							}
							if (_corotating2.y>267.3&&_corotating2.y<330.3) {
								linejudge=4;
								upper=291.3;
								lower=315.3;
							}
							if (_corotating2.y>330.3&&_corotating2.y<393.3) {
								linejudge=5;
								upper=345.3;
								lower=369.3;
							}
							if (_corotating2.y>399.3&&_corotating2.y<471.3) {
								linejudge=6;
								upper=423.3;
								lower=447.3;
							}

							d=0;
							lineY=0;
							//和弦內加線
							if (_corotating2.y-upper<0&&_corotating2.y-lower<0) {
								d=(upper-_corotating2.y)/6;
								lineY=upper-6;
								for (pp=1; pp<=d; pp++) {
									trace("lineY="+lineY);

									noteline=new Line;
									keysigncontainer.addChild(noteline);
									noteline.x=_corotating2.x-7;
									noteline.y=lineY;

									lineY=lineY-6;

								}
								trace("d="+d);

							}
							_corotating2.gotoAndStop(iconsign);
						}
					}
					gg.x=testlow;

					////////主音加上線
					d=0;
					lineY=0;

					if (gg.y-upper<0&&gg.y-lower<0) {
						d=(upper-gg.y)/6;
						lineY=upper-6;
						for (pp=1; pp<=d; pp++) {
							trace("lineY="+lineY);

							noteline=new Line  ;
							keysigncontainer.addChild(noteline);
							noteline.x=gg.x-7;
							noteline.y=lineY;

							lineY=lineY-6;

						}
						trace("d="+d);

					}
					d=0;
					lineY=0;

					if (gg.y-upper>0&&gg.y-lower>0) {
						d=(gg.y-lower)/6;
						lineY=lower+6;
						for (pp=1; pp<=d; pp++) {
							trace("lineY="+lineY);

							noteline=new Line  ;
							keysigncontainer.addChild(noteline);
							noteline.x=gg.x-7;
							noteline.y=lineY;

							lineY=lineY+6;

						}
						trace("d="+d);

					}

					//////////////

					if ((linelowcount>0) && (line8==false)) {//八分音符畫線
						if ((muslow[page][linelow][linelowcount-1][0].a_tempo=="Quaver") && (muslow[page][linelow][linelowcount][0].a_tempo=="Quaver")) {
							roundObject2 = new Line();
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(muslow[page][linelow][linelowcount-1][0].xx+3,muslow[page][linelow][linelowcount-1][0].yy-18);
							roundObject2.graphics.lineTo(muslow[page][linelow][linelowcount][0].xx+3,muslow[page][linelow][linelowcount][0].yy-18);
							container.addChild(roundObject2);

							containericonlow[page][linelow][linelowcount][0].gotoAndStop(containericonlow[page][linelow][linelowcount][0].currentFrame+30);

							if ((containericonlow[page][linelow][linelowcount-1][0].currentFrame+30)<50) {
								containericonlow[page][linelow][linelowcount-1][0].gotoAndStop(containericonlow[page][linelow][linelowcount-1][0].currentFrame+30);
							}
						} else if ((muslow[page][linelow][linelowcount-1][0].a_tempo=="Semiquaver") && (muslow[page][linelow][linelowcount][0].a_tempo=="Semiquaver")) {
							roundObject2 = new Line();
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(muslow[page][linelow][linelowcount-1][0].xx+3,muslow[page][linelow][linelowcount-1][0].yy-18);
							roundObject2.graphics.lineTo(muslow[page][linelow][linelowcount][0].xx+3,muslow[page][linelow][linelowcount][0].yy-18);
							container.addChild(roundObject2);
							containericonlow[page][linelow][linelowcount][0].gotoAndStop(containericonlow[page][linelow][linelowcount][0].currentFrame+30);

							if ((containericonlow[page][linelow][linelowcount-1][0].currentFrame+30)<50) {
								containericonlow[page][linelow][linelowcount - 1][0].gotoAndStop(containericonlow[page][linelow][linelowcount-1][0].currentFrame+30);
							}
							roundObject2 = new Line();
							roundObject2.graphics.lineStyle(2, 00000000, .75);
							roundObject2.graphics.moveTo(muslow[page][linelow][linelowcount-1][0].xx+3,muslow[page][linelow][linelowcount-1][0].yy-12);
							roundObject2.graphics.lineTo(muslow[page][linelow][linelowcount][0].xx+3,muslow[page][linelow][linelowcount][0].yy-12);
							container.addChild(roundObject2);
						}
					}
					gg.addEventListener(MouseEvent.MOUSE_UP,StartDrag);
					gg.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);
					linelowcount++;
					//目前
					if ((sectionlowstep==3) && ((tempsectionlow+sign(muslow[page][linelow][linelowcount][0]))>section) || (muslow[page][linelow][linelowcount][0].a_tempo==null)) {
						linelow++;
						sectionlowstep=0;
						tempsectionlow=0;
						linelowcount=0;
						testlow=section1st;
						if (linelow==3) {
							break;
						}
					}

				} else {

				}

			}

			//trace(ClassRef);
			//trace(muslow[page][0][0][1].a_tempo);

		}
		public var nnx:int=0;
		public function npage(event:MouseEvent) {
			if (page<9) {
				page=page+1;
			}
			trace("cc"+page);
			removeChild(container);
			container=new Sprite();
			init(page);
			//init(page);
		}

		public function lpage(event:MouseEvent) {
			if (page>0) {
				page=page-1;
			}

			removeChild(container);
			container=new Sprite();
			init(page);
			//init(page);
		}


		public function Note_Plus(event:MouseEvent):void {
			trace("Note_Plus");

			//trace(event.currentTarget.name);
			ClassRef = getDefinitionByName((event.currentTarget.name+1)) as Class;
			var 印章:MovieClip = new ClassRef();
			this.addChild(印章);
			印章.x=event.stageX;
			印章.y=event.stageY;
			印章.addEventListener(Event.ENTER_FRAME , StampDrag );
			印章.addEventListener(MouseEvent.MOUSE_DOWN, Stamp);
			印章.addEventListener(MouseEvent.MOUSE_WHEEL,CancelStamp);
		}

		public function Dot_Plus(event:MouseEvent):void {
			trace("Dot_Plus");
			//trace(event.currentTarget.name);
			ClassRef = getDefinitionByName((event.currentTarget.name+1)) as Class;
			var 印章:MovieClip = new ClassRef();
			container2.addChild(印章);

			印章.x=event.stageX-印章.width/2;
			印章.y=event.stageY-印章.height/2;
			印章.addEventListener(Event.ENTER_FRAME , StampDrag);
			//印章.addEventListener(MouseEvent.MOUSE_DOWN, Stamp);
			印章.addEventListener(MouseEvent.MOUSE_WHEEL,CancelStamp);
		}

		public function Sharp_Flat(event:MouseEvent):void {
			trace("Sharp_Flat");
			//trace(event.currentTarget.name);
			ClassRef = getDefinitionByName((event.currentTarget.name+1)) as Class;
			var 印章:MovieClip = new ClassRef();
			container2.addChild(印章);

			印章.x=event.stageX-印章.width/2;
			印章.y=event.stageY-印章.height/2;
			印章.addEventListener(Event.ENTER_FRAME , StampDrag );
			//印章.addEventListener(MouseEvent.MOUSE_DOWN, StampSharp_Flat);
			印章.addEventListener(MouseEvent.MOUSE_WHEEL,CancelStamp);
		}

		public function StampSharp_Flat(event:MouseEvent):void {
			if (stage.mouseX<=640) {

			}
			removeChild(container2);
			container2=new Sprite();
			init(page);
		}


		public function CancelStamp(event:MouseEvent):void {
			trace("CancelStamp");
			event.currentTarget.parent.removeChild(event.currentTarget);
			ClassRef=null;

			for (var nn:int=0; nn<10; nn++) {
				for (var bb:int=0; bb<3; bb++) {
					for (var vv:int=0; vv<32; vv++) {
						for (var cor:int=0; cor<5; cor++) {
							if (containericon[nn][bb][vv][cor]!=null) {
								containericon[nn][bb][vv][cor].mouseEnabled=true;
							}

							if (containericonlow[nn][bb][vv][cor]!=null) {
								containericonlow[nn][bb][vv][cor].mouseEnabled=true;
							}
						}
					}
				}
			}
		}

		public var linejudge=0;
		public var upper=0;
		public var lower=0;
		public function StampDrag(event:Event):void {

			var x=stage.mouseX;
			var y=stage.mouseY;
			event.currentTarget.x=x;
			event.currentTarget.y=Math.floor(y/3)*3;

			//加線
			if (y>57.3&&y<129.3) {
				linejudge=1;
				upper=81.3;
				lower=105.3;
			}
			if (y>135.3&&y<198.3) {
				linejudge=2;
				upper=159.3;
				lower=183.3;
			}
			if (y>198.3&&y<261.3) {
				linejudge=3;
				upper=213.3;
				lower=237.3;
			}
			if (y>267.3&&y<330.3) {
				linejudge=4;
				upper=291.3;
				lower=315.3;
			}
			if (y>330.3&&y<393.3) {
				linejudge=5;
				upper=345.3;
				lower=369.3;
			}
			if (y>399.3&&y<471.3) {
				linejudge=6;
				upper=423.3;
				lower=447.3;
			}
			//container.mouseEnabled=false;
			if (((ClassRef!=Sharp1) && (ClassRef!=Flat1)) && ((ClassRef!=Nature1) && (ClassRef!=dot_plus1))) {
				for (var nn:int=0; nn<10; nn++) {
					for (var bb:int=0; bb<3; bb++) {
						for (var vv:int=0; vv<32; vv++) {
							for (var cor:int=0; cor<5; cor++) {
								if (containericon[nn][bb][vv][cor]!=null) {
									containericon[nn][bb][vv][cor].mouseEnabled=false;
								}
								if (containericonlow[nn][bb][vv][cor]!=null) {
									containericonlow[nn][bb][vv][cor].mouseEnabled=false;
								}
							}
						}
					}
				}
			} else {
				for (nn=0; nn<10; nn++) {
					for (bb=0; bb<3; bb++) {
						for (vv=0; vv<32; vv++) {
							for (cor=0; cor<5; cor++) {
								if (containericon[nn][bb][vv][cor]!=null) {
									containericon[nn][bb][vv][cor].mouseEnabled=true;
								}
								if (containericonlow[nn][bb][vv][cor]!=null) {
									containericonlow[nn][bb][vv][cor].mouseEnabled=true;
								}
							}
						}
					}
				}

			}
			stage.addEventListener(MouseEvent.MOUSE_MOVE,lineHandler);
		}
		public function lineHandler(e:MouseEvent):void {
			if (ClassRef!=null) {
				if (stage.mouseX<=640) {
					for (var i = 1; i <= 6; i++) {
						for (var j=1; j<=4; j++) {
							if (i==linejudge) {
								//取得畫面上的線
								var upV:MovieClip=this["up"+linejudge+j];
								var downV:MovieClip=this["down"+linejudge+j];

								if (upV.y+1>e.stageY) {
									upV.visible=true;
								} else {
									upV.visible=false;

								}
								if (downV.y-1<e.stageY) {
									downV.visible=true;
								} else {
									downV.visible=false;

								}//跟隨滑鼠的座標
								downV.x=upV.x=e.stageX-7;
							} else if (i!=linejudge) {
								var upinV:MovieClip=this["up"+i+j];
								var downinV:MovieClip=this["down"+i+j];

								//線消失
								upinV.visible=false;
								downinV.visible=false;

								downinV.x=upinV.x=e.stageX-7;
							}
						}
					}
				}
			}
		}
		public var clickline:int=0;//1:第一列 2:第二列 3:第三列
		public var clickhighlow:int=0;//0高音譜 1低音譜
		public var sleepsign:Array=new Array("Crotchetrest","Minimrest","Semibreverest","Quaverrest");
		public var sleepkey=-1;
		public function Stamp(event:MouseEvent):void {
			var linepointhigh:Array=new Array(105,237,369);
			var linepointlow:Array=new Array(177,309,441);

			if (stage.mouseX<=640) {
				trace("Stamp");

				var mc:MovieClip = new ClassRef();
				//array.push(mc);

				container.addChild(mc);
				mc.x=event.stageX;
				mc.y=event.stageY;
				//mc.name = "OO";
				trace("xy:",stage.mouseX,stage.mouseY);
				clickline=0;
				determine(stage.mouseX,stage.mouseY);
				trace("cliciline"+clickline,clickhighlow);
				mc.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);
				//mc.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);

				//trace("tttttt"+highlocation);


				//多一個音符->
				if (clickhighlow==0) {

					var highlocation:int=-1;

					for (var i=0; i<32; i++) {
						if ((mus[page][clickline][i][0].xx>=event.currentTarget.x-2) && (mus[page][clickline][i][0].xx<=event.currentTarget.x+2)) {
							highlocation=i;
							break;
						}
					}
					trace("highlocation:"+highlocation);
					if (highlocation==-1) {
						pagecounthigh[page]=Number(pagecounthigh[page])+1;
						sa_linecount[page][clickline]=Number(sa_linecount[page][clickline])+1;
						//abc.text="h"+String(sa_linecount[0][clickline]);
						trace("程式尚未定位過的音符位置",event.currentTarget.x,event.currentTarget.y);
						var maxtemp:int=0;// 目前擺放此音符的前一個音符x座標位置
						var counttemp:int=-1;//目前擺放此音符的前一個音符 是第幾個音符
						for (i=0; i<Number(sa_linecount[page][clickline]); i++) {
							if ((event.currentTarget.x>mus[page][clickline][i][0].xx)) {
								if (mus[page][clickline][i][0].xx>maxtemp) {
									maxtemp=mus[page][clickline][i][0].xx;
									counttemp=i;
								}
							}
						}

						trace("前一個x"+maxtemp,"前一個音符第幾個"+counttemp,"目前幾個"+sa_linecount[page][clickline]+"頁數"+page);
						if ((sa_linecount[page][clickline]>0) && (counttemp+1<sa_linecount[page][clickline])) {
							move_next(counttemp,sa_linecount[page][clickline],clickhighlow);
						}
						//var tempo:Array();
						//237 369

						trace(clickline+":test");
						var cal_distance:int=(event.currentTarget.y-linepointhigh[clickline])/3;
						sleepkey=-1;

						for (var s:int=0; s<4; s++) {
							if (event.currentTarget.callname==sleepsign[s]) {
								sleepkey=s;
								break;
							}
						}
						if (sleepkey==-1) {
							if (sa_linecount[page][clickline]==0) {
								trace("t0"+clickline,counttemp+1);
								mus[page][clickline][sa_linecount[page][clickline]][0].xx=event.currentTarget.x;
								mus[page][clickline][sa_linecount[page][clickline]][0].yy=event.currentTarget.y;
								mus[page][clickline][sa_linecount[page][clickline]][0].cc=pagecounthigh[page];
								mus[page][clickline][sa_linecount[page][clickline]][0].a_tempo=event.currentTarget.callname;
								trace(event.currentTarget.callname);
								mus[page][clickline][sa_linecount[page][clickline]][0].a_pitch=3-cal_distance;
							} else {
								trace("t1"+clickline,counttemp+1);
								mus[page][clickline][counttemp+1][0].xx=event.currentTarget.x;
								mus[page][clickline][counttemp+1][0].yy=event.currentTarget.y;
								mus[page][clickline][counttemp+1][0].cc=pagecounthigh[page];
								mus[page][clickline][counttemp+1][0].a_tempo=event.currentTarget.callname;
								mus[page][clickline][counttemp+1][0].a_pitch=3-cal_distance;
							}
							var m:playm=new playm();

							m.voice(keysign,speed,mus[page][clickline][counttemp+1][0],playsteps2,ppause);

						} else {
							mus[page][clickline][counttemp+1][0].xx=event.currentTarget.x;
							mus[page][clickline][counttemp+1][0].yy=event.currentTarget.y;
							mus[page][clickline][counttemp+1][0].cc=pagecounthigh[page];
							mus[page][clickline][counttemp+1][0].a_tempo=event.currentTarget.callname;
							mus[page][clickline][counttemp+1][0].a_pitch=5;

						}

					} else {
						cal_distance=(event.currentTarget.y-linepointhigh[clickline])/3;
						//trace(":"+event.currentTarget.y);


						for (i=1; i<5; i++) {
							if (mus[page][clickline][highlocation][i].a_tempo==null) {
								mus[page][clickline][highlocation][i].xx=event.currentTarget.x;
								mus[page][clickline][highlocation][i].yy=event.currentTarget.y;
								mus[page][clickline][highlocation][i].cc=pagecounthigh[page];
								mus[page][clickline][highlocation][i].a_tempo=event.currentTarget.callname;
								mus[page][clickline][highlocation][i].a_pitch=3-cal_distance;
								var n:playm=new playm();

								n.voice(keysign,speed,mus[page][clickline][highlocation][i],playsteps2,ppause);
								break;
							}
						}

					}
				} else {
					var lowlocation:int=-1;

					for (i=0; i<32; i++) {
						if ((muslow[page][clickline][i][0].xx>=event.currentTarget.x-2) && (muslow[page][clickline][i][0].xx<=event.currentTarget.x+2)) {
							lowlocation=i;
							break;
						}
					}
					trace("lowlocation:"+lowlocation);
					if (lowlocation==-1) {
						pagecountlow[page]=Number(pagecountlow[page])+1;
						sb_linecount[page][clickline]=Number(sb_linecount[page][clickline])+1;
						//abc.text="L"+String(sb_linecount[0][clickline]+":"+clickline);
						trace("程式尚未定位過的音符位置",event.currentTarget.x,event.currentTarget.y);

						maxtemp=0;// 目前擺放此音符的前一個音符x座標位置
						counttemp=-1;//目前擺放此音符的前一個音符 是第幾個音符
						for (i=0; i<sb_linecount[page][clickline]; i++) {
							if ((event.currentTarget.x>muslow[page][clickline][i][0].xx)) {
								if (muslow[page][clickline][i][0].xx>maxtemp) {
									maxtemp=muslow[page][clickline][i][0].xx;
									counttemp=i;
								}
							}
						}

						trace("前一個x"+maxtemp,"前一個音符第幾個"+counttemp,"目前幾個"+sb_linecount[page][clickline]+"頁數"+page);
						if ((sb_linecount[page][clickline]>0) && (counttemp+1<sb_linecount[page][clickline])) {
							move_next(counttemp,sb_linecount[page][clickline],clickhighlow);
						}
						//var tempo:Array();


						trace(clickline+":test");
						var callow_distance:int=(event.currentTarget.y-linepointlow[clickline])/3;
						sleepkey=-1;

						for (s=0; s<4; s++) {
							if (event.currentTarget.callname==sleepsign[s]) {
								sleepkey=s;
								break;
							}
						}
						if (sleepkey==-1) {



							if (sb_linecount[page][clickline]==0) {
								trace("t0"+clickline,counttemp+1);
								muslow[page][clickline][sb_linecount[page][clickline]][0].xx=event.currentTarget.x;
								muslow[page][clickline][sb_linecount[page][clickline]][0].yy=event.currentTarget.y;
								muslow[page][clickline][sb_linecount[page][clickline]][0].cc=pagecountlow[page];
								muslow[page][clickline][sb_linecount[page][clickline]][0].a_tempo=event.currentTarget.callname;
								muslow[page][clickline][sb_linecount[page][clickline]][0].a_pitch=(-7)-callow_distance;
							} else {
								trace("t1"+clickline,counttemp+1);
								muslow[page][clickline][counttemp+1][0].xx=event.currentTarget.x;
								muslow[page][clickline][counttemp+1][0].yy=event.currentTarget.y;
								muslow[page][clickline][counttemp+1][0].cc=pagecountlow[page];
								muslow[page][clickline][counttemp+1][0].a_tempo=event.currentTarget.callname;
								muslow[page][clickline][counttemp+1][0].a_pitch=(-7)-callow_distance;
							}
							var m2:playm=new playm();

							m2.voice(keysign,speed,muslow[page][clickline][counttemp+1][0],playsteps2,ppause);
						} else {
							muslow[page][clickline][counttemp+1][0].xx=event.currentTarget.x;
							muslow[page][clickline][counttemp+1][0].yy=event.currentTarget.y;
							muslow[page][clickline][counttemp+1][0].cc=pagecountlow[page];
							muslow[page][clickline][counttemp+1][0].a_tempo=event.currentTarget.callname;
							muslow[page][clickline][counttemp+1][0].a_pitch=(-7)-callow_distance;

						}
					} else {
						callow_distance=(event.currentTarget.y-linepointlow[clickline])/3;
						for (i=1; i<5; i++) {
							if (muslow[page][clickline][lowlocation][i].a_tempo==null) {
								muslow[page][clickline][lowlocation][i].xx=event.currentTarget.x;
								muslow[page][clickline][lowlocation][i].yy=event.currentTarget.y;
								muslow[page][clickline][lowlocation][i].cc=pagecountlow[page];
								muslow[page][clickline][lowlocation][i].a_tempo=event.currentTarget.callname;
								muslow[page][clickline][lowlocation][i].a_pitch=(-7)-callow_distance;
								var n2:playm=new playm();

								n2.voice(keysign,speed,muslow[page][clickline][lowlocation][i],playsteps2low,ppause);
								break;
							}
						}

					}






				}
				
				removeChild(container);

				container=new Sprite();



				init(page);
			}

		}
		// 這裡的程式位置可以決定是新的音符 或是現有音符的位置


		public function StopDrag(event:MouseEvent):void {

			removeChild(container2);
			container2=new Sprite();
			trace("StopDrag");
			select=event.currentTarget;
			if (ClassRef==dot_plus1) {

				if (event.currentTarget.currentFrame<=10) {
					event.currentTarget.gotoAndStop(2);
					determine(event.currentTarget.x,event.currentTarget.y);

					if (clickhighlow==0) {
						for (var m:int=0; m<=sa_linecount[page][clickline]; m++) {
							for (var n:int=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sign="dot_plus1";
									trace("dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sign="dot_plus1";
									trace("dot:low");
								}
							}
						}
					}
				} else {
					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sign=null;
									trace("not dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sign=null;
									trace("not dot:low");
								}
							}
						}
					}
					event.currentTarget.gotoAndStop(1);


				}
			} else if (ClassRef==Sharp1) {
				trace("SHARP");
				if (event.currentTarget.currentFrame!=3) {
					event.currentTarget.gotoAndStop(3);
					determine(event.currentTarget.x,event.currentTarget.y);

					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat="Sharp";
									trace("dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat="Sharp";
									trace("dot:low");
								}
							}
						}
					}
				} else {
					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat=null;
									trace("not dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat=null;
									trace("not dot:low");
								}
							}
						}
					}
					event.currentTarget.gotoAndStop(1);


				}
			} else if (ClassRef==Flat1) {
				trace("FLAT");
				if (event.currentTarget.currentFrame!=4) {
					event.currentTarget.gotoAndStop(4);
					determine(event.currentTarget.x,event.currentTarget.y);

					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat="Flat";
									trace("dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat="Flat";
									trace("dot:low");
								}
							}
						}
					}
				} else {
					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat=null;
									trace("not dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat=null;
									trace("not dot:low");
								}
							}
						}
					}
					event.currentTarget.gotoAndStop(1);


				}
			} else if (ClassRef==Nature1) {
				trace("NATURE");
				if (event.currentTarget.currentFrame!=5) {
					event.currentTarget.gotoAndStop(5);
					determine(event.currentTarget.x,event.currentTarget.y);

					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat="Nature";
									trace("dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat="Nature";
									trace("dot:low");
								}
							}
						}
					}
				} else {
					if (clickhighlow==0) {
						for (m=0; m<=sa_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((mus[page][clickline][m][n].xx==event.currentTarget.x) && (mus[page][clickline][m][n].yy==event.currentTarget.y)) {
									mus[page][clickline][m][n].sharpflat=null;
									trace("not dot:high");
								}
							}
						}
					} else {
						for (m=0; m<=sb_linecount[page][clickline]; m++) {
							for (n=0; n<=4; n++) {
								if ((muslow[page][clickline][m][n].xx==event.currentTarget.x) && (muslow[page][clickline][m][n].yy==event.currentTarget.y)) {
									muslow[page][clickline][m][n].sharpflat=null;
									trace("not dot:low");
								}
							}
						}
					}
					event.currentTarget.gotoAndStop(1);


				}
			} else {
				event.currentTarget.startDrag();

			}
			select.addEventListener(MouseEvent.MOUSE_DOWN,StopDrag);
		}

		public function StartDrag(event:MouseEvent):void {
			trace("StartDrag");
			//trace(event.currentTarget.name);
			event.currentTarget.stopDrag();

			/*trace("程式尚未定位過的音符位置",event.currentTarget.x,event.currentTarget.y);
			var maxtemp:int=0;// 目前擺放此音符的前一個音符x座標位置
			var counttemp:int=-1;//目前擺放此音符的前一個音符 是第幾個音符
			
			
			
			for (var i:int=0; i<count; i++) {
			if ((event.currentTarget.x>mus[page][line][linecount][0].xx)) {
			if (mus[page][line][linecount][0].xx>maxtemp) {
			maxtemp=mus[page][line][linecount][0].xx;
			counttemp=i;
			}
			}
			}
			trace("前一個x"+maxtemp,"前一個音符第幾個"+counttemp,"目前幾個"+count);
			
			if ((count>0) && (counttemp+1<count)) {
			move_next(counttemp,count);
			}
			
			
			//event.currentTarget.y=102;
			x1=event.currentTarget.x;
			trace(event.currentTarget.note,event.currentTarget.y);
			if (event.currentTarget.note==4) {
			if ( (event.currentTarget.y>104) && (event.currentTarget.y<108)) {
			event.currentTarget.y=105;
			if (count==0) {
			mus[count].xx=event.currentTarget.x;
			mus[count].yy=event.currentTarget.y;
			mus[count].cc=count;
			mus[count].a_tempo="Semibreve";
			mus[count].a_pitch=4;
			} else {
			
			mus[counttemp+1].xx=event.currentTarget.x;
			mus[counttemp+1].yy=event.currentTarget.y;
			mus[counttemp+1].cc=count;
			mus[counttemp+1].a_tempo="Semibreve";
			mus[counttemp+1].a_pitch=4;
			}
			}
			
			if ( (event.currentTarget.y>107) && (event.currentTarget.y<111)) {
			event.currentTarget.y=108;
			if (count==0) {
			mus[count].xx=event.currentTarget.x;
			mus[count].yy=event.currentTarget.y;
			mus[count].cc=count;
			mus[count].a_tempo="Semibreve";
			mus[count].a_pitch=3;
			} else {
			
			mus[counttemp+1].xx=event.currentTarget.x;
			mus[counttemp+1].yy=event.currentTarget.y;
			mus[counttemp+1].cc=count;
			mus[counttemp+1].a_tempo="Semibreve";
			mus[counttemp+1].a_pitch=3;
			}
			}
			
			
			
			}
			*/
			
			removeChild(container);
			container=new Sprite();

			init(page);


		}
		public function move_next(counttemp:int,movecount:int,clickhighlow) {
			//var movetemp:musical=new musical();
			//mus[count+1]=mus[count];
			if (clickhighlow==0) {
				for (var i:int=movecount+1; i>counttemp+1; i--) {//TEST or i>counttemp+1
					if (i>0) {//  i>counttemp
						//mus[i+1]=mus[i];
						for (var k:int=0; k<5; k++) {
							mus[page][clickline][i][k]=mus[page][clickline][i-1][k];
							mus[page][clickline][i-1][k]=new musical();//...竟然卡在這
						}
						//trace(i,i-1,mus[i].xx,mus[i-1].xx);
					}
				}
			} else {
				for (var j:int=movecount+1; j>counttemp+1; j--) {//TEST or i>counttemp+1
					if (j>0) {//  i>counttemp
						//mus[i+1]=mus[i];
						for (var l:int=0; l<5; l++) {
							muslow[page][clickline][j][l]=muslow[page][clickline][j-1][l];

							muslow[page][clickline][j-1][l]=new musical();//...竟然卡在這
						}
						//trace(i,i-1,mus[i].xx,mus[i-1].xx);
					}
				}
			}
		}

		public var playmusicI:int=0;
		public var playsteps2:int=0;
		public var playsteps2low:int=0;
		public var playline:int=0;
		public var playline2:int=0;

		public var pauses:int=0;
		public var pauses2:int=0;
		public var pausesteps2:int=0;
		public var pausesteps2low:int=0;
		public var pausestats:int=0;


		public function pausemusic(event:MouseEvent) {
			pausesteps2=playsteps2;
			pausesteps2low=playsteps2low;
			trace("pa:"+playsteps2);
			trace("pb:"+playsteps2);
			ppause=0;

			if (pausestats==1) {
				pausestats=0;
			} else {
				pausestats=1;


			}
			fscommand("quit");
			//myTimer.reset();
		}
		public var myTimer:Timer;
		public var ppause:int=1;
		public var step:int=0;
		public var steplow:int=0;
public function playmusic(event:MouseEvent) {
				removeChild(container);
				container=new Sprite();
				init(page);
			step=0;
			steplow=0;
			var playsteps:int=0;
			var playstepslow:int=0;
			var playtemp:int=0;
			var playtemp2:int=0;
			ppause=1;
			playsteps2=1;
			playsteps2low=1;
			playmusicI=0;
			playline=0;
			playline2=0;
			for (var nn:int=0; nn<10; nn++) {
				for (var bb:int=0; bb<3; bb++) {
					for (var vv:int=0; vv<64; vv++) {
						if (mus[nn][bb][vv][0].a_tempo!=null) {
							playmus[step]=mus[nn][bb][vv];
							playmusicon[step]=containericon[nn][bb][vv];
							step++;
						} else {
							break;
						}
					}
				}
			}
			for (nn=0; nn<10; nn++) {
				for (bb=0; bb<3; bb++) {
					for (vv=0; vv<64; vv++) {
						if (muslow[nn][bb][vv][0].a_tempo!=null) {
							playmuslow[steplow]=muslow[nn][bb][vv];
							//trace("::::"+playmuslow[steplow][0].a_pitch);
							playmusiconlow[steplow]=containericonlow[nn][bb][vv];
							steplow++;
						} else {
							break;
						}
					}
				}
			}
			if (pausestats==0) {

				var m:playm=new playm();
				if (playmus[0][0].a_tempo!=null) {
					
					for (var s:int=0; s<4; s++) {
						if (playmus[0][0].a_tempo==sleepsign[s]) {
							break;
						}
					}
					
					if (s==4){
						m.voice(keysign,speed,playmus[0][0],0,ppause);
						setColor(playmusicon[0][0],255,0,0);///////////
					}
				}
				for (var corotating:int=1; corotating<5; corotating++) {
					var n:playm=new playm();
					if ((playmus[0][corotating].a_tempo) != null) {
						n.voice(keysign,speed,playmus[0][corotating],0,ppause);
						setColor(playmusicon[0][corotating],255,0,0);///////////
						trace("steps:"+ playsteps2 + ",:"+playmus[0][corotating].a_pitch);
					}
				}
				for (nn=1; nn<step; nn++) {
					if (playmus[nn][0].a_tempo!=null) {
						myTimer = new Timer(playtemp+(60/speed)*1000*sign(playmus[nn-1][0])/4,1);//一拍
						playtemp=playtemp+(60/speed)*1000*sign(playmus[nn-1][0])/4;
						trace((60/speed)*1000*nn*sign(playmus[nn-1][0])/4);
						myTimer.addEventListener("timer", timerHandler3);
						myTimer.start();
						trace("pauses:"+pauses);

					}
				}
				var ml:playm=new playm();
				if (playmuslow[0][0].a_tempo!=null) {
					for (s=0; s<4; s++) {
						if (playmuslow[0][0].a_tempo==sleepsign[s]) {
							break;
						}
					}
					
					if (s==4){
						ml.voice(keysign,speed,playmuslow[0][0],0,ppause);
						setColor(playmusiconlow[0][0],255,0,0);///////////
					}
				}
				for (corotating=1; corotating<5; corotating++) {
					var nl:playm=new playm();
					if ((playmuslow[0][corotating].a_tempo) != null) {
						nl.voice(keysign,speed,playmuslow[0][corotating],0,ppause);
						setColor(playmusiconlow[0][corotating],255,0,0);///////////
						trace("steps:"+ playsteps2 + ",:"+playmuslow[0][corotating].a_pitch);
					}
				}
				for (nn=1; nn<steplow; nn++) {
					if (playmuslow[nn][0].a_tempo!=null) {
						var myTimer2:Timer = new Timer(playtemp2+(60/speed)*1000*sign(playmuslow[nn-1][0])/4, 1);//一拍
						playtemp2=playtemp2+(60/speed)*1000*sign(playmuslow[nn-1][0])/4;
						myTimer2.addEventListener("timer", timerHandler4);
						myTimer2.start();
					}
				}

				trace("step"+step);
				for (var hh:int=0; hh<step; hh++) {
					trace(playmus[hh][0].a_pitch);
				}
			} else {
				playsteps2=pausesteps2;
				for (nn=pausesteps2; nn<step; nn++) {
					if (playmus[nn][0].a_tempo!=null) {
						myTimer = new Timer(playtemp+(60/speed)*1000*sign(playmus[nn-1][0])/4,1);//一拍
						playtemp=playtemp+(60/speed)*1000*tempo(playmus[nn-1][0].a_tempo)/4;
						trace((60/speed)*1000*nn*tempo(playmus[nn-1][0].a_tempo)/4);
						myTimer.addEventListener("timer", timerHandler3);
						myTimer.start();
						trace("pauses:"+pauses);

					}
				}
				playsteps2low=pausesteps2low;
				for (nn=pausesteps2low; nn<steplow; nn++) {
					if (playmuslow[nn][0].a_tempo!=null) {
						myTimer2= new Timer(playtemp2+(60/speed)*1000*sign(playmuslow[nn-1][0])/4, 1);//一拍
						playtemp2=playtemp2+(60/speed)*1000*sign(playmuslow[nn-1][0])/4;
						myTimer2.addEventListener("timer", timerHandler4);
						myTimer2.start();
					}
				}
			}
			

		}



		public function timerHandler3(event:TimerEvent):void {
			var m:playm=new playm();
			//trace("sleep:"+sleepkey);
			//if (pausestats==0){
			var tempsleepkey=-1;
			for (var s:int=0; s<4; s++) {
				if (playmus[playsteps2][0].a_tempo==sleepsign[s]) {
					tempsleepkey=s;
					break;
				}
			}
			if ((tempsleepkey==-1)) {//如果他不是休止符 再播放
				m.voice(keysign,speed,playmus[playsteps2][0],playsteps2,ppause);
				if (ppause!=0)
				setColor(playmusicon[playsteps2][0],255,0,0);///////////
			}
			for (var corotating:int=1; corotating<5; corotating++) {
				var n:playm=new playm();
				if (((playmus[playsteps2][corotating].a_tempo) != null) && (sleepkey==-1)) {
					n.voice(keysign,speed,playmus[playsteps2][corotating],playsteps2,ppause);
					if (ppause!=0)
					setColor(playmusicon[playsteps2][corotating],255,0,0);///////////
					//trace("steps:"+ playsteps2 + ",:"+playmus[playsteps2][corotating].a_pitch);
				}
			}
			//trace("steps:"+ playsteps2 + ",:"+playmus[playsteps2][0].a_pitch);

			//if (pauses==1)
			//{
			//return 0;
			//}


			playsteps2++;
			if ((playsteps2==(step)) && (ppause==1)) {
				trace("good");
				playsteps2==0;
				pausestats=0;
			}
			//trace("playsteps2:"+playsteps2+",step+1:"+step+",ppause:"+ppause);

		}


		public function timerHandler4(event:TimerEvent):void {
			var m:playm=new playm();
			var tempsleepkey=-1;
			//if (pausestats==0){
			for (var s:int=0; s<4; s++) {
				if (playmuslow[playsteps2low][0].a_tempo==sleepsign[s]) {
					tempsleepkey=s;
					break;
				}
			}
			if ((tempsleepkey==-1)) {
				m.voice(keysign,speed,playmuslow[playsteps2low][0],playsteps2low,ppause);
				if (ppause!=0)
				setColor(playmusiconlow[playsteps2low][0],255,0,0);///////////
			}
			for (var corotating:int=1; corotating<5; corotating++) {
				var n:playm=new playm();
				if (((playmuslow[playsteps2low][corotating].a_tempo) != null) && (sleepkey==-1)) {
					n.voice(keysign,speed,playmuslow[playsteps2low][corotating],playsteps2low,ppause);
					if (ppause!=0)
					setColor(playmusiconlow[playsteps2low][corotating],255,0,0);///////////
				}
			}
			//trace("steps:"+ playsteps2 + ",:"+playmuslow[playsteps2low][0].a_pitch);

			playsteps2low++;
			//}
		}



		public function determine(xx:int,yy:int) {
			var line1_upper:int=10;//y座標設定
			var line1_lower:int=198;
			var line1_middle:int=136;

			var line2_upper:int=199;
			var line2_lower:int=330;
			var line2_middle:int=269;

			var line3_upper:int=331;
			var line3_lower:int=498;
			var line3_middle:int=399;

			if ((yy <= line1_lower)) {
				if (yy<=line1_middle) {
					clickhighlow=0;//高音譜
				} else {
					clickhighlow=1;//低音譜
				}
				clickline=0;
			} else if ((yy >=line2_upper) && (yy<=line2_lower)) {
				if (yy<=line2_middle) {
					clickhighlow=0;
				} else {
					clickhighlow=1;
				}
				clickline=1;
			} else if ((yy >=line3_upper)) {
				if (yy<=line3_middle) {
					clickhighlow=0;
				} else {
					clickhighlow=1;
				}
				clickline=2;
			}
		}
		public function tempo(namex:String) {
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


		public function sign(musicalarray:musical) {
			if (musicalarray.sign=="dot_plus1") {
				return tempo(musicalarray.a_tempo) * 1.5;
			} else {
				return tempo(musicalarray.a_tempo);
			}
		}
		public function tests() {
			trace("123456");
		}
		function setColor(target:DisplayObject, r:int, g:int, b:int):void {
			var matrix:Array = new Array();
			matrix = matrix.concat([0, 0, 0, 0, r]);// red
			matrix = matrix.concat([0, 0, 0, 0, g]);// green
			matrix = matrix.concat([0, 0, 0, 0, b]);// blue
			matrix = matrix.concat([0, 0, 0, 1, 0]);// alpha

			var filter:ColorMatrixFilter = new ColorMatrixFilter(matrix);
			var filters:Array = new Array();
			filters.push(filter);
			target.filters = filters;
		}
		//var testselects:selectt=new selectt(selectcontainer,area,container,page,linejudge,mus,底圖,Slur,Eightva,Deletebtn,Cancelbtn);//////////////////////////////////////
	}

}