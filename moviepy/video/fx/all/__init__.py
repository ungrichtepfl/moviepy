"""
Loads all the fx !
Usage:
import moviepy.video.fx.all as vfx
clip = vfx.resize(some_clip, width=400)
clip = vfx.mirror_x(some_clip)
"""

import pkgutil

import moviepy.video.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

# Pyinstaller does not support the exec command during scanning of the file
# for name in __all__:
#     exec("from ..%s import %s" % (name, name))

# import them statically:
from ..accel_decel import accel_decel
from ..blackwhite import blackwhite
from ..blink import blink
from ..colorx import colorx
from ..crop import crop
from ..even_size import even_size
from ..fadein import fadein
from ..fadeout import fadeout
from ..freeze import freeze
from ..freeze_region import freeze_region
from ..gamma_corr import gamma_corr
from ..headblur import headblur
from ..invert_colors import invert_colors
from ..loop import loop
from ..lum_contrast import lum_contrast
from ..make_loopable import make_loopable
from ..margin import margin
from ..mask_and import mask_and
from ..mask_color import mask_color
from ..mask_or import mask_or
from ..mirror_x import mirror_x
from ..mirror_y import mirror_y
from ..painting import painting
from ..resize import resize
from ..rotate import rotate
from ..scroll import scroll
from ..speedx import speedx
from ..supersample import supersample
from ..time_mirror import time_mirror
from ..time_symmetrize import time_symmetrize
