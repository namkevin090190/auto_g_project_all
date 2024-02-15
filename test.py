# from cores.utils import ExecuteJavaFile
# from cores.const.common import EnvironmentConst


# out = ExecuteJavaFile.execute_java_file(
#     path=EnvironmentConst.ExternalLib.TOTP, java_file='Main 345356')
# print(out)

from platforms.api.models import LoginModel


a = LoginModel()

# print(dir(a))
print(a.header)
