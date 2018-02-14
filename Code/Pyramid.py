def sqrt(n):
    return n**(1/2.0)
class Pyramid:
    l = 0
    w = 0
    h = 0
    def __init__(self, l, w, h):
      self.l = l
      self.w = w
      self.h = h
    def calcvolume(self):
        l = self.l
        w = self.w
        h = self.h
        print("The volume equals - ", str((l*w*h)/3))
    def calcsurface(self):
        l = self.l
        w = self.w
        h = self.h
        print("The surface area equals - ", str(str((l*w)+(l*sqrt((w/2.0)**2 +h**2)) + (w*sqrt((l/2.0)**2 +h**2)))))
