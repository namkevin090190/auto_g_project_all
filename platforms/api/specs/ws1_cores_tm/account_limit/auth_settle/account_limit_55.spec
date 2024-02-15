# [FullKYC] Verify user make settlement successfully within Per transaction limit - domestic card
Tags: ws1, ws1_account_limit, account_limit_55

## VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA
* [API][Customer] Create customer
* [API][Flag] Grant VKYC for customer id "current_customer_id"
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Authorisation at time stamp "current_time_stamp" with data - amount "30000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Settlement at time stamp "current_time_stamp" with data - amount "50000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA" - client transaction id order "1"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making settlement - "success" - client transaction id order "1"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "VKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "success", "fail", "fail", "success", "success"
* [API][CASA] Verify account "VKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "success", "success"

