# importation des librairies

from sqlalchemy import create_engine

# identifiants de ma base de donnee pour effectuer la connexion
hostname="localhost"
dbname="dbpro"
userame="root"
pswd=""

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
				.format(host=hostname, db=dbname, user=userame, pw=pswd))

# definition de la classe pour les elements de notre base de donnee

class datatb(object):

    @classmethod
    def getData(cls, data):
        data.to_sql('tbpro', engine, index=False)
        return 
