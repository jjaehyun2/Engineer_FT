import com.Utils.Archive;
import com.chosen.mobradar.lib.App;
import com.chosen.mobradar.lib.Icon;
import com.chosen.ui.ChosenUIAddon;
import mx.utils.Delegate;

/**
 * Mob Radar is an addon for Secret World Legends which displays a 
 * radar type display that tracks nearby enemies, NPCs and players.
 * @author Chosen-Wan
 * @version 0.0.1a
 */
class com.chosen.mobradar.MobRadar
{
	private var app:App;
	private var icon:Icon;
	
	public static function main(root:MovieClip)
	{
		var ui:ChosenUIAddon = new ChosenUIAddon("Mob Radar");		
		var mobRadar:MobRadar = new MobRadar(root);
	}
	
	public function MobRadar(root:MovieClip) 
	{
		app = App.Create(root);
		icon = Icon.Create(root);
		
		root.OnModuleActivated = Delegate.create(this, OnActivate);
		root.OnModuleDeactivated = Delegate.create(this, OnDeactivate);
	}
	
	public function OnActivate(archive:Archive)
	{
		app.OnActivate(archive);
		icon.OnActivate(archive);
	}
	
	public function OnDeactivate() : Archive
	{
		var archive:Archive = new Archive();
		app.OnDeactivate(archive);
		icon.OnDeactivate(archive);
		return new Archive();
	}
}