# coding=utf-8
"""Python异常处理：
    异常处理
    断言（ASsertion）"""
"""BaseException
    SystemExit
    KeyboardInterrupt
    Exception
    Stoplteration
    GeneratorExit
    StandardError
    ArithmeticError
    FloatingPointError
    OverflowError
    ZeroDivisionError
    AssertionError
    AttributeError
    EOFError
    EnvironmentError
    IOError
    OSError
    WindowsError
    ImportError
    LookupError
    IndexError
    KeyError
    MemoryError
    NameError
    UnboundLocalError
    ReferenceError
    RuntimeError
    NotImplementedError
    SyntaxError
    IndentationError
    TabError
    SystemError
    TypeError
    ValueError
    UnicodeError
    UnicodeDecodeError
    UnicodeEncodeError
    UnicodeTranslateError
    Warning
    DeprecationWarning
    DeprecationWarning
    FutureWarning
    OverflowWarning
    PendingDeprecationWarning
    RuntimeWarning
    SyntaxWarning
    UserWarning
    """

# chmod -w testfile

try:
    fh = open("testfile", "r")
    fh.write("this is a test file for exception")
except OSError:
    print "OSError"
except IOError, Arg:
    print "Error: the file is not exist or fail to read&write"
    print Arg
except BaseException:
    print "BaseError"
else:
    print "write successfully"
    fh.close()

# 使用except而不带任何异常类型，回捕获所有发生的异常，但也无法通过该程序识别出具体的异常信息
# 使用except而带多种类型
# try-finally：
# 异常的参数
# 触发异常
# 用户自定义异常