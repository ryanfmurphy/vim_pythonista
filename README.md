NOTE: This does not provide a way to actually use vim commands in Pythonista - my current aim is to create a way of emulating some vim macros through Python code, but I don't really know of a way to build in extra keyboard shortcuts into the Pythonista editor.

Some very basic and not-yet totally correct vim-like behaviors within the Pythonista editor. These are implemented as python functions with names the same as the normal-mode commands, e.g. i() to go into insert mode (which doesn't really mean anything yet) or w() to advance forwards a word.

Implemented so far:

o / O : open a line above or below
w / W / e / E / b / B : forward & back by 1 word or Word.  WARNING: incomplete / not yet compatible with native vim behavior

