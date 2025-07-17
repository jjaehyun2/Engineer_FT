package com.IndieGo.soal.quest {
	
	import flash.display.MovieClip;
	import com.IndieGo.utils.XMLLoader;

	public class InitQuest {

		
		private var Q:Object = {
			
			P: 0,  // Process [ 0: None, 1: Process, 2: Complete ]
			Q: [], // Quest
			O: [], // Order
			C: [], // Criteria
			S: {}, // Status
			RQ: false, // Random Quest
			RA: false, // Random Answer
			SL: false, // Show Live
			SA: false, // Show Answer
			SS: false, // Show Score
			SP: false, // Show Percentage
			SR: false, // Show Result
			QA: 0, // Quest Answered
			QF: 0, // Quest Failed
			QT: [ 0, 0, 0, 0 ], // Quest Total
			TN: 0, // Time Now
			TT: 0, // Time Total
			SN: 0, // Score Now
			ST: 0, // Score Total
			PN: '' // Player Name
			
		}
		
		private var complete:Function;
		
		/*	CONSTRUCTOR
		--------------------------------------------*/
		public function InitQuest( url:String, callback:Function ): void {

			complete = callback;

			XMLLoader( url, xmlInit );

		}

		private function xmlInit( xml:XML ): void {
			
			Q.RQ = xml.atur.acak.@soal == 'ya';
			Q.RA = xml.atur.acak.@jawaban == 'ya';
			Q.SL = xml.atur.lihat.@langsung == 'ya';
			Q.SA = xml.atur.lihat.@jawaban == 'ya';
			Q.SS = xml.atur.lihat.@skor == 'ya';
			Q.SP = xml.atur.lihat.@nilai == 'ya';
			Q.SR = xml.atur.lihat.@hasil == 'ya';
			Q.TT = parseInt( xml.atur.durasi );
			Q.QT[ 0 ] = parseInt( xml.atur.jumlah.soal.(@tipe == '1') );
			Q.QT[ 1 ] = parseInt( xml.atur.jumlah.soal.(@tipe == '2') );
			Q.QT[ 2 ] = parseInt( xml.atur.jumlah.soal.(@tipe == '3') );
			Q.QT[ 3 ] = parseInt( xml.atur.jumlah.soal.(@tipe == '4') );

			Q.S.P = parseFloat( xml.atur.kriteria.status.@persen ).toFixed( 2 );
			Q.S.G = xml.atur.kriteria.status.@lulus.toString();
			Q.S.F = xml.atur.kriteria.status.@gagal.toString();
			
			for each ( var item:XML in xml.atur.kriteria.nilai ) {
				
				Q.C.push({
					
					P: parseFloat( item.@persen ).toFixed( 2 ),
					C: item.warna.toString(),
					R: item.level.toString(),
					Q: item.pesan.toString()
					
				});
				
				item = null;
				
			}
			
			for ( var i:int = 0, len:int = xml.soal.length(); i < len; i++ ) {
				
				Q.Q[ i ] = xmlQuest( xml.soal[ i ], {} );
				Q.O[ i ] = i;
				
			}
			
			xml = null;

			complete( Q );
						
		}
		
		private function xmlQuest( X:XML, V:Object ): Object {
			
			V.T	= parseInt( X.@tipe );
			
			switch ( V.T ) {
				
				case 1:
					
					V.S = {
						
						C: parseInt( X.skor.@benar ),
						F: parseInt( X.skor.@salah )
						
					}
				
					V.Q = X.tanya.toString();
				
					V.M = new Array( X.media.length() );
				
					V.M.forEach( function( a, i ) {
						
						V.M[ i ] = {
							
							T: X.media[ i ].@tipe.toString(),
							V: X.media[ i ].toString()
							
						}
						
					});
					
					V.A = V.O = new Array( X.jawab.length() );
					
					V.A.forEach( function( a, i ) {
						
						V.O[ i ] = i;
						V.A[ i ] = {
							
							T: X.jawab[ i ].@tipe.toString(),
							V: X.jawab[ i ].toString(),
							C: X.jawab[ i ].@hasil == 'benar'
							
						}
						
					});
				
				break;
				
				case 2:
					
					V.Q = V.O = new Array( X.dnd.length() );
				
					V.Q.forEach( function( a, i ) {
						
						V.O[ i ] = i;
						V.Q[ i ] = {
							
							S: {
								
								C: parseInt( X.dnd[ i ].skor.@benar ),
								F: parseInt( X.dnd[ i ].skor.@salah )
								
							},
							
							Q: X.tanya.toString(),
							
							M: new Array( X.dnd[ i ].media.length() ),
							
							A: {
								
								T: X.dnd[ i ].jawab.@tipe.toString(),
								V: X.dnd[ i ].jawab.toString()
								
							}
						}
						
						V.Q[ i ].M.forEach( function( b, ii ) {
							
							V.Q[ i ].M[ ii ] = {
								
								T: X.dnd[ i ].media[ ii ].@tipe.toString(),
								V: X.dnd[ i ].media[ ii ].toString()
								
							}
							
						});
						
					});
					
				break;
					
				case 3:
					
					V.Q = V.O = new Array( X.konek.length() );
				
					V.Q.forEach( function( a, i ) {
						
						V.O[ i ] = i;
						V.Q[ i ] = {
							
							S: {
								
								C: parseInt( X.konek[ i ].skor.@benar ),
								F: parseInt( X.konek[ i ].skor.@salah )
								
							},
							
							L: new Array( X.konek[ i ].kiri.length() ),
							R: new Array( X.konek[ i ].kanan.length() )
							
						}
						
						V.Q[ i ].L.forEach( function( b, ii ) {
							
							V.Q[ i ].L[ ii ] = {
								
								T: X.konek[ i ].kiri[ ii ].@tipe.toString(),
								V: X.konek[ i ].kiri[ ii ].toString()
								
							}
							
						});
						
						V.Q[ i ].R.forEach( function( b, ii ) {
							
							V.Q[ i ].R[ ii ] = {
								
								T: X.konek[ i ].kanan[ ii ].@tipe.toString(),
								V: X.konek[ i ].kanan[ ii ].toString()
								
							}
							
						});
						
					});
					
				break;
				
				case 4:
					
					V.B = {};
					V.Q = {};
					V.O = [ 0 ];
				
					xmlCrossBox( X, V.B, 'V', 'kotak' );
					xmlCrossBox( X, V.B, 'H', 'lihat' );
					xmlCrossBox( X, V.B, 'N', 'nomor' );
					xmlCrossQuest( X, V.Q, V.O, 'H', 'datar' );
					xmlCrossQuest( X, V.Q, V.O, 'V', 'turun' );
					
					V.O.sort( Array.NUMERIC );
																									
				break;
					
				default: break;
					
			}
			
			return V;
			
		}
				
		private function xmlCrossBox( X:XML, V:Object, B:String, Z:String ): void {
			
			V[ B ] = new Array( X[ Z ].length() );

			V[ B ].forEach( function( a, i ) {
				
				a = X[ Z ][ i ].split( '|' );
				
				V[ B ][ i ] = new Array( a.length );
				
				V[ B ][ i ].forEach( function( b, ii ) {
					
					if ( a[ ii ] != '-' ) V[ B ][ i ][ ii ] = a[ ii ].toString();
					
				});
				
				a = null;
				
			});

		}
		
		private function xmlCrossQuest( X:XML, V:Object, O:Array, Q:String, Z:String ): void {
			
			V[ Q ] = new Array( X[ Z ].length() );
			
			V[ Q ].forEach( function( a, i ) {
				
				V[ Q ][ i ] = {
					
					N: parseInt( X[ Z ][ i ].@nomor ),
					
					S: {
						
						C: parseInt( X[ Z ][ i ].skor.@benar ),
						F: parseInt( X[ Z ][ i ].skor.@salah )
						
					},
					
					Q: X[ Z ][ i ].soal.toString(),
					
					M: new Array( X[ Z ][ i ].media.length() )
				}
				
				V[ Q ][ i ].M.forEach( function( b, ii ) {
					
					V[ Q ][ i ].M[ ii ] = {
						
						T: X[ Z ][ i ].media[ ii ].@tipe.toString(),
						V: X[ Z ][ i ].media[ ii ].toString()
						
					}
					
				});
								
				if ( notFound( O, V[ Q ][ i ].N - 1 ) ) O.push( V[ Q ][ i ].N - 1 );
				
			});

		}
		
		private function notFound( target:Array, value ): Boolean {
			
			return target.every( function( e:*, i:int, r:Array ): Boolean {
				
				return e != value;
				
			});
			
		}
				
	}
	
}