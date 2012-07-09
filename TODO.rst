- add visible walls
    - single Item, shape is multiple rectangles?
- collision detection:
    - cheat on collision response: Invert (perp?) velocity & set pos = prev pos
- camera zoom and aspect ratio compensation
- control for standard application controls (fullscreen, vsync, fps)
- add start game screen
- tank treads:
    - model may be 'attached to' another model. view collection stores this
      as a tree, so that matrices can be applied cumulatively. Or maybe each
      item has an 'items' collection, just like the world.
- tank turret
- tank can fire
- explosion
- enemy tanks
- shots destroy tanks
- respawn the player
- add sounds: fire, shoot wall, tank explode, tank drive
- add score


speculative
===========
- Beware of controllers that reference a model which has been removed
- world provides .items('aspect') which returns set of items filtered by
  those that have given attribute. (this instead of filtered by class as
  done in SinisterDucks.)
- instead of nearest neighbour, don't scale the bitmap, and use linear.
  Provides a blocky look, but still AA the edges between blocks.

done
====
- Add 'player' item, with sprite image name
- world sends 'add item' signal
- view converts image name into sprite
- move png to data dir
- test data dir on installed package
- resource manager loads all images files at startup, makes accessible by name
- try some transparent pixels
- try rendering with nearest-neighbour
- player position & rotation is used to render sprite
- Try lepton instead:
  pyglet sprites are (a) integer co-ord only, which looks bad for very slow
  moving or rotating sprites, especially small ones. (b) creates new ctypes
  array of sprite positions to send to GPU after each move and after each
  rotation. Ultradumb.
- model update methods are actually controllers:
- Consider ordering calls to controllers (e.g. update positions first)
    - control which converts tank state to tank velocity
        (particular to tanks)
    - control which processes player input, converts keys to tank states
        (particular to player-controlled tank)
- Need a collection of controllers so that we can call each one (?) every frame.
- start_game is another control

