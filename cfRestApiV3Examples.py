# Crypto Facilities Ltd REST API V3

# Copyright (c) 2016 Crypto Facilities

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

import cfRestApiV3 as cfApi
import datetime

apiPath = "https://www.cryptofacilities.com/derivatives"
apiPublicKey = "..."  # accessible on your Account page under Settings -> API Keys
apiPrivateKey = "..."  # accessible on your Account page under Settings -> API Keys
timeout = 10
checkCertificate = True  # when using the test environment, this must be set to "False"

cfPublic = cfApi.cfApiMethods(apiPath, timeout=timeout, checkCertificate=checkCertificate)
cfPrivate = cfApi.cfApiMethods(apiPath, apiPublicKey=apiPublicKey, apiPrivateKey=apiPrivateKey, \
                               checkCertificate=checkCertificate)


def APITester():
    ##### public endpoints #####  

    # get instruments    
    result = cfPublic.get_instruments()
    print("get_instruments:\n", result)

    # get tickers
    result = cfPublic.get_tickers()
    print("get_tickers:\n", result)

    # get order book
    symbol = "f-xbt:usd-sep16"
    result = cfPublic.get_orderbook(symbol)
    print("get_orderbook:\n", result)

    # get history
    symbol = "f-xbt:usd-sep16"  # "f-xbt:usd-sep16", "cf-bpi", "cf-hbpi"
    lastTime = datetime.datetime.strptime("2016-01-20", "%Y-%m-%d").isoformat() + ".000Z"
    result = cfPublic.get_history(symbol, lastTime=lastTime)
    print("get_history:\n", result)

    ##### private endpoints #####

    # get account  
    result = cfPrivate.get_accounts()
    print("get_accounts:\n", result)

    # send limit order
    orderType = "lmt"
    symbol = "f-xbt:usd-sep16"
    side = "buy"
    size = 1
    limitPrice = 1.00
    result = cfPrivate.send_order(orderType, symbol, side, size, limitPrice)
    print("send_order (limit):\n", result)

    # send stop order
    orderType = "stp"
    symbol = "f-xbt:usd-sep16"
    side = "buy"
    size = 1
    limitPrice = 1.00
    stopPrice = 2.00
    result = cfPrivate.send_order(orderType, symbol, side, size, limitPrice, stopPrice=stopPrice)
    print("send_order (stop):\n", result)

    # cancel order
    order_id = "e35d61dd-8a30-4d5f-a574-b5593ef0c050"
    result = cfPrivate.cancel_order(order_id)
    print("cancel_order:\n", result)

    # batch order
    jsonElement = {
        "batchOrder":
            [
                {
                    "order": "send",
                    "order_tag": "1",
                    "orderType": "lmt",
                    "symbol": "f-xbt:usd-sep16",
                    "side": "buy",
                    "size": 1,
                    "limitPrice": 1.00,
                },
                {
                    "order": "send",
                    "order_tag": "2",
                    "orderType": "stp",
                    "symbol": "f-xbt:usd-sep16",
                    "side": "buy",
                    "size": 1,
                    "limitPrice": 2.00,
                    "stopPrice": 3.00,
                },
                {
                    "order": "cancel",
                    "order_id": "e35d61dd-8a30-4d5f-a574-b5593ef0c050",
                },
                {
                    "order": "cancel",
                    "order_id": "ce927332-87ba-4611-9bd7-ce38af84afdb",
                },
            ],
    }
    result = cfPrivate.send_batchorder(jsonElement)
    print("send_batchorder:\n", result)

    ## get open orders
    result = cfPrivate.get_openorders()
    print("get_openorders:\n", result)

    # get fills  
    lastFillTime = datetime.datetime.strptime("2016-02-01", "%Y-%m-%d").isoformat() + ".000Z"
    result = cfPrivate.get_fills(lastFillTime=lastFillTime)
    print("get_fills:\n", result)

    # get open positions
    result = cfPrivate.get_openpositions()
    print("get_openpositions:\n", result)

    # send xbt withdrawal request
    targetAddress = "xxxxxxxxxx"
    currency = "xbt"
    amount = 0.12345678
    result = cfPrivate.send_withdrawal(targetAddress, currency, amount)
    print("send_withdrawal:\n", result)

    # get xbt transfers    
    lastTransferTime = datetime.datetime.strptime("2016-02-01", "%Y-%m-%d").isoformat() + ".000Z"
    result = cfPrivate.get_transfers(lastTransferTime=lastTransferTime)
    print("get_transfers:\n", result)


