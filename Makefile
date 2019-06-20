all:
	python links.py --markdownify
	git add README.md
	git commit -m 'Add links'
	git push
