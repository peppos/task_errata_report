#!/usr/bin/python
　
import argparse
import json
import requests
import sys
import getpass
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
　
　
parser = argparse.ArgumentParser(description="Task and job errata report")
parser.add_argument("-n", "--server", type=str.lower, required=True, help="Satellite server (defaults to localhost)", default='localhost')
parser.add_argument("-u", "--username", type=str, required=True, help="Username to access Satellite")
parser.add_argument("-p", "--password", type=str, required=False, help="Password to access Satellite. The user will be asked interactively if password is not provided.")
parser.add_argument("-j", "--job", action="store_true", default=False, help="Use this flag if you want see the jobs")
　
args = parser.parse_args()
　
# Satellite specific parameters
url = "https://" + args.server
api = url + "/api/v2/"
katello_api = url + "/katello/api/v2/"
foreman_tasks_api = url + "/foreman_tasks/api/tasks"
job_api = api + "job_invocations"
　
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
　
    tasks = get_with_json(foreman_tasks_api + '?search=label=Actions::Katello::Host::Erratum::Install', json.dumps({"per_page": "10000000"}))["results"]
　
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
　
def job_report():
    # Print headline
    print "Job_id;Hostname;Status;Date;Type;User;Errata"
    jobs = get_with_json(job_api + '?search=job_category=Katello', json.dumps({"per_page": "10000000"}))["results"]
　
    for job in jobs:
        job_id = job["id"]
        task_id = job["dynflow_task"]["id"]
        tasks = get_with_json(foreman_tasks_api + "/" + str(task_id), json.dumps({"per_page": "10000000"}))
        job_details = get_with_json(job_api + "/" + str(job_id), json.dumps({"per_page": "10000000"}))
        errata = str(job_details["template_invocations"][0]["template_invocation_input_values"][2]["value"])
        host = str(job_details["targeting"]["hosts"][0]["name"])
        status = job_details["status_label"]
        date = job_details["start_at"]
        template_name =  str(job_details["template_invocations"][0]["template_name"])
        user = tasks["username"]
        print str(job_id) + ";" + str(host) + ";" + str(status) + ";" + str(date) + ";" + str(template_name) + ";" + str(user) + ";" + str(errata)
　
if __name__ == "__main__":
　
  if args.job:
        job_report()
  else:
        task_report()
