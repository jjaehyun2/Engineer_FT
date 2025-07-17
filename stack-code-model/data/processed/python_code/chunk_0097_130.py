/**
 * @author Landaes
 * se usa así:
 var d:DragNDrop = new DragNDrop();
 d.crea(	d:DragNDrop, 		// se llama a sí mismo
		preguntas:Array, 	// contiene movieClips
		respuestas:Array,	// contiene movieClips
		win:Array,		// contiene movieClips
		lose:Array,		// contiene movieClips
		feedbackFinal:Array,	// contiene movieClips
		callback:Function,	// función de feedback positivo (cuando aprietas el botón del final, cuando ganaste)
		callbackMal:Function,	// función de feedback negativo (cuando aprietas el botón del final, cuando ya agotas el máximo de repeticiones)
		maxRepeticiones:Number	// cantida de veces que puedes hacer drag and drop
	);
 */
import com.greensock.*;
import com.greensock.easing.*;
class landaes.DragNDrop extends MovieClip
{
	private var ap:Array = new Array();
	private var ar:Array = new Array();
	private var aRespondidas:Array = new Array();
	private var buenas:Number = 0;
	public var mc_ganaste:MovieClip;
	public var mc_perdiste:MovieClip;
	public var mc_perdiste_final:MovieClip;
	public var bt_ganaste:MovieClip;
	public var bt_perdiste:MovieClip;
	public var bt_perdiste_final:MovieClip;
	
	
	private var maxReps:Number = 0;
	private var intentos:Number = 0;
	
	public function DragNDrop() 
	{
		
	}
	
