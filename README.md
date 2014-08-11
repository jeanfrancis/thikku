# Thikku

Get direction through SMS. Works anywhere around the world.

### Install dependencies

Following steps are only needed one time

  1. npm install
  2. bower install
  3. virtualenv venv
  4. source venv/bin/activate
  5. pip install -r requirements.txt


### Run gulp to watch and compile Sass

To compile a sass

    gulp

To compile and watch for sass file changes

    gulp watch

### Export configurations in development

    export PLIVO_AUTH_ID=<copy_from_pilvo>
    export PLIVO_AUTH_TOKEN=<copy_from_pilvo>
    export PLIVO_NUMBER=<copy_from_pilvo>
    export TEST_NUMBER=<test_mobile_number>

### Run server

    source venv/bin/activate
    export PYTHONPATH=$(pwd)/server/
    mongod
    foreman start
