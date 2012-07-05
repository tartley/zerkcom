- test data dir on installed package
- try some transparent pixels
- view stores sprite in its own collection
- player is rendered using nearest-neighbour
- player is controllable by keyboard (input is a type of control)
- start_game is another control
- control for standard application controls (fullscreen, vsync, fps)
- add visible walls
    - single Item, shape is multiple rectangles
- model update methods are actually controllers:
  Need a collection of controllers so that we can call each one (?) every frame.
  Beware of controllers that reference a model which has been removed
  Consider ordering calls to controllers (e.g. update positions first)
  Consider only calling the ones that are not 'asleep'
    - control which processes player input, converts keys to tank states
        (particular to player-controlled tank)
    - control which converts tank state to tank velocity
        (particular to tanks)
    - control which adds: pos += vel
        (general to all moving things)
- camera zoom and aspect ratio compensation
- collision detection:
    - cheat on collision response: Invert (perp?) velocity & set pos = prev pos
- add start game screen
- bitmaps on each rect, all from the same imageatlas
- tank treads, tank turret:
    - model may be 'attached to' another model. view collection stores this
      as a tree, so that matrices can be applied cumulatively. Or maybe each
      item has an 'items' collection, just like the world.
- enemy tanks
- add score
- add a sound: tank drive

speculative
===========
- world provides .items('aspect') which returns set of items filtered by
  those that have given attribute. (this instead of filtered by class as
  done in SinisterDucks.)

done
====
- Add 'player' item, with sprite image name
- world sends 'add item' signal
- view converts image name into sprite
- move png to data dir
