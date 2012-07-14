- Big insight: for glyphs, either 2D or 3D, specifying indices is not required
  on the input, just colors and loops of positions.

    Idea of specifying indices is to let the shape design share a vertex
    between one poly and another.
    
    In polyhedra, this never happens, because although corners is re-used
    by all adjacent faces, the normals are different, so separate vertices for
    each face are required.

    The only vertex reuse comes in due to tesselating individual faces into
    triangles - and this step can be done automatically during Glyph
    construction.

    In 3D patches (curved surfaces) then we do share normals, but I don't
    plan on supporting these, and even if I was, I'm far from certain what
    the best input format should be.

    In 2d polygons, vertices are:
      - Not re-used within a single polygon (except by tesselation)
      - Not re-used by different polygons of different colors, because
            colors differ betwen vertices
      - Might be re-used if different polygons of the same color touch
        each other. e.g. two triangles in a butterfly. Is this common?

        Is the efficiency of catering to this case worth the cost of
        complicating input for all cases? Can this re-use be automatically
        detected by comparing if the vertex position equal to any used before?
        I think it can.

    But does that actually put a burden on the shape designer, to re-specify
    the same positions over and over? I don't *think* so.

    So input goes from:

        [p1, p2, p3...]
        [
            (color, [i1, i2, i3...])
            ...
        ]

    To:

        [
            (color, [p1, p2, p3...])
            ...
        ]

- add visible walls - one Item per wall
- replace tank bitmap with copy of tank from 'Combat'
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
- consider optimising the render of walls into a single draw call


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
- Rect should be function rect.create(), which returns a list of verts

