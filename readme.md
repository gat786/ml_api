# ML API

This repository is made by me to demonstrate an example of how you can make a 
REST API over a Machine Learning model.

It is a part of interactive [video lesson]() which goes on how you can deploy a
machine learning model on to Azure or any other Cloud Provider if you follow
seperate instruction to actually deploy the code. 

The process of building a docker image around your Machine Learning model is 
done to make sure you never have dependency issues when deploying it anywhere.

Click on this button to get a collection for using this api whenever you run it in person.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c9a9fb95f0c114bef0a0)

Running this API on your local machine involves these processes. 

Make sure you have `Python-3` installed on your machine and a 
python-version-manager such as [pyenv](https://github.com/pyenv/pyenv) or 
[pyenv-win](https://github.com/pyenv-win/pyenv-win) on your machine.

Install `pipenv` in your python installation like this 

```sh
pip install pipenv
```

After pipenv installation has completed install all the dependencies for this project using 

```sh
cd path/to/ml_api/
pipenv install
```
After all the dependencies are installed running this project will be like -

```sh
uvicorn app.main:app --port 8000
```

Building Docker Image for this project is as simple as 

```sh
docker build -t tag-name .
```

Notice `tag-name` can be replaced by any name you like or want to set. Make 
sure you are in the project directory or this command will not be able to find the `Dockerfile`.

After making the Image running the container requires the following command.

```sh
docker run --name container-name -p 80:80 tag-name
```

Here container-name is anything you want your container to be named and 
tag-name represents the tag-name you had setup in the earlier shell command.

Whether you are running this with docker or on your system directly if you 
have successfully managed to run the project you should be greated with some 
message like this in the commandline.

```
INFO:     Started server process [19600]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:80 (Press CTRL+C to quit)
```