from cores.const.__const import Const


class SwaggerConst(Const):
    SWAGGER_OBJ = 'SWAGGER_OBJ'
    SWAGGER_JSON = 'SWAGGER_JSON'
    SERVICE_LIST: list = []
    API_LIST: list = []
    PROJECT: str = ''
    GITLAB_CONFIG_SERVICES = {PROJECT: dict(service_list=SERVICE_LIST,
                                            path='docs/api',
                                            version='v1')}
