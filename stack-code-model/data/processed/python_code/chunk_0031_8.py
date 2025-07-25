/*
 * This file is part of Apparat.
 * 
 * Apparat is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * Apparat is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with Apparat. If not, see <http://www.gnu.org/licenses/>.
 * 
 * Copyright (C) 2009 Joa Ebert
 * http://www.joa-ebert.com/
 * 
 */

package com.joa_ebert.apparat.memory 
{
	import flash.utils.ByteArray;
	import flash.utils.Endian;

	/**
	 * The ImmutableByteArray class represents a ByteArray whose endian and
	 * length can not be changed.
	 * 
	 * @private
	 * 
	 * @author Joa Ebert
	 */
	internal final class ImmutableByteArray extends ByteArray 
	{
		public function ImmutableByteArray( length: uint )
		{
			super();
			
			super.length = length;
			super.endian = Endian.LITTLE_ENDIAN;
		}

		
		override public function set endian( type : String ) : void
		{
			throw new Error( 'You are not allowed to change the endian.' );
		}

		override public function set length( value : uint ) : void
		{
			throw new Error( 'You are not allowed to change the length.' );
		}
	}
}