# [eKYC] Verify user is credit (cash in) successfully with E-Banking and Daily/Monthly limit
Tags: ws1, ws1_account_limit, account_limit_87

## Precondition
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "50000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "40000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"

## VIKKI_TO_VIKKI - credit amount < limit
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "9999999" - from account id "default_account_id" - to account id "current_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after getting credit - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"

## VIKKI_TO_HDBANK- credit amount = limit
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "10000000" - from account id "default_account_id" - to account id "current_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after getting credit - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"

## VIKKI_TO_NAPAS- credit amount > limit
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "10000001" - from account id "default_account_id" - to account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after getting credit - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"
