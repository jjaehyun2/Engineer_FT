/*
 PureMVC - Copyright(c) 2006, 2007 FutureScale, Inc., Some rights reserved.
 Your reuse is governed by the Creative Commons Attribution 3.0 United States License
*/
package org.puremvc.interfaces
{
	/**
	 * The interface definition for a PureMVC Controller.
	 * 
	 * <P>
	 * In PureMVC, an <code>IController</code> implementor 
	 * follows the 'Command and Controller' strategy, and 
	 * assumes these responsibilities:
	 * <UL>
	 * <LI> Remembering which <code>ICommand</code>s 
	 * are intended to handle which <code>INotifications</code>.</LI>
	 * <LI> Registering itself as an <code>IObserver</code> with
	 * the <code>View</code> for each <code>INotification</code> 
	 * that it has an <code>ICommand</code> mapping for.</LI>
	 * <LI> Creating a new instance of the proper <code>ICommand</code>
	 * to handle a given <code>INotification</code> when notified by the <code>View</code>.</LI>
	 * <LI> Calling the <code>ICommand</code>'s <code>execute</code>
	 * method, passing in the <code>INotification</code>.</LI> 
	 * </UL>
	 *
	 * @see org.puremvc.interfaces INotification
	 * @see org.puremvc.interfaces ICommand
	 */
	public interface IController extends IFacadeClient
	{

		/**
		 * Register a particular <code>ICommand</code> class as the handler 
		 * for a particular <code>INotification</code>.
		 * 
		 * @param notificationName the name of the <code>INotification</code>
		 * @param commandClassRef the Class of the <code>ICommand</code>
		 */
		function registerCommand( notificationName : String, commandClassRef : Class ) : void;
		
		/**
		 * Execute the <code>ICommand</code> previously registered as the
		 * handler for <code>INotification</code>s with the given notification name.
		 * 
		 * @param notification the <code>INotification</code> to execute the associated <code>ICommand</code> for
		 */
		function executeCommand( notification : INotification ) : void;

		/**
		 * Remove a previously registered <code>ICommand</code> to <code>INotification</code> mapping.
		 * 
		 * @param notificationName the name of the <code>INotification</code> to remove the <code>ICommand</code> mapping for
		 */
		function removeCommand( notificationName : String ):void;

		/**
		 * Set the reference to the related View instance
		 * 
		 * @param view should implement <code>IView</code>
		 */
		function setView( view : IView ):void;

		/**
		 * Get the reference to the related View instance
		 * 
		 * @param view should implement <code>IView</code>
		 */
		function getView() : IView;
	}
}