from parsers.base_parser import baseParser


def joinData(stations ):

    at_list = baseParser("air_temperature.xlsx", "air_temperature")
    rst_list = baseParser("surface_temp.xlsx", "Температура поверхности")
    observations_list = []
    for i in range(0, len(at_list)):
        air_station_name = at_list[i]["station_name"]
        for j in range(0, len(rst_list)):
            for station in stations:
                surface_station_name = rst_list[j]["station_name"]
                if (air_station_name == station[1]) & (surface_station_name == station[1]) & (str(at_list[i]["observation_time"])[0:15] == str(rst_list[j]["observation_time"])[0:15]):
                    dict = {"station_id": station[0], "observation_time": at_list[i]["observation_time"], \
                            "air_temperature": at_list[i]["parameter_value"], "road_surface_temperature": rst_list[j]["parameter_value"]}
                    observations_list.append(dict)
                    break
                # # print(at_list[i]["observation_time"] , " // ", rst_list[i]["observation_time"])
            
                # if (air_station_name == surface_station_name) & (str(at_list[i]["observation_time"])[0:15] == str(rst_list[i]["observation_time"])[0:15]):
                #     dict = {"station_id": station[0], "observation_time": at_list[i]["observation_time"], \
                #             "air_temperature": at_list[i]["parameter_value"], "road_surface_temperature": rst_list[i]["parameter_value"]}
                #     observations_list.append(dict)
                # break
    return observations_list