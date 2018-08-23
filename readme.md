# Hostname REST Api

This is built with Flask, Flask-RESTful, Flask-SQLAlchemy, psycopg2, datetime and random

Create:

curl -X POST @parameters.json http://URL/hostname/create

Description:

Creates a hostname and stores it in a Postgres DB

Parameters:
country	string The country where the machine is located (uk,de)
server_type	string	What the server type is (s=server, c=cluster)
os	string	What OS the server is (l = linux, w = windows)



Delete:

curl -X DELETE http://URL/hostname/delete/<hostname>

Deletes the specified hostname passed in the url




List all:

curl -X GET http://URL/hostname/list

Returns a list of all hostnames and when they were reserved




List single hostname:

curl -X GET http://URL/hostname/list/<hostname>

Returns the requested hostname and when it was reserved
