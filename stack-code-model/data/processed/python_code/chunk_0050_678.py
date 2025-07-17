/*
	Casual Game Engine: Casual Pixel Warrior
	
	A sample and test game for Casual Game Engine
	
	(C) 2021 - 2022 by Daniel Brendel

	Contact: dbrendel1988<at>gmail<dot>com
	GitHub: https://github.com/danielbrendel/

	Released under the MIT license
*/

#include "headcrabcls.as"
#include "tankcls.as"
#include "teslatowercls.as"

/* Wave point entity */
class CWavePoint : IScriptedEntity
{
	Vector m_vecPos;
	Vector m_vecSize;
	Model m_oModel;
	string m_szTarget;
	size_t m_uiEntCount;
	size_t m_uiWaveCount;
	size_t m_uiCurCount;
	uint32 m_uiWaveDelay;
	Timer m_tmrSpawnWave;
	bool m_bRemove;
	
	CWavePoint()
    {
		this.m_uiCurCount = 0;
		this.m_bRemove = false;
    }
	
	//Set target entity type
	void SetTarget(const string &in szTarget)
	{
		this.m_szTarget = szTarget;
	}
	
	//Set entity spawn count
	void SetEntityCount(size_t uiCount)
	{
		this.m_uiEntCount = uiCount;
	}
	
	//Set wave count
	void SetWaveCount(size_t uiCount)
	{
		this.m_uiWaveCount = uiCount;
	}
	
	//Set wave delay
	void SetWaveDelay(uint32 uiDelay)
	{
		this.m_uiWaveDelay = uiDelay;
	}
	
	//Indicate if all waves are over
	bool AllWavesOver()
	{
		return this.m_uiCurCount >= this.m_uiWaveCount;
	}
	
	//Spawn current wave
	void SpawnWave()
	{
		for (size_t i = 0; i < this.m_uiEntCount; i++) {
			Vector vecSpawnPos = Vector(this.m_vecPos[0] + Util_Random(0, 50) - 25, this.m_vecPos[1] + Util_Random(0, 50) - 25);
			
			if (this.m_szTarget == "headcrab") {
				CHeadcrabEntity@ ent = CHeadcrabEntity();
				Ent_SpawnEntity("headcrab", @ent, vecSpawnPos);
			} else if (this.m_szTarget == "tank") {
				CTankEntity@ ent = CTankEntity();
				Ent_SpawnEntity("tank", @ent, vecSpawnPos);
			} else if (this.m_szTarget == "teslatower") {
				CTeslaTower@ ent = CTeslaTower();
				Ent_SpawnEntity("teslatower", @ent, vecSpawnPos);
			}
		}
	}
	
	//Called when the entity gets spawned. The position in the map is passed as argument
	void OnSpawn(const Vector& in vec)
	{	
		this.m_vecPos = vec;
		this.m_tmrSpawnWave.SetDelay(this.m_uiWaveDelay);
		this.m_tmrSpawnWave.Reset();
		this.m_tmrSpawnWave.SetActive(true);
		this.SpawnWave();
		this.m_oModel.Alloc();
	}
	
	//Called when the entity gets released
	void OnRelease()
	{
	}
	
	//Process entity stuff
	void OnProcess()
	{
		if (this.m_tmrSpawnWave.IsActive()) {
			this.m_tmrSpawnWave.Update();
			if (this.m_tmrSpawnWave.IsElapsed()) {
				this.m_tmrSpawnWave.Reset();
				
				this.m_uiCurCount++;
				if (this.m_uiCurCount >= this.m_uiWaveCount) {
					this.m_tmrSpawnWave.SetActive(false);
					this.m_bRemove = true;
				}
				
				this.SpawnWave();
			}
		}
	}
	
	//Entity can draw everything in default order here
	void OnDraw()
	{
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
		return false;
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
		return "world_wavepoint";
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
			Props_CreateProperty("target", this.m_szTarget) +
			Props_CreateProperty("entcount", formatInt(this.m_uiEntCount)) +
			Props_CreateProperty("wavecount", formatInt(this.m_uiWaveCount)) +
			Props_CreateProperty("wavedelay", formatInt(this.m_uiWaveDelay));
	}
}