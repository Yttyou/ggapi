"""  脚本执行文件  """

import pytest
if __name__ == '__main__':
    pytest.main(["-m", "all", "--html=HtmlTestReport/pytest_result.html",
                 "--junitxml=HtmlTestReport/result.xml"])
