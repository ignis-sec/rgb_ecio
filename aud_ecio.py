
import math
import asyncio
from .audio_loopback.audio_loopback import AudioController
from .audio_loopback.audio_visualizer import AudioVisualizer1D
import allogate as logging

class ECIOAudioVisualizer(AudioVisualizer1D):
    def __init__(self, chroma_app, audio_controller=None, fade=0.8, delay=0.0, dampen=0, ceiling=180, ambient_brightness_coef=0.1):
         super().__init__(chroma_app, audio_controller, fade, delay, dampen, ceiling, ambient_brightness_coef)

    def visualizeOnce(self, falloff=0.8, rows=5, col=50):
        """ Visualize current levels of audio on the razer devices, and render it
        """
        super().visualizeOnce(falloff,rows,col)
        self.device_controller.update_color(self.device_controller.r,self.device_controller.g,self.device_controller.b)

    async def change_color(self, r,g,b):
        self.device_controller.fade(r,g,b)


