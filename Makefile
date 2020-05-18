
prefix=/usr
datadir=$(prefix)/share
pkgdatadir=$(datadir)/publican
contentdir=$(pkgdatadir)/Common_Content
branddir=$(contentdir)

all: html pdf

html:
	publican build --langs=en-US --formats=html --common_content=$(contentdir) --brand_dir=$(branddir)

pdf:
	publican build --langs=en-US --formats=pdf --common_content=$(contentdir) --brand_dir=$(branddir)

rpm:
	publican package --lang=en-US --binary --desktop --common_content=$(contentdir) --brand_dir=$(branddir)

clean:
	publican clean --common_content=$(contentdir)
