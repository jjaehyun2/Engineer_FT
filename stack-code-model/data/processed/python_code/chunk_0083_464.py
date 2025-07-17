class FireballSpell: Spell
{
	FireballSpell(VertexAndIndexDataType@ VIDT)
	{
        super(VIDT, Icon(Vec2f(96.0f,0.0f), Vec2f(160.0f,64.0f)));
	}
    int getSpellID() override
	{
		return 3;
	}
	bool execute() override
	{
		CBitStream params;
		CPlayer@ player = getLocalPlayer();
		uint16 id = player.getNetworkID();
		params.write_u16(id);
		getRules().SendCommand(getRules().getCommandID("controllableFireball"), params);
		
		return true;
	}
}