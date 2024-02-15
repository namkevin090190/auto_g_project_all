# [eKYC] Verify user make authorisation FAIL without Per transaction limit - domestic card
Tags: ws1, ws1_account_limit, account_limit_43

## VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Authorisation at time stamp "current_time_stamp" with data - amount "50000001" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Verify Contract Violations - Reason of posting id "current_posting_id" should be "exceeds the transaction limit"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_REJECTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "fail"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"

