build:
    python3 swtfa.py

copy: build
    cp foo.pdf $WINHOME/Downloads
