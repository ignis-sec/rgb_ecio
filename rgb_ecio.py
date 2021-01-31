from ctypes import *
from .audio_loopback.audio_loopback import *
import allogate as logging
import os 


class ECIOController:
    def __init__(self, port=104, page=7,r_addr=73, g_addr=74, b_addr=75,calibration_r=55, calibration_g=255, calibration_b=120):
        self.ecio = WinDLL(f"{os.path.dirname(os.path.realpath(__file__))}/ECIO.dll")
        self.ecio.LoadDriver()

        self.port = port
        self.lightbar_page = page
        self.lightbar_r_addr = r_addr
        self.lightbar_g_addr = g_addr
        self.lightbar_b_addr = b_addr

        self.r=0
        self.g=0
        self.b=0
        self.coef = 1
        self.calibration_r=calibration_r/255
        self.calibration_g=calibration_g/255
        self.calibration_b=calibration_b/255
    
    def set_ECIO_color(self,r,g,b):
        r = c_uint8(int(r/256*36*self.calibration_r))
        g = c_uint8(int(g/256*36*self.calibration_g))
        b = c_uint8(int(b/256*36*self.calibration_b))
        ret = self.ecio.OemSetECRAMPage(c_uint8(self.port), c_uint8(self.lightbar_page), c_uint8(self.lightbar_r_addr),r)
        ret = self.ecio.OemSetECRAMPage(c_uint8(self.port), c_uint8(self.lightbar_page), c_uint8(self.lightbar_g_addr),g)
        ret = self.ecio.OemSetECRAMPage(c_uint8(self.port), c_uint8(self.lightbar_page), c_uint8(self.lightbar_b_addr),b)

    def fade(self,r,g,b, step=1):
        """ Fade from current color to target, gradually
        """
        logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 5)
        while True:
            logging.pprint(f"Fading to {r},{g},{b} from {self.r},{self.g},{self.b}", 5)
            if(abs(self.r-r)<step): self.r=r
            if(r>self.r): self.r+=step
            elif(r<self.r): self.r-=step

            if(abs(self.r-r)<step): self.g=g
            if(g>self.g):self.g+=step
            elif(g<self.g): self.g-=step
            
            if(abs(self.r-r)<step): self.b=b
            if(b>self.b):self.b+=step
            elif(b<self.b): self.b-=step

            self.update_color(self.r, self.g, self.b)
            if(r == self.r and g == self.g and b==self.b): return
    
    def set(self,r,g,b):
        """ Instantly set color
        """
        self.r = r
        self.g = g
        self.b = b
        self.update_color(self.r, self.g, self.b)

        def update_color(self, r, g, b):
            """ Update and render colors
        """
        logging.pprint(f"setting color to {r},{g},{b}", 5)
        #if(self.delay):
        #    time.sleep(self.delay)
        r= int(r*self.coef)
        g= int(g*self.coef)
        b= int(b*self.coef)


        if(r>255): r=255
        if(g>255): g=255
        if(b>255): b=255

        if(r<0): r=0
        if(g<0): g=0
        if(b<0): b=0

        self.set_ECIO_color(r,g,b)

    def update_color(self, r, g, b):
        """ Update and render colors
        """
        #print(r,g,b)
        logging.pprint(f"setting color to {r},{g},{b}", 5)
        #if(self.delay):
        #    time.sleep(self.delay)
        r= int(r*self.coef)
        g= int(g*self.coef)
        b= int(b*self.coef)


        if(r>255): r=255
        if(g>255): g=255
        if(b>255): b=255

        if(r<0): r=0
        if(g<0): g=0
        if(b<0): b=0
        self.set_ECIO_color(r,g,b)

ec = ECIOController()

ec.set_ECIO_color(255,255,255)