import planet_types;
import regions.regions;

tidy class MoonData {
	uint style = 0;
	float size = 0.f;
};

tidy class PlanetScript {
	double tickTimer = randomd(-0.2,0.2);
	array<MoonData@>@ moons;

	void destroy(Planet& planet) {
		planet.destroySurface();
		leaveRegion(planet);
		planet.destroyObjResources();
	}

	bool onOwnerChange(Planet& planet, Empire@ prevOwner) {
		regionOwnerChange(planet, prevOwner);
		return false;
	}

	double tick(Planet& planet, double time) {
		//Update region
		Region@ prevRegion = planet.region;
		if(updateRegion(planet)) {
			planet.changeResourceRegion(prevRegion, planet.region);
			planet.changeSurfaceRegion(prevRegion, planet.region);
			auto@ node = planet.getNode();
			if(node !is null)
				node.hintParentObject(planet.region);
		}

		tickTimer += time;
		if(tickTimer >= 1.f) {
			tickTimer = 0.f;
			planet.updateFleetStrength();
		}

		if(planet.hasMover)
			planet.moverTick(time);
		else
			planet.orbitTick(time);
		planet.resourceTick(time);
		planet.surfaceTick(time);
		planet.constructionTick(time);

		if(planet.hasAbilities)
			planet.abilityTick(time);
		return 0.2;
	}

	// [[ MODIFY BASE GAME START ]]
	void syncShields(Planet& planet, Message& msg) {
		if (msg.readBit()) {
			planet.Shield = msg.read_float();
			planet.MaxShield = msg.read_float();
		} else {
			planet.Shield = 0;
			planet.MaxShield = 0;
		}
	}
	// [[ MODIFY BASE GAME END ]]

	void syncInitial(Planet& planet, Message& msg) {
		//Read planet data
		planet.Health = msg.read_float();
		planet.MaxHealth = msg.read_float();
		// [[ MODIFY BASE GAME START ]]
		syncShields(planet, msg);
		// [[ MODIFY BASE GAME END ]]
		planet.PlanetType = msg.readSmall();
		msg >> planet.renamed;
		msg >> planet.OrbitSize;
		planet.readResources(msg);
		planet.readSurface(msg);
		planet.readOrbit(msg);
		planet.Population = planet.population;

		//Create graphics
		PlanetNode@ plNode = cast<PlanetNode>(bindNode(planet, "PlanetNode"));
		plNode.establish(planet);
		plNode.flags = planet.planetGraphicsFlags;

		planet.readLeaderAI(msg);
		planet.readStatuses(msg);
		planet.readCargo(msg);

		if(msg.readBit()) {
			if(!planet.hasAbilities)
				planet.activateAbilities();
			planet.readAbilities(msg);
		}

		uint ringStyle = 0;
		if(msg.readBit())
			msg >> ringStyle;

		if(plNode !is null) {
			plNode.planetType = planet.PlanetType;
			plNode.colonized = planet.owner.valid;
			if(ringStyle != 0)
				plNode.addRing(ringStyle);
			plNode.hintParentObject(planet.region);
		}

		if(msg.readBit()) {
			if(!planet.hasMover)
				planet.activateMover();
			planet.readMover(msg);
		}

		if(msg.readBit()) {
			if(moons is null)
				@moons = array<MoonData@>();

			moons.length = msg.readSmall();
			for(uint i = 0, cnt = moons.length; i < cnt; ++i) {
				MoonData dat;
				msg >> dat.size;
				msg >> dat.style;
				@moons[i] = dat;

				if(plNode !is null)
					plNode.addMoon(dat.size, dat.style);
			}
		}

		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			planet.allowPathlessImport = 1;
		} else {
			planet.allowPathlessImport = 0;
		}
		// [[ MODIFY BASE GAME END ]]
	}

	void syncDelta(Planet& planet, Message& msg, double tDiff) {
		if(msg.readBit())
			planet.readResourceDelta(msg);
		if(msg.readBit()) {
			planet.readSurfaceDelta(msg);
			planet.Population = planet.population;
		}
		if(msg.readBit())
			planet.readConstructionDelta(msg);
		if(msg.readBit())
			planet.readLeaderAIDelta(msg);
		if(msg.readBit()) {
			if(!planet.hasAbilities)
				planet.activateAbilities();
			planet.readAbilityDelta(msg);
		}
		if(msg.readBit())
			planet.readStatusDelta(msg);
		if(msg.readBit())
			planet.readCargoDelta(msg);
		if(msg.readBit()) {
			planet.Health = msg.read_float();
			planet.MaxHealth = msg.read_float();
		}
		// [[ MODIFY BASE GAME START ]]
		if(msg.readBit()) {
			syncShields(planet, msg);
		}
		// [[ MODIFY BASE GAME END ]]
		if(msg.readBit()) {
			if(!planet.hasMover)
				planet.activateMover();
			planet.readMoverDelta(msg);
		}
		if(msg.readBit())
			planet.readOrbitDelta(msg);

		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			planet.allowPathlessImport = 1;
		} else {
			planet.allowPathlessImport = 0;
		}
		// [[ MODIFY BASE GAME END ]]
	}

	void syncDetailed(Planet& planet, Message& msg, double tDiff) {
		planet.Health = msg.read_float();
		planet.MaxHealth = msg.read_float();
		// [[ MODIFY BASE GAME START ]]
		syncShields(planet, msg);
		// [[ MODIFY BASE GAME END ]]
		planet.readResources(msg);
		planet.readSurface(msg);
		planet.readConstruction(msg);
		planet.readStatuses(msg);
		planet.readCargo(msg);
		if(msg.readBit()) {
			if(!planet.hasAbilities)
				planet.activateAbilities();
			planet.readAbilities(msg);
		}
		planet.Population = planet.population;

		if(msg.readBit()) {
			if(!planet.hasMover)
				planet.activateMover();
			planet.readMover(msg);
		}

		// [[ MODIFY BASE GAME START ]]
		if (msg.readBit()) {
			planet.allowPathlessImport = 1;
		} else {
			planet.allowPathlessImport = 0;
		}
		// [[ MODIFY BASE GAME END ]]
	}

	// [[ MODIFY BASE GAME START ]]
	double get_shield(const Planet& planet) {
		double value = planet.Shield;
		if (planet.owner !is null) {
			return value * planet.owner.PlanetShieldProjectorFactor;
		} else {
			return value;
		}
	}

	double get_maxShield(const Planet& planet) {
		double value = planet.MaxShield;
		if (planet.owner !is null) {
			return value * planet.owner.PlanetShieldProjectorFactor;
		} else {
			return value;
		}
	}
	// [[ MODIFY BASE GAME END ]]

	uint get_moonCount() {
		if(moons is null)
			return 0;
		return moons.length;
	}
};