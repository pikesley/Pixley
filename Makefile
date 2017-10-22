test:
	pytest tests -v

clean:
	find . -name "*pyc" -delete

copy-to-trinket: clean
	rsync -av patterns /Volumes/CIRCUITPY/lib/Pixley/
	cp *.py  /Volumes/CIRCUITPY/lib/Pixley
