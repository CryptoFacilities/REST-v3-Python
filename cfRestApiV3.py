# Crypto Facilities Ltd REST API v3

# Copyright (c) 2018 Crypto Facilities

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
# IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import time
import base64
import hashlib
import hmac
import json
import urllib.request as urllib2
import urllib.parse as urllib
import ssl


class cfApiMethods(object):
    def __init__(self, apiPath, apiPublicKey="", apiPrivateKey="", timeout=10, checkCertificate=True, useNonce=False):
        self.apiPath = apiPath
        self.apiPublicKey = apiPublicKey
        self.apiPrivateKey = apiPrivateKey
        self.timeout = timeout
        self.nonce = 0
        self.checkCertificate = checkCertificate
        self.useNonce = useNonce

    ##### public endpoints #####

    # returns all instruments with specifications
    def get_instruments(self):
        endpoint = "/derivatives/api/v3/instruments"
        return self.make_request("GET", endpoint)

    # returns market data for all instruments
    def get_tickers(self):
        endpoint = "/derivatives/api/v3/tickers"
        return self.make_request("GET", endpoint)

    # returns the entire order book of a futures
    def get_orderbook(self, symbol):
        endpoint = "/derivatives/api/v3/orderbook"
        postUrl = "symbol=%s" % symbol
        return self.make_request("GET", endpoint, postUrl=postUrl)

    # returns historical data for futures and indices
    def get_history(self, symbol, lastTime=""):
        endpoint = "/derivatives/api/v3/history"
        if lastTime != "":
            postUrl = "symbol=%s&lastTime=%s" % (symbol, lastTime)
        else:
            postUrl = "symbol=%s" % symbol
        return self.make_request("GET", endpoint, postUrl=postUrl)

    ##### private endpoints #####

    # returns key account information
    # Deprecated because it returns info about the Futures margin account
    # Use get_accounts instead
    def get_account(self):
        endpoint = "/derivatives/api/v3/account"
        return self.make_request("GET", endpoint)

    # returns key account information
    def get_accounts(self):
        endpoint = "/derivatives/api/v3/accounts"
        return self.make_request("GET", endpoint)

    # places an order
    def send_order(self, orderType, symbol, side, size, limitPrice, stopPrice=None, clientOrderId=None):
        endpoint = "/derivatives/api/v3/sendorder"
        postBody = "orderType=%s&symbol=%s&side=%s&size=%s&limitPrice=%s" % (
            orderType, symbol, side, size, limitPrice)

        if orderType == "stp" and stopPrice is not None:
            postBody += "&stopPrice=%s" % stopPrice

        if clientOrderId is not None:
            postBody += "&cliOrdId=%s" % clientOrderId

        return self.make_request("POST", endpoint, postBody=postBody)

    # places an order
    def send_order_1(self, order):
        endpoint = "/derivatives/api/v3/sendorder"
        postBody = urllib.urlencode(order)
        return self.make_request("POST", endpoint, postBody=postBody)

    # edit an order
    def edit_order(self, edit):
        endpoint = "/derivatives/api/v3/editorder"
        postBody = urllib.urlencode(edit)
        return self.make_request("POST", endpoint, postBody=postBody)

    # cancels an order
    def cancel_order(self, order_id=None, cli_ord_id=None):
        endpoint = "/derivatives/api/v3/cancelorder"

        if order_id is None:
            postBody = "cliOrdId=%s" % cli_ord_id
        else:
            postBody = "order_id=%s" % order_id

        return self.make_request("POST", endpoint, postBody=postBody)

    # cancel all orders
    def cancel_all_orders(self, symbol=None):
        endpoint = "/derivatives/api/v3/cancelallorders"
        if symbol is not None:
            postbody = "symbol=%s" % symbol
        else:
            postbody = ""

        return self.make_request("POST", endpoint, postBody=postbody)

    # cancel all orders after
    def cancel_all_orders_after(self, timeoutInSeconds=60):
        endpoint = "/derivatives/api/v3/cancelallordersafter"
        postbody = "timeout=%s" % timeoutInSeconds

        return self.make_request("POST", endpoint, postBody=postbody)

    # places or cancels orders in batch
    def send_batchorder(self, jsonElement):
        endpoint = "/derivatives/api/v3/batchorder"
        postBody = "json=%s" % jsonElement
        return self.make_request("POST", endpoint, postBody=postBody)

    # returns all open orders
    def get_openorders(self):
        endpoint = "/derivatives/api/v3/openorders"
        return self.make_request("GET", endpoint)

    # returns filled orders
    def get_fills(self, lastFillTime=""):
        endpoint = "/derivatives/api/v3/fills"
        if lastFillTime != "":
            postUrl = "lastFillTime=%s" % lastFillTime
        else:
            postUrl = ""
        return self.make_request("GET", endpoint, postUrl=postUrl)

    # returns all open positions
    def get_openpositions(self):
        endpoint = "/derivatives/api/v3/openpositions"
        return self.make_request("GET", endpoint)

    # sends an xbt withdrawal request
    def send_withdrawal(self, targetAddress, currency, amount):
        endpoint = "/derivatives/api/v3/withdrawal"
        postBody = "targetAddress=%s&currency=%s&amount=%s" % (
            targetAddress, currency, amount)
        return self.make_request("POST", endpoint, postBody=postBody)

    # returns xbt transfers
    def get_transfers(self, lastTransferTime=""):
        endpoint = "/derivatives/api/v3/transfers"
        if lastTransferTime != "":
            postUrl = "lastTransferTime=%s" % lastTransferTime
        else:
            postUrl = ""
        return self.make_request("GET", endpoint, postUrl=postUrl)

    # returns all notifications
    def get_notifications(self):
        endpoint = "/derivatives/api/v3/notifications"
        return self.make_request("GET", endpoint)

    # makes an internal transfer
    def transfer(self, fromAccount, toAccount, unit, amount):
        endpoint = "/derivatives/api/v3/transfer"
        postBody = "fromAccount=%s&toAccount=%s&unit=%s&amount=%s" % (
            fromAccount, toAccount, unit, amount)
        return self.make_request("POST", endpoint, postBody=postBody)

    # accountlog csv
    def get_accountlog(self):
        endpoint = "/api/history/v2/accountlogcsv"
        return self.make_request("GET", endpoint)

    def _get_partial_historical_elements(self, elementType, since=None, contToken=None):
        endpoint = "/api/history/v2/%s" % elementType

        if contToken is not None:
            return self.make_request_raw("GET", endpoint, postUrl="continuationToken=%s" % contToken)
        else:
            if since is not None:
                return self.make_request_raw("GET", endpoint, postUrl="since=%s" % since)

        return self.make_request_raw("GET", endpoint)

    def _get_historical_elements(self, elementType, since=None):
        elements = []

        more = True
        contToken = None

        while more:
            res = self._get_partial_historical_elements(elementType, since, contToken)
            body = json.loads(res.read().decode('utf-8'))
            elements = elements + body['elements']

            if res.headers['is-truncated'] is None or res.headers['is-truncated'] == "false":
                more = False
                contToken = None
            else:
                contToken = res.headers['next-continuation-token']

        elements.sort(key=lambda el: el['timestamp'], reverse=True)
        return elements

    # historical orders after a certain point in reverse chronological order
    def get_historical_orders(self, since=None):
        return self._get_historical_elements('orders', since)

    # recent orders in reverse chronological order
    def get_recent_orders(self):
        return self.get_historical_orders(None)
    
    # historical executions after a certain point in reverse chronological order
    def get_historical_executions(self, since=None):
        return self._get_historical_elements('executions', since)

    # recent executions in reverse chronological order
    def get_recent_executions(self):
        return self.get_historical_executions(None)

    # signs a message
    def sign_message(self, endpoint, postData, nonce=""):
        if endpoint.startswith('/derivatives'):
            endpoint = endpoint[len('/derivatives'):]

        # step 1: concatenate postData, nonce + endpoint
        message = postData + nonce + endpoint

        # step 2: hash the result of step 1 with SHA256
        sha256_hash = hashlib.sha256()
        sha256_hash.update(message.encode('utf8'))
        hash_digest = sha256_hash.digest()

        # step 3: base64 decode apiPrivateKey
        secretDecoded = base64.b64decode(self.apiPrivateKey)

        # step 4: use result of step 3 to has the result of step 2 with HMAC-SHA512
        hmac_digest = hmac.new(secretDecoded, hash_digest,
                               hashlib.sha512).digest()

        # step 5: base64 encode the result of step 4 and return
        return base64.b64encode(hmac_digest)

    # creates a unique nonce
    def get_nonce(self):
        # https://en.wikipedia.org/wiki/Modulo_operation
        self.nonce = (self.nonce + 1) & 8191
        return str(int(time.time() * 1000)) + str(self.nonce).zfill(4)

    # sends an HTTP request
    def make_request_raw(self, requestType, endpoint, postUrl="", postBody=""):
        # create authentication headers
        postData = postUrl + postBody

        if self.useNonce:
            nonce = self.get_nonce()
            signature = self.sign_message(endpoint, postData, nonce=nonce)
            authentHeaders = {"APIKey": self.apiPublicKey,
                              "Nonce": nonce, "Authent": signature}
        else:
            signature = self.sign_message(endpoint, postData)
            authentHeaders = {
                "APIKey": self.apiPublicKey, "Authent": signature}

        authentHeaders["User-Agent"] = "cf-api-python/1.0"

        # create request
        if postUrl != "":
            url = self.apiPath + endpoint + "?" + postUrl
        else:
            url = self.apiPath + endpoint

        request = urllib2.Request(url, str.encode(postBody), authentHeaders)
        request.get_method = lambda: requestType

        # read response
        if self.checkCertificate:
            response = urllib2.urlopen(request, timeout=self.timeout)
        else:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urllib2.urlopen(
                request, context=ctx, timeout=self.timeout)

        # return
        return response

    # sends an HTTP request and read response body
    def make_request(self, requestType, endpoint, postUrl="", postBody=""):
        return self.make_request_raw(requestType, endpoint, postUrl, postBody).read().decode("utf-8")
