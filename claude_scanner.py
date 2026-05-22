# -*- coding: utf-8 -*-

from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenuItem
from java.util import ArrayList
import urllib2
import json
import ssl
import threading
import sys

# Force UTF-8 (Jython fix)
reload(sys)
sys.setdefaultencoding('utf-8')

# ==========================================
# LOCAL PROXY CONFIG
# ==========================================
API_URL = "http://127.0.0.1:5000/analyze"


class BurpExtender(IBurpExtender, IContextMenuFactory):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Vultrex Sec - Claude Scanner")
        callbacks.registerContextMenuFactory(self)

        print("-" * 50)
        print("Vultrex Sec - Claude Scanner Loaded")
        print("Status: Waiting for analysis request...")
        print("-" * 50)

    def createMenuItems(self, invocation):
        self.invocation = invocation
        menu = ArrayList()

        item = JMenuItem("Analyze with Claude (Vultrex)")
        item.addActionListener(lambda x: self.start_analysis(self.invocation))

        menu.add(item)
        return menu

    def start_analysis(self, invocation):
        print("[DEBUG] Menu clicked")

        messages = invocation.getSelectedMessages()

        for message in messages:
            request_bytes = message.getRequest()
            request_str = self._helpers.bytesToString(request_bytes)

            print("[+] Sending request to local AI proxy...")

            threading.Thread(
                target=self.get_ai_analysis,
                args=(request_str,)
            ).start()

    def get_ai_analysis(self, http_data):
        prompt = (
            "Analyze this HTTP request for vulnerabilities such as SQL Injection, XSS, SSRF, and IDOR. "
            "Provide a short summary and a test payload:\n\n" + http_data
        )

        body = {
            "model": "claude-3-7-sonnet",
            "messages": [
                {
                    "role": "user",
                    "content": prompt[:4000]
                }
            ]
        }

        try:
            ctx = ssl.create_default_context()

            req = urllib2.Request(API_URL, json.dumps(body))
            req.add_header("Content-Type", "application/json")

            response = urllib2.urlopen(req, timeout=60, context=ctx)
            result = json.loads(response.read())

            if 'choices' in result:
                analysis = result['choices'][0]['message']['content']
            elif 'content' in result:
                analysis = result['content'][0]['text']
            elif 'error' in result:
                print("[!] API Error: {}".format(result['error']))
                return
            else:
                print("[!] Unexpected response:")
                print(result)
                return

            print("\n" + "=" * 30 + " VULTREX REPORT " + "=" * 30)
            print(analysis.encode('utf-8'))
            print("=" * 80 + "\n")

        except urllib2.HTTPError as e:
            print("[!] HTTP Error {}: {}".format(e.code, e.read()))

        except Exception as e:
            print("[!] Connection Error: {}".format(str(e).encode('utf-8')))