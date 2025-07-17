/*
	Casual Game Engine: Casual Pixel Warrior
	
	A sample and test game for Casual Game Engine
	
	(C) 2021 - 2022 by Daniel Brendel

	Contact: dbrendel1988<at>gmail<dot>com
	GitHub: https://github.com/danielbrendel/

	Released under the MIT license
*/

#include "blooddecal.as"

const float C_HEADCRAB_DEFAULT_SPEED = 350;
const int C_HEADCRAB_REACT_RANGE = 500;
const int C_HEADGRAB_ATTACK_RANGE = 50;
const uint C_HEADGRAB_DAMAGE_VALUE = 5;

/* Headcrab entity */
class CHeadcrabEntity : IScriptedEntity
{
	Vector m_vecPos;
	Vector m_vecSize;
	Model m_oModel;
	SpriteHandle m_hSprite;
	float m_fRotation;
	uint32 m_uiHealth;
	Timer m_tmrMovement;
	Timer m_tmrDirChange;
	Timer m_tmrEnemyCheck;
	Timer m_tmrShaking;
	Timer m_tmrWalkSound;
	Timer m_tmrAttack;
	Timer m_tmrFlicker;
	bool m_bGotEnemy;
	float m_fShakeRot;
	float m_fSpeed;
	uint m_uiFlickerCount;
	SoundHandle m_hWalkSound;
	SoundHandle m_hPainSound;
	SoundHandle m_hAttackSound;
	
	void LookAt(const Vector &in vPos)
	{
		//Look at position
		float flAngle = atan2(float(vPos[1] - this.m_vecPos[1]), float(vPos[0] - this.m_vecPos[0]));
		this.m_fRotation = flAngle + 6.30 / 4;
	}
	
	void CheckForEnemiesInRange()
	{
		//Check for enemies in close range and act accordingly
		
		this.m_bGotEnemy = false;
		IScriptedEntity@ pEntity = null;
		
		for (size_t i = 0; i < Ent_GetEntityCount(); i++) {
			@pEntity = @Ent_GetEntityHandle(i);
			if ((@pEntity != null) && (pEntity.GetName() == "player")) {
				if (this.m_vecPos.Distance(pEntity.GetPosition()) <= C_HEADCRAB_REACT_RANGE) {
					this.m_bGotEnemy = true;
					break;
				}
			}
		}
		
		if (this.m_bGotEnemy) {
			if (this.m_fSpeed == C_HEADCRAB_DEFAULT_SPEED)
				this.m_fSpeed *= 2;
				
			if (pEntity.GetName().length() > 0) {
				this.LookAt(pEntity.GetPosition());
			}

			if (this.m_vecPos.Distance(pEntity.GetPosition()) <= C_HEADGRAB_ATTACK_RANGE) {
				this.m_tmrAttack.Update();
				if (this.m_tmrAttack.IsElapsed()) {
					pEntity.OnDamage(C_HEADGRAB_DAMAGE_VALUE);
					S_PlaySound(this.m_hAttackSound, S_GetCurrentVolume());
					this.m_tmrAttack.Reset();
				}
			}
		} else {
			if (this.m_fSpeed != C_HEADCRAB_DEFAULT_SPEED)
				this.m_fSpeed = C_HEADCRAB_DEFAULT_SPEED;
		}
	}
	
	CHeadcrabEntity()
    {
		this.m_uiHealth = 50;
		this.m_vecSize = Vector(59, 52);
		this.m_uiFlickerCount = 0;
    }
	
	//Called when the entity gets spawned. The position in the map is passed as argument
	void OnSpawn(const Vector& in vec)
	{
		this.m_vecPos = vec;
		this.m_fRotation = 0.0f;
		this.m_hSprite = R_LoadSprite(GetPackagePath() + "gfx\\headcrab.png", 1, 32, 32, 1, true);
		this.m_tmrMovement.SetDelay(100);
		this.m_tmrMovement.Reset();
		this.m_tmrMovement.SetActive(true);
		this.m_tmrDirChange.SetDelay(5000);
		this.m_tmrDirChange.Reset();
		this.m_tmrDirChange.SetActive(true);
		this.m_tmrEnemyCheck.SetDelay(1);
		this.m_tmrEnemyCheck.Reset();
		this.m_tmrEnemyCheck.SetActive(true);
		this.m_tmrShaking.SetDelay(1000);
		this.m_tmrShaking.Reset();
		this.m_tmrShaking.SetActive(true);
		this.m_tmrWalkSound.SetDelay(1000 + Util_Random(1, 2000));
		this.m_tmrWalkSound.Reset();
		this.m_tmrWalkSound.SetActive(true);
		this.m_tmrAttack.SetDelay(1000);
		this.m_tmrAttack.Reset();
		this.m_tmrAttack.SetActive(true);
		this.m_tmrFlicker.SetDelay(250);
		this.m_tmrFlicker.Reset();
		this.m_tmrFlicker.SetActive(false);
		this.m_hWalkSound = S_QuerySound(GetPackagePath() + "sound\\hc_walk.wav");
		this.m_hPainSound = S_QuerySound(GetPackagePath() + "sound\\hc_hurt.wav");
		this.m_hAttackSound = S_QuerySound(GetPackagePath() + "sound\\hc_attack.wav");
		BoundingBox bbox;
		bbox.Alloc();
		bbox.AddBBoxItem(Vector(0, 0), this.m_vecSize);
		this.m_oModel.Alloc();
		this.m_oModel.Initialize2(bbox, this.m_hSprite);
	}
	
