class SpongeXplosionSpell: Spell
{
	SpongeXplosionSpell(VertexAndIndexDataType@ VIDT)
	{
        super(VIDT, Icon(Vec2f(32.0f,0.0f), Vec2f(96.0f,64.0f)));
	}
    int getSpellID() override
	{
		return 2;
	}
	bool execute() override
	{

		CBitStream params;
		CPlayer@ player = getLocalPlayer();
		uint16 id = player.getNetworkID();
		params.write_u16(id);
		getRules().SendCommand(getRules().getCommandID("spongeExplosion"), params);
		return true;
	}
}