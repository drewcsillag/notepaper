import sys


print( """<svg height="850" width="1100">""")
offset = 11

mmToHundthsInch = 1 / .254

hundint = (offset * mmToHundthsInch)

margin = 8.5 * mmToHundthsInch

linePitchMm = 6.5 * 1.5 #mm

strokeWidth = 1.5625 / 2

rightLeftMargin = 550 + margin
rightCenterLine = 550 * 1.5
rightRightMargin = 1100 - margin
leftLeftMargin = margin
leftCenterLine = 550 / 2
leftRightMargin = 550 - margin

def findEndOffset():
    global offset
    toff = offset
    hundint = toff * mmToHundthsInch
    while hundint < 850.0:
        toff += linePitchMm
        hundint = toff * mmToHundthsInch

    return toff

endOffset = findEndOffset()



# left center line
print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    leftCenterLine + 16.5, 11 * mmToHundthsInch,
    leftCenterLine + 16.5, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))

# left center line
print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    leftLeftMargin+33, 11 * mmToHundthsInch,
    leftLeftMargin+33, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))

# right center line
print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    rightCenterLine + 16.5, 11 * mmToHundthsInch,
    rightCenterLine + 16.5, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))

# right right of number
print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    rightLeftMargin+33, 11 * mmToHundthsInch,
    rightLeftMargin+33, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))

def padno(x):
    if x < 10:
        return "&nbsp;" + repr(x)
    return repr(x)

counter = 7
while hundint < 850.0:
    sys.stderr.write("hundint %f\n" % hundint)
    if counter >= 9 and counter <= 16:
        sw = strokeWidth
    else:
        sw = strokeWidth * 3
    print("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
        margin, hundint, 550 - margin, hundint, sw))
    if counter >= 9:
        print("""<text x="%d" y="%d" font-family="Georgia" font-size="18pt" fill="%s">%s</text>""" % (
            margin+5, hundint-12, "rgb(150,150,150)", padno(counter)))
        print("""<text x="%d" y="%d" font-family="Georgia" font-size="18pt" fill="%s">%s</text>""" % (
            rightLeftMargin+5, hundint-12, "rgb(150,150,150)", padno(counter)))
        
    counter += 1
    if counter == 18:
        counter = 8
    print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
        550 + margin, hundint, 1100 - margin, hundint, sw))

    offset += linePitchMm
    hundint = offset * mmToHundthsInch 

# verticals for left side
print( """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    leftLeftMargin, 11 * mmToHundthsInch,
    leftLeftMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth))

print ("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    leftRightMargin, 11 * mmToHundthsInch,
    leftRightMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth))


# verticals for right side
print ("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    rightLeftMargin, 11 * mmToHundthsInch,
    rightLeftMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))

print ("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    rightRightMargin, 11 * mmToHundthsInch,
    rightRightMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth * 3))



print( """</svg>""")
