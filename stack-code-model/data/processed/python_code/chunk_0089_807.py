import orders.Order;
import systems;
import regions.regions;
import ftl;

tidy class AutoExploreOrder : Order {
	Region@ dest;
	bool ftl = false;
	// introduce a flag for when we run out of regions that
	// we've never seen so we can start maintaining vision instead
	// rather than stopping exploration
	bool switchedToMaintainingVision = false;
	set_int inner;
	array<int> edge;
	uint scoutMask = 0;

	AutoExploreOrder(bool useFTL) {
		ftl = useFTL;
	}

	AutoExploreOrder(SaveFile& msg) {
		Order::load(msg);
		msg >> dest;
		msg >> ftl;
		msg >> switchedToMaintainingVision;
	}

	~AutoExploreOrder() {
		if(dest !is null)
			dest.ScoutingMask &= ~scoutMask;
	}

	void destroy() override {
		if(dest !is null) {
			dest.ScoutingMask &= ~scoutMask;
			@dest = null;
		}
	}

	void save(SaveFile& msg) {
		Order::save(msg);
		msg << dest;
		msg << ftl;
		msg << switchedToMaintainingVision;
	}

	OrderType get_type() {
		return OT_AutoExplore;
	}

	string get_name() {
		return "Automically Exploring";
	}

	bool get_hasMovement() {
		return false;
	}

	vec3d getMoveDestination(const Object& obj) override {
		return obj.position;
	}

	void doMoveTo(Object& obj, Region@ to) {
		if(to !is null) {
			scoutMask = obj.owner.mask;
			uint prevMask = (to.ScoutingMask |= scoutMask);
			if(prevMask & scoutMask != 0) {
				//print("Skipped guard on scouting mask");
				//doMoveTo(obj, null);
				//return;
			}

			vec3d pt = to.position + (obj.position - to.position).normalize(to.OuterRadius - 100.0);

			bool moved = false;
			if(ftl && obj.isShip) {
				Empire@ owner = obj.owner;
				if(canHyperdrive(obj)) {
					double cost = hyperdriveCost(obj, pt);
					//Hyperdrive if at least half the empire's ftl capacity will be left
					if((owner.FTLStored - cost) / owner.FTLCapacity >= 0.5) {
						obj.insertHyperdriveOrder(pt, getIndex());
						moved = true;
					}
				}

				if(!moved && canJumpdrive(obj)) {
					double cost = jumpdriveCost(obj, pt);
					double range = jumpdriveRange(obj);
					double dist = obj.position.distanceTo(pt);

					//Jumpdrive if at least half the empire's ftl capacity will be left
					if((owner.FTLStored - cost) / owner.FTLCapacity >= 0.5 && range >= dist) {
						obj.insertJumpdriveOrder(pt, getIndex());
						moved = true;
					}
				}

				if(!moved && owner.hasFlingBeacons) {
					double cost = flingCost(obj, pt);
					//Fling if at least half the empire's ftl capacity will be left
					if((owner.FTLStored - cost) / owner.FTLCapacity >= 0.5) {
						Object@ fling = owner.getFlingBeacon(obj.position);
						if(fling !is null) {
							obj.insertFlingOrder(fling, pt, getIndex());
							moved = true;
						}
					}
				}
			}

			if(!moved)
				obj.insertMoveOrder(pt, getIndex());
		}
		else
			obj.stopMoving(enterOrbit = false);
		@dest = to;
	}

	OrderStatus tick(Object& obj, double time) {
		if(!obj.hasMover)
			return OS_COMPLETED;

		//Search for nearby systems, by number of jumps
		if(dest !is null) {
			if(obj.region is dest)
				@dest = null;
		}

		if(dest is null) {
			if(edge.length == 0) {
				uint sysIndex = obj.region !is null ? obj.region.SystemId : findNearestRegion(obj.position).SystemId;
				edge.insertLast(sysIndex);
				inner.insert(sysIndex);
			}

			array<int> newEdge;
			newEdge.reserve(edge.length * 2);

			for(uint i = 0, cnt = edge.length; i < cnt; ++i) {
				auto@ sys = getSystem(edge[i]);
				for(uint j = 0, jcnt = sys.adjacent.length; j < jcnt; ++j) {
					int sysIndex = sys.adjacent[j];
					if(inner.contains(sysIndex))
						continue;
					inner.insert(sysIndex);
					newEdge.insertLast(sysIndex);
				}
			}

			// switch to scouting to maintain vision instead of finding new
			// systems
			if (newEdge.length == 0) {
				switchedToMaintainingVision = true;

				// regenerate the curent edge and clear the inner set
				// so we find adjacent systems again
				edge.length = 0;
				inner.clear();
				uint sysIndex = obj.region !is null ? obj.region.SystemId : findNearestRegion(obj.position).SystemId;
				edge.insertLast(sysIndex);
				inner.insert(sysIndex);

				newEdge.reserve(edge.length * 4);

				for(uint i = 0, cnt = edge.length; i < cnt; ++i) {
					auto@ sys = getSystem(edge[i]);
					for(uint j = 0, jcnt = sys.adjacent.length; j < jcnt; ++j) {
						int sysIndex = sys.adjacent[j];
						if(inner.contains(sysIndex))
							continue;
						inner.insert(sysIndex);
						newEdge.insertLast(sysIndex);
						auto@ sys2 = getSystem(sysIndex);
						for (uint k = 0, kcnt = sys2.adjacent.length; k < kcnt; ++k) {
							int sysIndex = sys2.adjacent[k];
							if(inner.contains(sysIndex))
								continue;
							inner.insert(sysIndex);
							newEdge.insertLast(sysIndex);
						}
					}
				}

				// randomise the list of new edges
				// according to https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
				for (uint i = newEdge.length - 1; i > 0; i--) {
					// random j should be inclusive on both ranges
					// TODO: check that this is the case!
					uint j = randomi(0, i);
					uint tmp = newEdge[i];
					newEdge[i] = newEdge[j];
					newEdge[j] = tmp;
				}
			}

			uint mask = obj.owner.mask;
			Region@ nearest;
			double dist = 1.0e35;
			for(uint i = 0, cnt = newEdge.length; i < cnt; ++i) {
				auto@ reg = getSystem(newEdge[i]).object;
				// use vision mask instead of seen mask once switch over to maintaining
				// vision
				if (((switchedToMaintainingVision) && (reg.VisionMask & mask == 0))
					|| (!switchedToMaintainingVision && (reg.SeenMask & mask == 0 && reg.ScoutingMask.value & mask == 0))) {
					double d = obj.position.distanceTo(reg.position);
					if (switchedToMaintainingVision) {
						// pick randomly once just trying to maintain vision
						// as picking nearest will cause bouncing back and fourth
						// between two regions which isn't ideal
						@nearest = reg;
					} else {
						// prioritise nearest unseen/unscouted while trying to
						// discover the entire map
						if(d < dist) {
							@nearest = reg;
							dist = d;
						}
					}
				}
			}

			if(nearest !is null) {
				doMoveTo(obj, nearest);
				edge.length = 0;
				inner.clear();
			}
			else {
				edge = newEdge;
			}
		}

		return OS_BLOCKING;
	}
};