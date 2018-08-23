from flask import request
from flask_restful import Resource
import random
import datetime

from models.host import Host


def hostnamegeneration():
    data = request.get_json()
    name = (data['country'] + data['server_type'] + data['os'] + str(random.randint(0, 99999)).zfill(5))
    return name


class CreateHostname(Resource):
    def post(self):
        hostname = hostnamegeneration()
        date = datetime.datetime.now().strftime("%d-%m-%y %H:%M")
        if Host.find_by_hostname(hostname):
            hostname = hostnamegeneration()
        hosttoadd = Host(hostname, date)
        Host.save_to_db(hosttoadd)
        return hostname, 201


class DeleteHostname(Resource):
    def delete(self, hostname):
        host = Host.find_by_hostname(hostname)
        if host:
            Host.delete_from_db(host)
        return {'message': 'Hostname {} deleted'.format(host.hostname)}


class GetHostname(Resource):
    def get(self, hostname):
        host = Host.find_by_hostname(hostname)
        if host:
            return host.json()
        return {'message': 'Host not found'}, 404


class HostnameList(Resource):
    def get(self):
        try:
            return {'Hostnames': list(map(lambda x: x.json(), Host.query.all()))}, 200
        except Exception:
            return {'message': 'No hosts found'}, 404
