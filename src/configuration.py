import yaml
import os

def getConfiguration(config_name, working_directory):
    
    conf={}
    config_file= working_directory +'./config/' + config_name + '.yml'
    with open(config_file, 'r') as stream:
        try:
            conf = yaml.load(stream, Loader=yaml.FullLoader)
            #conf = yaml.load(stream)
            conf['connection']['libUri'] = checkJarFile(conf['connection']['libUri'], working_directory)
        except yaml.YAMLError as exc:
            print(exc)

    return conf

def checkJarFile(file, working_directory):
    file = working_directory+'/libs/'+file 
    return file