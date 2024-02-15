# [eKYC] Verify user make transactions successfully within Daily limit - same transaction code - domestic card
Tags: ws1, ws1_account_limit, account_limit_14

## VIRTUAL_CARD_CARD_NOT_PRESENT
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Outbound Hard Settlement at time stamp "current_time_stamp" with data - amount "10000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then Outbound Hard Settlement at time stamp "current_time_stamp" with data - amount "40000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "success", "fail", "fail", "success", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "success", "success"