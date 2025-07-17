import com.IndieGo.utils.Transforms;
import com.IndieGo.utils.XMLLoader;
import flash.display.Loader;
import flash.events.Event;
import flash.events.MouseEvent;
import flash.net.URLRequest;
import flash.utils.setTimeout;
import flash.utils.setInterval;
import flash.utils.clearInterval;
import flash.desktop.NativeApplication;

/*______________ INIT ________________*/

var Trans:Transforms = new Transforms( stage );

function initBtn( btn:Object, callback:Function ):void {
	
	var isDown:Boolean = false;
	
	btn.addEventListener( MouseEvent.MOUSE_OVER, function( e:MouseEvent ):void {

	});
	
	btn.addEventListener( MouseEvent.MOUSE_OUT,  function( e:MouseEvent ):void {
		
		Trans.animScale( btn, 1, 1, 0, 1 );
		
		if( isDown ) isDown = false;
		
	});
	
	btn.addEventListener( MouseEvent.MOUSE_DOWN,  function( e:MouseEvent ):void {
		
		Trans.animScale( btn, 1.1, 1.1, 0, 1 );
		
		isDown = true;
		
	});
	
	btn.addEventListener( MouseEvent.MOUSE_UP,  function( e:MouseEvent ):void {
		
		if( isDown ) {
			
			Trans.animScale( btn, 1, 1, 0, 1 );
			
			callback();
			
			isDown = false;
			
		}
		
	});
	
}

/*______________ HOME ________________*/

function homeAlpha( val:Number ):void {
	
	Trans.alpha( home_title1, val );
	Trans.alpha( home_title2, val );
	Trans.alpha( home_btn_start, val );
	
}

function showHome():void {
	
	homeAlpha( 1 );
	
	Trans.place( home_title1, 1/2, 1/4 );
	Trans.place( home_title2, 1/2, 2/4 );
	Trans.place( home_btn_start, 1/2, 3/4 );
	Trans.scale( home_title1, 0, 0 );
	Trans.scale( home_title2, 0, 0 );
	Trans.scale( home_btn_start, 0, 0 );

	setTimeout( Trans.animScale, 100, home_title1, 1, 1 );
	setTimeout( Trans.animScale, 500, home_title2, 1, 1 );
	setTimeout( Trans.animScale, 1000, home_btn_start, 1, 1, 1, 1 );

}

function hideHome():void {
	
	Trans.animPlace( home_btn_start, 1/2, 7/5, false, 1 );
	setTimeout( Trans.animPlace, 100, home_title1, 1/2, -2/5, false, 1 );
	setTimeout( Trans.animPlace, 300, home_title2, 1 / 2, -2 / 5, false, 1 );
	setTimeout( homeAlpha, 2000, 0 );
	setTimeout( showLevel, 2000 );
	
}

initBtn( home_btn_start, hideHome );

showHome();

/*______________ LEVEL ________________*/

function levelAlpha( val:Number ):void {
	
	Trans.alpha( level_title, val );
	Trans.alpha( level_btn_home, val );
	Trans.alpha( level_btn_easy, val );
	Trans.alpha( level_btn_hard, val );
	Trans.alpha( level_btn_med, val );
	
}

function showLevel():void {
	
	levelAlpha( 1 );

	Trans.place( level_title, 1/2, -1/2 );
	Trans.place( level_btn_home, 1/2, 4/7 );
	Trans.place( level_btn_easy, 1/2, 4/7 );
	Trans.place( level_btn_hard, 1/2, 4/7 );
	Trans.place( level_btn_med, 1/2, 4/7 );
	Trans.scale( level_btn_home, 0, 0 );
	Trans.scale( level_btn_easy, 0, 0 );
	Trans.scale( level_btn_hard, 0, 0 );
	Trans.scale( level_btn_med, 0, 0 );

	setTimeout( Trans.animScale, 100, level_btn_home, 1, 1 );
	setTimeout( Trans.animScale, 200, level_btn_easy, 1, 1 );
	setTimeout( Trans.animScale, 300, level_btn_hard, 1, 1 );
	setTimeout( Trans.animScale, 400, level_btn_med, 1, 1 );
	setTimeout( Trans.animPlace, 100, level_title, 1/2, 1/5, false, 1 );

}

function hideLevel():void {
	
	setTimeout( Trans.animPlace, 100, level_title, 1/2, -1/2, false, 1 );
	setTimeout( Trans.animScale, 200, level_btn_easy, 0, 0 );
	setTimeout( Trans.animScale, 300, level_btn_hard, 0, 0 );
	setTimeout( Trans.animScale, 400, level_btn_med, 0, 0 );
	setTimeout( Trans.animScale, 500, level_btn_home, 0, 0 );
	setTimeout( levelAlpha, 2000, 0 );
	
}

