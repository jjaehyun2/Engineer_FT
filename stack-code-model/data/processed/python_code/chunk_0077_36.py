// Fig. 17.2: BoxCode.as
// Object animation in ActionScript.
package 
{
   import flash.events.MouseEvent; // import MouseEvent class
   import flash.display.MovieClip; // import MovieClip class
 
   public class BoxCode extends MovieClip
   {
      // create two new box objects
      public var box1 = new Box();
      public var box2 = new Box();
     
      // initialize Box coordinates, add Boxes
      // to the stage and register MOUSE_DOWN event handler
      public function BoxCode() : void
      {
         box1.x = 15; // set box1's x-coordinate
         box1.y = 20; // set box1's y-coordinate
         box2.x = 115; // set box2's x-coordinate
         box2.y = 20; // set box2's y-coordinate
         
         addChild( box1 ); // add box1 to the stage
         addChild( box2 ); // add box2 to the stage

         // handleClick is called when box1 is clicked
         box1.addEventListener( MouseEvent.MOUSE_DOWN, handleClick );
      } // end BoxCode constructor

      // move box2 5 spaces to the left whenever box1 is clicked
      private function handleClick( args : MouseEvent )
      {
         box2.x -= 5;
      } // end function handleClick
   } // end class BoxCode 
} // end package