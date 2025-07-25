/**
 * Kerneos
 * Copyright (C) 2011 Bull S.A.S.
 * Contact: jasmine AT ow2.org
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307
 * USA
 *
 * $Id$
 */
package org.ow2.kerneos.profile.model {

/**
 * An enumerated type representing the states of Login.
 */
[Bindable]
public class ProfileState {

    /**
     * Idle state
     */
    public static var IDLE:String = "idle";

    /**
     * When load profile
     */
    public static var LOAD:String = "load";

    /**
     * When unload profile
     */
    public static var UNLOAD:String = "unload";

    /**
     * When the profile is loaded
     */
    public static var LOADED:String = "loaded";

    /**
     * Constructor
     */
    function ProfileState()
    {

    }
}
}