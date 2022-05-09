# credentials
host = "157.230.209.171"
username = "jemison_1766"
user = username
password = "V7cqC0PDBEoZGribnaS3CMN4RAtQPtUA"

def get_db_url(db_name):
    url=f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
    return url
