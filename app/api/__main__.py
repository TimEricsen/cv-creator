import uvicorn

from fastapi import FastAPI

from app.api.main_factory import create_app
from app.api.routers import include_routers
from app.core.utils.exception_handlers import setup_exception_handlers


def main() -> FastAPI:
    app = create_app()
    include_routers(app)
    setup_exception_handlers(app)

    return app


def run():
    uvicorn.run('app.api:main', reload=True, host='0.0.0.0', port=80)


if __name__ == '__main__':
    run()
