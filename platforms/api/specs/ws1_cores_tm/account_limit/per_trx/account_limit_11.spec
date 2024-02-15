# [FullKYC] [FullKYC] Verify user make transaction FAIL without Per transaction limit - foreign card
Tags: ws1, ws1_account_limit, account_limit_11

## VIRTUAL_CARD_FX_CARD_NOT_PRESENT
* [API][Customer] Create customer
* [API][Flag] Grant VKYC for customer id "current_customer_id"
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Outbound Hard Settlement at time stamp "current_time_stamp" with data - amount "50000001" - account id "current_account_id" - transaction code "VIRTUAL_CARD_FX_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Verify Contract Violations - Reason of posting id "current_posting_id" should be "exceeds the transaction limit"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_REJECTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_FX_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "fail"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "VKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "VKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"
