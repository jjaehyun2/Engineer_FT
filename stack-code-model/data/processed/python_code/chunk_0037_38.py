package com.illuzor.spinner.errors {
	
	/**
	 * ...
	 * @author illuzor  //  illuzor.com
	 */
	
	public class ShapeError extends Error {
		
		public function ShapeError(message:*="", id:*=0) {
			name = "ShapeError";
			super(name + ": " + message, id);
		}
		
	}
}