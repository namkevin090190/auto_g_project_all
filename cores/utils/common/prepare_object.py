from cores.model import RequestObj


class PrepareObj:

    @staticmethod
    def preparation(obj) -> RequestObj:
        return RequestObj(**obj.__dict__)
