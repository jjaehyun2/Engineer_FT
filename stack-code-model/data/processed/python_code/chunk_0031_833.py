package  {
	
	
	public class RowCount4 {
		
		static var row;
		static var moveList;
		
		
		static function check(diffX, row0, xList, target, moveList0):void {
			
			row = row0;
			moveList = moveList0;
				
			if (diffX > 0) {
				if (row[0].x > row[1].x - row[0].width) {
					setX(1);
					row[1].x = row[0].x + row[0].width;						
				}
				if (row[1].x > row[2].x - row[1].width) {
					setX(2);
					row[2].x = row[1].x + row[1].width;
				}
				if (row[2].x > row[3].x - row[2].width) {
					setX(3);
					row[3].x = row[2].x + row[2].width;
				}
			}
			
			if (diffX < 0) { // always reverse!!
				if (row[3].x < row[2].x + row[2].width) {
					setX(-1);	
					row[2].x = row[3].x - row[2].width;
				}
				if (row[2].x < row[1].x + row[1].width) {
					setX(-2);	
					row[1].x = row[2].x - row[1].width;
				}
				if (row[1].x < row[0].x + row[0].width) {
					setX(-3);	
					row[0].x = row[1].x - row[0].width;
				}
			}
			
			
			// SET X			
			function setX(potential) {
				if (potential == 1) {
					if (xList.length == 1) {
						if (target == row[0]) {
							xList[1] = row[1].x;
							moveList.push(row[1]);
						}
					}
				}
				if (potential == 2) {
					if (xList.length == 1) {
						if (target == row[1]) {
							xList[1] = row[2].x;
							moveList.push(row[2]);
						}
					} else if (xList.length == 2) {
						if (target == row[0]) {
							xList[2] = row[2].x;
							moveList.push(row[2]);
						}
					}
				}
				if (potential == 3) {
					if (xList.length == 1) {
						if (target == row[2]) {
							xList[1] = row[3].x;
							moveList.push(row[3]);
						}
					} else if (xList.length == 2) {
						if (target == row[1]) {
							xList[2] = row[3].x;
							moveList.push(row[3]);
						}
					} else if (xList.length == 3) {
						if (target == row[0]) {
							xList[3] = row[3].x;
							moveList.push(row[3]);
						}
					}
				}
				
				if (potential == -1) {
					if (xList.length == 1) {
						if (target == row[3]) {
							xList[1] = row[2].x;
							moveList.push(row[2]);
						}
					}
				}
				if (potential == -2) {
					if (xList.length == 1) {
						if (target == row[2]) {
							xList[1] = row[1].x;
							moveList.push(row[1]);
						}
					} else if (xList.length == 2) {
						if (target == row[3]) {
							xList[2] = row[1].x;
							moveList.push(row[1]);
						}
					}
				}
				if (potential == -3) {
					if (xList.length == 1) {
						if (target == row[1]) {
							xList[1] = row[0].x;
							moveList.push(row[0]);
						}
					} else if (xList.length == 2) {
						if (target == row[2]) {
							xList[2] = row[0].x;
							moveList.push(row[0]);
						}
					} else if (xList.length == 3) {
						if (target == row[3]) {
							xList[3] = row[0].x;
							moveList.push(row[0]);
						}
					}
				}
			}
			
			
			// MAGNET			
			if (moveList.length == 2) {
				if (moveList[0].x < moveList[1].x) {
					
					if (moveList[1].x > xList[1]) {
						moveList[1].x = target.x + target.width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
				} else 
				if (moveList[0].x > moveList[1].x) {
					if (moveList[1].x < xList[1]) {
						moveList[1].x = target.x - moveList[1].width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
				}
			} else 
			
			if (moveList.length == 3) {
				if (moveList[1].x < moveList[2].x) {
					
					if (moveList[2].x > xList[2]) {
						moveList[2].x = target.x + target.width + moveList[1].width;
					} else {
						moveList[2].x = xList[2];
						moveList.splice(2,1);
						xList.splice(2,1);
					}
					
					if (moveList[1].x > xList[1]) {
						moveList[1].x = target.x + target.width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
					
				} else 
				if (moveList[1].x > moveList[2].x) {
					
					if (moveList[2].x < xList[2]) {
						moveList[2].x = target.x - moveList[1].width - moveList[2].width;
					} else {
						moveList[2].x = xList[2];
						moveList.splice(2,1);
						xList.splice(2,1);
					}
					
					if (moveList[1].x < xList[1]) {
						moveList[1].x = target.x - moveList[1].width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
				}
			} else 
			
			if (moveList.length == 4) {
				if (moveList[2].x < moveList[3].x) {
					
					if (moveList[3].x > xList[3]) {
						moveList[3].x = target.x + target.width + moveList[1].width + moveList[2].width;
					} else {
						moveList[3].x = xList[3];
						moveList.splice(3,1);
						xList.splice(3,1);
					}
					
					if (moveList[2].x > xList[2]) {
						moveList[2].x = target.x + target.width + moveList[1].width;
					} else {
						moveList[2].x = xList[2];
						moveList.splice(2,1);
						xList.splice(2,1);
					}
					
					if (moveList[1].x > xList[1]) {
						moveList[1].x = target.x + target.width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
					
				} else 
				if (moveList[2].x > moveList[3].x) {
					
					if (moveList[3].x < xList[3]) {
						moveList[3].x = target.x - moveList[1].width - moveList[2].width - moveList[3].width;
					} else {
						moveList[3].x = xList[3];
						moveList.splice(3,1);
						xList.splice(3,1);
					}
					
					if (moveList[2].x < xList[2]) {
						moveList[2].x = target.x - moveList[1].width - moveList[2].width;
					} else {
						moveList[2].x = xList[2];
						moveList.splice(2,1);
						xList.splice(2,1);
					}
					
					if (moveList[1].x < xList[1]) {
						moveList[1].x = target.x - moveList[1].width;
					} else {
						moveList[1].x = xList[1];
						moveList.splice(1,1);
						xList.splice(1,1);
					}
				}
			}
			
			
			// BOUNDS			
			if (row[0].x < 0) {
				row[0].x = 0;
			}
			if (row[0].x >= Board.dotWidth) {
				row[0].x = Board.dotWidth;
			}
			
			if (row[1].x < Board.dotWidth) {
				row[1].x = Board.dotWidth;
			}
			if (row[1].x >= Board.dotWidth*2) {
				row[1].x = Board.dotWidth*2;
			}
			
			if (row[2].x < Board.dotWidth*2) {
				row[2].x = Board.dotWidth*2;
			}
			if (row[2].x >= Board.dotWidth*3) {
				row[2].x = Board.dotWidth*3;
			}
			
			if (row[3].x < Board.dotWidth*3) {
				row[3].x = Board.dotWidth*3;
			}
			if (row[3].x >= Board.dotWidth*4) {
				row[3].x = Board.dotWidth*4;
			}
		}
		
		
		static function snap(row0) {
			
			row = row0;
			
			if (row[0].x < Board.dotWidth/2) {
				row[0].x = 0;
			}
			if (row[0].x >= Board.dotWidth/2) {
				row[0].x = Board.dotWidth;
			}
			
			
			if (row[1].x < Board.dotWidth*1.5) {
				row[1].x = Board.dotWidth;
			}
			if (row[1].x >= Board.dotWidth*1.5) {
				row[1].x = Board.dotWidth*2;
			}
			
			
			if (row[2].x < Board.dotWidth*2.5) {
				row[2].x = Board.dotWidth*2;
			}
			if (row[2].x >= Board.dotWidth*2.5) {
				row[2].x = Board.dotWidth*3;
			}
			
			
			if (row[3].x < Board.dotWidth*3.5) {
				row[3].x = Board.dotWidth*3;
			}
			if (row[3].x >= Board.dotWidth*3.5) {
				row[3].x = Board.dotWidth*4;
			}
		}
	}
}