import sys

def error_message_detail(error_message,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    
    line_number=exc_tb.tb_lineno
    file_name=exc_tb.tb_frame.f_code.co_filename
    
    return "Error occured in python script [{0}] line number [{1}] with error message [{2}]".format(file_name,line_number,str(error_message))

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail)
        
    def __str__(self):
        return self.error_message