	//Called when the entity gets released
	void OnRelease()
	{
		CBloodSplash @obj = CBloodSplash();
		Ent_SpawnEntity("blooddecal", @obj, this.m_vecPos);
		
		SoundHandle hSplash = S_QuerySound(GetPackagePath() + "sound\\hc_splash.wav");
		S_PlaySound(hSplash, S_GetCurrentVolume());
	}
	
	//Process entity stuff
	void OnProcess()
	{
		this.m_tmrShaking.Update();
		if (this.m_tmrShaking.IsElapsed()) {
			if (!this.m_bGotEnemy)
				this.m_fShakeRot = -0.25 + float(Util_Random(1, 5)) / 10.0;
		}
		
		this.m_tmrDirChange.Update();
		if (this.m_tmrDirChange.IsElapsed()) {
			this.m_tmrDirChange.Reset();
			if (!this.m_bGotEnemy)
				this.m_fRotation = float(Util_Random(1, 360));
		}
		
		this.m_tmrWalkSound.Update();
		if (this.m_tmrWalkSound.IsElapsed()) {
			this.m_tmrWalkSound.Reset();
			S_PlaySound(this.m_hWalkSound, 8);
		}
		
		this.CheckForEnemiesInRange();
		
		this.m_tmrMovement.Update();
		if (this.m_tmrMovement.IsElapsed()) {
			this.m_tmrMovement.Reset();
			
			Ent_Move(this, this.m_fSpeed, MOVE_FORWARD);
		}
		
		if (this.m_tmrFlicker.IsActive()) {
			this.m_tmrFlicker.Update();
			if (this.m_tmrFlicker.IsElapsed()) {
				this.m_tmrFlicker.Reset();
				
				this.m_uiFlickerCount++;
				if (this.m_uiFlickerCount >= 6) {
					this.m_tmrFlicker.SetActive(false);
					this.m_uiFlickerCount = 0;
				}
			}
		}
	}
	
	//Entity can draw everything in default order here
	void OnDraw()
	{
	}
	
	//Entity can draw on-top stuff here
	void OnDrawOnTop()
	{
		if (!R_ShouldDraw(this.m_vecPos, this.m_vecSize))
			return;
			
		Vector vOut;
		R_GetDrawingPosition(this.m_vecPos, this.m_vecSize, vOut);
		
		Color sDrawingColor = (this.m_tmrFlicker.IsActive()) ? Color(255, 0, 0, 150) : Color(0, 0, 0, 0);
		bool bCustomColor = (this.m_tmrFlicker.IsActive()) && (this.m_uiFlickerCount % 2 == 0);
		
		R_DrawSprite(this.m_hSprite, vOut, 0, this.m_fRotation, Vector(-1, -1), 0.0, 0.0, bCustomColor, sDrawingColor);
	}
	
	//Indicate whether this entity shall be removed by the game
	bool NeedsRemoval()
	{
		return this.m_uiHealth == 0;
	}
	
	//Indicate whether this entity is collidable
	bool IsCollidable()
	{
		return true;
	}
	
	//Called when the entity collided with another entity
	void OnCollided(IScriptedEntity@ ref)
	{
	}
	
	//Called when entity gets damaged
	void OnDamage(uint32 damageValue)
	{
		if (this.m_uiHealth < damageValue) {
			this.m_uiHealth = 0;
		} else {
			this.m_uiHealth -= damageValue;
		}
		
		this.m_tmrFlicker.Reset();
		this.m_tmrFlicker.SetActive(true);
		this.m_uiFlickerCount = 0;
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
	
	//Set new position
	void SetPosition(const Vector &in vecPos)
	{
		this.m_vecPos = vecPos;
	}
	
	//This vector is used for getting the overall drawing size
	Vector& GetSize()
	{
		return this.m_vecSize;
	}
	
	//Return the rotation.
	float GetRotation()
	{
		return this.m_fRotation;
	}
	
	//Set new rotation
	void SetRotation(float fRot)
	{
		this.m_fRotation = fRot;
	}
	
	//Return a name string here, e.g. the class name or instance name.
	string GetName()
	{
		return "headcrab";
	}
	
	//Called for wall collisions
	void OnWallCollided()
	{
	}
	
	//Return save game properties
	string GetSaveGameProperties()
	{
		return Props_CreateProperty("id", formatInt(Ent_GetId(@this))) +
				Props_CreateProperty("x", formatInt(this.m_vecPos[0])) +
				Props_CreateProperty("y", formatInt(this.m_vecPos[1])) +
				Props_CreateProperty("rot", formatFloat(this.m_fRotation)) +
				Props_CreateProperty("health", formatInt(this.m_uiHealth));
	}
}