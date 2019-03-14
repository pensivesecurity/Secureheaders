#!/usr/bin/env python3
import requests
import argparse

def verifysecureheaders(url,ssl):
    if ssl == True:
        req =  requests.get('https://'+url)
        # strict-Transport-security Header
        if 'strict-transport-security' in req.headers:
            print ("[+] strict-transport-security YES ")
        else:
            print ("[+] strict-transport-security NO ")
        # X-Frame-Options headers
        if 'X-Frame-Options' in req.headers:
            print("[+] X-Frame-Options YES ")
        else:
            print("[+] X-Frame-Options NO ")
        # XSS Protection Header
        if 'X-XSS-Protection' in req.headers:
            print("[+] XSS Protection YES ")
        else:
            print("[+] XSS Protection NO ")
        # X-Content-Type-Options
        if 'X-Content-Type-Options' in req.headers:
            print("[+] X-Content-Type-Options YES ")
        else:
            print("[+] X-Content-Type-Options NO ")
        # Content-Security-Policy
        if 'Content-Security-Policy' in req.headers:
            print("[+] Content-Security-Policy YES ")
        else:
            print("[+] Content-Security-Policy NO ")
        # X-Permitted-Cross-Domain-Policies
        if 'X-Permitted-Cross-Domain-Policies' in req.headers:
            print("[+] X-Permitted-Cross-Domain-Policies YES ")
        else:
            print("[+] X-Permitted-Cross-Domain-Policies NO ")
        # Referrer-Policy
        if 'Referrer-Policy' in req.headers:
            print("[+] Referrer-Policy YES ")
        else:
            print("[+] Referrer-Policy NO ")
        return True
    else:
        req = requests.get('http://' + url)
        # strict-Transport-security Header
        if 'strict-transport-security' in req.headers:
            print("[+] strict-transport-security YES ")

        else:
            print("[+] strict-transport-security NO ")
        # X-Frame-Options headers
        if 'X-Frame-Options' in req.headers:
            print("[+] X-Frame-Options YES ")
        else:
            print("[+] X-Frame-Options NO ")

        # XSS Protection Header
        if 'X-XSS-Protection' in req.headers:
            print("[+] XSS Protection YES ")
        else:
            print("[+] XSS Protection NO ")
        # X-Content-Type-Options
        if 'X-Content-Type-Options' in req.headers:
            print("[+] X-Content-Type-Options YES ")
        else:
            print("[+] X-Content-Type-Options NO ")
        # Content-Security-Policy
        if 'Content-Security-Policy' in req.headers:
            print("[+] Content-Security-Policy YES ")
        else:
            print("[+] Content-Security-Policy NO ")
        # X-Permitted-Cross-Domain-Policies
        if 'X-Permitted-Cross-Domain-Policies' in req.headers:
            print("[+] X-Permitted-Cross-Domain-Policies YES ")
        else:
            print("[+] X-Permitted-Cross-Domain-Policies NO ")
        # Referrer-Policy
        if 'Referrer-Policy' in req.headers:
            print("[+] Referrer-Policy YES ")
        else:
            print("[+] Referrer-Policy NO ")
        return True
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u','--url',required=True,nargs='+',help='URL you need Scan')
    parser.add_argument('-ssl', '--ssl',action="store_true",help='URL you need Scan')
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
            verifysecureheaders(urls,args.ssl)
            print("===============")

if __name__ == '__main__':
    main()
