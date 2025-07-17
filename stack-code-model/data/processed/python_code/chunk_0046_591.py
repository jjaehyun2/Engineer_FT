/**
 * Created by vizoli on 4/8/16.
 */
package ageofai.layout.view.view
{
    import ageofai.game.event.GameEvent;

    import common.mvc.view.base.ABaseMediator;

    public class LayoutMediator extends ABaseMediator
    {
        override public function initialize():void
        {
            this.dispatch( new GameEvent( GameEvent.INIT_GAME ) );
        }
    }
}