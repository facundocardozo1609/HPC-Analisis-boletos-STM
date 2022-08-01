
import os
import json
import glob

def processResults(nombreUsuario, pid):
    my_path = os.path.abspath(os.path.dirname(__file__))
    my_path+= "/../../../"
    server_path = "/scratch/" + str(nombreUsuario) + "/"
    result = {} 
    os.chdir(server_path)
    for file in glob.glob("*_" + str(pid) + ".json"):
        path = server_path  + file
        with open(path, "r") as outfile:
            result.update(json.load(outfile))

    result_path = my_path + "src/resources/resultado_" + str(pid) + ".json"
    with open(result_path, "w") as outfile:
        outfile.write(json.dumps(result))
        outfile.close()
        
    for file in glob.glob("*_" + str(pid) + ".json"):
        if file == "resultado_" + str(pid) + ".json":
            continue
        os.remove(file)
