/*
 * @author Ryan C. Knaggs
 * @date 04/30/2007
 * @description: Channel listener interface
 * Every time you add a new channel.  The channel
 * will be added to an array of channels stored
 * in the channel manager class object.
 * @see ChannelManager.as
 * This interface is used when you use the
 * addListener method.
 */


package eventexchange {
	public interface IEventListener {
		function update(e:Object):void;
	}
}