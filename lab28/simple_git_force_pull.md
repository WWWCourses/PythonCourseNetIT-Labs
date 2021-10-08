# How to force git pull to overwrite local files

**IMPORTANT: If you have any local changes, they will be lost.**

1. run a fetch to update all origin/<branch> refs to latest origin state:

	`git fetch --all`

2. overwrite local files with fetched remote files:

	`git reset --hard origin/main`