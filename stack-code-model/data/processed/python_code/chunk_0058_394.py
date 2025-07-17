package zombie.entities 
{
    import net.flashpunk.Entity;
    import net.flashpunk.graphics.Spritemap;
    import zombie.Assets;
	/**
     * ...
     * @author ...
     */
    public class OldMan extends Entity
    {
        private var _isZombie : Boolean;
        public var sprite : Spritemap;
        
        public function OldMan( x:Number = 0, y:Number = 0 ) 
        {
            super(x, y);
            
            sprite = new Spritemap(Assets.SPRITE_OLDMAN, 195, 163);
			sprite.add("normal", [0, 1, 2], 10, true);
			sprite.add("zombie", [3, 4, 5], 10, true);
            sprite.play("normal");
            sprite.scrollX = sprite.scrollY = 0;
            sprite.scale = 0.33
            
            width = 195 * sprite.scale;
            height = 163 * sprite.scale;
            
            graphic = sprite;
        }
        
        public function setEvil(evil : Boolean) : void
		{
        if ( evil )
			{
                sprite.play("zombie");
			}
			else
			{
				sprite.play("normal");
			}
			
			_isZombie = evil;
		}
    }

}