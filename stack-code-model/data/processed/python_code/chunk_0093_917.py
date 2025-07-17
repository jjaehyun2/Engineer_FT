package 
{
	import Entidades.Flecha;
	import net.flashpunk.World;
	import Entidades.Cuadro;
	import Entidades.Estatus;
	import Entidades.Flecha;
	import net.flashpunk.World;
	import net.flashpunk.tweens.motion.LinearMotion;
	import net.flashpunk.utils.Ease;
	import net.flashpunk.utils.Key;
	import net.flashpunk.utils.Input;
	import net.flashpunk.Entity;
	import net.flashpunk.graphics.Text;
	import net.flashpunk.FP;
	
	/**
	 * ...
	 * @author ...
	 */
	public class Binaria extends World 
	{	
		private var cuadros:Vector.<Cuadro>;
		
		private var minimo:Flecha;
		private var pivote:Flecha;
		private var maximo:Flecha;
		
		private var status:Estatus;
		
		private var buscar:int = 0;
		
		private var medio:uint = 0;
		private var max:uint = 0;
		private var min:uint = 0;
		
		private var pasos:uint = 0;
		
		private var tmp:Cuadro = null;
		private var tmp2:Cuadro = null;
		private var tmp3:Cuadro = null;
		
		private var encontrado:Boolean = false;
		
		public function Binaria() 
		{
			super();
			
			cuadros = new Vector.<Cuadro>();
			
			pivote = new Flecha( -100, -100);
			minimo = new Flecha( -100, -100, true);
			maximo = new Flecha( -100, -100, true);
			
			add(minimo);
			add(maximo);
			add(pivote);
			
			var pad:uint = 30;
			var cnt:uint = 0;
			
			for (var i:uint = 0; i < 8; i++) {
				for (var j:uint = 0; j < 13; j++) {
					var tmp:Cuadro = new Cuadro((j * 70) + 2 * pad, (i * 70) + 2*pad, cnt);
					add(tmp);
					cuadros.push(tmp);
					cnt++;
				}
			}
			
			min = 0;
			max = cuadros.length-1;
			
			status = new Estatus(10, 580);
			add(status);
			add(new Entity(740, 775, new Text("Aldrin Salazar @ AlphaSigma.web.ve", 0, 0, { font: "aldrin" } )));
			actualizarStatus();
		}
		
		override public function update():void {
			super.update();	
			
			if (Input.pressed(Key.SPACE)) {
				if (encontrado) {
					resetear();
				}else{
					busqueda();
				}
			}
			
			
				if (Input.pressed(Key.RIGHT)) {
					buscar++;
					actualizarStatus();
				}
				
				if (Input.pressed(Key.LEFT)) {
					buscar--;
					actualizarStatus();
				}
				
				if (Input.pressed(Key.UP)) {
					buscar += 100;
					actualizarStatus();
				}
				
				if (Input.pressed(Key.DOWN)) {
					buscar -= 100;
					actualizarStatus();
				}
				
				if (Input.mouseWheel) {
					if (Input.mouseWheelDelta > 0) {
						buscar += 10;
					}else {
						buscar -= 10;
					}
					
					actualizarStatus();
				}
				
				if (Input.pressed(Key.R)) {
					randomOrdenado();
				}
				
				if (Input.pressed(Key.M)) {
					FP.world = new Transition(Menu);
				}
		}
		
		private function actualizarStatus():void {
			status.setText("Presiona espacio para iniciar busqueda del numero "+buscar+".");
		}
		
		private function randomRange(minNum:Number, maxNum:Number):Number 
		{
			return (Math.floor(Math.random() * (maxNum - minNum + 1)) + minNum);
		}
		
		private function randomOrdenado():void {
			var anterior:int = randomRange(0, 100);
			
			for (var i:uint = 0; i < cuadros.length; i++) {
				anterior = anterior + randomRange(1, 10);
				cuadros[i].cambiarValor(anterior);
			}
		}
		
		private function fin():void {
			encontrado = true;
			status.setText("Valor "+buscar+" encontrado\n posicion "+medio+", pasos "+pasos);
		}
		
		public function noEncontrado():void {
			encontrado = true;
			status.setText("Valor "+buscar+" no se encuentra en el arreglo.");
		}
		
		private function resetear():void {
			actualizarStatus();
			
			try{
			tmp.deSeleccionado();
			tmp2.deSeleccionado();
			tmp3.deSeleccionado();
			}catch (error:Error) {
				
			}
			
			//Pivote
			var t:LinearMotion = new LinearMotion();
			t.setMotion(pivote.x, pivote.y, -100, -100, 0.5, Ease.backOut);
			t.object = pivote;
			addTween(t, true);
			
			//min
			var t2:LinearMotion = new LinearMotion();
			t2.setMotion(minimo.x, minimo.y, -100, -100, 0.5, Ease.backOut);
			t2.object = minimo;
			addTween(t2, true);
			
			//max
			var t3:LinearMotion = new LinearMotion();
			t3.setMotion(maximo.x, maximo.y, -100, -100, 0.5, Ease.backOut);
			t3.object = maximo;
			addTween(t3, true);
			
			min = 0;
			max = cuadros.length - 1;
			pasos = 0;
			encontrado = false;
		}
		
		private function busqueda():void {
			
			medio = (min + max) / 2;
			
			try{
			tmp.deSeleccionado();
			tmp2.deSeleccionado();
			tmp3.deSeleccionado();
			}catch (error:Error) {
				
			}
			
			//Pivote
			var t:LinearMotion = new LinearMotion();
			tmp = cuadros[medio];
			tmp.seleccionado();
			t.setMotion(pivote.x, pivote.y, tmp.x - 30, tmp.y - 130, 0.5, Ease.backOut);
			t.object = pivote;
			addTween(t, true);
			
			//min
			var t2:LinearMotion = new LinearMotion();
			tmp2 = cuadros[min];
			tmp2.seleccionado(true);
			t2.setMotion(minimo.x, minimo.y, tmp2.x - 30, tmp2.y - 130, 0.5, Ease.backOut);
			t2.object = minimo;
			addTween(t2, true);
			
			//max
			var t3:LinearMotion = new LinearMotion();
			tmp3 = cuadros[max];
			tmp3.seleccionado(true);
			t3.setMotion(maximo.x, maximo.y, tmp3.x - 30, tmp3.y - 130, 0.5, Ease.backOut);
			t3.object = maximo;
			addTween(t3, true);
			
			pasos++;
			status.setText("Buscar: "+buscar+" , Actual: "+tmp.valor+" \nPasos: "+pasos);
			
			if (cuadros[medio].valor == buscar) {
				fin();
			}else if (cuadros[medio].valor > buscar) {
				max = medio - 1;
			}else if (cuadros[medio].valor < buscar) {
				min = medio + 1;
			}
			
			if (max < min) {
				noEncontrado();
			}
		}
		
	}

}