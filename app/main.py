# Third Party
from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
async def health_check():
    """Return app status."""
    return {'status': 'ok'}


if __name__ == '__main__':
    # Third Party
    import uvicorn

    uvicorn.run(app, host='127.0.0.1', port=8000)
