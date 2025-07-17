/*
	Casual Game Engine: Casual Pixel Warrior
	
	A sample and test game for Casual Game Engine
	
	(C) 2021 - 2022 by Daniel Brendel

	Contact: dbrendel1988<at>gmail<dot>com
	GitHub: https://github.com/danielbrendel/

	Released under the MIT license
*/

/* Coin item entity */
class CCoinItem : IScriptedEntity
{
	Vector m_vecPos;
	Vector m_vecSize;
	Model m_oModel;
	Timer m_tmrSpriteChange;
	SpriteHandle m_hSprite;
	int m_iSpriteIndex;
	bool m_bRemove;
	SoundHandle m_hCollect;
	
	CCoinItem()
    {
		this.m_vecSize = Vector(40, 43);
		this.m_iSpriteIndex = 0;
		this.m_bRemove = false;
    }
	
	//Called when the entity gets spawned. The position in the map is passed as argument
	void OnSpawn(const Vector& in vec)
	{
		this.m_vecPos = vec;
		this.m_hSprite = R_LoadSprite(GetPackagePath() + "gfx\\coins.png", 4, this.m_vecSize[0], this.m_vecSize[1], 1, false);
		this.m_tmrSpriteChange.SetDelay(200);
		this.m_tmrSpriteChange.Reset();
		this.m_tmrSpriteChange.SetActive(true);
		this.m_hCollect = S_QuerySound(GetPackagePath() + "sound\\coin_collect.wav");
		BoundingBox bbox;
		bbox.Alloc();
		bbox.AddBBoxItem(Vector(0, 0), this.m_vecSize);
		this.m_oModel.Alloc();
		this.m_oModel.Initialize2(bbox, this.m_hSprite);
	}
	
	//Called when the entity gets released
	void OnRelease()
	{
	}
	
	//Process entity stuff
	void OnProcess()
	{
		this.m_tmrSpriteChange.Update();
		if (this.m_tmrSpriteChange.IsElapsed()) {
			this.m_tmrSpriteChange.Reset();
			
			this.m_iSpriteIndex++;
			if (this.m_iSpriteIndex >= 4) {
				this.m_iSpriteIndex = 0;
			}
		}
	}
	
	//Entity can draw everything in default order here
	void OnDraw()
	{
		if (!R_ShouldDraw(this.m_vecPos, this.m_vecSize))
			return;
			
		Vector vOut;
		R_GetDrawingPosition(this.m_vecPos, this.m_vecSize, vOut);
		
		R_DrawSprite(this.m_hSprite, vOut, this.m_iSpriteIndex, 0.0, Vector(-1, -1), 0.0, 0.0, false, Color(0, 0, 0, 0));
	}
	
	//Draw on top
	void OnDrawOnTop()
	{
	}
	
	//Indicate whether this entity shall be removed by the game
	bool NeedsRemoval()
	{
		return this.m_bRemove;
	}
	
	//Indicate if entity can be collided
	bool IsCollidable()
	{
		return true;
	}
	
	//Called when the entity recieves damage
	void OnDamage(uint32 damageValue)
	{
	}
	
	//Called for wall collisions
	void OnWallCollided()
	{
	}
	
	//Called for entity collisions
	void OnCollided(IScriptedEntity@ ref)
	{
		if (ref.GetName() == "player") {
			IPlayerEntity@ player = cast<IPlayerEntity>(ref);
			player.AddPlayerScore(1);
			
			HUD_UpdateCollectable("coins", HUD_GetCollectableCount("coins") + 1);
			
			S_PlaySound(this.m_hCollect, S_GetCurrentVolume());
			
			this.m_bRemove = true;
		}
	}
	
	//Called for accessing the model data for this entity.
	Model& GetModel()
	{
		return this.m_oModel;
	}
	
	//Called for recieving the current position. This is useful if the entity shall move.
	Vector& GetPosition()
	{
		return this.m_vecPos;
	}
	
	//Set position
	void SetPosition(const Vector &in vec)
	{
		this.m_vecPos = vec;
	}
	
	//Return the rotation.
	float GetRotation()
	{
		return 0.0;
	}
	
	//Set rotation
	void SetRotation(float fRot)
	{
	}
	
	//Return a name string here, e.g. the class name or instance name.
	string GetName()
	{
		return "item_coin";
	}
	
	//This vector is used for drawing the selection box
	Vector& GetSize()
	{
		return this.m_vecPos;
	}
	
	//Return save game properties
	string GetSaveGameProperties()
	{
		return Props_CreateProperty("x", formatInt(this.m_vecPos[0])) +
			Props_CreateProperty("y", formatInt(this.m_vecPos[1])) +
			Props_CreateProperty("rot", formatFloat(this.GetRotation()));
	}
}

//Create coin entity
void CreateEntity(const Vector &in vecPos, float fRot, const string &in szIdent, const string &in szPath, const string &in szProps)
{
	CCoinItem @coin = CCoinItem();
	Ent_SpawnEntity(szIdent, @coin, vecPos);
}