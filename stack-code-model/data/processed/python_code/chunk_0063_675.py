/**
 *
 * MetaBalls
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package com.absolut.metaballs{
	/**
	 * @author AbsolutRenal
	 */
	public class MetaballManager{
		private static var _instance:MetaballManager;
		
		private var activePool:Vector.<Metaball>;
		private var pool:Vector.<Metaball>;
		
		public function MetaballManager(singleton:Singleton){
			activePool = new Vector.<Metaball>();
			pool = new Vector.<Metaball>();
		}
		
		//----------------------------------------------------------------------
		// E V E N T S
		//----------------------------------------------------------------------
		
		
		//----------------------------------------------------------------------
		// P R I V A T E
		//----------------------------------------------------------------------
		
		
		//----------------------------------------------------------------------
		// P R O T E C T E D
		//----------------------------------------------------------------------
		
		
		//----------------------------------------------------------------------
		// P U B L I C
		//----------------------------------------------------------------------
		
		public static function getInstance():MetaballManager{
			if(!_instance)
				_instance = new MetaballManager(new Singleton());
			
			return _instance;
		}
		
		public function add():Metaball{
			var ball:Metaball;
			
			if(pool.length > 0)
				ball = pool.pop();
			else
				ball = new Metaball();
			
			activePool.push(ball);
			return ball;
		}
		
		public function remove(ball:Metaball):void{
			if(ball.parent)
				ball.parent.removeChild(ball);
			
			activePool.splice(activePool.indexOf(ball), 1);
			ball.clear();
			pool.push(ball);
		}
		
		public function render():void{
			var b:Metaball;
			for each (b in activePool) {
				b.clear();
				b.update();
			}
			
			var nb:int = activePool.length;
			var ball:Metaball;
			for(var i:int = 0; i < nb; i++){
				ball = activePool[i];
				
				for each (b in activePool) {
					if(ball == b)
						continue;
					
					if(ball.collideWith(b)){
						if(!ball.isInteractingWith(b) && !b.isInteractingWith(ball)){
							ball.interactWith(b, ball.radius > b.radius);
							b.interactWith(ball, b.radius >= ball.radius);
						}
					}
				}
			}
		}
		
		
		//----------------------------------------------------------------------
		// G E T T E R  /  S E T T E R
		//----------------------------------------------------------------------
		
		
	}
}

internal class Singleton{
	public function Singleton(){}
}