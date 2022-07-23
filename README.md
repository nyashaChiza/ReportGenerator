# ReportGenerator
A SQL-based report generator based on Pandas

# Arguments
1. report title : string
2. report format: string
3. sql query : string
4. connection string: string

# Usage
if __name__ == '__main__':
    
    report_title = 'testreport'
    report_format = 'XLSX'
    sql_query = 'SELECT * FROM Users'
    connection_string = 'mysql+pymysql://db_user:password@localhost:3306/db_name'    
    
    generate_report = ReportGenerator(report_title, report_format, sql_query, connection_string)
    
    my_report = generate_report.report()
