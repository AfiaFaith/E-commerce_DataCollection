# importation des librairies

from sqlalchemy import create_engine

# identifiants de ma base de donnee pour effectuer la connexion
hostname="localhost"
dbname="dbpro"
uname="root"
pwd=""

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=uname, pw=pwd))

# definition de la
class dataSave(object):

    @classmethod
    def getData(cls, data):
        data.to_sql('tbpro', engine, index=False)
        return 'Data save'