initBtn( level_btn_home, function():void { hideLevel(); setTimeout( showHome, 2000 ) });
initBtn( level_btn_easy, function():void { hideLevel(); setTimeout( showQuest, 2000, 'easy' ) });
initBtn( level_btn_med, function():void { hideLevel(); setTimeout( showQuest, 2000, 'med' ) });
initBtn( level_btn_hard, function():void { hideLevel(); setTimeout( showQuest, 2000, 'hard' ) });

levelAlpha( 0 );

/*______________ QUEST ________________*/

var Q:Object = {
	
	READ : new Loader(),
	IMAGE : new Loader(),
	JAWAB : true,
	QUEST : [],
	REFER : [],
	LEVEL : '',
	SCORE : 0,
	NOMOR : 0,
	LISTS : 0,
	WAKTU : 60 * 60,
	TIMER : new Object()
	
}


function readImage( link:String, type:uint = 0 ):void {
	
	trace( link );
	
	var isDown:Boolean = false;
	var old_x:Number = 0;
	var old_y:Number = 0;
	var img_x:Number = 0;
	var img_y:Number = 0;
	
	try {
		
		baca_image.removeChild( Q.READ );
		
	} catch ( e:Error ) {}
	
	Q.READ = new Loader();
	
	baca_image.addChild( Q.READ );
	
	Q.READ.addEventListener( MouseEvent.MOUSE_DOWN , function( e:MouseEvent ):void {
		
		old_x = e.stageX;
		old_y = e.stageY;
		img_x = Q.READ.x;
		img_y = Q.READ.y;
		
		isDown = true;
		
	});
	
	Q.READ.addEventListener( MouseEvent.MOUSE_UP , function( e:MouseEvent ):void {
		
		old_x = e.stageX;
		old_y = e.stageY;
		img_x = Q.READ.x;
		img_y = Q.READ.y;
		
		isDown = false;
		
	});
	
	Q.READ.addEventListener( MouseEvent.MOUSE_OUT , function( e:MouseEvent ):void {
		
		isDown = false;
		
	});
	
	Q.READ.addEventListener( MouseEvent.MOUSE_MOVE , function( e:MouseEvent ):void {
		
		if ( isDown ) {
			
			Q.READ.x = img_x + e.stageX - old_x;
			Q.READ.y = img_y + e.stageY - old_y;
			
		}
		
	});
		
	Q.READ.contentLoaderInfo.addEventListener( Event.COMPLETE, function():void {
		
		baca_image.x = stage.stageWidth / 2;
		baca_image.y = 10;
		
		Q.READ.x = -Q.READ.width / 2;
		Q.READ.y = 0;
		
		if ( type == 0 ) Trans.animScale( baca_image, 1, 1 );
		else if ( type == 1 ) Trans.place( baca_image, stage.stageWidth * -1 / 2, baca_image.y, true );
		else if ( type == 2 ) Trans.place( baca_image, stage.stageWidth * 3 / 2, baca_image.y, true );
		
		Trans.animPlace( baca_image, stage.stageWidth / 2, baca_image.y, true, 1, 1 );
		
	});
	
	Q.READ.load( new URLRequest( link ) );
	
}

function loadImage( link:String ):void {
	
	try {
		
		soal_image.removeChild( Q.IMAGE );
		
	} catch ( e:Error ) {}
	
	Q.IMAGE = new Loader();
	
	soal_image.addChild( Q.IMAGE );
	
	Q.IMAGE.contentLoaderInfo.addEventListener( Event.COMPLETE, function():void {
		
		Q.JAWAB = Q.QUEST[ Q.NOMOR ].VALUE;
		soal_nomor.text = ( Q.NOMOR + 1 ) + ' / ' + Q.QUEST.length;
		
		Q.IMAGE.x = 0;
		Q.IMAGE.y = -Q.IMAGE.height / 2;
		
		Trans.place( soal_image, 0.5 / 7, 6.5 / 7 );
		Trans.place( soal_nomor, -soal_nomor.width / 2, -soal_nomor.height / 2, true );
		
		Trans.animPlace( soal_btn_back, 0.3 / 7, 1 / 2 );
		Trans.animPlace( soal_btn_next, 6.7 / 7, 1 / 2 );
		Trans.animScale( baca_image, 1, 1 );
		Trans.animScale( soal_image, 1, 1 );
		Trans.animSize( soal_nomor_bg, soal_nomor.width, soal_nomor.height, 1, 1 );		
		Trans.animPlace( soal_nomor_bg, soal_nomor_bg.width / 2, soal_nomor_bg.height / 2 + 3, true, 1 );
		setTimeout( Trans.animPlace, 300, soal_btn_true, 6/7, 6.5/7, false, 1 );
		setTimeout( Trans.animPlace, 300, soal_btn_false, 6/7, 6.5/7, false, 1 );
		
	});
	
	Q.IMAGE.load( new URLRequest( link ) );
	
}

