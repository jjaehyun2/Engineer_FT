///////////////////////////////////////////////////////////
//  AttackInfo.as
//  Macromedia ActionScript Implementation of the Class AttackInfo
//  Generated by Enterprise Architect
//  Created on:      24-һ��-2014 14:06:13
//  Original author: johnny
///////////////////////////////////////////////////////////

/**
 * @author johnny
 * @version 1.0
 */
package com.xgame.godwar.enum
{
	public class AttackInfo
	{
		public var skillId: String = null;
	    public var attackerGuid: String = null;
	    public var defenderGuid: String = null;
		
	    public var attackerCard: String = null;
		public var attackerCardPosition: int = int.MIN_VALUE;
		public var attackCardUp: Boolean = false;
		public var isSetAttackerCardUp: Boolean = false;
		public var attackCardDisabled: Boolean = true;
		public var isSetAttackerCardDisabled: Boolean = false;
	    public var defenderCard: String = null;
		public var defenderCardPosition: int = int.MIN_VALUE;
		public var defenderCardUp: Boolean = false;
		public var isSetDefenderCardUp: Boolean = false;
		public var defenderCardDisabled: Boolean = true;
		public var isSetDefenderCardDisabled: Boolean = false;
		
	    public var attackerAttackChange: int = int.MIN_VALUE;
	    public var attackerAttack: int = int.MIN_VALUE;
	    public var attackerDefChange: int = int.MIN_VALUE;
	    public var attackerDef: int = int.MIN_VALUE;
	    public var attackerMdefChange: int = int.MIN_VALUE;
	    public var attackerMdef: int = int.MIN_VALUE;
	    public var attackerHealthChange: int = int.MIN_VALUE;
	    public var attackerHealth: int = int.MIN_VALUE;
	    public var attackerHealthMaxChange: int = int.MIN_VALUE;
	    public var attackerHealthMax: int = int.MIN_VALUE;
	    public var attackerIsStatus: Boolean = false;
		public var isSetAttackerStatus: Boolean = false;
	    public var attackerRemainRound: int = int.MIN_VALUE;
		
		public var defenderAttackChange: int = int.MIN_VALUE;
		public var defenderAttack: int = int.MIN_VALUE;
		public var defenderDefChange: int = int.MIN_VALUE;
		public var defenderDef: int = int.MIN_VALUE;
		public var defenderMdefChange: int = int.MIN_VALUE;
		public var defenderMdef: int = int.MIN_VALUE;
		public var defenderHealthChange: int = int.MIN_VALUE;
		public var defenderHealth: int = int.MIN_VALUE;
		public var defenderHealthMaxChange: int = int.MIN_VALUE;
		public var defenderHealthMax: int = int.MIN_VALUE;
		public var defenderIsStatus: Boolean = false;
		public var isSetDefenderStatus: Boolean = false;
		public var defenderRemainRound: int = int.MIN_VALUE;
	
		public function AttackInfo()
		{
		}
	
	}
}