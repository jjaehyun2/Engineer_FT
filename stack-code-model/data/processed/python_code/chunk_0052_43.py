import com.GameInterface.AccountManagement;
import com.GameInterface.FeatData;
import com.GameInterface.Game.Character;
import com.GameInterface.Game.Shortcut;
import com.GameInterface.Game.ShortcutData;
import com.GameInterface.ProjectUtils;
import GUI.HUD.AbilitySlot;
import com.Utils.ID32;
import com.GameInterface.FeatInterface;
/*
* ...
* @author fox
*/
class com.fox.AgentSwitcher.Utils.Player extends Character {
	private static var ROLE_TANK = ProjectUtils.GetUint32TweakValue("GroupFinder_Tank_Buff");
	private static var ROLE_HEALER = ProjectUtils.GetUint32TweakValue("GroupFinder_Healer_Buff");
	private static var ROLE_DPS = ProjectUtils.GetUint32TweakValue("GroupFinder_DamageDealer_Buff");
    
	public function Player(charID:ID32) {
        super(charID);
    }
	public function IsTank(): Boolean {
		return GetStat(_global.Enums.Stat.e_TriangleHealthRatio, 2) > 50;
	}
	public function IsDps(): Boolean {
		return !IsTank() && !IsHealer();
	}
	public function IsHealer(): Boolean {
		return GetStat(_global.Enums.Stat.e_TriangleHealingRatio, 2) > 50;
	}
	public function IsRightRole(role:String) {
		if (role == "all") return true;
		else {
			if (role == "tank" && IsTank()) {
				return true;
			}
			if (role == "dps" && IsDps()) {
				return true;
			}
			if (role == "healer" && IsHealer()) {
				return true;
			}
		}
	}
	//Cutscene/dead etc..
	public function IsinPlay():Boolean {
		if (AccountManagement.GetInstance().GetLoginState() != _global.Enums.LoginState.e_LoginStateInPlay ||
			IsDead() ||	
			IsInCinematic() ||
			_root.fadetoblack.m_BlackScreen._visible)
		{
			return false
		}
		return true
	}
	// Probably not the best way to check cooldowns
	public static function SlotHasCooldown(slotID:Number):Boolean {
		var slot:AbilitySlot = _root.abilitybar.m_AbilitySlots[slotID];
		if (slot["m_IsCooldown"]) {
			return true
		}
		return false
	}
	static function GetFeatId(spellId:Number):Number
	{
		for (var featId in FeatInterface.m_FeatList)
		{
			var featData:FeatData = FeatInterface.m_FeatList[featId];
			if (featData.m_Spell == spellId)
			{
				return featData.m_Id;
			}
		}
		
		return null;
	}
	private static function GetSkillSlotID(indx:Number):Number
	{
		var positions:Array = [_global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot, _global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot + 2, 
								_global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot + 4, _global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot + 5,
								_global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot + 1, _global.Enums.ActiveAbilityShortcutSlots.e_PrimaryShortcutBarFirstSlot + 3 ];
		return positions[indx];
	}
	// Probably not the best way to check cooldowns
	public static function HasCooldown(BuildName):Boolean {
		for (var i in _root["boobuilds\\boobuilds"].appBuilds.m_quickBuilds) {
			if (_root["boobuilds\\boobuilds"].appBuilds.m_quickBuilds[i].m_name.toLowerCase() == BuildName.toLowerCase()) {
				for (var y:Number = 0; y < _root["boobuilds\\boobuilds"].appBuilds.m_quickBuilds[i].m_skills.length; y++ ){
					var shortcutPos = GetSkillSlotID(y);
					var shortcutData:ShortcutData = Shortcut.m_ShortcutList[shortcutPos];
					var abilitySlot = _root.abilitybar.GetAbilitySlot(shortcutPos);
					if (_root["boobuilds\\boobuilds"].appBuilds.m_quickBuilds[i].m_skills[y] && (_root["boobuilds\\boobuilds"].appBuilds.m_quickBuilds[i].m_skills[y] != GetFeatId(shortcutData.m_SpellId)) && abilitySlot["m_IsCooldown"]){
						return true;
					}
				}
				return false;
			}
		}
		for (var i in _root["boobuilds\\boobuilds"].appBuilds.m_builds) {
			if (_root["boobuilds\\boobuilds"].appBuilds.m_builds[i].m_name.toLowerCase() == BuildName.toLowerCase()) {
				for (var y:Number = 0; y < _root["boobuilds\\boobuilds"].appBuilds.m_builds[i].m_skills.length; y++ ){
					var shortcutPos = GetSkillSlotID(y);
					var shortcutData:ShortcutData = Shortcut.m_ShortcutList[shortcutPos];
					var abilitySlot = _root.abilitybar.GetAbilitySlot(shortcutPos);
					if ((_root["boobuilds\\boobuilds"].appBuilds.m_builds[i].m_skills[y] != GetFeatId(shortcutData.m_SpellId)) && abilitySlot["m_IsCooldown"]){
						return true;
					}
				}
				return false;
			}
		}
		for (var i in _root.abilitybar.m_AbilitySlots) {
			var slot:AbilitySlot = _root.abilitybar.m_AbilitySlots[i];
			if (slot["m_IsCooldown"]) {
				return true
			}
		}
		return false
	}
}