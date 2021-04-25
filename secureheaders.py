#!/usr/bin/env python3
import requests
import argparse

requests.packages.urllib3.disable_warnings()


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def verifysecureheaders(url,proxy):
    headers = [
        "Content-Type",
        "Content-Disposition",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Referrer-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "X-Permitted-Cross-Domain-Policies",
        "Clear-Site-Data",
        "Cross-Origin-Embedder-Policy",
        "Cross-Origin-Opener-Policy",
        "Cross-Origin-Resource-Policy"
    ]

    req = None
    proxies={}

    if(proxy):
        proxy = proxy[0]
        proxies={
                "http":"http://" + proxy,
                "https":"http://" + proxy
        }
        req = requests.get('http://'+url,proxies=proxies,verify=False)
    else:
        req = requests.get('http://'+url)

    response_headers = {k.lower(): v for k, v in req.headers.items()}

    for header in headers:
        if (header.lower()) in response_headers:
            prGreen("[✓]" + header + " : " + response_headers[header.lower()])
        else:
            prRed("[✗]" + header)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',required=True,nargs='+',help='URL to Scan')
    parser.add_argument('-p','--proxy',required=False,nargs='+',help='ip:port of Burp Proxy Server')
    args = parser.parse_args()
    print("""
    
    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ███████╗    ██╗  ██╗███████╗ █████╗ ██████╗ ███████╗██████╗ ███████╗
    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██╔════╝    ██║  ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
    ███████╗█████╗  ██║     ██║   ██║██████╔╝█████╗      ███████║█████╗  ███████║██║  ██║█████╗  ██████╔╝███████╗
    ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝      ██╔══██║██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗╚════██║
    ███████║███████╗╚██████╗╚██████╔╝██║  ██║███████╗    ██║  ██║███████╗██║  ██║██████╔╝███████╗██║  ██║███████║
    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                                                                 
    """)
    for urls in args.url:
            print("=== "+urls+" ===")
            verifysecureheaders(urls,args.proxy)
            print("===============")

if __name__ == '__main__':
    main()
