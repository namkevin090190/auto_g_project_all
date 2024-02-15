# [eKYC] Verify user make transactions successfully within Daily limit - eBanking and domestic card
Tags: ws1, ws1_account_limit, account_limit_16

## VIKKI_TO_VIKKI - VIKKI_TO_HDBANK - VIKKI_TO_NAPAS - VIRTUAL_CARD_CARD_NOT_PRESENT
* [API][Customer] Create customer
* [API][CASA] Create CASA account - opening at "current_time_stamp" with product version id "official_product_version_id"
* [API][PostingInstruction] Inbound Hard Settlement at time stamp "current_time_stamp" with data - amount "1000000000" - account id "current_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "25000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_VIKKI,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "success", "fail", "fail", "success", "fail", "fail", "success", "fail", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "success", "fail", "success"

* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "25000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_HDBANK,INTERNAL_TRANSFER,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "success", "fail", "success", "fail", "fail", "success", "fail", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "success", "fail", "success"

* [API][PostingInstruction] Get balance and info of "current_account_id", then transfer at time stamp "current_time_stamp" with data - amount "25000000" - from account id "current_account_id" - to account id "default_account_id" - transaction code "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIKKI_TO_NAPAS,E_BANKING,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "success", "fail", "fail", "fail", "success", "fail", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "success", "fail", "success"

* [API][PostingInstruction] Get balance and info of "current_account_id", then Outbound Hard Settlement at time stamp "current_time_stamp" with data - amount "25000000" - account id "current_account_id" - transaction code "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][PostingInstruction] Verify status of posting id "current_posting_id" should be "POSTING_INSTRUCTION_BATCH_STATUS_ACCEPTED"
* [API][PostingInstruction] Verify Instruction Detail and Transaction code of posting id "current_posting_id" should match with "VIRTUAL_CARD_CARD_NOT_PRESENT,CARD,CASA"
* [API][Balances][Verify] Default balance of "current_account_id" should be "calculated_amount" after making transaction - "success"
* [API][Common] Sleep "2" seconds
* [API][CASA] Verify account "EKYC" - daily limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "fail", "fail", "fail", "success", "fail", "fail", "success", "success"
* [API][CASA] Verify account "EKYC" - monthly limit of CASA account with id "current_account_id" should be correct after making transaction - "fail", "success", "success"