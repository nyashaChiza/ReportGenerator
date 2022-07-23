import pandas as pd
from loguru import logger


class ReportGenerator:
    
    def __init__(self,report_title:str, report_format:str, sql_query:str, connection_string:str):
        self.report_title = report_title
        self.report_format = report_format
        self.sql_query = sql_query
        self.connection_string = connection_string
        
    
    def __get_dataframe(self):
        try:
            df =pd.read_sql(self.sql_query, con = self.connection_string)
            return df
        
        except Exception as e:
            logger.error(e)    
            return None


    def __validate_report_format(self)->dict:
        df = self.__get_dataframe()
        
        valid_report_formats = {
            'XLSX': df.to_excel(self.report_title+'.xlsx'),
            'JSON': df.to_json(self.report_title+'.json'),
            'CSV': df.to_csv(self.report_title+'.csv'),
                
            }

        try:
            return {
                'status':True,
                'report_with_format':valid_report_formats[self.report_format]                
                    }
        
        except Exception as e:
            logger.error(e)

            return {
                'status':False,
                'report_with_format':e
            }
    
    
    def report(self):
        report = self.__validate_report_format()
        
        if report['status']:
            return report['report_with_format']
        
        else:
            return report['report_with_format']
            
    
if __name__ == '__main__':
    
    report_title = 'testreport'
    report_format = 'XLSX'
    sql_query = 'SELECT * FROM Users'
    connection_string = 'mysql+pymysql://db_user:password@localhost:3306/db_name'    
    
    generate_report = ReportGenerator(report_title, report_format, sql_query, connection_string)
    
    my_report = generate_report.report()

          