package ru.nacid.base.services.windows
{
	import com.junkbyte.console.Cc;
	
	import flash.events.Event;
	import flash.events.FocusEvent;
	import flash.events.IEventDispatcher;
	import flash.events.MouseEvent;
	
	import ru.nacid.base.data.Global;
	import ru.nacid.base.data.managment.VOIterator;
	import ru.nacid.base.data.managment.VOManager;
	import ru.nacid.base.data.store.VOList;
	import ru.nacid.base.services.windows.events.WindowPolicyEvent;
	import ru.nacid.base.services.windows.interfaces.IWindow;
	import ru.nacid.base.services.windows.interfaces.IWindowStorage;
	import ru.nacid.base.view.interfaces.IDisplayContainerProxy;

	/**
	 * Wm.as
	 * Created On: 5.8 17:25
	 *
	 * @author Nikolay nacid Bondarev
	 * @url https://github.com/nacid/nCore
	 *
	 *
	 *		Copyright 2012 Nikolay nacid Bondarev
	 *
	 *	Licensed under the Apache License, Version 2.0 (the "License");
	 *	you may not use this file except in compliance with the License.
	 *	You may obtain a copy of the License at
	 *
	 *		http://www.apache.org/licenses/LICENSE-2.0
	 *
	 *	Unless required by applicable law or agreed to in writing, software
	 *	distributed under the License is distributed on an "AS IS" BASIS,
	 *	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	 *	See the License for the specific language governing permissions and
	 *	limitations under the License.
	 *
	 */
	public class Wm extends VOManager
	{

		private static var m_instance:Wm;

		private var container:IDisplayContainerProxy;
		private var windows:VOList=new VOList();

		public var topOnFocus:Boolean;
		public var focusOnTop:Boolean=true;

		/* Wm
		 * Use Wm.instance
		 * @param singleton DO NOT USE THIS - Use Wm.instance */
		public function Wm(singleton:*)
		{
			dispatcherMode = true;

			if (singleton is Wm || singleton is Singleton)
			{
				super();
				init();
			}
			else
			{
				throw new Error("Wm is a singleton class.  Access via ''Wm.instance''.");
			}
		}

		protected function init():void
		{
			//virtual
		}

		/* instance
		 * Gets the Wm instance */
		public static function get instance():Wm
		{
			if (Wm.m_instance == null)
				Wm.m_instance=new Wm(new Singleton());
			return Wm.m_instance;
		}

		public function regWindow($param:IWindowStorage):void
		{
			if (list.add($param))
			{
				$param.policy.addEventListener(WindowPolicyEvent.OPEN_WINDOW, policyOpenHandler);
				$param.policy.addEventListener(WindowPolicyEvent.CLOSE_WINDOW, policyCloseHandler);

				Cc.infoch(MANAGER_CHANNEL, 'window', $param.symbol, 'added');
			}
			else
			{
				Cc.warnch(MANAGER_CHANNEL, 'window with id', $param.symbol, 'cannot be added');
			}
		}

		private function policyOpenHandler(e:WindowPolicyEvent):void
		{
			if (e.displayIndex < 0)
				return Cc.warnch(MANAGER_CHANNEL, 'window', e.targetWindow, 'is not open');

			var window:IWindow=createWindow(list.atId(e.targetWindow) as IWindowStorage);
			window.setData(e.openData);
			windows.add(window);

			activate(e.targetWindow)
			container.addAt(window, e.displayIndex);

			if (window is IEventDispatcher)
			{
				IEventDispatcher(window).addEventListener(FocusEvent.FOCUS_IN, focusHandler);
				IEventDispatcher(window).addEventListener(MouseEvent.MOUSE_DOWN, focusHandler);
			}

			if (focusOnTop)
				container.setFocus(window);

			Cc.logch(MANAGER_CHANNEL, 'window', e.targetWindow, 'opened');
		}

		private function policyCloseHandler(e:WindowPolicyEvent):void
		{
			var target:IWindow=windows.removeAtId(e.targetWindow) as IWindow;
			deactivate(e.targetWindow);
			container.rem(target);

			if (target is IEventDispatcher)
			{
				IEventDispatcher(target).removeEventListener(FocusEvent.FOCUS_IN, focusHandler);
				IEventDispatcher(target).removeEventListener(MouseEvent.MOUSE_DOWN, focusHandler);
			}

			Cc.logch(MANAGER_CHANNEL, 'window', e.targetWindow, 'closed');
		}

		public function showWindow($id:String, $data:Object=null):void
		{
			if (!inited)
			{
				return channelError('window manager not inited');
			}

			var param:IWindowStorage=list.atId($id) as IWindowStorage;
			if (param == null)
				return Cc.errorch(MANAGER_CHANNEL, 'windows with id', $id, 'is not registered');

			if (isActive($id))
				return Cc.errorch(MANAGER_CHANNEL, 'windows with id', $id, 'already active');

			param.policy.applyOpen(activeList, $id, $data);
		}

		public function closeWindow($id:String, $force:Boolean=false):void
		{
			if (!inited)
			{
				return channelError('window manager not inited');
			}

			if (isActive($id))
			{
				var param:IWindowStorage=list.atId($id) as IWindowStorage;
				param.policy.applyClose(activeList, $id, $force);
			}
			else
			{
				Cc.warnch(MANAGER_CHANNEL, 'window', $id, 'is not opened');
			}
		}

		public function closeAll():void
		{
			while (activeList.length)
				closeWindow(activeList[0], true);
		}

		public function makeTop($id:String):void
		{
			if (isActive($id))
			{
				deactivate($id);
				container.move(windows.atId($id) as IWindow, activeList.length);
				activate($id);

				Cc.infoch(MANAGER_CHANNEL, 'move window', $id, 'on top');
			}
			else
			{
				Cc.infoch(MANAGER_CHANNEL, 'can not move', $id, 'up because it closed');
			}
		}

		private function focusHandler(e:Event):void
		{
			if (topOnFocus)
			{
				makeTop(e.currentTarget.symbol);
			}
			e.currentTarget.onFocus();
		}

		public function get inited():Boolean
		{
			return container != null;
		}

		private function createWindow($params:IWindowStorage):IWindow
		{
			if ($params is IWindow)
				return $params as IWindow;

			var response:IWindow=new $params.renderer;
			response.applyParam($params as WindowParam);

			if (response.cached)
				list.setAtId($params.symbol, response);

			return response;
		}

		public function setContainer($container:IDisplayContainerProxy):void
		{
			if (container == null)
			{
				container=$container;
				container.main.stage.addEventListener(Event.RESIZE, resizeHandler);
			}
			else
			{
				channelError('container already created');
			}
		}

		public function getWindow($id:String):IWindow
		{
			if (!isActive($id))
			{
				channelWarning('window::'.concat($id, ' is not active'));
			}
			
			return windows.atId($id) as IWindow;
		}

		private function resizeHandler(e:*):void
		{
			var it:VOIterator=windows.createIterator();

			Global.stageW=e.target.stageWidth;
			Global.stageH=e.target.stageHeight;
			while (it.hasNext())
			{
				IWindow(it.next()).arrange();
			}
		}
	}
}

class Singleton
{
}