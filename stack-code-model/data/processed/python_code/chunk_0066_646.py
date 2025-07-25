////////////////////////////////////////////////////////////////////////////////
//
//  ADOBE SYSTEMS INCORPORATED
//  Copyright 2006-2007 Adobe Systems Incorporated
//  All Rights Reserved.
//
//  NOTICE: Adobe permits you to use, modify, and distribute this file
//  in accordance with the terms of the license agreement accompanying it.
//
////////////////////////////////////////////////////////////////////////////////

package mx.managers
{

import mx.managers.IHistoryManagerClient;

[ExcludeClass]

/**
 *  @private
 */
public interface IHistoryManager
{
	function register(obj:IHistoryManagerClient):void;
	function unregister(obj:IHistoryManagerClient):void;
	function save():void;
}

}