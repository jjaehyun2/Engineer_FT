package mrd {
    import flash.display.MovieClip;
    import flash.utils.*;
    import flash.events.Event;

    public class Level extends MovieClip {
 		private var positions = [];
 		private const groundY = 500;
 		private const posWidth = 308;

 		public function Level() {
            var i, j;
            for (i = 0, j = 0; i <= 3; i++, j += posWidth){
                positions.push(addChild(new Position(j, groundY-50)));
            }

            for (i = 0; i < positions.length; i++){
                positions[i].previousPosition = (positions[i-1]) ? positions[i-1] : null;
                positions[i].nextPosition = (positions[i+1]) ? positions[i+1] : null;
            }

    	    spawn('footbot', 0);
    	    spawn('wall', 2);
    	    spawn('wall', 3);
 		}

        public function spawn(type:String, posIndex:Number) {
            switch (type.toLowerCase()) {
            case 'wall':
                return place(new Wall(getCoordinates(posIndex), groundY), posIndex);
            case 'footbot':
   			    return place(new FootBot(getCoordinates(posIndex), groundY), posIndex);
            default:
                throw new Error('Unknow spawn type requested');
            }
        }

    	public function place(obj, positionIndex:Number) {
    	    if (obj is FootBot) {
    	        positions[positionIndex].boomBots.push(obj);
    	    } else if (obj is Wall) {
    	        positions[positionIndex].wallHere = obj;
    	    } else {
    	        throw new Error('Cannot place object of unknown type');
    	    }
    	    return addChild(obj);
    	}

    	public function getCoordinates(posIndex:Number) {
    	    if (positions[posIndex]) {
    	        return positions[posIndex].x;
    	    } else {
    	        return -1;
    	    }
    	}

        public function getCenter(posIndex:Number) {
    	    if (positions[posIndex]) {
    	        return posIndex * posWidth + posWidth / 2;
    	    } else {
    	        return -1;
    	    }
    	}
//     	public function pos(){
//  			this.addEventListener(Event.ENTER_FRAME, this.onEnterFrame);
//  		}
//
//  		private function onEnterFrame(e) {
//             if (!positions[0].hitTestObject(boomBot[0])) {
//                 positions.boomBots[0] = 0;
//                 positions.boomBots[1] = boomBot[0];
//             }
//  		}
    }
}