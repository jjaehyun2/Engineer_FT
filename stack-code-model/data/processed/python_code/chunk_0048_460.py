package 
{
	/**
	 * ...
	 * @author Reece Clydesdale
	 */
	import flash.events.Event;
	import flash.media.SoundChannel;
	import flash.media.Sound;
	import flash.utils.Timer;
	
	public class MusicPlayer
	{
		private var channel : SoundChannel;
		private var track : Sound;
		
		private var trackPosition : Number;
		
		private var tracks : Array;
		private var trackNames : Array;
		
		private var trackName : String;
		
		private var isPlaying : Boolean;
		private var isPaused : Boolean;
		
		public function play() : void
		{
			if (!isPlaying)
			{
				if (track == null)
				{
					setRandomTrack();
				}
				channel = track.play(trackPosition);
				isPlaying = true;
				isPaused = false;
			}
		}
		
		public function pause() : void
		{
			if (isPlaying)
			{
				trackPosition = channel.position;
				channel.stop();
				isPaused = true;
				isPlaying = false;
			}
		}
		
		public function setTrack(sound : Sound) : void
		{
			track = sound;
			for (var i : int = 0; i < this.tracks.length; i++)
			{
				if (this.tracks[i] == sound)
				{
					this.trackName = this.trackNames[i];
				}
			}
			
			if (isPlaying)
			{
				this.stop();
				this.play();
			}
			if (isPaused)
			{
				this.trackPosition = 0;
			}
		}
		
		public function stop() : void
		{
			if (isPlaying)
			{
				if (channel != null)
				{
					channel.stop();
				}
				trackPosition = 0;
				
				this.isPlaying  = false;
			}
		}
		
		public function addTrack(sound : Sound, trackName : String) : void
		{
			tracks.push(sound);
			trackNames.push(trackName);
		}
		
		public function setRandomTrack() : void
		{
			var id : int;
			do
			{
				id = Math.floor(tracks.length * Math.random());
			} while (track == tracks[id] && tracks.length > 1);
			
			setTrack(tracks[id]);
		}
		
		public function getTrackName() : String
		{
			return trackName;
		}
		
		public function getProgress() : Number
		{
			if (this.channel != null && this.track != null)
			{
				return (this.channel.position / this.track.length);
			}
			return 0;
		}
		
		public function handleTimerEventSongAlive(e : Event) : void
		{
			var oldTrack : Sound = this.track;
			if (this.isPlaying)
			{
				if (this.channel.position >= this.track.length)
				{
					this.channel.stop();
					do {
						this.setRandomTrack();
					} while (this.track == oldTrack && this.tracks.length != 1);
					
					this.play();
				}
			}
		}
		
		public function MusicPlayer()
		{
			this.tracks = [];
			this.trackNames = [];
			var timer : Timer = new Timer(1000);
			timer.addEventListener("timer", handleTimerEventSongAlive);
			timer.start();
		}
		
	}

}