# Thikku

Get direction through SMS. It works even in remote areas of the country
where mobile internet is not available or not stable.

Check out [thikku](http://thikku.herokuapp.com/)

### Install dependencies

Following steps are only needed one time

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Export configurations in development

    export PLIVO_AUTH_ID=<copy_from_pilvo>
    export PLIVO_AUTH_TOKEN=<copy_from_pilvo>
    export PLIVO_NUMBER=<copy_from_pilvo>

### Run server

    source venv/bin/activate
    foreman start
