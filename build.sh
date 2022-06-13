cd /www/wwwroot/projects/GitScratchFrontend
git fetch --all
git reset --hard
yarn install
yarn build
pm2 restart GitScratchFrontend