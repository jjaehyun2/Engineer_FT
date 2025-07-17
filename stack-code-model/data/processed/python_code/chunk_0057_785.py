/**
 *
 * Blackhole/Repulsor
 *
 * https://github.com/AbsolutRenal
 *
 * Copyright (c) 2012 AbsolutRenal (Renaud Cousin). All rights reserved.
 * 
 * This ActionScript source code is free.
 * You can redistribute and/or modify it in accordance with the
 * terms of the accompanying Simplified BSD License Agreement.
**/

package com.game.data {
	import com.game.data.HexagonData;

	/**
	 * @author renaud.cousin
	 */
	public class HexagonBlocData extends HexagonData {
		private var _orientation:int;

		public function HexagonBlocData(datas:Object) {
			super(datas);
			
			_orientation = parseInt(datas.o);
		}
		
		
		//----------------------------------------------------------------------
		// G E T T E R / S E T T E R
		//----------------------------------------------------------------------
		
		public function get orientation():int{
			return _orientation;
		}
	}
}