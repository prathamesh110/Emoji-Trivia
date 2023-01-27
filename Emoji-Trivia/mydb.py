import random
import mysql.connector




eidrep = [0]
class dbconnect:
    def __init__(self,db,cursor):

        self.db=db
        self.cursor=cursor
        
    
    def emojifetch(self,name,eid):
        eid = random.randint(1, 20)
        if name == "Brand":
            print(eidrep)
            for idrep in eidrep:
                if eid == idrep:
                    pass

                else: 
                    print(eid)
                    eidrep.append(eid)
                    sql = "SELECT * FROM brand WHERE id = %s"
                    eid = (eid, )

                    self.cursor.execute(sql,eid)

                    results = self.cursor.fetchall()
                    efetchlist = []
                    for r in results:
                        ename = r[1]
                        eunicode = r[2]
                        efetchlist.append(ename)
                        efetchlist.append(eunicode)
                



                    self.db.close()

                    return  efetchlist


        elif name == "Song":
            sql = "SELECT * FROM song WHERE id = %s"
            eid = (eid, )

            self.cursor.execute(sql,eid)

            results = self.cursor.fetchall()
            efetchlist = []
            for r in results:
                ename = r[1]
                eunicode = r[2]
                efetchlist.append(ename)
                efetchlist.append(eunicode)
        



            self.db.close()

            return  efetchlist

        elif name == "Word":
            sql = "SELECT * FROM word WHERE id = %s"
            eid = (eid, )


            self.cursor.execute(sql,eid)

            results = self.cursor.fetchall()
            efetchlist = []
            for r in results:
                ename = r[1]
                eunicode = r[2]
                efetchlist.append(ename)
                efetchlist.append(eunicode)
        



            self.db.close()

            return  efetchlist

        elif name == "Movie":
            sql = "SELECT * FROM movie WHERE id = %s"
            eid = (eid, )


            self.cursor.execute(sql,eid)

            results = self.cursor.fetchall()
            efetchlist = []
            for r in results:
                ename = r[1]
                eunicode = r[2]
                efetchlist.append(ename)
                efetchlist.append(eunicode)
        



            self.db.close()

            return  efetchlist

           
