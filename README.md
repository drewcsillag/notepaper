# Making note paper

Instructions are for Linux and my particular printer, but should be
reasonably adaptable to whatever OS and printer combination you have.

## Printing the PDF

Load the pdf in evince, and print.  For Page Setup, if junior sized
paper, chose two-sided Short Edge (Flip), otherwise Long Edge
(Standard).  For junior sized paper, pick landscape orientation, and
for paper size, choose Letter borderless.


## Generating the PDF from the script

Run the python `notepaper.py` script, redirecting to `notepaper.py`.
```
python notepaper.py > notepaper.html
```

Load the `notepaper.html` in Chrome or Chromium.  Print the page to
PDF, for the junior sized paper, print in landscape.  Paper size
should be letter and margins should be set to none.  You may have to
choose specific pages to print as sometimes there's a first or last
blank page.  Then save.

Use pdftk to duplicate the page into a two sided notepaper pdf.
```
pdftk notepaper.pdf notepaper.pdf cat output notepaper-2sided.pdf
```

