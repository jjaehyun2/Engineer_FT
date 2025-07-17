class ZCL_ARDRONE_CONTROL definition
  public
  final
  create public .

public section.
*"* public components of class ZCL_ARDRONE_CONTROL
*"* do not include other source files here!!!

  class-data NAVDATA type ZARDRONE_NAVDATA read-only .

  class-methods ROLL_RIGHT .
  class-methods ROLL_LEFT .
  class-methods PITCH_UP .
  class-methods PITCH_DOWN .
  class-methods YAW_RIGHT .
  class-methods YAW_LEFT .
  class-methods GAZ_UP .
  class-methods GAZ_DOWN .
  class-methods LAUNCH .
  class-methods LAND .
  class-methods HOVER .
  class-methods SNAPSHOT .
  class-methods UP .
  class-methods DOWN .
  class-methods SPIN_LEFT .
  class-methods SPIN_RIGHT .
  class-methods SHUFFLE .
  class-methods REFRESH .
*"* protected components of class ZCL_ARDRONE_CONTROL
*"* do not include other source files here!!!
protected section.
private section.
*"* private components of class ZCL_ARDRONE_CONTROL
*"* do not include other source files here!!!

  constants CO_ROLL_RIGHT type STRING value 'D'. "#EC NOTEXT
  constants CO_ROLL_LEFT type STRING value 'A'. "#EC NOTEXT
  constants CO_PITCH_UP type STRING value 'W'. "#EC NOTEXT
  constants CO_PITCH_DOWN type STRING value 'S'. "#EC NOTEXT
  constants CO_YAW_RIGHT type STRING value 'LeftArrow'. "#EC NOTEXT
  constants CO_YAW_LEFT type STRING value 'Right'. "#EC NOTEXT
  constants CO_GAZ_UP type STRING value 'Up'. "#EC NOTEXT
  constants CO_GAZ_DOWN type STRING value 'DownArrow'. "#EC NOTEXT
  constants CO_LAUNCH type STRING value 'Return'. "#EC NOTEXT
  constants CO_LAND type STRING value 'Return'. "#EC NOTEXT
  constants CO_HOVER type STRING value 'NumPad0'. "#EC NOTEXT
  constants CO_EMERGENCY type STRING value 'Space'. "#EC NOTEXT
  constants CO_CAMERA type STRING value 'C'. "#EC NOTEXT

  class-methods SEND_COMMAND
    importing
      !COMMAND type STRING .
ENDCLASS.



CLASS ZCL_ARDRONE_CONTROL IMPLEMENTATION.


method DOWN.
 send_command( 'D6' ).
endmethod.


method GAZ_DOWN.
 send_command( co_gaz_down ).
endmethod.


method GAZ_UP.
 send_command( co_gaz_up ).
endmethod.


method HOVER.
 send_command( co_hover ).
endmethod.


method LAND.
 send_command( co_land ).
endmethod.


method LAUNCH.
  send_command( co_launch ).

  WAIT UP TO 2 SECONDS.

  hover( ).


endmethod.


method PITCH_DOWN.
 send_command( co_pitch_down ).
endmethod.


method PITCH_UP.
 send_command( co_pitch_up ).
endmethod.


method REFRESH.
   send_command( 'REFRESH' ).
endmethod.


method ROLL_LEFT.
 send_command( co_roll_left ).
endmethod.


method ROLL_RIGHT.
 send_command( co_roll_right ).
endmethod.


method SEND_COMMAND.

      CALL FUNCTION 'ZARDRONE_PROXY'
        DESTINATION 'ARDRONE'
        EXPORTING
          command               = command
        IMPORTING
          altitude              = navdata-altitude
          batterylevel          = navdata-batterylevel
          phi                   = navdata-phi
          psi                   = navdata-psi
          theta                 = navdata-theta
          vx                    = navdata-vx
          vy                    = navdata-vy
          vz                    = navdata-vz
          imagefile             = navdata-imagefile
        EXCEPTIONS
          system_failure        = 1
          communication_failure = 2
          OTHERS                = 3.

endmethod.


method SHUFFLE.
 send_command( 'D5' ).
endmethod.


method SNAPSHOT.
 send_command( 'D4' ).
endmethod.


method SPIN_LEFT.
 send_command( 'D8' ).
endmethod.


method SPIN_RIGHT.
 send_command( 'D9' ).
endmethod.


method UP.
 send_command( 'D7' ).
endmethod.


method YAW_LEFT.
 send_command( co_yaw_left ).
endmethod.


method YAW_RIGHT.
 send_command( co_yaw_right ).
endmethod.
ENDCLASS.