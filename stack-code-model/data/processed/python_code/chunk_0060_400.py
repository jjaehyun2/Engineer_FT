package
{
import flash.ui.Mouse;
import org.flixel.FlxG;
import org.flixel.FlxState;
import org.flixel.FlxSprite;

public class Intro extends FlxState {
	[Embed(source="../assets/images/logo.png")] protected var img_Logo:Class;
	[Embed(source="../assets/sounds/RetroFuture Clean.mp3")] public static var snd_Music:Class;

	private var m_timer:Number = 0;
	private var m_logo:FlxSprite = new FlxSprite(320/2 - 64/2, 240/2 - 64/2, img_Logo);

	public function Intro():void
	{
		super();
		Mouse.show();
		bgColor = 0xffdddddd;
		FlxG.playMusic(snd_Music);
	}

	override public function create():void
	{
		add(m_logo);
		m_timer = 0.0;
		m_logo.alpha = 0.0;
	}

	override public function update():void
	{
		super.update();
		m_timer += FlxG.elapsed;

		if (m_timer > 1.0 && m_timer < 2.0) {
			m_logo.alpha += 0.025;
		} else if (m_timer > 3.0 && m_timer < 4.0) {
			m_logo.alpha -= 0.025;
		} else if (m_timer > 4.0) {
			FlxG.state = Manager.state_title;
		}
	}
}
} // package