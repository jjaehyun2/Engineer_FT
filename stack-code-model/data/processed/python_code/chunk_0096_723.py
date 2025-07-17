// Copyright 2018, Earthfiredrake
// Released under the terms of the MIT License
// https://github.com/Earthfiredrake/SWL-GlitterGone

// Makes shiny agents look like basic ones
// Minimod, not framework enabled for now

import gfx.utils.Delegate;
import com.GameInterface.DistributedValue;

function onLoad():Void {
	// HACK: Faking static storage, to avoid needing a class file
	if (_global.efd == undefined) { _global.efd = new Object(); }
	if (_global.efd.GlitterGone == undefined) { _global.efd.GlitterGone = new Object(); }

	HookUI(false); // Tries a pre-emptive hook, in case the protoype has been pre-loaded
	if (!_global.efd.GlitterGone.AgentIconHookApplied) { // Could not apply hook, setup triggers to try later
		AgentWindow = DistributedValue.Create("agentSystem_window");
		AgentWindow.SignalChanged.Connect(HookAgentWindow, this);
		HookItemUse();
	}
}

// New hook pattern:
//   Permits multiple mods hooking a single function without having to ensure a unique name for each nested copy
//   Side-effect based conflicts may still occur, hooking order is arbitrary and there is no way to safely disconnect a hook after the fact
function HookUI(useTimeout:Boolean):Void {
	if (!_global.efd.GlitterGone.AgentIconHookApplied) {
		var proto:Object = _global.GUI.AgentSystem.RosterIcon.prototype;
		if (proto) {
			var wrapper:Function = function():Void {
				arguments.callee.Base.apply(this, arguments);
				this.m_Foil._visible = false;
				this.m_Foil.gotoAndStop(1);
			};
			wrapper.Base = proto.UpdateVisuals;
			proto.UpdateVisuals = wrapper;
			_global.efd.GlitterGone.AgentIconHookApplied = true;

			// AgentUnlock window loads before hook is applied and doesn't update visuals
			// So force a refresh if the window exists
			_root.agentunlock.m_Window.m_Content.m_AgentIcon.UpdateVisuals();
		} else if (useTimeout) { // Expect to have a prototype soon
			setTimeout(Delegate.create(this, HookUI), 50, useTimeout);
		}
	}
}

function HookAgentWindow(dv:DistributedValue):Void { HookUI(dv.GetValue()); }
function HookItemUse():Void { // Triggers a hook attempt when an agent dossier is used from within main inventory
	if (!_global.efd.GlitterGone.InventoryHookApplied) {
		var wrapper:Function = function(itemPos:Number):Void {
			arguments.callee.Base.apply(this, arguments);
			if (this.GetItemAt(itemPos).m_ItemTypeGUI == 253188674 &&
				this.GetInventoryID().m_Type == _global.Enums.InvType.e_Type_GC_BackpackContainer) {
				HookUI(true);
			}
		}
		var proto:Object = _global.com.GameInterface.Inventory.prototype; // This one pre-loads
		wrapper.Base = proto.UseItem;
		proto.UseItem = wrapper;
		_global.efd.GlitterGone.InventoryHookApplied = true;
	}
}

var AgentWindow:DistributedValue;