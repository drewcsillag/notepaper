import sys


print """<svg height="850" width="1100">"""
offset = 11

mmToHundthsInch = 1 / .254

hundint = (offset * mmToHundthsInch)

margin = 8.5 * mmToHundthsInch

linePitchMm = 6.5 #mm

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
print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    leftCenterLine, 11 * mmToHundthsInch,
    leftCenterLine, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth)

# right center line
print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(220,220,220); stroke-width:%f"/>""" % (
    rightCenterLine, 11 * mmToHundthsInch,
    rightCenterLine, (endOffset - linePitchMm) * mmToHundthsInch,
    strokeWidth)



while hundint < 850.0:
    sys.stderr.write("hundint %f\n" % hundint)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
        margin, hundint, 550 - margin, hundint, strokeWidth)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
        550 + margin, hundint, 1100 - margin, hundint, strokeWidth)

    offset += linePitchMm
    hundint = offset * mmToHundthsInch 

# verticals for left side
print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    leftLeftMargin, 11 * mmToHundthsInch,
    leftLeftMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    leftRightMargin, 11 * mmToHundthsInch,
    leftRightMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth)


# verticals for right side
print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    rightLeftMargin, 11 * mmToHundthsInch,
    rightLeftMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(150,150,150); stroke-width:%f" />""" % (
    rightRightMargin, 11 * mmToHundthsInch,
    rightRightMargin, (offset - linePitchMm) * mmToHundthsInch,
    strokeWidth)



print """</svg>"""
