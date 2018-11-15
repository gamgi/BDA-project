# Aggressive in place linting
# max-line leght 90
# ignore E402 imports at beginning of file due to Tkinter config required before some imports
./venv/bin/autopep8 --in-place --aggressive --aggressive --exclude venv --recursive --max-line-length 90 --ignore=E402 .
