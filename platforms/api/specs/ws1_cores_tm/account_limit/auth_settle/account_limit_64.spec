# [eKYC] Verify user make multiple transactions successfully with Auth = Settle
Tags: ws1, ws1_account_limit, account_limit_64

## VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA
* [API][SchedulerTag] Create Scheduler Tag with pause_time "2023-10-26T01:20:00Z"
* [API][Product] Create product
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "2023-10-26T01:20:00Z" with product version id "current_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "2023-10-26T01:25:00Z" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-26T01:25:00Z", then Authorisation at time stamp "2023-10-26T01:30:00Z" with data - amount "5000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-26T01:30:00Z", then Authorisation at time stamp "2023-10-26T01:35:00Z" with data - amount "6000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"

* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-26T01:35:00Z", then Settlement at time stamp "2023-10-26T01:40:00Z" with data - amount "6000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA" - client transaction id order "2"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making settlement - "success" - client transaction id order "2"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" at pause time "2023-10-26T01:40:00Z" should be correct after making transaction - "fail", "fail", "fail", "fail", "success", "fail", "fail", "success", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" at pause time "2023-10-26T01:40:00Z" should be correct after making transaction - "fail", "success", "success"

* [API][PostingInstruction] Get balance and info of "current_account_id" at pause time "2023-10-27T01:35:00Z", then Settlement at time stamp "2023-10-27T01:40:00Z" with data - amount "5000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA" - client transaction id order "1"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making settlement - "success" - client transaction id order "1"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" at pause time "2023-10-27T01:40:00Z" should be full limit
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" at pause time "2023-10-27T01:40:00Z" should be correct after making transaction - "fail", "success", "success"