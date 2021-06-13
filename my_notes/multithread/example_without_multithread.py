# program without multithread

import re
import json
import time
from datetime import datetime

def prepare_report_links(build:dict):
    """ export report links from build """
    build_task_log = dict()
    build_task_log["build_id"] = build["build_id"]
    build_task_log["jobs"] = list()

    for job in build.get("jobs", []):
        job_dict = dict()
        job_dict["name"] = job.get("name")
        job_dict["tasks"] = list()

        for task in job.get("tasks", []):
            task_dict = dict()
            task_dict["name"] = task.get("name", "")
            task_dict["report_link"] = task.get("report_link", "")
            job_dict["tasks"].append(task_dict)
        
        build_task_log["jobs"].append(job_dict)

    return build_task_log

def get_data_from_link(link):
    """ Mock Request to 3rd Party API Part. """

    today = datetime.today().strftime("%Y-%M-%d %H:%M:%S")
    number = int(link.split("/")[-1])
    string = f'''
    [f{today}] [sarpine_LOG] copy input aposto/{number}{number}/{number}{number} -> aposto/{number}
    [f{today}] [sarpine_LOG] copy output aposto/{number+10}{number+10}/{number+10}{number+10} -> aposto/{number+10}
    [f{today}] [sarpine_LOG] copy input aposto/{number+20}{number+20}/{number+20}{number+20} -> aposto/{number+20}
    '''
    time.sleep(2)
    return string

def parse_link_content(link_content):
    """ Parse Link Conntent from 3rd Party API """

    result = dict()
    result["dep_in"] = []
    result["dep_out"] = []

    matches_out = re.findall(r"copy output .* -> .*", link_content)
    matches_in = re.findall(r"copy input .* -> .*", link_content)

    for dep_in in matches_in:
        result["dep_in"].append(dep_in.split(" ")[2])
    for dep_out in matches_out:
        result["dep_out"].append(dep_out.split(" ")[2])

    return result

def prepare_document(build:dict):
    """ Create new document from raw data. """

    build_id = build.get("build_id")
    job_tasks_with_report_links = prepare_report_links(build)
    result = dict()
    result["build_id"] = build_id
    result["deps"] = list()

    for job in job_tasks_with_report_links.get("jobs", []):
        job_dict = dict()
        job_dict["job_name"] = job.get("name")
        job_dict["tasks"] = list()
        for task in job.get("tasks", []):
            task_dict = dict()
            task_dict["task_name"] = task["name"]
            report_link = task.get("report_link")
            link_content = get_data_from_link(report_link)
            task_content_output = parse_link_content(link_content)
            task_dict["dep_in"] = task_content_output["dep_in"]
            task_dict["dep_out"] = task_content_output["dep_out"]
            job_dict["tasks"].append(task_dict)
        result["deps"].append(job_dict)

    return result


def main():
    """ Main Function. """
    data = ""
    with open("build.json", "r") as file_2:
        data = json.load(file_2)
    prepare_document(data)
    # print(prepare_document(data))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"It takes {time.time() - start_time} seconds.")
