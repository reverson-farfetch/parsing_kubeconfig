#!/usr/bin/python3

import yaml
import os
from pathlib import Path

home = os.getenv('HOME')

config_dict = {
    "apiVersion":"v1",
    "kind": "Config",
    "clusters" : [],
    "contexts": [],
    "users": [],
    "current-context": ""
}

def list_files(path="/etc/kubernetes",prefix="*-config"):
    path_file = Path(path)
    list_path_file = []

    for config in path_file.glob(prefix):
        list_path_file.append(str(config))

    return list_path_file

def read_config(config_file):
    with open(config_file) as file: 
        kubeconfig_json = yaml.safe_load(file)
        
    return kubeconfig_json

def write_config(kubeconfig_dict,path_file):
    with open(path_file, "w") as file:
            yaml.dump(kubeconfig_dict, file)

    return path_file

def append_configs(config_file):

    kubeconfig_json = read_config(config_file)
    if kubeconfig_json['local']:
        kubeconfig_json = kubeconfig_json['local']

    for cluster in kubeconfig_json['clusters']:
        config_dict['clusters'].append(cluster)

    for context in kubeconfig_json['contexts']:
        config_dict['contexts'].append(context)
        print(" ~> Context created \'%s\'" % context['name'])

    for user in kubeconfig_json['users']:
        config_dict['users'].append(user)

    return config_dict
            
if __name__ == "__main__":

    print("""
    *****************************************************************************************************************
      [NOTE]:The script will try looking for to files which ends like "*-config" in the path that was asked or you 
      can setting customize prefix.
      And it will concatenate every file found in one. You can pass the source directory where the files are stored 
      and the recipient where the file will be save. Also you can keep the default recipients if as well as wished.
    *****************************************************************************************************************
    """)
    path_config_files = str(input("Where are stored the kubeconfig files?[/etc/kubernetes]: ") or "/etc/kubernetes/")
    path_to_save_kubeconfig = str(input("Where do want to save the kubeconfig file?[~/.kube/config]: ") or home+"/.kube/config")
    prefix = str(input("Do you want to change the default prefix?[*-config]: ") or "*-config")


    list_path_file = list_files(path_config_files,prefix)
    if not list_path_file:
        print("\n[ERROR] Wasn't possible to find any file to load in \"%s\" using the prfix \"%s\"!" %  (path_config_files,prefix))
    else:
        for path_file in list_path_file:            
            kubeconfig_json = append_configs(path_file)

        current_context = str(input("\nDo you want to config a current context?[None]: ") or "")
        kubeconfig_json['current-context'] = current_context
        if write_config(kubeconfig_json,path_to_save_kubeconfig):
            print("\nThe file was created in \"%s\"" % path_to_save_kubeconfig)
    
