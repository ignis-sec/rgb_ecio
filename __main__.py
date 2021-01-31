from .rgb_ecio import *
from .aud_ecio import ECIOAudioVisualizer
import asyncio


e = ECIOController()
vis = ECIOAudioVisualizer(e)

e.set(255,255,255)
asyncio.run(vis.visualize())