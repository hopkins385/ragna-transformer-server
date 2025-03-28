from fastapi import FastAPI
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

from routers import ner

app = FastAPI()
app.include_router(ner.router)

if __name__ == "__main__":
    import uvicorn
    try:
        logger.info("Starting server...")
        uvicorn.run(app, host="127.0.0.1", port=3030)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}", exc_info=True)
        raise RuntimeError(f"Server startup failed: {str(e)}")