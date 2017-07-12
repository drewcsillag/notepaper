import sys


print """<svg height="1100" width="850">"""
offset = 11

hundint = (offset/.2540)

margin = 8.5/.254

while hundint < 1075.0:
    sys.stderr.write("hundint %f\n" % hundint)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
        margin, hundint, 550 - margin, hundint, 1.5625 / 2)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
        margin, hundint, 850 - margin, hundint, 1.5625 / 2)

    offset += 6.5
    hundint = (offset/.254) 

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    margin, 11/.254,
    margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    850 - margin, 11/.254,
    850 - margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """</svg>"""
