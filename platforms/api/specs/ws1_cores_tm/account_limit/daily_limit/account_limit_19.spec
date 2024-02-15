# [FullKYC] Verify user make transactions FAIL without Daily limit - different transaction code - eBanking
Tags: ws1, ws1_account_limit, account_limit_19

## VIKKI_TO_VIKKI - VIKKI_TO_HDBANK - VIKKI_TO_NAPAS
* [API][Customer] Create customer
* [API][Flag] Grant VKYC for customer id "current_customer_id"
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "3000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "499999999" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "499999999" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "499999999" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "499999999" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"

* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "5" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify Contract Violations - Reason of posting id "current_posting_id" should be "exceeds the remaining daily limit"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_REJECTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "fail"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "VKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "VKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"

* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "5" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Verify Contract Violations - Reason of posting id "current_posting_id" should be "exceeds the remaining daily limit"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_REJECTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "fail"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "VKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "VKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"

* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "5" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify Contract Violations - Reason of posting id "current_posting_id" should be "exceeds the remaining daily limit"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_REJECTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "fail"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "VKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail", "fail"
* [API][CASA] Verify account "VKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail"