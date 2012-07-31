- word.add can update attributes to the item, use this to set player
  position and angle on insertion
- glyph should use index array
- I think attributes of glyph class are no longer required. Can we remove the
  class and use a function which returns VAO id?
- refactor glyph.create function
- add sound: tank drive
- collision detection
    - player needs a collision rect defining
- cheat on collision response: Invert (perp?) velocity & set pos = prev pos
- control for standard application controls (fullscreen, vsync, fps)
- add cursor keys too
- tank can fire
    - firing sound effect
- explosion when shot hits anything
- enemy tanks exist
- shots destroy tanks
    - destroy animation
    - destroy sound effect
    - respawn in furthest spawn point
    - leave old broken tank behind?
- add start game screen
- add score
- juice: zoom/fade in at start
- juice: tank spawn effect
- key to reset tank positions and scores to zero
    - advertise on start screen


speculative
-----------
- tank treads:
    - model may be 'attached to' another model. view collection stores this
      as a tree, so that matrices can be applied cumulatively. Or maybe each
      item has an 'items' collection, just like the world.
    - or just pre-create all possible combinations of left/right tread posns.
- consider optimising the render of walls into a single draw call

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
- replace tank bitmap with copy of tank from 'Combat'
- add visible walls - one Item per wall
- camera zoom and aspect ratio compensation
    ATARIVCS: 4:3 screen, court 642 x 480, in 16x16 squares, gives 40x30
    screens commonly:
        4:3, e.g. 800x600
        16:10, e.g. 1680x1050 (my mac), height into 30 gives width of 48
        16:9, e.g. ?
- choose proper colors. pass them in from level construct. incorporate
  colortuple package.