	public function crea(d:DragNDrop, preguntas:Array, respuestas:Array, win:Array, lose:Array, feedbackFinal:Array, callback:Function, callbackMal:Function, maxRepeticiones:Number) {
		trace("CreA");
		
		mc_ganaste = win[0];
		bt_ganaste = win[1];
		mc_perdiste = lose[0];
		bt_perdiste = lose[1];
		mc_perdiste_final = feedbackFinal[0];
		bt_perdiste_final = feedbackFinal[1];

		
		mc_ganaste._visible = false;
		bt_ganaste._visible = false;
		mc_perdiste._visible = false;
		bt_perdiste._visible = false;
		mc_perdiste_final._visible = false;
		bt_perdiste_final._visible = false;
		
		bt_ganaste.onRelease = function() {
			d.ocultaTodo();
			callback();
		};
		
		bt_perdiste.onRelease = function() {
			d.resetea();
		};
		
		bt_perdiste_final.onRelease = function() {
			d.animaSolito(callbackMal);
			
		};

		maxReps = maxRepeticiones;
		
		for (var i:Number = 0; i < preguntas.length; i++) 
		{
			aRespondidas.push(false);
			var mc:MovieClip = preguntas[i];
			mc._name = "preg" + i;
			mc.i = i;
			ap.push([mc, mc._x, mc._y]);
			
			var cm:MovieClip = respuestas[i];
			cm._name = "resp" + i;
			cm.i = i;
			ar.push([cm, cm._x, cm._y]);
			
			mc.onPress = function() {
				//swapDepths(getNextHighestDepth());
				startDrag(mc);
				//clearInterval(TiempoRevisor);
				trace("nombre: "+this);
			};
			/*cm.onPress = function() {
				trace("nombre: "+this);
			};*/
			mc.onRelease = mc.onReleaseOutside=function () {
				stopDrag();
				trace("stopDrag: " + this);
				//trace(_parent);
				if (this.hitTest(_parent["resp"+this.i])) {
					trace("\nhit correcto");
					d.aRespondidas[this.i] = true;
					d.buenas+=1;
					new TweenMax(this, 0.2, { _x:d.ar[this.i][1], _y:d.ar[this.i][2], ease:Linear.easeOut } );
					_parent["resp" + this.i]._x = 5000;
					this.enabled = false;
					d.revisor();
				} else {
					trace("\nhit INcorrecto");
					//malas += 1;
					for (var j:Number=0; j<=preguntas.length; j++) {
						if (j != this.i) {
							if (this.hitTest(_parent["resp"+j])) {
								d.aRespondidas[this.i] = true;
								trace(this + " hit en j " + j);
								new TweenMax(this, 0.2, { _x:_parent["resp" + j]._x, _y:_parent["resp" + j]._y, ease:Linear.easeOut } );
								_parent["resp" + j]._x = 5000;
								this.enabled = false;
								d.revisor();
								return;
							} else {
								//trace("hola Pame");
							}
						}
					}
					trace("NO TOCA NADA");
					d.vuelvePreg(this);
				}
			}
		}
	}
	private function ocultaTodo():Void 
	{
		mc_ganaste._visible = false;
		bt_ganaste._visible = false;
		mc_perdiste._visible = false;
		bt_perdiste._visible = false;
		for (var i:Number = 0; i < ap.length; i++) 
		{
			var mc:MovieClip = ap[i][0];
			mc._visible = false;
			
			var cm:MovieClip = ar[i][0];
			cm._visible = false;
			
		}
	}
	private function resetea():Void 
	{
		buenas = 0;
		mc_ganaste._visible = false;
		bt_ganaste._visible = false;
		mc_perdiste._visible = false;
		bt_perdiste._visible = false;
		mc_perdiste_final._visible = false;
		bt_perdiste_final._visible = false;
		for (var i:Number = 0; i < ap.length; i++) 
		{
			var mc:MovieClip = ap[i][0];
			mc.enabled = true;
			vuelvePreg(mc);
			vuelveResp(ar[i][0]);
		}
		
		for (var j:Number = 0; j < aRespondidas.length; j++) 
		{
			aRespondidas[j] = false;
		}
	}
	private function revisor():Void 
	{
		var k:Number = 0;
		//trace("aRespondidas.length: " + aRespondidas.length);
		for (var i:Number = 0; i < aRespondidas.length; i++) 
		{
			trace(aRespondidas[i]);
			if (aRespondidas[i]) 
			{
				k += 1;
			}
		}
		//trace("k en revisor:" +k);
		if (k == aRespondidas.length) 
		{
			trace("revisor");
			trace(mc_perdiste);
			if (buenas == aRespondidas.length) {		
				mc_ganaste._visible = true;
				mc_perdiste._visible = false;
				//mc_ganaste.swapDepths(998);
				bt_ganaste._visible = true;
				bt_perdiste._visible = false;
				//bt_ganaste.swapDepths(999);
			} else if (intentos < maxReps - 1) {
				intentos+=1;
				mc_ganaste._visible = false;
				mc_perdiste._visible = true;
				//mc_perdiste.swapDepths(998);
				bt_ganaste._visible = false;
				bt_perdiste._visible = true;
				//bt_perdiste.swapDepths(999);
			} else {
				mc_perdiste_final._visible = true;
				bt_perdiste_final._visible = true;
				//mc_perdiste_final.swapDepths(getNextHighestDepth()+1);
				//bt_perdiste_final.swapDepths(getNextHighestDepth()+2);

			}
		}
	}
	
	private function vuelvePreg(mc:MovieClip) {
		trace("vuelvePreg " + mc);
		new TweenMax(mc,0.7,{_x:ap[mc.i][1],_y:ap[mc.i][2], ease:Bounce.easeOut});
	}
	private function vuelveResp(mc:MovieClip) {
		trace("vuelveResp " + mc);
		//new TweenMax(mc,0.7,{_x:ap[mc.i][1],_y:ap[mc.i][2], ease:Bounce.easeOut});
		mc._x = ar[mc.i][1];
		mc._y = ar[mc.i][2];
	}
	private function animaSolito(callbackMal:Function) {
		mc_perdiste_final._visible = false;
		bt_perdiste_final._visible = false;
		
		for (var j:Number = 0; j < ap.length; j++) 
		{
			var animBB = ap[j][0];
			//var mcB = ar[j];
			if(j == ap.length-1){
				new TweenMax(animBB, 1, { _x:ar[j][1], _y:ar[j][2], ease:Linear.easeOut, delay:j*0.2, onComplete:callbackMal } );
			} else {
				new TweenMax(animBB, 1, { _x:ar[j][1], _y:ar[j][2], ease:Linear.easeOut, delay:j*0.2 } );
			}
			
		}
		//hits_on_A +=1;
	}
	
}