# Flask & Docker REST API

## Summary

Here is a template for creating a Flask server with REST API for serving data at URLs.
The server here is just a single file, with one endpoint `/example` which returns 
dummy data.

## Usage

To start the server without using Docker, just run:

```bash
python server.py
```

To test that this works use cURL which should return the data seen at the top of
`server.py`:

```bash
curl localhost:5000/example
```

To use Docker, you must first build using (you may need to use `sudo` before the `docker` 
command):

```bash
docker build -t flask-rest-api:dev .
```

And then running the container is simple since it does not use any volumes. However
it is necessary to expose port 5000, since this is the port set in `server.py`

```bash
docker run -d -p 5000:5000 --name flask flask-rest-api
```