Trans.place( soal_btn_false, -1/2, 6/7 );
Trans.place( soal_btn_true, 3/2, 6/7 );
Trans.place( soal_jwb_benar, 1/2, 1/2 );
Trans.place( soal_jwb_salah, 1/2, 1/2 );
Trans.place( soal_btn_back, -1/7, 1/2 );
Trans.place( soal_btn_next, 8/7, 1/2 );
Trans.scale( soal_jwb_benar, 0, 0 );
Trans.scale( soal_jwb_salah, 0, 0 );
Trans.scale( baca_image, 0, 0 );
Trans.scale( soal_image, 0, 0 );

soal_nomor_bg.addChild( soal_nomor );
soal_timer_bg.addChild( soal_timer );
soal_nomor.autoSize = TextFieldAutoSize.CENTER;
soal_timer.autoSize = TextFieldAutoSize.CENTER;
Trans.place( soal_nomor_bg, soal_nomor_bg.width / 2, -soal_nomor_bg.height * 2, true );
Trans.place( soal_timer_bg, stage.stageWidth - soal_timer_bg.width / 2, -soal_timer_bg.height * 2, true );

function showQuest( lvl:String ):void {
	
	Q.LEVEL = lvl;
	
	XMLLoader( 'res/Quest.xml', initQuest );
	
}

function hideQuest():void {
	
	Trans.animPlace( soal_btn_false, -1/2, 6/7, false, 1 );
	Trans.animPlace( soal_btn_true, 3/2, 6/7, false, 1 );
	Trans.animPlace( soal_nomor_bg, soal_nomor_bg.width / 2, -soal_nomor_bg.height * 2, true, 1, 1 );
	Trans.animPlace( soal_timer_bg, stage.stageWidth - soal_timer_bg.width / 2, -soal_timer_bg.height * 2, true, 1, 1 );
	Trans.animScale( baca_image, 0, 0, 1, 1 );
	Trans.animScale( soal_image, 0, 0, 1, 1 );
	Trans.animPlace( soal_btn_back, -1/7, 1/2 );
	Trans.animPlace( soal_btn_next, 8/7, 1/2 );

}

function initQuest( X:XML ):void {

	Q.NOMOR = 0;
	Q.QUEST = [];
	Q.WAKTU = 60 * parseInt( X.atur.@dur );
	
	
	for ( var i:Number = 0, len:Number = X.baca.length(); i < len; i++ ) {
		
		if ( X.baca[ i ].@lvl == Q.LEVEL ) {
			
			Q.REFER.push( X.baca[ i ].@img.toString() );
			
		}
		
	}
	
	for ( var i2:Number = 0, len2:Number = X.soal.length(); i2 < len2; i2++ ) {
		
		if ( X.soal[ i2 ].@lvl == Q.LEVEL ) {
			
			Q.QUEST.push({
				
				IMAGE : X.soal[ i2 ].@img.toString(),
				VALUE : X.soal[ i2 ].@val == 'yes'
				
			});
			
		}
		
	}
	
	Q.JAWAB = Q.QUEST[ Q.NOMOR ].VALUE;
	readImage( 'res/' + Q.REFER[ Q.LISTS ] );
	loadImage( 'res/' + Q.QUEST[ Q.NOMOR ].IMAGE );
	
	Q.TIMER = setInterval( function():void {
		
		Q.WAKTU--;
		soal_timer.text = Math.floor( Q.WAKTU / 60 ) + ' : ' + Math.floor( Q.WAKTU % 60 );
		Trans.place( soal_timer, -soal_timer.width / 2, -soal_timer.height / 2, true );
		Trans.animSize( soal_timer_bg, soal_timer.width, soal_timer.height, 1, 1 );
		Trans.animPlace( soal_timer_bg, stage.stageWidth - soal_timer_bg.width / 2, soal_nomor_bg.height / 2 + 3, true, 1, 1 );
		
		if ( Q.WAKTU < 0 ) {
			
			clearInterval( Q.TIMER );
			hideQuest();
			showResult();
			
		}
		
	}, 1000);
	
}

