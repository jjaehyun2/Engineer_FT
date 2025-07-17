import regions.regions;
from designs import getDesignMesh;

tidy class ShipScript {
	float commandUsed = 0.f;

	float timer = 1.f;

	bool hasGraphics = false;

	bool get_isStation(Ship& ship) {
		return ship.blueprint.design.hasTag(ST_Station);
	}

	// Computes the mass of the ship factoring in the empire mass factor
	void computeMass(Ship& ship) {
		const Design@ dsg = ship.blueprint.design;
		if (ship.owner !is null) {
			double mass = dsg.total(HV_Mass) * ship.owner.EmpireMassFactor;
			// increase mass by support capacity mass factor, in
			// proportion to the amount of support capacity on the ship
			double bonusMass = dsg.total(HV_SupportCapacityMass) * ship.owner.EmpireMassFactor;
			mass += bonusMass * max(ship.owner.EmpireSupportCapacityMassFactor - 1.0, 0.0);
			// also increase mass by repair mass factor, in proportion
			// to the amount of repair on the ship
			double repairBonusMass = dsg.total(HV_RepairMass) * ship.owner.EmpireMassFactor;
			mass += repairBonusMass * max(ship.owner.EmpireRepairMassFactor - 1.0, 0.0);
			ship.Mass = mass;
		} else {
			ship.Mass = dsg.total(HV_Mass);
		}
	}

	void occasional_tick(Ship& ship, float time) {
		// [[ MODIFY BASE GAME START ]]
		// Moving updateRegion here since this now does more
		Region@ reg = ship.region;
		// [[ MODIFY BASE GAME END ]]
		if(updateRegion(ship)) {
			auto@ node = ship.getNode();
			if(node !is null)
				node.hintParentObject(ship.region);
		}
		// [[ MODIFY BASE GAME START ]]
		if (ship.hasResources) {
			ship.changeResourceRegion(reg, ship.region);
		}
		// [[ MODIFY BASE GAME END ]]

		if(ship.hasLeaderAI)
			ship.updateFleetStrength();

		// [[ MODIFY BASE GAME START ]]
		computeMass(ship);
		// [[ MODIFY BASE GAME END ]]
	}

	double tick(Ship& ship, double time) {
		// [[ MODIFY BASE GAME START ]]
		// updateRegion was part of occasional_tick in server Ship.as?
		// [[ MODIFY BASE GAME END ]]

		ship.moverTick(time);
		if(ship.hasLeaderAI)
			ship.leaderTick(time);

		// [[ MODIFY BASE GAME START ]]
		if (!ship.hasSupportAI) {
			if (ship.hasResources)
				ship.resourceTick(time);
		}
		// [[ MODIFY BASE GAME END ]]

		timer += float(time);
		if(timer >= 1.f) {
			occasional_tick(ship, timer);
			timer = 0.f;
		}
		return 0.2;
	}

	void destroy(Ship& ship) {
		if(ship.inCombat) {
			auto@ region = ship.region;
			if(region !is null) {
				uint debris = uint(log(ship.blueprint.design.size) / log(2.0));
				if(debris > 0)
					region.addShipDebris(ship.position, debris);
			}
		}

		leaveRegion(ship);
		if(ship.hasLeaderAI)
			ship.leaderDestroy();
		// [[ MODIFY BASE GAME START ]]
		if (ship.hasResources)
			ship.destroyObjResources();
		// [[ MODIFY BASE GAME END ]]
	}

	bool onOwnerChange(Ship& ship, Empire@ prevOwner) {
		regionOwnerChange(ship, prevOwner);
		if(ship.hasLeaderAI)
			ship.leaderChangeOwner(prevOwner, ship.owner);
		// [[ MODIFY BASE GAME START ]]
		if (ship.hasResources)
			ship.changeResourceOwner(prevOwner);
		// [[ MODIFY BASE GAME END ]]
		return false;
	}

	void createGraphics(Ship& ship, const Design@ dsg) {
		if(dsg is null)
			return;
		MeshDesc shipMesh;
		getDesignMesh(ship.owner, ship.blueprint.design, shipMesh);
		shipMesh.memorable = ship.memorable;
		bindMesh(ship, shipMesh);
		hasGraphics = true;
		if(ship.hasLeaderAI) {
			auto@ node = ship.getNode();
			if(node !is null)
				node.animInvis = true;
		}
	}

	void syncInitial(Ship& ship, Message& msg) {
		//Find hull
		uint hullID = msg.readSmall();

		const Hull@ hull = getHullDefinition(hullID);

		//Sync data
		ship.blueprint.recvDetails(ship, msg);

		if(msg.readBit()) {
			ship.activateLeaderAI();
			ship.leaderInit();
			ship.readLeaderAI(msg);
			auto@ node = ship.getNode();
			if(node !is null)
				node.animInvis = true;
		}
		else {
			ship.activateSupportAI();
			ship.readSupportAI(msg);
		}

		ship.readMover(msg);
		if(msg.readBit()) {
			msg >> ship.MaxEnergy;
			ship.Energy = msg.readFixed(0.f, ship.MaxEnergy, 16);
		}
		if(msg.readBit()) {
			msg >> ship.MaxSupply;
			ship.Supply = msg.readFixed(0.f, ship.MaxSupply, 16);
		}
		if(msg.readBit()) {
			msg >> ship.MaxShield;
			ship.Shield = msg.readFixed(0.f, ship.MaxShield, 16);
		}

		if(msg.readBit()) {
			ship.activateAbilities();
			ship.readAbilities(msg);
		}

		if(msg.readBit()) {
			ship.activateStatuses();
			ship.readStatuses(msg);
		}

		if(msg.readBit()) {
			ship.activateCargo();
			ship.readCargo(msg);
		}

		if(msg.readBit()) {
			ship.activateConstruction();
			ship.readConstruction(msg);
		}

		if(msg.readBit()) {
			ship.activateOrbit();
			ship.readOrbit(msg);
		}

		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			ship.activateResources();
			ship.readResources(msg);
		}
		// [[ MODIFY BASE GAME END ]]

		// [[ MODIFY BASE GAME START ]]
		// Sync bonus mass (shadow can infer mass from design + empire)
		if (msg.readBit()) {
			msg >> ship.BonusMass;
		} else {
			ship.BonusMass = 0.0;
		}
		// [[ MODIFY BASE GAME END ]]

		createGraphics(ship, ship.blueprint.design);
	}

	void syncDetailed(Ship& ship, Message& msg, double tDiff) {
		ship.readMover(msg);
		if(ship.hasLeaderAI)
			ship.readLeaderAI(msg);
		else
			ship.readSupportAI(msg);
		ship.blueprint.recvDetails(ship, msg);
		updateStats(ship);
		msg >> ship.Energy;
		msg >> ship.MaxEnergy;
		msg >> ship.Supply;
		msg >> ship.MaxSupply;
		msg >> ship.Shield;
		msg >> ship.MaxShield;
		ship.isFTLing = msg.readBit();
		ship.inCombat = msg.readBit();
		if(ship.hasAbilities)
			ship.readAbilities(msg);
		if(ship.hasStatuses)
			ship.readStatuses(msg);
		if(msg.readBit()) {
			if(!ship.hasCargo)
				ship.activateCargo();
			ship.readCargo(msg);
		}
		if(msg.readBit()) {
			if(!ship.hasOrbit)
				ship.activateOrbit();
			ship.readOrbit(msg);
		}
		if(msg.readBit()) {
			if(!ship.hasConstruction)
				ship.activateConstruction();
			ship.readConstruction(msg);
		}
		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			if (!ship.hasResources)
				ship.activateResources();
			ship.readResources(msg);
		}
		// [[ MODIFY BASE GAME END ]]

		// [[ MODIFY BASE GAME START ]]
		// Sync bonus mass (shadow can infer mass from design + empire)
		if (msg.readBit()) {
			msg >> ship.BonusMass;
		} else {
			ship.BonusMass = 0.0;
		}
		// [[ MODIFY BASE GAME END ]]
	}

	void updateStats(Ship& ship) {
		const Design@ dsg = ship.blueprint.design;
		if(dsg is null)
			return;

		ship.DPS = ship.blueprint.getEfficiencySum(SV_DPS);
		ship.MaxDPS = dsg.total(SV_DPS);
		ship.MaxSupply = dsg.total(SV_SupplyCapacity);
		ship.MaxShield = dsg.total(SV_ShieldCapacity);
		// [[ MODIFY BASE GAME START ]]
		computeMass(ship);
		// [[ MODIFY BASE GAME END ]]
		commandUsed = dsg.variable(ShV_REQUIRES_Command);
	}

	void syncDelta(Ship& ship, Message& msg, double tDiff) {
		if(msg.readBit())
			ship.readMoverDelta(msg);
		if(msg.readBit()) {
			ship.blueprint.recvDelta(ship, msg);
			if(!hasGraphics)
				createGraphics(ship, ship.blueprint.design);
			updateStats(ship);
		}

		if(msg.readBit())
			ship.Shield = msg.readFixed(0.f, ship.MaxShield, 16);

		if(msg.readBit()) {
			if(ship.hasLeaderAI)
				ship.readLeaderAIDelta(msg);
			else
				ship.readSupportAIDelta(msg);
		}
		if(ship.hasAbilities) {
			if(msg.readBit())
				ship.readAbilityDelta(msg);
		}
		if(ship.hasStatuses) {
			if(msg.readBit())
				ship.readStatusDelta(msg);
		}
		if(ship.hasLeaderAI) {
			if(msg.readBit()) {
				if(!ship.hasCargo)
					ship.activateCargo();
				ship.readCargoDelta(msg);
			}
		}
		if(msg.readBit()) {
			if(msg.readBit())
				msg >> ship.Energy;
			else
				ship.Energy = 0;
			if(msg.readBit())
				msg >> ship.Supply;
			else
				ship.Supply = 0;

			ship.isFTLing = msg.readBit();
			ship.inCombat = msg.readBit();
		}
		if(msg.readBit()) {
			if(!ship.hasOrbit)
				ship.activateOrbit();
			ship.readOrbitDelta(msg);
		}
		if(ship.hasLeaderAI) {
			if(msg.readBit()) {
				if(!ship.hasConstruction)
					ship.activateConstruction();
				ship.readConstructionDelta(msg);
			}
		}

		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			if (!ship.hasResources)
				ship.activateResources();
			ship.readResourceDelta(msg);
		}
		// [[ MODIFY BASE GAME END ]]

		// [[ MODIFY BASE GAME START ]]
		// Sync bonus mass (shadow can infer mass from design + empire)
		if (msg.readBit()) {
			msg >> ship.BonusMass;
		} else {
			ship.BonusMass = 0.0;
		}
		// [[ MODIFY BASE GAME END ]]
	}
};