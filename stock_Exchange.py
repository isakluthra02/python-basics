from flask import Flask, render_template
from financial_data import EODHDAPIsDataFetcher
from config import API_TOKEN #where only api key is stored
import re
import sys
import argparse

parser=argparse.ArgumentParser(description="EODHD APIs used here")
parser.add_argument("--host",type=str,help="Web server IP (127.0.0.1)")
parser.add_argument("--port",type=int,help="Web server port (5000)")
parser.add_argument("--debug",action="store_true",help="Enable Debugging")
args=parser.parse_args()
http_host="0.0.0.0"
if args.host is not None:
    p = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$") # re:-each number after the dot will be from 1 to 3 digits so 4 numbers each 1-3 digits
    if p.match(args.host):
        http_host=args.host
    else:
        parser.print_help(sys.stderr)
http_port=5000
if args.port is not None:
    if args.port>0 and args.port<=65535:
        http_port=args.port
    else:
        parser.print_help(sys.stderr)

application=Flask(__name__)
data=EODHDAPIsDataFetcher(API_TOKEN)
@application.route("/")
def exchange():
    exchange=data.get_Exchange()
    return render_template("stockHTML.html",exchanges=exchange)
@application.route("/<code>")
def exchange_markets(code):
    markets=data.fetch_exchange_markets(code)
    return render_template("stockMarket.html",code=code,exchanges=markets)
if __name__=="__main__":
    application.run(host=http_host,port=http_port,debug=args.debug)