Crypto Facilities REST API v3
==================================
This is a sample RESTful application for [Crypto Facilities Ltd](https://www.cryptofacilities.com/), to demonstrate
the REST v3 API.


Getting Started
---------------

1. Amend the `cfRestApiV3Examples.py` script to enter your api keys and other details
1. Run the `cfRestApiV3Examples.py` script after you check the example script actions

Functionality Overview
----------------------

* This application makes a REST call to every Crypto Facilities endpoint 

Application Sample Output
-------------------------

The following is some of what you can expect when running this application:

```
   get_instruments:
    {'result': 'success', 'instruments': [{'symbol': 'fi_xbtusd_180606', 'type': 'futures_inverse', 'underlying': 'rr_xbtusd', 'lastTradingTime': '2018-06-06T16:00:00.000Z', 'tickSize': 1, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fi_xrpusd_180606', 'type': 'futures_inverse', 'underlying': 'rr_xrpusd', 'lastTradingTime': '2018-06-06T16:00:00.000Z', 'tickSize': 0.0001, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fv_xrpxbt_180606', 'type': 'futures_vanilla', 'underlying': 'rr_xrpxbt', 'lastTradingTime': '2018-06-06T16:00:00.000Z', 'tickSize': 1e-07, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fi_ethusd_180606', 'type': 'futures_inverse', 'underlying': 'rr_ethusd', 'lastTradingTime': '2018-06-06T16:00:00.000Z', 'tickSize': 0.01, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fi_xbtusd_180519', 'type': 'futures_inverse', 'underlying': 'rr_xbtusd', 'lastTradingTime': '2018-05-19T16:00:00.000Z', 'tickSize': 1, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fi_xrpusd_180519', 'type': 'futures_inverse', 'underlying': 'rr_xrpusd', 'lastTradingTime': '2018-05-19T16:00:00.000Z', 'tickSize': 0.0001, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fv_xrpxbt_180519', 'type': 'futures_vanilla', 'underlying': 'rr_xrpxbt', 'lastTradingTime': '2018-05-19T16:00:00.000Z', 'tickSize': 1e-07, 'contractSize': 1, 'tradeable': True}, {'symbol': 'fi_ethusd_180519', 'type': 'futures_inverse', 'underlying': 'rr_ethusd', 'lastTradingTime': '2018-05-19T16:00:00.000Z', 'tickSize': 0.01, 'contractSize': 1, 'tradeable': True}, {'symbol': 'rr_xbtusd', 'type': 'spot index', 'tradeable': False}, {'symbol': 'in_xbtusd', 'type': 'spot index', 'tradeable': False}, {'symbol': 'rr_xrpusd', 'type': 'spot index', 'tradeable': False}, {'symbol': 'in_xrpusd', 'type': 'spot index', 'tradeable': False}, {'symbol': 'rr_xrpxbt', 'type': 'spot index', 'tradeable': False}, {'symbol': 'in_xrpxbt', 'type': 'spot index', 'tradeable': False}, {'symbol': 'rr_ethusd', 'type': 'spot index', 'tradeable': False}, {'symbol': 'in_ethusd', 'type': 'spot index', 'tradeable': False}], 'serverTime': '2018-05-09T15:50:45.543Z'}
   get_tickers:
    {'result': 'success', 'tickers': [{'symbol': 'fi_xrpusd_180519', 'markPrice': 0.8017, 'vol24h': 0, 'suspended': False}, {'symbol': 'fi_ethusd_180606', 'markPrice': 749.33, 'vol24h': 0, 'suspended': False}, {'symbol': 'fi_ethusd_180519', 'markPrice': 749.33, 'vol24h': 0, 'suspended': False}, {'symbol': 'fi_xbtusd_180606', 'markPrice': 9292, 'vol24h': 0, 'suspended': False}, {'symbol': 'fv_xrpxbt_180519', 'markPrice': 8.62e-05, 'vol24h': 0, 'suspended': False}, {'symbol': 'fi_xrpusd_180606', 'markPrice': 0.8017, 'vol24h': 0, 'suspended': False}, {'symbol': 'fv_xrpxbt_180606', 'markPrice': 8.62e-05, 'vol24h': 0, 'suspended': False}, {'symbol': 'fi_xbtusd_180519', 'markPrice': 9292, 'bid': 5640, 'bidSize': 100, 'vol24h': 600, 'open24h': 6800, 'last': 5640, 'lastTime': '2018-05-09T14:28:15.275Z', 'lastSize': 100, 'suspended': False}, {'symbol': 'in_xbtusd', 'last': 9288, 'lastTime': '2018-05-09T15:50:41.000Z'}, {'symbol': 'in_xrpusd', 'last': 0.8013, 'lastTime': '2018-05-09T15:50:41.000Z'}, {'symbol': 'in_ethusd', 'last': 748.96, 'lastTime': '2018-05-09T15:50:41.000Z'}, {'symbol': 'in_ltcusd', 'last': 158.29, 'lastTime': '2018-05-09T15:50:41.000Z'}, {'symbol': 'in_xrpxbt', 'last': 8.613e-05, 'lastTime': '2018-05-09T15:50:41.000Z'}, {'symbol': 'rr_xbtusd', 'last': 9269, 'lastTime': '2018-05-09T15:00:00.000Z'}, {'symbol': 'rr_xrpusd', 'last': 0.7937, 'lastTime': '2018-05-09T15:00:00.000Z'}, {'symbol': 'rr_ethusd', 'last': 744.53, 'lastTime': '2018-05-09T15:00:00.000Z'}, {'symbol': 'rr_ltcusd', 'last': 156.57, 'lastTime': '2018-05-09T15:00:00.000Z'}, {'symbol': 'rr_xrpxbt', 'last': 8.563e-05, 'lastTime': '2018-05-09T15:00:00.000Z'}], 'serverTime': '2018-05-09T15:50:45.548Z'}
   get_orderbook:
    {'result': 'success', 'orderBook': {'bids': [[5640, 100], [5620, 1190], [1, 3]], 'asks': []}, 'serverTime': '2018-05-09T15:50:45.561Z'}
   get_history:
    {'result': 'success', 'history': [], 'serverTime': '2018-05-09T15:50:45.570Z'}
   get_accounts:
    {'result': 'success', 'accounts': {'fi_xbtusd': {'type': 'marginAccount', 'auxiliary': {'usd': 0, 'pv': 0.40321572134, 'pnl': -0.00480628374, 'af': 0.39955674003}, 'marginRequirements': {'im': 0.00365898131, 'mm': 0.001829490655, 'lt': 0.001829490655, 'tt': 0.001829490655}, 'triggerEstimates': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'balances': {'xbt': 0.40802200508, 'xrp': 0, 'eth': 0, 'fi_xbtusd_180519': -1700}, 'currency': 'xbt'}, 'cash': {'type': 'cashAccount', 'balances': {'xbt': 0, 'xrp': 0, 'eth': 0}}, 'fv_xrpxbt': {'type': 'marginAccount', 'auxiliary': {'usd': 0, 'pv': 0.3200027937, 'pnl': 0, 'af': 0.3200027937}, 'marginRequirements': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'triggerEstimates': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'balances': {'xbt': 0.3200027937, 'xrp': 0, 'eth': 0}, 'currency': 'xbt'}, 'fi_xrpusd': {'type': 'marginAccount', 'auxiliary': {'usd': 0, 'pv': 3512.22578455212, 'pnl': 0, 'af': 3512.22578455212}, 'marginRequirements': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'triggerEstimates': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'balances': {'xrp': 3512.22578455212, 'xbt': 0, 'eth': 0}, 'currency': 'xrp'}, 'fi_ethusd': {'type': 'marginAccount', 'auxiliary': {'usd': 0, 'pv': 4.36367445959, 'pnl': 0, 'af': 4.36367445959}, 'marginRequirements': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'triggerEstimates': {'im': 0, 'mm': 0, 'lt': 0, 'tt': 0}, 'balances': {'eth': 4.36367445959, 'xrp': 0, 'xbt': 0}, 'currency': 'eth'}}, 'serverTime': '2018-05-09T15:50:45.583Z'}
   send_order (limit):
    {'result': 'success', 'serverTime': '2018-05-09T15:50:45.598Z', 'sendStatus': {'status': 'tooManySmallOrders'}}
   send_order (limit) with client id:
    {'result': 'success', 'serverTime': '2018-05-09T15:50:45.607Z', 'sendStatus': {'status': 'tooManySmallOrders'}}
   send_order (stop):
    {'result': 'success', 'serverTime': '2018-05-09T15:50:45.621Z', 'sendStatus': {'status': 'tooManySmallOrders'}}
   cancel_order:
    {'result': 'success', 'cancelStatus': {'status': 'notFound', 'receivedTime': '2018-05-09T15:50:45.637Z'}, 'serverTime': '2018-05-09T15:50:45.637Z'}
   send_batchorder:
    {'result': 'success', 'batchStatus': [{'order_tag': '1', 'status': 'clientOrderIdAlreadyExist'}, {'order_tag': '2', 'status': 'tooManySmallOrders'}, {'order_id': 'e35d61dd-8a30-4d5f-a574-b5593ef0c050', 'status': 'notFound'}, {'status': 'notFound'}], 'serverTime': '2018-05-09T15:50:45.653Z'}
   get_openorders:
    {'result': 'success', 'openOrders': [{'order_id': '635cd703-db52-4ae9-8c19-858dbb1b0578', 'symbol': 'fi_xbtusd_180519', 'side': 'buy', 'orderType': 'lmt', 'limitPrice': 1, 'unfilledSize': 1, 'receivedTime': '2018-05-09T15:36:13.962Z', 'status': 'untouched', 'filledSize': 0}, {'order_id': 'e05ad9d1-10c7-4e26-a6bc-e0d96c174068', 'cliOrdId': 'my_another_client_id', 'symbol': 'fi_xbtusd_180519', 'side': 'buy', 'orderType': 'lmt', 'limitPrice': 1, 'unfilledSize': 1, 'receivedTime': '2018-05-09T15:32:19.516Z', 'status': 'untouched', 'filledSize': 0}, {'order_id': 'd427f920-ec55-4c18-ba95-5fe241513b30', 'cliOrdId': 'hello id', 'symbol': 'fi_xbtusd_180519', 'side': 'buy', 'orderType': 'lmt', 'limitPrice': 5640, 'unfilledSize': 100, 'receivedTime': '2018-05-09T14:28:12.287Z', 'status': 'partiallyFilled', 'filledSize': 100}, {'order_id': '1313a0af-f2ae-4db3-ac27-ee9ae109fcd3', 'cliOrdId': '36825274-4c2f-4fb4-acd9-583f897d2b3f', 'symbol': 'fi_xbtusd_180519', 'side': 'buy', 'orderType': 'lmt', 'limitPrice': 5620, 'unfilledSize': 200, 'receivedTime': '2018-05-09T14:25:38.064Z', 'status': 'untouched', 'filledSize': 0}], 'serverTime': '2018-05-09T15:50:45.668Z'}
   get_fills:
    {'result': 'success', 'fills': [], 'serverTime': '2018-05-09T15:50:45.682Z'}
   get_openpositions:
    {'result': 'success', 'openPositions': [{'side': 'short', 'symbol': 'fi_xbtusd_180519', 'price': 9054.335894621296, 'fillTime': '2018-05-09T15:50:45.698Z', 'size': 1700}], 'serverTime': '2018-05-09T15:50:45.698Z'}
   get_transfers:
    {'result': 'success', 'transfers': [], 'serverTime': '2018-05-09T15:50:45.723Z'}
```