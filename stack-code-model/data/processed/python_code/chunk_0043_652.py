package widgets.Pmgd2.Class
{
	import mx.controls.Alert;
	import mx.controls.Text;
	import mx.validators.Validator;
	

	public class ValidarRut
	{
		public  static var ErrorRut:int = 0;
		public  static var RutOK:Text;
		//public static var RutTxt:String;
		
		public function ValidarRut2(RutTxt:String):String
		{	
			// Definicion de Variables Utilizadas 
			var suma:int=0; 
			var rut:String=RutTxt; 
			var ultimoN:String=RutTxt;
			var numMag:int=2; 
			var resto:int=0; 
			var i:int; 
			
			
			//Aqui vemos cuantos digitos tiene el rut
			
			if(rut.length == 9) {				
				rut = rut.substring(0,8);
				RutTxt=rut;
				ultimoN = ultimoN.substring(8,9);	
			}
			else if(rut.length == 8) 
			{                   
				rut = rut.substring(0,7);
				RutTxt=rut;
				ultimoN = ultimoN.substring(7,8);
			}
			
			
			// Defino el arreglo con los posibles digitos verificadores 
			var digVer:Array = new Array("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "K", "0"); 
			var parteNumerica:Array = new Array(); 
			
			for(i=0;i<rut.length;i++) 
			{ 
				parteNumerica[i]=rut.charAt(i); 
			} 
			
			// Calcula el digito verificador del rut 
			for (i=parteNumerica.length-1; i>=0; i--, numMag++) 
			{ 
				suma += parteNumerica[i]*numMag; 
				if (numMag>6) 
				{ 
					numMag = 1; 
				} 
			} 
			// Esto arroja el valor que debe tener el digito verificador 
			resto = 11-(suma%11);
			
			if(digVer[resto] == ultimoN.toUpperCase()) 
			{
				//RutTxt= SeparaRut(RutTxt) + ultimoN;
				RutTxt = SeparaRut(RutTxt) + ultimoN;
				ErrorRut = 0;
			} 
			else 
			{ 
				//Alert.show("Rut no valido"); 
				ErrorRut = 1;
				RutTxt="";
				
			} 
			return RutTxt;
		}
		
		public function SeparaRut(Rt:String):String{
		if(Rt !="") 
		{ 
			var rut:String = Rt;
			
			trace (rut); 
			
			if(rut.length == 8) 
			{ 
				var valor1:String = rut.substring(0,2); 
				valor1 = valor1 + ".";                
				var valor2:String = rut.substring(2,rut.length-3); 
				valor2 = valor2 + ".";                
				var valor3:String = rut.substring(5,rut.length); 
				valor3 = valor3 + "-";                
				var valor4:String = rut.substring(8); 
				valor4 = valor4;                
				Rt = valor1 + valor2 + valor3 + valor4; 
				
				trace(Rt);              
				
				
			}             
			else if(rut.length == 7)
			{ 
				var valor5:String = rut.substring(0,1); 
				valor5 = valor5 + ".";                 
				var valor6:String = rut.substring(1,rut.length-3); 
				valor6 = valor6 + ".";                
				var valor7:String = rut.substring(4,rut.length); 
				valor7 = valor7 + "-";                
				var valor8:String = rut.substring(7); 
				valor8 = valor8;                
				Rt = valor5 + valor6 + valor7 + valor8; 
				
				trace(Rt); 
			
			} 
		}
		return Rt;
		}	
	}
}