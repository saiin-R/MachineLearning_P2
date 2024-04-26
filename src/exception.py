import sys


def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in Execution name[{0}] in line number[{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    return error_message

        )
    

class customException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super.__init__(error_message)