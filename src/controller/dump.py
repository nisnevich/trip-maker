# ----- System imports
import json
import pprint
import time

# ----- Local imports
from src.const.constants import *
from src.entity.flightroute import FlightsRoute
from src.model.composing.dfs import DFSComposer
from src.util.log import Logger

pretty_printer = pprint.PrettyPrinter()
dfs_composer = DFSComposer()

dump = open(PATH_ROUTE_DUMP, 'r').read()
route_flights = FlightsRoute.from_json(json.loads(dump))

visited_countries = set()
total_cost = 0
for f in route_flights:
    visited_countries.add(f.orig_country)
    visited_countries.add(f.dest_country)
    total_cost += f.price

orig_iata = route_flights[-1].dest_city
start_time = time.time()

count_result, cost_result, countries_result, route_result = \
    dfs_composer.get_flights(route_flights, visited_countries, total_cost)

Logger.info("Best result: visited {} countries for {} rub: {}".format(count_result,
                                                                      cost_result, countries_result))
Logger.info("The route:")
Logger.info(pretty_printer.pformat([vars(obj) for obj in route_result]))