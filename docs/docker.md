You can run the proyect in docker containers, how can you run docker containers?.

You have a bunch of information online, here only will go a little cheat code to update and set this web app.


UPDATE WEB TEMPLATES
------

- you need to update the local repo, if you are using github:

git pull 

- After that you need to stop the docker container:

if you are using a build.yml file, go to the location and execute this command:

sudo docker-compose --file build.yml stop

- After stoping you need to remove all everything from the docker container and setup it again, for that:

sudo docker rm container_name

sudo docker rmi base_image_name

- Finally you need to reload the container:

sudo docker-compose --file build.yml up -d --no-recreate

And wait until the container is up.


UPDATE STATIC FILES
-----

for static files it can be easier, just update you server folder as you want (git, sftp...) and the copy the files to the server static folder.

you can copy with:

sudo cp -rvf folder /static/folder/path/

