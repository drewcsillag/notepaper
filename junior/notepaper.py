import sys


print """<svg height="850" width="1100">"""
offset = 11

hundint = (offset/.2540)

margin = 8.5/.254

while hundint < 850.0:
    sys.stderr.write("hundint %f\n" % hundint)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
        margin, hundint, 550 - margin, hundint, 1.5625 / 2)
    print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
        550 + margin, hundint, 1100 - margin, hundint, 1.5625 / 2)

    offset += 6.5
    hundint = (offset/.254) 

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    margin, 11/.254,
    margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    550 - margin, 11/.254,
    550 - margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    550 + margin, 11/.254,
    550 + margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(200,200,200); stroke-width:%f" />""" % (
    1100 - margin, 11/.254,
    1100 - margin, (offset - 6.5) / .254,
    1.5625 / 2)

print """</svg>"""
