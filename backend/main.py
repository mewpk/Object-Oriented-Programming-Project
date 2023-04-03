from app.main import app
from settings import settings

if __name__ == "__main__":
    import uvicorn
    
    # pass the application as an import string
    uvicorn.run(
        "app.main:app", # <--- updated line
        host=settings.api_host,
        port=settings.api_port,
        log_level=settings.log_level,
        reload=True
    )
