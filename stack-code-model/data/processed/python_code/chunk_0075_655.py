package com.bojinx.utils.tasks.event
{
	import flash.events.Event;
	import com.bojinx.utils.tasks.TaskState;
	
	/**
	 *  The StateChangeEvent class represents an event that is dispatched when the
	 *  <code>currentState</code> property of a component changes.
	 *
	 *  @see mx.core.UIComponent
	 *  @see mx.states.State
	 *
	 *  @langversion 3.0
	 *  @playerversion Flash 9
	 *  @playerversion AIR 1.1
	 *  @productversion Flex 3
	 */
	public class TaskStateChangeEvent extends Event
	{
		
		/*============================================================================*/
		/*= PUBLIC PROPERTIES                                                         */
		/*============================================================================*/
		
		/**
		 *  The name of the view state that the component is entering.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public var newState:TaskState;
		
		/**
		 *  The name of the view state that the component is exiting.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public var oldState:TaskState;
		
		/**
		 *  Constructor.
		 *  Normally called by a Flex control and not used in application code.
		 *
		 *  @param type The event type; indicates the action that caused the event.
		 *
		 *  @param bubbles Specifies whether the event can bubble
		 *  up the display list hierarchy.
		 *
		 *  @param cancelable Specifies whether the behavior
		 *  associated with the event can be prevented.
		 *
		 *  @param oldState The name of the view state the component is exiting.
		 *
		 *  @param newState The name of the view state the component is entering.
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public function TaskStateChangeEvent( type:String, bubbles:Boolean = false,
											  cancelable:Boolean = false,
											  oldState:TaskState = null,
											  newState:TaskState = null )
		{
			super( type, bubbles, cancelable );
			
			this.oldState = oldState;
			this.newState = newState;
		}
		
		
		/*============================================================================*/
		/*= STATIC PUBLIC PROPERTIES                                                  */
		/*============================================================================*/
		
		/**
		 *  The StateChangeEvent.CURRENT_STATE_CHANGE constant defines the
		 *  value of the <code>type</code> property of the event that is dispatched
		 *  when the view state has changed.
		 *  The value of this constant is "currentStateChange".
		 *
		 *  <p>The properties of the event object have the following values:</p>
		 *  <table class="innertable">
		 *     <tr><th>Property</th><th>Value</th></tr>
		 *     <tr><td><code>bubbles</code></td><td>false</td></tr>
		 *     <tr><td><code>cancelable</code></td><td>false</td></tr>
		 *     <tr><td><code>currentTarget</code></td><td>The Object that defines the
		 *       event listener that handles the event. For example, if you use
		 *       <code>myButton.addEventListener()</code> to register an event listener,
		 *       myButton is the value of the <code>currentTarget</code>. </td></tr>
		 *     <tr><td><code>newState</code></td><td>The name of the view state
		 *       that was entered.</td></tr>
		 *     <tr><td><code>oldState</code></td><td>The name of the view state
		 *       that was exited.</td></tr>
		 *     <tr><td><code>target</code></td><td>The Object that dispatched the event;
		 *       it is not always the Object listening for the event.
		 *       Use the <code>currentTarget</code> property to always access the
		 *       Object listening for the event.</td></tr>
		 *     <tr><td><code>type</code></td><td>StateChangeEvent.CURRENT_STATE_CHANGE</td></tr>
		 *  </table>
		 *
		 *  @eventType currentStateChange
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public static const CURRENT_STATE_CHANGE:String = "currentStateChange";
		
		/**
		 *  The StateChangeEvent.CURRENT_STATE_CHANGING constant defines the
		 *  value of the <code>type</code> property of the event that is dispatched
		 *  when the view state is about to change.
		 *  The value of this constant is "currentStateChanging".
		 *
		 *  <p>The properties of the event object have the following values:</p>
		 *  <table class="innertable">
		 *     <tr><th>Property</th><th>Value</th></tr>
		 *     <tr><td><code>bubbles</code></td><td>false</td></tr>
		 *     <tr><td><code>cancelable</code></td><td>false</td></tr>
		 *     <tr><td><code>currentTarget</code></td><td>The Object that defines the
		 *       event listener that handles the event. For example, if you use
		 *       <code>myButton.addEventListener()</code> to register an event listener,
		 *       myButton is the value of the <code>currentTarget</code>. </td></tr>
		 *     <tr><td><code>newState</code></td><td>The name of the view state
		 *       that is being entered.</td></tr>
		 *     <tr><td><code>oldState</code></td><td>The name of the view state
		 *       that is being exited.</td></tr>
		 *     <tr><td><code>target</code></td><td>The Object that dispatched the event;
		 *       it is not always the Object listening for the event.
		 *       Use the <code>currentTarget</code> property to always access the
		 *       Object listening for the event.</td></tr>
		 *     <tr><td><code>type</code></td><td>StateChangeEvent.CURRENT_STATE_CHANGING</td></tr>
		 *  </table>
		 *
		 *  @eventType currentStateChanging
		 *
		 *  @langversion 3.0
		 *  @playerversion Flash 9
		 *  @playerversion AIR 1.1
		 *  @productversion Flex 3
		 */
		public static const CURRENT_STATE_CHANGING:String = "currentStateChanging";
		
		
		/*============================================================================*/
		/*= PUBLIC METHODS                                                            */
		/*============================================================================*/
		
		/**
		 *  @private
		 */
		override public function clone():Event
		{
			return new TaskStateChangeEvent( type, bubbles, cancelable, oldState, newState );
		}
	}
}