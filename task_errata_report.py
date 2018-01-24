#!/usr/bin/python

import argparse
import json
import requests
import sys
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


parser = argparse.ArgumentParser(description="Task errata report")
parser.add_argument("-n", "--server", type=str.lower, required=True, help="Satellite server (defaults to localhost)", default='localhost')
parser.add_argument("-u", "--username", type=str, required=True, help="Username to access Satellite")
parser.add_argument("-p", "--password", type=str, required=False, help="Password to access Satellite. The user will be asked interactively if password is not provided.")

args = parser.parse_args()

# Satellite specific parameters
url = "https://" + args.server
api = url + "/api/"
katello_api = url + "/katello/api/"
foreman_tassk_api = url + "/foreman_tasks/api/"

post_headers = {'content-type': 'application/json'}
ssl_verify=True

if args.password is None:
    args.password = getpass.getpass()

def get_with_json(location, json_data):
    """
    Performs a GET and passes the data to the url location
    """
    try:
        result = requests.get(location,
                            data=json_data,
                            auth=(args.username, args.password),
                            verify=ssl_verify,
                            headers=post_headers)

    except requests.ConnectionError, e:
        print sys.argv[0] + " Couldn't connect to the API, check connection or url"
        print e
        sys.exit(1)
    return result.json()

def task_report():

    # Print headline
    print "Hostname;TaskAction;TaskID;Username;TaskEnd;TaskResult;TaskState;Errata"

    # Get all hosts (alter if you have more than 10000 hosts)

    tasks = get_with_json(foreman_tassk_api + 'tasks?search=label=Actions::Katello::Host::Erratum::Install', json.dumps({"per_page": "10000000"}))["results"]

    for task in tasks:
        user = task["username"]
        task_id = task["id"]
        end = task["ended_at"]
        errata = str(task["humanized"]["input"])
        host = task["input"]["host"]["name"]
        action = task["humanized"]["action"]
        result = task["result"]
        state = task["state"]

        print str(host) + ";" + str(action) + ";" + str(task_id) + ";" + str(user) + ";" + str(end) + ";" + str(result) + ";" + str(state) + ";" + errata


if __name__ == "__main__":

        task_report()
