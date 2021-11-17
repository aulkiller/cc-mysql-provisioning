import random
import shelve
import time
import uuid
import docker
import hashlib

class ContainerProvisioning:
    def __init__(self,username='royyana',info=dict()):
        self.id = str(uuid.uuid1())
        self.username=username
        self.dbports = shelve.open('dbports.db',writeback=True)
    def nomor_ports_belum_dialokasikan(self,no_port=11111):
        try:
            return (no_port in self.dbports.keys()) is False
        except:
            return True
    def find_port(self):
        the_port = 11111
        gagal=5
        while True:
            the_port = random.randint(11111, 22222)
            if (self.nomor_ports_belum_dialokasikan(the_port)):
                break
            time.sleep(1)
            gagal=gagal-1
            if (gagal<0):
                raise Exception
        return the_port

    def run_container(self):
        try:
            docker_client = docker.from_env()
            the_port_mysql = self.find_port()
            container_mysql = docker_client.containers.run(name=f"mysql-{self.username}-{self.id}", image="mysql:5.7",
                                                     environment=dict(MYSQL_ROOT_PASSWORD="mysql-4567"), ports={'3306/tcp': the_port_mysql},
                                                     detach=True)

            the_port_phpmyadmin = self.find_port()
            container_phpmyadmin = docker_client.containers.run(name=f"phpmyadmin-{self.username}-{self.id}", image="phpmyadmin/phpmyadmin",
                                                     environment=dict(PMA_HOST="127.0.0.1",PMA_PORT="3306"), ports={'80/tcp': the_port_phpmyadmin},
                                                     detach=True)



        except Exception as e:
            return dict(status="ERROR")


def run():
    pass

if __name__=='__main__':
    run()