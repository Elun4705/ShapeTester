import Box
import Sphere
import Pyramid

myShape = input("Select the shape to calculate: Box = b, Sphere = s, Pyramind = p - ")

if myShape == 'b':
    l = int(input("Print your Length of box - "))
    w = int(input("Print your Width of box - "))
    h = int(input("Print your Height of box - "))
    b = Box.Box(l,w,h)
    print(b.calcvolume())
    print(b.calcsurface())
elif myShape == 's':
    r = int(input("Print your Radius of sphere - "))
    s = Sphere.Sphere(r)
    print(s.calcvolume())
    print(s.calcsurface())

elif myShape == 'p':
    l = int(input("Print your Length of pyramid - "))
    w = int(input("Print your Width of pyramid - "))
    h = int(input("Print your Height of pyramid - "))
    p = Pyramid.Pyramid(l,w,h)
    print(p.calcvolume())
    print(p.calcsurface())
