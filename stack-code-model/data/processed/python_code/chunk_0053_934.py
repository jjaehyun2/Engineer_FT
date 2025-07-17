package
{
import org.flixel.FlxGroup;
import org.flixel.FlxSprite;

public class Invaders extends FlxGroup {
	[Embed(source="../assets/images/invader_bullet.png")] protected var img_InvaderBullet:Class;

	public var X:int = -1;
	public var WAVES:Array = [
		// WAVE 1
		[
		 1,1,1,0,0,0,0,1,1,1,
		 X,X,1,0,0,0,0,1,X,X,
		 X,X,X,X,0,0,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 2
		[
		 1,1,1,1,1,1,1,1,1,1,
		 X,X,X,1,1,1,1,X,X,X,
		 0,0,X,X,0,0,X,X,0,0,
		 0,0,X,X,X,X,X,X,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 3
		[
		 X,X,0,0,2,2,0,0,X,X,
		 X,X,0,0,2,2,0,0,X,X,
		 0,0,0,0,0,0,0,0,0,0,
		 1,1,X,X,X,X,X,X,1,1,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 4
		[
		 2,2,2,2,2,2,2,2,2,2,
		 1,1,1,1,1,1,1,1,1,1,
		 0,X,X,0,X,X,0,X,X,0,
		 0,X,X,0,X,X,0,X,X,0,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 5
		[
		 2,X,X,2,X,X,2,X,X,2,
		 2,X,X,2,X,X,2,X,X,2,
		 2,3,3,2,3,3,2,3,3,2,
		 2,X,X,2,X,X,2,X,X,2,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 6
		[
		 2,3,2,3,0,0,3,2,3,2,
		 0,2,0,2,0,0,2,0,2,0,
		 X,0,X,0,X,X,0,X,0,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 7
		[
		 3,3,3,3,3,3,3,3,3,3,
		 2,2,0,0,2,2,0,0,2,2,
		 0,0,0,0,0,0,0,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 8
		[
		 3,2,3,2,3,2,3,2,3,2,
		 2,3,2,3,2,3,2,3,2,3,
		 X,2,X,2,X,2,X,2,X,X,
		 X,2,X,2,X,2,X,2,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 9
		[
		 3,3,3,3,3,3,3,3,3,3,
		 3,3,3,3,3,3,3,3,3,3,
		 2,2,2,2,2,2,2,2,2,2,
		 0,0,0,0,0,0,0,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 10
		[
		 4,4,3,X,X,X,X,3,4,4,
		 4,4,3,X,X,X,X,3,4,4,
		 3,3,3,X,0,0,X,3,3,3,
		 X,X,X,X,2,2,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 11
		[
		 4,0,4,0,4,0,4,0,4,X,
		 4,X,4,X,4,X,4,X,4,X,
		 4,X,4,X,4,X,4,X,4,X,
		 4,0,4,0,4,0,4,0,4,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 12
		[
		 X,0,0,0,0,0,0,0,0,X,
		 X,0,3,3,1,1,2,2,0,X,
		 X,0,3,3,1,1,2,2,0,X,
		 X,0,0,0,0,0,0,0,0,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 13
		[
		 X,X,X,X,3,3,X,X,X,X,
		 X,4,X,X,3,3,X,X,4,X,
		 X,4,X,X,3,3,X,X,4,X,
		 4,4,4,0,2,2,0,4,4,4,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 14
		[
		 0,0,0,0,0,0,0,0,0,0,
		 0,0,3,3,4,4,3,3,0,0,
		 0,0,3,3,0,0,3,3,0,0,
		 X,X,3,3,4,4,3,3,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 15
		[
		 5,0,0,0,0,0,0,0,0,5,
		 X,4,4,4,X,X,4,4,4,X,
		 X,5,5,5,X,X,5,5,5,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 16
		[
		 X,X,X,X,X,X,X,X,X,X,
		 X,4,X,X,X,X,X,X,4,X,
		 X,5,3,3,3,3,3,3,5,X,
		 X,4,X,X,0,0,X,X,4,X,
		 X,X,X,X,0,0,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 17
		[
		 5,5,4,4,X,X,4,4,5,5,
		 5,5,4,4,X,X,4,4,5,5,
		 5,5,4,4,X,X,4,4,5,5,
		 X,X,4,4,X,X,4,4,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 18
		[
		 X,X,5,X,0,0,X,5,X,X,
		 X,X,5,X,3,3,X,5,X,X,
		 5,5,5,X,3,3,X,5,5,5,
		 X,X,X,X,X,X,X,X,X,X,
		 0,0,0,X,3,3,X,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 19
		[
		 X,X,X,0,0,0,0,X,X,X,
		 X,X,X,0,4,4,0,X,X,X,
		 X,5,X,0,4,4,0,X,5,X,
		 5,5,5,0,2,2,0,5,5,5,
		 X,5,X,X,X,X,X,X,5,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 20
		[
		 5,4,3,2,2,2,2,3,4,5,
		 X,5,4,3,3,3,3,4,5,X,
		 X,X,5,4,4,4,4,5,X,X,
		 X,X,X,5,5,5,5,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 21
		[
		 5,5,5,5,5,5,5,5,5,5,
		 1,1,1,0,0,0,0,2,2,2,
		 2,2,0,X,X,X,X,0,3,3,
		 2,0,X,X,X,X,X,X,0,3,
		 0,X,X,X,X,X,X,X,X,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 22
		[
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,5,5,5,5,X,X,X,
		 X,X,X,4,6,6,4,X,X,X,
		 X,X,X,4,5,5,4,X,X,X,
		 3,3,4,4,X,X,4,4,3,3,
		 0,0,X,X,X,X,X,X,0,0,
		],

		// WAVE 23
		[
		 0,X,1,5,6,6,5,1,X,0,
		 0,X,1,5,6,6,5,1,X,0,
		 0,X,1,5,6,6,5,1,X,0,
		 0,X,1,1,6,6,1,1,X,0,
		 0,X,X,X,X,X,X,X,X,0,
		 X,0,X,X,X,X,X,X,0,X,
		],

		// WAVE 24
		[
		 X,X,X,5,5,5,5,X,X,X,
		 X,0,0,X,6,6,X,0,0,X,
		 X,0,0,X,X,X,X,0,0,X,
		 X,X,X,X,4,4,X,X,X,X,
		 X,X,X,4,X,X,4,X,X,X,
		 X,3,3,3,X,X,3,3,3,X,
		],

		// WAVE 25
		[
		 X,6,5,4,3,3,4,5,6,X,
		 X,6,5,4,4,4,4,5,6,X,
		 X,6,6,5,5,5,5,6,6,X,
		 X,0,0,6,6,6,6,0,0,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 26
		[
		 X,X,X,0,4,4,0,X,X,X,
		 X,X,X,0,4,4,0,X,X,X,
		 0,0,0,0,4,4,0,0,0,0,
		 6,6,6,X,X,X,X,6,6,6,
		 6,X,6,X,X,X,X,6,X,6,
		 6,X,6,X,X,X,X,6,X,6,
		],

		// WAVE 27
		[
		 0,0,0,0,0,0,0,0,0,0,
		 6,6,6,6,6,6,6,6,6,6,
		 0,0,6,6,0,0,6,6,0,0,
		 2,2,2,2,2,2,2,2,2,2,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 28
		[
		 7,7,7,7,X,X,7,7,7,7,
		 X,6,6,X,X,X,X,6,6,X,
		 5,5,5,5,X,X,5,5,5,5,
		 0,0,0,0,0,0,0,0,0,0,
		 X,X,X,X,0,0,X,X,X,X,
		 X,X,X,X,0,0,X,X,X,X,
		],

		// WAVE 29
		[
		 6,X,X,X,X,X,X,X,X,6,
		 6,X,0,0,0,0,0,0,X,6,
		 6,X,0,7,7,7,7,0,X,6,
		 6,X,0,7,7,7,7,0,X,6,
		 6,X,0,0,0,0,0,0,X,6,
		 6,X,X,X,X,X,X,X,X,6,
		],

		// WAVE 30
		[
		 1,1,1,1,1,1,1,1,1,1,
		 7,5,7,6,7,5,7,6,7,5,
		 7,5,7,6,7,5,7,6,7,5,
		 7,5,7,6,7,5,7,6,7,5,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 31
		[
		 0,0,0,0,0,0,0,0,0,0,
		 0,1,1,1,1,1,1,1,1,0,
		 0,7,7,7,7,7,7,7,7,0,
		 0,4,4,4,4,4,4,4,4,0,
		 0,3,3,3,3,2,2,2,2,0,
		 0,0,0,0,0,0,0,0,0,0,
		],

		// WAVE 32
		[
		 6,7,6,X,X,X,X,6,7,6,
		 6,7,6,X,X,X,X,6,7,6,
		 6,7,6,5,5,5,5,6,7,6,
		 X,6,4,4,4,4,4,4,6,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 33
		[
		 2,2,X,7,8,8,7,X,0,0,
		 2,2,X,7,8,8,7,X,0,0,
		 2,2,X,7,8,8,7,X,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 34
		[
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,3,3,3,3,3,3,X,X,
		 X,X,3,3,3,3,3,3,X,X,
		 8,8,0,0,0,0,0,0,8,8,
		 8,8,0,5,5,5,5,0,8,8,
		 X,X,X,5,X,X,5,X,X,X,
		],

		// WAVE 35
		[
		 X,X,5,5,5,5,5,5,X,X,
		 X,5,4,7,7,7,7,4,5,X,
		 5,4,4,0,7,7,0,4,4,5,
		 5,4,5,7,7,7,7,5,4,5,
		 5,5,X,5,5,5,5,X,5,5,
		 5,X,X,X,X,X,X,X,X,5,
		],

		// WAVE 36
		[
		 0,0,8,X,X,X,X,8,0,0,
		 0,0,8,X,X,X,X,8,0,0,
		 4,4,0,8,8,8,8,0,4,4,
		 X,X,4,0,X,X,0,4,X,X,
		 X,X,3,3,3,3,3,3,X,X,
		 X,X,3,X,X,X,X,3,X,X,
		],

		// WAVE 37
		[
		 3,2,0,8,1,1,8,0,2,3,
		 3,2,0,8,1,1,8,0,2,3,
		 3,2,0,8,8,8,8,0,2,3,
		 3,2,0,0,0,0,0,0,2,3,
		 3,2,2,2,2,2,2,2,2,3,
		 3,3,3,3,3,3,3,3,3,3,
		],

		// WAVE 38
		[
		 9,9,X,X,X,X,X,X,9,9,
		 9,9,X,0,0,0,0,X,9,9,
		 X,X,X,1,1,1,1,X,X,X,
		 X,X,X,2,2,2,2,X,X,X,
		 X,X,X,5,5,5,5,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 39
		[
		 4,9,4,X,X,X,X,4,9,4,
		 4,9,4,X,X,X,X,4,9,4,
		 4,4,4,X,X,X,X,4,4,4,
		 X,X,0,X,X,X,X,0,X,X,
		 X,X,0,1,4,4,1,0,X,X,
		 X,X,0,0,0,0,0,0,X,X,
		],

		// WAVE 40
		[
		 0,0,0,9,X,X,9,0,0,0,
		 8,8,0,9,9,9,9,0,8,8,
		 X,8,0,0,0,0,0,0,8,X,
		 X,8,8,8,8,8,8,8,8,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 41
		[
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,9,9,9,9,X,X,X,
		 X,X,X,9,9,9,9,X,X,X,
		 X,X,X,0,2,2,0,X,X,X,
		 X,8,8,0,2,2,0,8,8,X,
		 X,8,8,0,0,0,0,8,8,X,
		],

		// WAVE 42
		[
		 X,X,X,X,0,0,X,X,X,X,
		 X,7,7,X,0,0,X,7,7,X,
		 X,7,7,X,0,0,X,7,7,X,
		 X,X,X,X,0,0,X,X,X,X,
		 1,1,1,1,0,0,1,1,1,1,
		 2,2,2,2,2,2,2,2,2,2,
		],

		// WAVE 43
		[
		 0,0,1,1,2,2,3,3,4,4,
		 0,0,1,1,2,2,3,3,4,4,
		 5,5,6,6,7,7,8,8,9,9,
		 5,5,6,6,7,7,8,8,9,9,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 44
		[
		 9,9,9,9,9,9,9,9,9,9,
		 8,8,8,8,8,8,8,8,8,8,
		 7,7,7,7,7,7,7,7,7,7,
		 X,X,X,X,X,X,X,X,X,X,
		 0,X,0,X,0,X,0,X,0,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 45
		[
		 9,0,9,0,9,0,9,0,9,0,
		 0,9,0,9,0,9,0,9,0,9,
		 9,0,9,0,9,0,9,0,9,0,
		 0,9,0,9,0,9,0,9,0,9,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 46
		[
		 X,X,X,X,2,2,X,X,X,X,
		 X,X,2,2,0,0,2,2,X,X,
		 2,2,0,0,0,0,0,0,2,2,
		 0,0,0,0,9,9,0,0,0,0,
		 0,0,9,9,X,X,9,9,0,0,
		 9,9,X,X,X,X,X,X,9,9,
		],

		// WAVE 47
		[
		 X,X,5,X,X,X,X,5,X,X,
		 X,X,5,X,X,X,X,5,X,X,
		 9,9,9,9,4,4,9,9,9,9,
		 0,0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,0,
		],

		// WAVE 48
		[
		 9,9,8,6,X,X,6,8,9,9,
		 9,9,8,6,X,X,6,8,9,9,
		 9,9,8,6,4,4,6,8,9,9,
		 X,9,X,5,5,5,5,X,9,X,
		 X,9,X,X,X,X,X,X,9,X,
		 X,9,X,X,X,X,X,X,9,X,
		],

		// WAVE 49
		[
		 X,6,5,8,8,8,8,5,6,X,
		 X,6,5,8,9,9,8,5,6,X,
		 X,6,5,8,9,9,8,5,6,X,
		 X,6,5,8,8,8,8,5,6,X,
		 X,6,5,5,5,5,5,5,6,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 50
		[
		 4,4,4,X,X,X,X,4,4,4,
		 3,3,3,X,X,X,X,3,3,3,
		 2,2,2,X,X,X,X,2,2,2,
		 1,1,1,X,X,X,X,1,1,1,
		 0,0,0,X,X,X,X,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 51
		[
		 5,5,5,X,X,X,X,6,6,6,
		 7,7,5,5,5,6,6,6,7,7,
		 X,X,7,7,7,7,7,7,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		 0,0,0,0,0,0,0,0,0,0,
		],

		// WAVE 52
		[
		 5,5,X,X,0,0,X,X,1,1,
		 5,X,X,X,0,0,X,X,X,1,
		 X,X,X,X,0,0,X,X,X,X,
		 X,0,0,0,0,0,0,0,0,0,
		 X,4,4,4,4,4,4,4,4,X,
		 4,4,4,4,4,4,4,4,4,4,
		],

		// WAVE 53
		[
		 X,0,0,0,0,0,0,0,0,X,
		 X,7,7,7,X,X,7,7,7,X,
		 X,7,8,7,X,X,7,8,7,X,
		 X,7,7,7,9,9,7,7,7,X,
		 X,X,X,X,9,9,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 54
		[
		 7,X,7,X,X,X,X,7,X,7,
		 7,7,7,X,X,X,X,7,7,7,
		 X,7,X,5,5,5,5,X,7,X,
		 X,7,X,3,3,3,3,X,7,X,
		 X,7,X,2,2,2,2,X,7,X,
		 X,7,X,X,X,X,X,X,7,X,
		],

		// WAVE 55
		[
		 0,0,X,X,X,X,X,X,0,0,
		 0,0,X,X,7,7,X,X,0,0,
		 X,X,X,X,8,8,X,X,X,X,
		 X,X,9,9,X,X,9,9,X,X,
		 9,9,9,9,X,X,9,9,9,9,
		 9,9,X,X,X,X,X,X,9,9,
		],

		// WAVE 56
		[
		 3,3,5,5,0,0,5,5,3,3,
		 X,3,5,5,X,X,5,5,3,X,
		 X,3,5,5,X,X,5,5,3,X,
		 X,3,5,5,X,X,5,5,3,X,
		 X,X,5,5,X,X,5,5,X,X,
		 X,X,5,5,0,0,5,5,X,X,
		],

		// WAVE 57
		[
		 9,X,X,X,4,4,X,X,X,9,
		 9,9,X,X,4,4,X,X,9,9,
		 9,9,X,0,4,4,0,X,9,9,
		 X,9,0,0,X,X,0,0,9,X,
		 X,9,0,X,X,X,X,0,9,X,
		 X,9,X,X,X,X,X,X,9,X,
		],

		// WAVE 58
		[
		 X,X,X,3,2,2,3,X,X,X,
		 X,X,5,3,2,2,3,5,X,X,
		 X,5,5,3,2,2,3,5,5,X,
		 5,5,5,X,X,X,X,5,5,5,
		 5,5,X,X,X,X,X,X,5,5,
		 5,X,0,0,0,0,0,0,X,5,
		],

		// WAVE 59
		[
		 9,X,2,X,1,X,3,X,4,X,
		 X,9,X,2,X,1,X,3,X,4,
		 8,X,9,X,2,X,1,X,3,X,
		 X,8,X,9,X,2,X,1,X,3,
		 5,X,8,X,9,X,2,X,1,X,
		 X,5,X,8,X,9,X,2,X,1,
		],

		// WAVE 60
		[
		 0,X,0,X,0,X,0,X,0,X,
		 X,0,X,0,X,0,X,0,X,0,
		 4,X,4,X,4,X,4,X,4,X,
		 X,4,X,4,X,4,X,4,X,4,
		 6,X,6,X,6,X,6,X,6,X,
		 X,6,X,6,X,6,X,6,X,6,
		],

		// WAVE 61
		[
		 X,X,X,X,X,X,X,X,X,X,
		 0,0,0,0,X,X,0,0,0,0,
		 0,9,9,0,X,X,0,9,9,0,
		 0,9,9,0,X,X,0,9,9,0,
		 0,0,0,0,X,X,0,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 62
		[
		 9,X,2,0,X,X,0,2,X,9,
		 9,X,2,0,0,0,0,2,X,9,
		 9,X,2,2,2,2,2,2,X,9,
		 9,X,X,X,X,X,X,X,X,9,
		 9,9,9,9,9,9,9,9,9,9,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 63
		[
		 X,9,0,X,X,X,X,0,9,X,
		 X,9,0,0,0,0,0,0,9,X,
		 8,8,8,9,8,8,9,8,8,8,
		 X,X,X,9,9,9,9,X,X,X,
		 3,3,X,X,X,X,X,X,3,3,
		 X,3,3,3,3,3,3,3,3,X,
		],

		// WAVE 64
		[
		 X,4,5,7,X,X,7,5,4,X,
		 4,5,7,X,X,X,X,7,5,4,
		 4,4,5,7,X,X,7,5,4,4,
		 X,4,5,7,X,X,7,5,4,X,
		 X,4,5,7,X,X,7,5,4,X,
		 X,0,0,0,0,0,0,0,0,X,
		],

		// WAVE 65
		[
		 4,4,4,X,6,6,X,4,4,4,
		 4,4,4,X,6,6,X,4,4,4,
		 4,4,4,X,6,6,X,4,4,4,
		 6,6,6,X,6,6,X,6,6,6,
		 6,6,6,X,X,X,X,6,6,6,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 66
		[
		 7,0,0,0,0,0,0,0,0,7,
		 X,7,0,0,0,0,0,0,7,X,
		 X,X,7,0,0,0,0,7,X,X,
		 X,X,X,7,0,0,7,X,X,X,
		 X,X,X,X,7,7,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 67
		[
		 X,X,X,X,1,1,X,X,X,X,
		 X,X,X,1,2,2,1,X,X,X,
		 X,X,1,2,3,3,2,1,X,X,
		 X,1,2,3,4,4,3,2,1,X,
		 1,2,3,4,5,5,4,3,2,1,
		 X,X,X,6,6,6,6,X,X,X,
		],

		// WAVE 68
		[
		 6,6,6,6,2,2,6,6,6,6,
		 6,6,6,6,2,2,6,6,6,6,
		 X,X,6,6,3,3,6,6,X,X,
		 X,X,6,6,3,3,6,6,X,X,
		 X,X,0,0,0,0,0,0,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 69
		[
		 1,1,1,3,3,3,3,0,0,0,
		 1,1,1,X,X,X,X,0,0,0,
		 1,1,1,2,2,2,2,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 0,X,0,X,0,X,0,X,0,X,
		 X,0,X,0,X,0,X,0,X,0,
		],

		// WAVE 70
		[
		 X,X,1,2,4,4,2,1,X,X,
		 0,X,X,1,2,2,1,X,X,0,
		 0,0,X,X,1,1,X,X,0,0,
		 0,0,0,X,X,X,X,0,0,0,
		 8,9,8,9,8,9,8,9,8,9,
		 9,8,9,8,9,8,9,8,9,8,
		],

		// WAVE 71
		[
		 9,9,9,9,9,9,9,9,9,9,
		 X,7,7,7,7,7,7,7,7,X,
		 X,X,5,5,5,5,5,5,X,X,
		 X,X,X,3,3,3,3,X,X,X,
		 X,X,X,X,1,1,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 72
		[
		 8,8,8,8,8,8,8,8,8,8,
		 6,X,6,X,6,X,6,X,6,X,
		 X,6,X,6,X,6,X,6,X,6,
		 4,X,4,X,4,X,4,X,4,X,
		 X,4,X,4,X,4,X,4,X,4,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 73
		[
		 X,7,5,7,X,X,7,5,7,X,
		 X,X,5,X,X,X,X,5,X,X,
		 X,1,1,1,X,X,1,1,1,X,
		 1,2,2,2,1,1,2,2,2,1,
		 0,0,0,0,0,0,0,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 74
		[
		 1,1,1,0,5,5,0,1,1,1,
		 1,X,X,0,5,5,0,X,X,1,
		 1,X,X,0,0,0,0,X,X,1,
		 1,X,X,X,X,X,X,X,X,1,
		 4,4,4,X,X,X,X,4,4,4,
		 4,4,4,X,X,X,X,4,4,4,
		],

		// WAVE 75
		[
		 X,6,X,X,X,X,X,X,6,X,
		 X,6,5,X,X,X,X,5,6,X,
		 X,6,5,4,X,X,4,5,6,X,
		 X,6,5,4,0,0,4,5,6,X,
		 X,6,5,4,2,2,4,5,6,X,
		 X,6,X,4,3,3,4,X,6,X,
		],

		// WAVE 76
		[
		 X,3,0,0,X,X,0,0,3,X,
		 X,3,0,0,X,X,0,0,3,X,
		 X,3,0,0,X,X,0,0,3,X,
		 X,X,3,3,3,3,3,3,X,X,
		 X,X,5,5,5,5,5,5,X,X,
		 X,X,5,2,2,2,2,5,X,X,
		],

		// WAVE 77
		[
		 9,5,X,1,1,1,1,X,5,9,
		 9,5,X,1,0,0,1,X,5,9,
		 9,1,X,1,0,0,1,X,1,9,
		 9,1,X,1,0,0,1,X,1,9,
		 X,1,1,1,0,0,1,1,1,X,
		 X,X,X,5,5,5,5,X,X,X,
		],

		// WAVE 78
		[
		 4,4,4,4,4,4,4,4,4,4,
		 3,X,3,X,3,X,3,X,3,X,
		 X,3,X,3,X,3,X,3,X,3,
		 7,X,7,X,7,X,7,X,7,X,
		 X,0,X,0,X,0,X,0,X,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 79
		[
		 X,5,7,9,X,X,9,7,5,X,
		 X,X,5,7,9,9,7,5,X,X,
		 1,X,X,5,7,7,5,X,X,1,
		 0,1,X,X,5,5,X,X,1,0,
		 0,0,1,X,X,X,X,1,0,0,
		 0,0,0,1,X,X,1,0,0,0,
		],

		// WAVE 80
		[
		 7,7,7,7,X,X,4,4,4,4,
		 4,4,4,4,X,X,7,7,7,7,
		 6,6,6,6,X,X,5,5,5,5,
		 X,0,0,X,X,X,X,0,0,X,
		 X,0,0,0,0,0,0,0,0,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 81
		[
		 1,1,1,4,0,0,4,1,1,1,
		 1,1,1,4,X,X,4,1,1,1,
		 X,1,1,4,0,0,4,1,1,X,
		 X,1,1,4,X,X,4,1,1,X,
		 X,1,1,4,0,0,4,1,1,X,
		 X,1,1,1,1,1,1,1,1,X,
		],

		// WAVE 82
		[
		 6,6,6,6,6,6,6,6,6,6,
		 X,X,X,X,X,X,X,X,X,X,
		 0,0,0,0,X,X,0,0,0,0,
		 3,3,3,0,X,X,0,3,3,3,
		 3,3,3,0,X,X,0,3,3,3,
		 0,0,0,0,X,X,0,0,0,0,
		],

		// WAVE 83
		[
		 X,X,X,X,9,9,X,X,X,X,
		 X,9,9,X,9,9,X,9,9,X,
		 X,9,9,X,X,X,X,9,9,X,
		 X,X,X,X,9,9,X,X,X,X,
		 X,9,9,X,9,9,X,9,9,X,
		 X,9,9,X,X,X,X,9,9,X,
		],

		// WAVE 84
		[
		 X,8,8,X,0,0,X,8,8,X,
		 X,8,8,X,0,0,X,8,8,X,
		 X,X,X,X,0,0,X,X,X,X,
		 X,X,X,X,0,0,X,X,X,X,
		 X,8,8,X,0,0,X,8,8,X,
		 X,8,8,1,1,1,1,8,8,X,
		],

		// WAVE 85
		[
		 0,0,X,2,3,3,2,X,0,0,
		 0,0,X,2,3,3,2,X,0,0,
		 X,X,X,2,3,3,2,X,X,X,
		 2,2,2,2,3,3,2,2,2,2,
		 4,4,4,4,4,4,4,4,4,4,
		 5,5,6,X,X,X,X,6,5,5,
		],

		// WAVE 86
		[
		 4,4,4,4,5,5,6,6,6,6,
		 X,7,X,7,X,X,7,X,7,X,
		 X,7,8,7,X,X,7,8,7,X,
		 X,7,8,7,X,X,7,8,7,X,
		 X,X,8,X,9,9,X,8,X,X,
		 9,X,X,X,9,9,X,X,X,9,
		],

		// WAVE 87
		[
		 X,X,X,3,3,3,3,X,X,X,
		 1,1,1,6,6,6,6,1,1,1,
		 6,6,6,6,6,6,6,6,6,6,
		 6,6,6,0,0,0,0,6,6,6,
		 0,0,0,X,X,X,X,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 88
		[
		 0,X,X,5,X,X,5,X,X,0,
		 0,0,X,5,5,5,5,X,0,0,
		 0,0,0,3,4,4,3,0,0,0,
		 X,0,0,3,4,4,3,0,0,X,
		 X,X,0,3,4,4,3,0,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 89
		[
		 0,X,X,0,X,X,0,X,X,0,
		 0,0,0,0,X,X,0,0,0,0,
		 0,6,6,0,X,X,0,6,6,0,
		 X,6,6,X,2,2,X,6,6,X,
		 X,6,6,X,3,3,X,6,6,X,
		 X,6,6,X,4,4,X,6,6,X,
		],

		// WAVE 90
		[
		 4,5,6,7,X,X,7,6,5,4,
		 5,5,6,7,X,X,7,6,5,5,
		 6,6,6,7,X,X,7,6,6,6,
		 7,7,7,7,X,X,7,7,7,7,
		 0,0,X,0,0,0,0,X,0,0,
		 X,0,0,0,X,X,0,0,0,X,
		],

		// WAVE 91
		[
		 X,9,9,9,X,X,9,9,9,X,
		 9,9,9,9,9,9,9,9,9,9,
		 0,X,X,X,0,0,X,X,X,0,
		 0,0,X,0,0,0,0,X,0,0,
		 X,0,0,0,X,X,0,0,0,X,
		 X,X,0,X,X,X,X,0,X,X,
		],

		// WAVE 92
		[
		 9,9,X,X,X,X,X,X,9,9,
		 7,9,9,X,X,X,X,9,9,7,
		 X,7,9,9,X,X,9,9,7,X,
		 X,X,7,9,9,9,9,7,X,X,
		 X,X,X,7,9,9,7,X,X,X,
		 X,X,X,X,8,8,X,X,X,X,
		],

		// WAVE 93
		[
		 8,8,8,8,8,8,8,8,8,8,
		 9,9,9,9,9,9,9,9,9,9,
		 X,X,6,6,6,6,6,6,X,X,
		 X,X,6,6,6,6,6,6,X,X,
		 X,X,X,X,4,4,X,X,X,X,
		 X,X,X,X,4,4,X,X,X,X,
		],

		// WAVE 94
		[
		 9,9,9,9,9,9,9,9,9,9,
		 9,9,9,9,9,9,9,9,9,9,
		 9,9,8,8,8,8,8,8,9,9,
		 9,9,8,X,X,X,X,8,9,9,
		 9,9,8,X,X,X,X,8,9,9,
		 9,9,8,X,X,X,X,8,9,9,
		],

		// WAVE 95
		[
		 9,9,6,0,X,X,0,6,9,9,
		 9,9,6,0,X,X,0,6,9,9,
		 6,6,6,0,X,X,0,6,6,6,
		 0,0,0,0,0,0,0,0,0,0,
		 X,X,X,X,X,X,X,X,X,X,
		 2,2,2,2,2,2,2,2,2,2,
		],

		// WAVE 96
		[
		 1,6,3,4,9,3,2,6,5,8,
		 7,4,2,3,7,6,4,5,7,3,
		 0,4,3,2,4,3,7,8,3,0,
		 4,2,3,7,2,7,4,7,4,6,
		 3,2,5,2,7,6,8,5,6,7,
		 3,6,7,5,4,6,5,7,9,4,
		],

		// WAVE 97
		[
		 1,1,6,2,6,2,6,3,3,3,
		 1,6,1,2,6,2,6,3,6,6,
		 1,6,1,2,6,2,6,3,6,6,
		 1,1,6,6,2,6,6,3,3,6,
		 1,6,1,6,2,6,6,3,6,6,
		 1,1,1,6,2,6,6,3,3,3,
		],

		// WAVE 98
		[
		 0,0,1,1,1,1,1,1,0,0,
		 0,0,3,3,3,3,3,3,0,0,
		 0,0,4,4,5,5,4,4,0,0,
		 0,0,4,4,5,5,4,4,0,0,
		 6,6,4,4,5,5,4,4,6,6,
		 X,X,6,6,6,6,6,6,X,X,
		],

		// WAVE 99
		[
		 6,6,0,0,0,0,0,0,6,6,
		 6,6,6,6,6,6,6,6,6,6,
		 6,6,6,6,6,6,6,6,6,6,
		 8,8,8,8,6,6,8,8,8,8,
		 X,X,X,X,8,8,X,X,X,X,
		 X,X,X,X,X,X,X,X,X,X,
		],

		// WAVE 100
		[
		 9,9,9,9,6,6,9,9,9,9,
		 9,9,9,9,9,9,9,9,9,9,
		 9,9,9,9,9,9,9,9,9,9,
		 8,8,8,8,8,8,8,8,8,8,
		 8,8,8,8,8,8,8,8,8,8,
		 9,9,9,9,9,9,9,9,9,9,
		],
	];

	static public var m_bullets:Array = new Array;
	static public var stalkers:int = 0;
	static public var level:int = 1;

	private var m_invaders:Array = new Array;

	private var m_min:int = 999;
	private var m_max:int = -99;
	private var m_dx:int = 1;
	private var m_dy:int = 0;
	private var m_traverse:int = 0;

	public function create():void
	{
		var i:int;
		Invaders.stalkers = 0;
		Invaders.m_bullets.length = 0;
		for (i = 0; i < 128; ++i) {
			var oneBullet:FlxSprite = new FlxSprite(420, -100);
			oneBullet.loadGraphic(img_InvaderBullet);
			oneBullet.visible = false;
			add(oneBullet);
			Invaders.m_bullets.push(oneBullet);
		}
		create_invaders();
	}

	public function create_invaders():void
	{
		var level:int = Manager.level;
		level -= 1;
		level %= WAVES.length;
		m_invaders.length = 0;
		for (var i:int = 0; i < WAVES[level].length; ++i) {
			if (WAVES[level][i] != -1){
				var invader:Invader = new Invader(32 + (i%10)*26, 36 + (int(i/10))*26, WAVES[level][i]);
				m_invaders.push(add(invader));
			}
		}
	}

	override public function update():void
	{
		super.update();
		var i:int;

		m_min = 999;
		m_max = -99;

		// find min and max on x axis of invaders
		if (m_dx == 1) {
			for (i = 0; i < m_invaders.length; ++i)
				if (!m_invaders[i].dead && m_invaders[i].baseX+16 > m_max)
					m_max = m_invaders[i].baseX+16;

			if (m_max > 314) {
				m_dx = -1;
				m_dy = 2;
			}
		} else {
			for (i = 0; i < m_invaders.length; ++i)
				if (!m_invaders[i].dead && m_invaders[i].baseX < m_min)
					m_min = m_invaders[i].baseX;

			if (m_min < 6) {
				m_dx = 1;
				m_dy = 2;
			}
		}

		if (m_traverse > 1) {
			for (i = 0; i < m_invaders.length; ++i)
				m_invaders[i].add_to_base(m_dx, 0);

			m_traverse = 0;
		}

		if (m_dy != 0) {
			for (i = 0; i < m_invaders.length; ++i)
				m_invaders[i].add_to_base(0, m_dy);

			m_dy = 0;
		}

		m_traverse += 1;

		for (i = 0; i < Invaders.m_bullets.length; ++i) {
			if (Invaders.m_bullets[i].y > 240) {
				Invaders.m_bullets[i].velocity.y = 0;
				Invaders.m_bullets[i].visible = false;
				Invaders.m_bullets[i].x = 420;
				Invaders.m_bullets[i].y = -100;
			}
		}
	}

	static public function fire_bullet(x:int, y:int):void
	{
		for (var i:int = 0; i < Invaders.m_bullets.length; ++i) {
			if (Invaders.m_bullets[i].visible == false) {
				Invaders.m_bullets[i].x = x + 8 - 2;
				Invaders.m_bullets[i].y = y + 6
				Invaders.m_bullets[i].velocity.y = 125;
				Invaders.m_bullets[i].visible = true;
				break;
			}
		}

	}

	static public function can_stalk():Boolean
	{
		return Invaders.stalkers < Invaders.level;
	}

	public function destroyed():Boolean
	{
		for (var i:int = 0; i < m_invaders.length; ++i)
			if (!m_invaders[i].dead)
				return false;
		return true;
	}

}
} // package