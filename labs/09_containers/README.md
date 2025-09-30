# Containers



1. Create a Docker image specification **Dockerfile** that runs the Playwrigt script `test_home.py` towards your locally deployed (without docker) backend and frontend.


1. Send a pull request with the Dockerfile and, if it apply, the additional files you had to create to make run the test_home.py script run inside of a docker container.


The commands to build and run the image locally should be just:

```
docker build . -t test_pw

docker run --rm [add to network] test_pw
```


Hints:

Useful documentation:  https://playwright.dev/python/docs/docker

Command to check local IP in windows:  `ipconfig`

export an environment variable `export APP_FRONT_URL=http://???`
