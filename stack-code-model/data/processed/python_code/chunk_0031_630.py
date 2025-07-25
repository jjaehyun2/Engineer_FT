#include "PhysicsObject.as"

shared class Flag : PhysicsObject, IRenderable, IHasTeam, IHasConfig
{
	private Model@ model;
	private u8 team;

	Flag(Vec3f position, u8 team)
	{
		super(position);
		LoadConfig(openConfig("Flag.cfg"));

		SetTeamNum(team);

		SetCollisionBox(AABB(Vec3f(0.6f, 1.6f, 0.6f)));
		SetCollisionFlags(CollisionFlag::Blocks);
	}

	Flag(CBitStream@ bs)
	{
		super(bs);
		LoadConfig(openConfig("Flag.cfg"));

		SetTeamNum(bs.read_u8());

		SetCollisionBox(AABB(Vec3f(0.6f, 1.6f, 0.6f)));
		SetCollisionFlags(CollisionFlag::Blocks);
	}

	bool opEquals(Flag flag)
	{
		return opEquals(cast<PhysicsObject>(flag));
	}

	void opAssign(Flag flag)
	{
		opAssign(cast<PhysicsObject>(flag));
		team = flag.team;
	}

	bool isVisible()
	{
		return true;//model !is null;
	}

	void Render()
	{
		AABB@ collisionBox = getCollisionBox();
		if (collisionBox !is null)
		{
			collisionBox.Render(interPosition);
		}

		// model.Render(this);
	}

	u8 getTeamNum()
	{
		return team;
	}

	void SetTeamNum(u8 team)
	{
		this.team = team;
	}

	void Serialize(CBitStream@ bs)
	{
		PhysicsObject::Serialize(bs);
		bs.write_u8(team);
	}

	void LoadConfig(ConfigFile@ cfg)
	{
		PhysicsObject::LoadConfig(cfg);
	}
}