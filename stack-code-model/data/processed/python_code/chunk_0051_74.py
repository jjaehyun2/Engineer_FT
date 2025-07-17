class Accelerometer : ZUtil::IHandleCpEvents
{
	protected BarHud@ _barHud;
	protected GraphHud@ _graphHud;

	protected ZUtil::CpDataManager@ _cpManager;

	protected bool is_ingame = false;
	protected bool is_respawn = true;

	void OnSettingsChanged()
	{
		_barHud.OnSettingsChanged();
		_graphHud.OnSettingsChanged();
	}

	void OnCPNewTimeEvent(int i, int t){
		if (_graphHud is null) return;
		print (i + " : " + Time::Format(t));
	}

	void OnCpTimesCountChangeEvent(int i){
		if (_graphHud is null) return;
	}

	Accelerometer()
	{
		print("Accelerometer ctor");
		protected @_barHud = BarHud();
		protected @_graphHud = GraphHud();

		protected @_cpManager = ZUtil::CpDataManager(this);
	}
protected 
	protected bool InGameCheck(CGameCtnApp@ app){
		CSmArenaClient@ playground = cast<CSmArenaClient>(app.CurrentPlayground);
		if(playground is null) return;
		if(playground.GameTerminals.Length <= 0
			|| cast<CSmPlayer>(playground.GameTerminals[0].GUIPlayer) is null
			|| playground.Arena is null
			|| playground.Map is null) 
		{
			return false;
		}
		return true;	
	}

	void Update(float dt)
	{
		CGameCtnApp@ app = GetApp();
		is_ingame = InGameCheck(app);
		if(is_ingame) return;

		auto player = Util::GetViewingPlayer();
		if (player is null) return;
protected 
protected 		// print("viewingPlayer:" + player.User.Name);

protected 		_cpManager.Update(player);

		protected // if(playground.GameTerminals.Length > 0 && is_ingame) 
		protected // {					
		// 	auto sceneVis = app.GameScene;
		// 	if (sceneVis is null) return;		

		// 	CSceneVehicleVis@ vis = null;		
		// 	CGameCtnChallenge@ map = app.RootMap;

		// 	if (player !is null)
		// 		@vis = Vehicle::GetVis(sceneVis, player);
		// 	else 
		// 		@vis = Vehicle::GetSingularVis(sceneVis);
			
		// 	if (vis is null) return;


		// 	if (Setting_General_ShowHud) {
		// 		_barHud.Update(dt, vis.AsyncState);
		// 	}
		// 	if (Setting_General_ShowGraph){
		// 		_graphHud.Update(dt, vis.AsyncState);
		// 	}
		// }
	}

	void Render()
	{
// 		auto app = GetApp();

		// Interface hidden
		// if (Setting_General_HideOnHiddenInterface) {
		// 	if (app.CurrentPlayground !is null && app.CurrentPlayground.Interface !is null) {
		// 		if (Dev::GetOffsetUint32(app.CurrentPlayground.Interface, 0x1C) == 0) {
		// 			return;
		// 		}
		// 	}
		// }
		

		// auto player = Util::GetViewingPlayer();
		// if (player !is null) {
		// 	@vis = Vehicle::GetVis(sceneVis, player);
		// } else {
		// 	@vis = Vehicle::GetSingularVis(sceneVis);
		// }


// #if TMNEXT
// 		uint entityId = Vehicle::GetEntityId(vis);
// 		if ((entityId & 0xFF000000) == 0x04000000) {
// 			// If the entity ID has this mask, then we are either watching a replay, or placing
// 			// down the car in the editor. So, we will check if we are currently in the editor,
// 			// and stop if we are.
// 			if (cast<CGameCtnEditorFree>(app.Editor) !is null) {
// 				return;
// 			}
// 		}
// #endif
// 		if (Setting_General_ShowHud) {
// 			_barHud.m_pos = Setting_General_HudPos;
// 			_barHud.m_size = Setting_General_HudSize;
// 			_barHud.InternalRender();
// 		}
		
// 		if (Setting_General_ShowGraph) {
// 			_graphHud.m_pos = Setting_General_GraphPos;
// 			_graphHud.m_size = Setting_General_GraphSize;
// 			_graphHud.InternalRender();
// 		}
	
	}
}