
# MNSU Final Grade Checker

This is a simple build to allow students to be proactively & continuously updated when their final grades for the semester have been entered in to E-services.

## Installation

Initially, you must first clone into the repository using the following:

```bash
git clone https://github.com/fancyHeat/FinalGradeUtility.git
```
Next you must configure your settings. There is an example config file provided in the repository. Simply open that file and enter in the respective credentials. Lastly, rename ``config-example`` to ``config.py``using the following:
```bash
mv config-example.py config.py
```
Next, build your Docker container with the following:
```bash
docker build -t "enter your tag here" .
```
Lastly, simply run the docker container using your preferred arguments. Below is an example to start the container in the background:
```bash
docker run -itd --name FinalsServer "enter tag from above"
```
# Future Work
Work is currently underway to allow the use of ``docker pull``  in addition to releasing a ``docker-compopse`` file as apposed to running ``docker build`` yourself.