# Terminal Play v 1.0.0
<p float="left">
 <img src="https://komarev.com/ghpvc/?username=merwin-terminal-play&label=Project%20Views-Github&color=0e75b6&style=flat" alt="darkmash-org" /> 
<img alt="" src="https://static.pepy.tech/personalized-badge/terminalplay?period=total&units=international_system&left_color=blue&right_color=orange&left_text=Downloads">

</p>

Python Module for playing videos in terminal !! 

-  Works on both windows and linux :)


## Installation

```sh
pip install terminalplay
```


## Usage

```python
from terminalplay import *

# Load the video , this may take time on the first run (for a specific video)
tp = TerminalPlay("test.mp4", div=0.4)  # Div is for reducing the size of the frame , default 0.5
tp.play() # Plays the video
```
