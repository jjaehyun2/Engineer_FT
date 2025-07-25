package 
{
	
	/**
	 * ...
	 * @author Petr Horák
	 */
	public class elements extends raiders
	{
		
		public static const fireArray:Array = new Array ([1],[1],[1],[1],[1],[1]);
			
		public static const ufoArray:Array = new Array (
		[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
		[0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0],
		[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
		[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]);	
			
		public static const playerArray:Array = new Array (
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1]);
			
		public static const shieldCelek:Array = new Array (
		[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
		[0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
		[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]);
			
		public static const enemy1_:Array = new Array(
		[0,0,1,1,0,0,0,0,1,1,0,0],
		[0,0,1,1,0,0,0,0,1,1,0,0],
		[0,0,0,0,1,0,0,1,0,0,0,0],
		[0,0,0,0,1,1,1,1,0,0,0,0],
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,1,1,1,1,1,1,1,1,0,0],
		[0,1,1,1,1,1,1,1,1,1,1,0],
		[1,0,1,1,0,0,0,0,1,1,0,1],
		[1,0,0,1,1,1,1,1,1,0,0,1],
		[0,0,0,0,1,0,0,1,0,0,0,0],
		[0,0,0,1,0,0,0,0,1,0,0,0],
		[0,0,0,0,1,0,0,1,0,0,0,0]);	   
		   
		public static const enemy1:Array = new Array(
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[0,0,1,0,0,0,0,0,0,1,0,0],
		[0,0,0,1,0,1,1,0,1,0,0,0],
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,1,1,1,1,1,1,1,1,0,0],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,1,1,0,0,0,0,1,1,0,0],
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,0,0,1,0,0,1,0,0,0,0],
		[0,0,0,1,0,0,0,0,1,0,0,0],
		[0,0,1,0,0,0,0,0,0,1,0,0]);	   

		public static const enemy2:Array = new Array(
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,1,1,0,0,0,0,1],
		[1,1,1,0,0,1,1,1,1,0,0,1],
		[1,0,0,0,0,1,1,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,1,0,1,1,1,1,0,1,0,0],
		[0,1,0,0,1,1,1,1,0,0,1,0],
		[1,0,0,0,0,1,1,0,0,0,0,1],
		[0,1,0,0,0,0,0,0,0,0,1,0],
		[0,0,1,0,0,0,0,0,0,1,0,0]);	   
		  
		public static const enemy2_:Array = new Array(
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[1,1,0,0,0,0,0,0,0,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,1,1,0,0,0,0,1],
		[1,0,0,1,1,1,1,0,0,1,1,1],
		[1,0,0,0,0,1,1,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,1,0,1,1,1,1,0,1,0,0],
		[0,0,1,0,1,1,1,1,0,1,0,0],
		[0,0,1,0,0,1,1,0,0,1,0,0],
		[0,0,1,0,0,0,0,0,0,1,0,0],
		[0,0,1,0,0,0,0,0,0,1,0,0]);	   
		   
		public static const enemy3:Array = new Array(
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,1,1,1,1,1,1,1,1,0,0],
		[0,1,1,1,1,1,1,1,1,1,1,0],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,1,1,0,1,1,1,1,0,1,1],
		[1,1,1,1,0,1,1,1,1,0,1,1],
		[1,1,1,1,0,1,1,1,1,0,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,0,1,1,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,1,1,0,0,0]);	   
		   
		public static const enemy3_:Array = new Array(
		[0,0,0,1,1,1,1,1,1,0,0,0],
		[0,0,1,1,1,1,1,1,1,1,0,0],
		[0,1,1,1,1,1,1,1,1,1,1,0],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[1,1,0,1,1,1,1,0,1,1,1,1],
		[1,1,0,1,1,1,1,0,1,1,1,1],
		[1,1,0,1,1,1,1,0,1,1,1,1],
		[1,1,1,1,1,1,1,1,1,1,1,1],
		[0,0,1,1,1,1,1,1,1,0,0,0],
		[0,0,1,1,0,0,0,0,1,1,0,0],
		[0,1,1,0,0,0,0,0,0,1,1,0],
		[1,1,0,0,0,0,0,0,0,0,1,1]);
		   
		public static const vybuch:Array = new Array(
		[0,0,0,1,0,0,0,0,0,0,0,0],
		[0,0,0,0,1,0,0,1,0,0,0,1],
		[0,1,0,0,1,0,0,1,0,0,1,0],
		[0,0,1,0,0,1,1,0,0,1,0,0],
		[0,0,0,1,0,0,0,0,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,1,0,0,0,0,1,0,0,0],
		[0,1,1,0,0,1,1,0,0,1,1,0],
		[1,0,0,0,1,0,0,1,0,0,1,1],
		[0,0,0,0,1,0,0,1,1,0,0,0],
		[0,0,0,1,0,0,0,0,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0]);	   

		public static const nula:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);
		
		public static const jedna:Array = new Array(
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0],
		[0,0,0,1,1,0,0,0]);
		
		public static const dve:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,0,0,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);
		
		public static const tri:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);

		public static const ctyri:Array = new Array(
		[0,1,1,0,0,0,0,0],
		[0,1,1,0,0,0,0,0],
		[0,1,1,0,0,0,0,0],
		[0,1,1,0,1,1,0,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,1,1,0,0],
		[0,0,0,0,1,1,0,0]);
		
		public static const pet:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,0,0,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);
		
		public static const sest:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,0,0,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);		
		
		public static const sedm:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,0,0,0,0,1,1,0]);		

		public static const osm:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);						

		public static const devet:Array = new Array(
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,0,0,0,0,1,1,0],
		[0,1,1,1,1,1,1,0],
		[0,1,1,1,1,1,1,0]);
		
		public static const cisla:Array = new Array (nula,jedna,dve,tri,ctyri,pet,sest,sedm,osm,devet);						
		
		public static const high:Array = new Array(
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
	
		public static const gameIsOver:Array = new Array(
		[0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0],
[0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0],
[0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0],
[0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
[0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0]	
		);
				
}

}