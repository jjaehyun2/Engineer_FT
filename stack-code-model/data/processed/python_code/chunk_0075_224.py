package
{
import org.flixel.FlxSprite;
import org.flixel.FlxG;

public class Invader extends FlxSprite {
	[Embed(source="../assets/images/invader_0.png")] protected var img_Invader_0:Class;
	[Embed(source="../assets/images/invader_1.png")] protected var img_Invader_1:Class;
	[Embed(source="../assets/images/invader_2.png")] protected var img_Invader_2:Class;
	[Embed(source="../assets/images/invader_3.png")] protected var img_Invader_3:Class;
	[Embed(source="../assets/images/invader_4.png")] protected var img_Invader_4:Class;
	[Embed(source="../assets/images/invader_5.png")] protected var img_Invader_5:Class;
	[Embed(source="../assets/images/invader_6.png")] protected var img_Invader_6:Class;
	[Embed(source="../assets/images/invader_7.png")] protected var img_Invader_7:Class;
	[Embed(source="../assets/images/invader_8.png")] protected var img_Invader_8:Class;
	[Embed(source="../assets/images/invader_9.png")] protected var img_Invader_9:Class;

	private var m_kind:int;

	private var m_base_x:Number;
	private var m_base_y:Number;
	private var m_dir_x:Number;
	private var m_dir_y:Number;
	private var m_mode:String;

	private var m_fire_rate:int = 10;
	private var m_fire_cooldown:Number = 1.0;

	private var m_stalk_rate:int = 10;
	private var m_stalk_points:int = 5;
	private var m_stalk_cooldown:Number = 2.0;
	private var m_stalk_speed:Number = 50.0;

	public function Invader(x:int, y:int, kind:int = 0):void
	{
		super(x, y)
		m_base_x = x;
		m_base_y = y;
		m_kind = kind;
		m_kind %= 10;
		m_mode = "";

		var img_class:Class = img_Invader_1;
		if (m_kind == 0) {
			img_class = img_Invader_0;
			m_mode = "firing";
		} else if (m_kind == 1) {
			img_class = img_Invader_1;
		} else if (m_kind == 2) {
			img_class = img_Invader_2;
		} else if (m_kind == 3) {
			img_class = img_Invader_3;
		} else if (m_kind == 4) {
			img_class = img_Invader_4;
		} else if (m_kind == 5) {
			img_class = img_Invader_5;
		} else if (m_kind == 6) {
			img_class = img_Invader_6;
		} else if (m_kind == 7) {
			img_class = img_Invader_7;
		} else if (m_kind == 8) {
			img_class = img_Invader_8;
		} else if (m_kind == 9) {
			img_class = img_Invader_9;
		}

		loadGraphic(img_class, false, false, 16, 16);

		addAnimation("normal", [0, 1], 4 + int(Math.random()*6));
		addAnimation("attack", [2, 3], 6);
		play("normal");
	}

	override public function update():void
	{
		super.update();

		move_logic();
		m_fire_cooldown -= FlxG.elapsed;
		m_stalk_cooldown -= FlxG.elapsed;
	}

	private function move_logic():void
	{
		if (m_mode == "firing") {
			firing();
			move_to_base();
		} else if (m_mode == "stalking") {
			firing();
			var dx:Number = m_dir_x - x;
			var dy:Number = m_dir_y - y;
			if (dx * dx + dy * dy < 10) {
				if (m_stalk_points > 0) {
					m_dir_x = 32 + Math.random() * (320 - 32 - 16);
					m_dir_y = 32 + Math.random() * (200 - 32 - 16);
					m_stalk_points -= 1;
				} else {
					m_mode = "";
					Invaders.stalkers -= 1;
					restore_stalk_cooldown();
					play("normal");
				}
			} else {
				x += dx / m_stalk_speed;
				y += dy / m_stalk_speed;
			}
		} else {
			move_to_base();
			change_mode();
		}
	}

	private function change_mode():void
	{
		if (Invaders.can_stalk() && m_stalk_cooldown < 0 && Math.random() * 2000 < m_stalk_rate) {
			m_dir_x = 32 + Math.random() * (320 - 32 - 16);
			m_dir_y = 32 + Math.random() * (200 - 32 - 16);
			m_mode = "stalking";
			m_stalk_points = 4;
			Invaders.stalkers += 1;
			play("attack");
		}
	}

	private function move_to_base():void
	{
		var dx:Number = m_base_x - x;
		var dy:Number = m_base_y - y;
		x += dx / 8;
		y += dy / 8;
	}

	private function firing():void
	{
		if (m_fire_cooldown < 0 && Math.random()*1000 < m_fire_rate) {
			Invaders.fire_bullet(x, y);
			restore_fire_cooldown();
		}
	}

	private function restore_fire_cooldown():void
	{
		if (m_kind == 0) {
			m_fire_cooldown = 2.0;
			m_fire_rate = 100;
			m_stalk_rate = 1;
			m_stalk_speed = 50.0;
		} else if (m_kind == 1) {
			m_fire_cooldown = 4.0;
			m_fire_rate = 50;
			m_stalk_rate = 50;
			m_stalk_speed = 20.0;
		} else if (m_kind == 2) {
			m_fire_cooldown = 4.0;
			m_fire_rate = 100;
			m_stalk_rate = 10;
			m_stalk_speed = 10.0;
		} else if (m_kind == 3) {
			m_fire_cooldown = 5.0;
			m_fire_rate = 100;
			m_stalk_rate = 5;
			m_stalk_speed = 30.0;
		} else if (m_kind == 4) {
			m_fire_cooldown = 3.0;
			m_fire_rate = 100;
			m_stalk_rate = 12;
			m_stalk_speed = 60.0;
		} else if (m_kind == 5) {
			m_fire_cooldown = 1.0;
			m_fire_rate = 50;
			m_stalk_rate = 100;
			m_stalk_speed = 70.0;
		} else if (m_kind == 6) {
			m_fire_cooldown = 0.5;
			m_fire_rate = 150;
			m_stalk_rate = 5;
			m_stalk_speed = 5.0;
		} else if (m_kind == 7) {
			m_fire_cooldown = 2.0;
			m_fire_rate = 100;
			m_stalk_rate = 10;
			m_stalk_speed = 10.0;
		} else if (m_kind == 8) {
			m_fire_cooldown = 4.0;
			m_fire_rate = 100;
			m_stalk_rate = 20;
			m_stalk_speed = 150.0;
		} else if (m_kind == 9) {
			m_fire_cooldown = 0.2;
			m_fire_rate = 250;
			m_stalk_rate = 100;
			m_stalk_speed = 50.0;
		} else {
			m_fire_cooldown = 2.0;
			m_fire_rate = 100;
			m_stalk_rate = 1;
		}
	}

	private function restore_stalk_cooldown():void
	{
		if (m_kind == 0) {
			m_stalk_cooldown = 2.0;
			m_stalk_points = 10;
		} else if (m_kind == 1) {
			m_stalk_cooldown = 4.0;
			m_stalk_points = 5;
		} else if (m_kind == 2) {
			m_stalk_cooldown = 4.0;
			m_stalk_points = 10;
		} else if (m_kind == 3) {
			m_stalk_cooldown = 5.0;
			m_stalk_points = 6;
		} else if (m_kind == 4) {
			m_stalk_cooldown = 3.0;
			m_stalk_points = 10;
		} else if (m_kind == 5) {
			m_stalk_cooldown = 1.0;
			m_stalk_points = 50;
		} else if (m_kind == 6) {
			m_stalk_cooldown = 0.5;
			m_stalk_points = 5;
		} else if (m_kind == 7) {
			m_stalk_cooldown = 2.0;
			m_stalk_points = 2;
		} else if (m_kind == 8) {
			m_stalk_cooldown = 4.0;
			m_stalk_points = 1;
		} else if (m_kind == 9) {
			m_stalk_cooldown = 0.25;
			m_stalk_points = 20;
		} else {
			m_stalk_cooldown = 2.0;
			m_stalk_points = 100;
		}
	}

	public function add_to_base(dx:int, dy:int):void
	{
		m_base_x += dx;
		m_base_y += dy;
	}

	public function get baseX():Number
	{
		return m_base_x;
	}

	public function get baseY():Number
	{
		return m_base_y;
	}

	override public function kill():void
	{
		if (m_mode == "stalking") {
			Invaders.stalkers -= 1;
		}
		super.kill();
	}
}
} // package