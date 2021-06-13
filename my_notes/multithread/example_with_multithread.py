# program with multithread

import re
import json
import time
import concurrent.futures
from datetime import datetime


def separate_data(build):
    """ Separate build data to run multithread. """

    part_of_build = list()
    for job in build.get("jobs"):
        for task in job.get("tasks"):
            part_of_build.append((job["name"], task["name"], task["report_link"]))
    return part_of_build, build["build_id"]

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

def run_separated_build_data_with_threads(separated_data, build_id):
    # Do Multithread Operation

    max_workers = 10
    print(f"Multithreading With {max_workers} workers.")
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(create_deps_data_from_task, separated_data)

    # group by job name
    job_group = dict()

    for result in results:
        job_name = result[1]
        output = result[0]
        job_tasks_list = job_group.get(job_name, [])
        job_tasks_list.append(output)
        job_group[job_name] = job_tasks_list

    # create result data from grouped multithread data
    result_data = dict()
    result_data["build_id"] = build_id
    deps = list()
    for i in job_group:
        temp_dict = dict()
        temp_dict["job_name"] = f"{i}"
        temp_dict["tasks"] = job_group[i]
        deps.append(temp_dict)
    result_data["deps"] = deps

    return result_data

def create_deps_data_from_task(item):
    """ Create Data to use in collection. """

    job_name, task, link = item
    link_content = get_data_from_link(link)
    content_output = parse_link_content(link_content)
    task_dict = dict()
    task_dict["task_name"] = task
    task_dict["dep_in"] = content_output.get("dep_in", [])
    task_dict["dep_out"] = content_output.get("dep_out", [])

    return task_dict, job_name
    

def main():
    """ Main Function. """

    data = ""
    with open("build.json", "r") as file_2:
        data = json.load(file_2)
    separated_build_data, build_name = separate_data(data)
    collection_data = run_separated_build_data_with_threads(separated_build_data, build_name)
    # print(collection_data)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"It takes {time.time() - start_time} seconds.")