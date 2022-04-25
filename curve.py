import math
from PIL import Image
from PIL import ImageDraw

image = Image.new('RGB', (1190, 841), 'white')
draw = ImageDraw.Draw(image)
curve_smoothness = 100

# First, select start and end of curve (pixels)
# curve_start = [(167, 688)] ## this would be the current x,y
# curve_end = [(678, 128)]


# controlX, controlY, curve_endX, curveendY, smoothness
def curveTo(currentX, currentY, curve_endX, curve_endY, smoothness=100):
    curve = []
    split = (curve_endX - currentX) / smoothness
    for i in range(1, smoothness):
        x = currentX + (split * i)
        curve.append(
            (x, (-7 * math.pow(10, -7) * math.pow(x, 3) -
             0.0011 * math.pow(x, 2) + 0.235 * x + 682.68))
        )
    return [currentX, currentY] + curve + [curve_endX, curve_endY]


newCurve = curveTo(167, 688, 678, 128)


# Third, edit any other corners of polygon
other = [(1026, 721), (167, 688)]

# Finally, combine all parts of polygon into one list
# putting all parts of the polygon together
xys = [(167, 688)] + newCurve + [(678, 128)] + other
draw.polygon(xys, fill=None, outline=256)

image.show()