function showAnswer( isTrue:Boolean ):void {
	
	if ( isTrue ) Trans.animScale( soal_jwb_benar, 1, 1 );
	else Trans.animScale( soal_jwb_salah, 1, 1 );
	
	setTimeout( function():void {
		
		Trans.animScale( soal_jwb_benar, 0, 0, 1 );
		Trans.animScale( soal_jwb_salah, 0, 0, 1 );
		
		if ( Q.NOMOR < Q.QUEST.length - 1 ) {
			
			Q.NOMOR++;
			
			loadImage( 'res/' + Q.QUEST[ Q.NOMOR ].IMAGE );
			
		} else {
			
			clearInterval( Q.TIMER );
			hideQuest();
			showResult();
			
		}
		
	}, 2000 );
	
}

initBtn( soal_btn_back, function():void {
	
	if ( Q.LISTS < 1 ) return;
	
	else {
		
		Q.LISTS--;
		
		readImage( 'res/' + Q.REFER[ Q.LISTS ], 1 );
		
	}
	
});

initBtn( soal_btn_next, function():void {
	
	if ( Q.LISTS >= Q.REFER.length - 1 ) return;
	
	else {
		
		Q.LISTS++;
		
		readImage( 'res/' + Q.REFER[ Q.LISTS ], 2 );
		
	}
	
});

initBtn( soal_btn_true, function():void {
	
	hideQuest();
	
	if ( Q.JAWAB ) {
	
		Q.SCORE += 100 / Q.QUEST.length;
		
		showAnswer( true );
		
	} else {
		
		showAnswer( false );
		
	}
	
});

initBtn( soal_btn_false, function():void {
	
	hideQuest();
	
	if ( !Q.JAWAB ) {
		
		Q.SCORE += 100 / Q.QUEST.length;
		
		showAnswer( true );
	
	} else {
		
		showAnswer( false );
		
	}

});

/*______________ RESULT ________________*/

nilai_score_bg.addChild( nilai_score );
nilai_score_bg.addChild( nilai_hasil );

nilai_score.autoSize = TextFieldAutoSize.CENTER;
nilai_hasil.autoSize = TextFieldAutoSize.CENTER;

initBtn( nilai_btn_ulangi, function():void {
	
	Q.READ = new Loader();
	Q.IMAGE = new Loader();
	Q.JAWAB = true;
	Q.QUEST = [];
	Q.REFER = [];
	Q.LEVEL = '';
	Q.SCORE = 0;
	Q.NOMOR = 0;
	Q.LISTS = 0;
	Q.WAKTU = 60 * 60;
	Q.TIMER = new Object();
	
	hideResult();
	showLevel();
	
});

initBtn( nilai_btn_keluar, function():void {
	
	hideResult();
	
	setTimeout( function():void {
		
		NativeApplication.nativeApplication.exit();
		
	}, 2000 );
	
});

function showResult():void {
	
	var hasil:String = "Nilai Anda ";
	
	if ( Q.SCORE < 50 ) hasil += "Kurang,\n";
	else if ( Q.SCORE < 70 ) hasil += "Cukup,\n";
	else if ( Q.SCORE < 90 ) hasil += "Baik,\n";
	else if ( Q.SCORE < 100 ) hasil += "Sangat Baik,\n";
	else hasil += "Sempurna,\n";
	
	if ( Q.SCORE < 50 ) hasil += "Anda Tidak Lulus.";
	else hasil += "Anda Lulus.";
	
	nilai_score.text = parseInt( Q.SCORE );
	nilai_hasil.text = hasil;
	
	Trans.place( nilai_btn_ulangi, 1 / 2, 3 / 2 );
	Trans.place( nilai_btn_keluar, 1 / 2, 3 / 2 );
	Trans.place( nilai_score, -nilai_score.width / 2, -120, true );
	Trans.place( nilai_hasil, 160, -nilai_hasil.height / 2, true );
	Trans.place( nilai_score_bg, ( stage.stageWidth - nilai_hasil.width ) / 2, stage.stageHeight * 1/3, true )
	Trans.scale( nilai_score_bg, 0, 0 );

	Trans.animScale( nilai_score_bg, 1, 1 );
	setTimeout( Trans.animPlace, 200, nilai_btn_ulangi, 1 / 2, 2.5 / 3, false, 1 );
	setTimeout( Trans.animPlace, 400, nilai_btn_keluar, 1 / 2, 2.5/ 3, false, 1 );
}

function hideResult():void {
	
	Trans.animPlace( nilai_score_bg, nilai_score_bg.width * 2, stage.stageHeight * 1/3, true )
	Trans.animPlace( nilai_btn_ulangi, 1 / 2, 3 / 2, false, 1 );
	Trans.animPlace( nilai_btn_keluar, 1 / 2, 3 / 2, false, 1 );
	
}