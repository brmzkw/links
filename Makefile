VENV = .virtualenv


all: build_venv build_all commit push

build_venv:
	@test -d .virtualenv || (virtualenv "${VENV}" && "${VENV}/bin/pip" install pyrss2gen)

build_all:
	@"${VENV}/bin/python" links.py --markdownify --rss links.rss > README.md

commit:
	@git commit -a -m 'Update links'

push:
	@git push
