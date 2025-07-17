/*
	Casual Game Engine: Solitarius
	
	A top-down 2D singleplayer space wave shooter
	
	(C) 2021 - 2022 by Daniel Brendel

	Contact: dbrendel1988<at>gmail<dot>com
	GitHub: https://github.com/danielbrendel/

	Released under the MIT license
*/

#include "decal.as"

/* Explosion entity */
const uint C_DEFAULT_GRENADE_DAMAGE = 20;
class CExplosionEntity : IScriptedEntity
{
	Vector m_vecPos;
	Vector m_vecSize;
	Model m_oModel;
	Timer m_oExplosion;
	int m_iFrameCount;
	SpriteHandle m_hSprite;
	SoundHandle m_hSound;
	bool m_bDamageAble;
	uint m_uiDamage;
	IScriptedEntity@ m_pOwner;
	
	CExplosionEntity()
    {
		this.m_vecSize = Vector(32, 32);
		this.m_iFrameCount = 0;
		this.m_bDamageAble = false;
		@this.m_pOwner = null;
    }
	
	//Set damageable data
	void SetDamageable(bool flag, uint damage = C_DEFAULT_GRENADE_DAMAGE)
	{
		this.m_bDamageAble = flag;
		this.m_uiDamage = damage;
	}
	
	//Set owner
	void SetOwner(IScriptedEntity@ pOwner)
	{
		@this.m_pOwner = pOwner;
	}
	
	//Called when the entity gets spawned. The position in the map is passed as argument
	void OnSpawn(const Vector& in vec)
	{
		this.m_vecPos = vec;
		this.m_hSprite = R_LoadSprite(GetPackagePath() + "gfx\\explosion.png", 6, this.m_vecSize[0], this.m_vecSize[1], 6, false);
		this.m_oExplosion.SetDelay(100);
		this.m_oExplosion.Reset();
		this.m_oExplosion.SetActive(true);
		this.m_hSound = S_QuerySound(GetPackagePath() + "sound\\explosion.wav");
		S_PlaySound(this.m_hSound, S_GetCurrentVolume());
		CDecalEntity @dcl = CDecalEntity();
		Ent_SpawnEntity("decal", @dcl, this.m_vecPos);
		BoundingBox bbox;
		bbox.Alloc();
		bbox.AddBBoxItem(Vector(15, 15), Vector(100, 100));
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
		this.m_oExplosion.Update();
		if (this.m_oExplosion.IsElapsed()) {
			this.m_oExplosion.Reset();
			this.m_iFrameCount++;
		}
	}
	
	//Entity can draw everything in default order here
	void OnDraw()
	{
	}
	
	//Entity can draw everything on top here
	void OnDrawOnTop()
	{
		if (!R_ShouldDraw(this.m_vecPos, this.m_vecSize))
			return;
			
		Vector vOut;
		R_GetDrawingPosition(this.m_vecPos, this.m_vecSize, vOut);
		
		R_DrawSprite(this.m_hSprite, vOut, this.m_iFrameCount, 0.0, Vector(-1, -1), 2.0, 2.0, false, Color(0, 0, 0, 0));
	}
	
	//Indicate whether this entity shall be removed by the game
	bool NeedsRemoval()
	{
		return this.m_iFrameCount >= 6;
	}
	
	//Indicate if entity can be collided
	bool IsCollidable()
	{
		return this.m_bDamageAble;
	}
	
	//Indicate if entity can be dormant
	bool CanBeDormant()
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
		if (@this.m_pOwner != null) {
			if (@ref == @this.m_pOwner) {
				return;
			}
		}
		
		ref.OnDamage(this.m_uiDamage);
		
		if (ref.NeedsRemoval()) {
			if (@this.m_pOwner == @Ent_GetPlayerEntity()) {
				IPlayerEntity@ casted = cast<IPlayerEntity>(this.m_pOwner);
				
				if (ref.GetName() == "headcrab") {
					casted.AddPlayerScore(1);
				} else if (ref.GetName() == "tank") {
					casted.AddPlayerScore(3);
				} else if (ref.GetName() == "teslatower") {
					casted.AddPlayerScore(2);
				} else {
					casted.AddPlayerScore(1);
				}
			}
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
		return "explosion";
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