"""
Loads all the fx !
Usage:
import moviepy.audio.fx.all as afx
audio_clip = afx.volume_x(some_clip, .5)
"""

import pkgutil

import moviepy.audio.fx as fx

__all__ = [name for _, name, _ in pkgutil.iter_modules(
    fx.__path__) if name != "all"]

# Pyinstaller does not support the exec command during scanning of the file
# for name in __all__:
#     exec("from ..%s import %s" % (name, name))

# import them statically:
from ..audio_fadein import audio_fadein
from ..audio_fadeout import audio_fadeout
from ..audio_left_right import audio_left_right
from ..audio_loop import audio_loop
from ..audio_normalize import audio_normalize
from ..volumex import volumex
