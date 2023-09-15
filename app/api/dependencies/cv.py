from app.infrastructure.dao.cv import CVDAO


def dao_provider():
    return CVDAO()
