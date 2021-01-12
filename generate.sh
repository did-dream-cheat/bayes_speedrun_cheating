#!/bin/sh

BASE="did_dream_cheat"
NBPUB=nbpublish
if [ -x ~/.local/bin/nbpublish ] ; then
	NBPUB=~/.local/bin/nbpublish
elif [ -x "`which nbpublish`" ] ; then
	NBPUB=`which nbpublish`
else
	echo "ERROR: Cannot find nbpublish!"
	exit 1
fi

SOURCE="$BASE".ipynb
TARGET=converted/"$BASE".pdf

if [ ! -f "$TARGET" -o "$SOURCE" -nt "$TARGET" ] ; then

	$NBPUB -f latex_ipypublish_main "$SOURCE" && \
	(	cd converted
		pdflatex "$BASE".tex && (
			bibtex "$BASE"
			pdflatex "$BASE".tex
			pdflatex "$BASE".tex
			)
		)

fi
