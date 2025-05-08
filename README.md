## How to Use

### First time setup

#### Install `uv`

First, make sure you have `uv` installed. If not, you can install it using pip:

```bash
pip install uv
```

Alternatively, you can follow instructions from the [uv documentation](https://github.com/astral-sh/uv) for the latest install method.

#### Set up the GOOGLE_KEY

* This Microservice uses Google Maps API, so it requires setting up the key.

```bash
export GOOGLE_KEY=your-token
```

### Install dependencies

Once `uv` is installed:

```bash
uv sync
```

### Launching the app

Start the FastAPI app using `uv`:

```bash
uv run uvicorn main:application
```

If using Docker, remember to pass the `GOOGLE_KEY` explicitly:

```bash
docker run -e GOOGLE_KEY=your-token your_image_name
```

---

Ensure your machine has Python 3.13 installed for compatibility with modern `uv` and FastAPI dependencies.
